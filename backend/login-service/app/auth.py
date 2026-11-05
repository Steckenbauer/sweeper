from datetime import datetime, timedelta, timezone
from uuid import uuid4

from authlib.integrations.base_client.errors import OAuthError
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import AuthIdentity, OAuthCode, User
from app.providers import configured_providers
from app.schemas import (
    AccessTokenResponse,
    OneTimeCodeExchange,
    PasswordLogin,
    PasswordRegistration,
    UserResponse,
)
from app.security import (
    get_current_user,
    hash_one_time_code,
    hash_password,
    issue_access_token,
    new_one_time_code,
    verify_password,
)

router = APIRouter()


def _token_response(user_id: str, request: Request) -> AccessTokenResponse:
    token, expires_in = issue_access_token(user_id, request)
    return AccessTokenResponse(access_token=token, expires_in=expires_in)


@router.get("/methods")
def available_methods(request: Request) -> dict[str, list[str]]:
    providers = configured_providers(request.app.state.provider_definitions)
    return {"methods": ["password", "passkey", *providers]}


@router.post(
    "/password/register",
    response_model=AccessTokenResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_password(
    body: PasswordRegistration,
    request: Request,
    db: Session = Depends(get_db),
) -> AccessTokenResponse:
    if db.scalar(select(User.id).where(User.email == body.email)) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exists")
    user = User(
        id=str(uuid4()),
        email=body.email,
        password_hash=hash_password(body.password),
        created_at=datetime.now(timezone.utc),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Account already exists",
        ) from exc
    return _token_response(user.id, request)


@router.post("/password/login", response_model=AccessTokenResponse)
def login_password(
    body: PasswordLogin,
    request: Request,
    db: Session = Depends(get_db),
) -> AccessTokenResponse:
    user = db.scalar(select(User).where(User.email == body.email))
    if user is None or not verify_password(body.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return _token_response(user.id, request)


@router.get("/me", response_model=UserResponse)
def current_user_profile(user: User = Depends(get_current_user)) -> UserResponse:
    return UserResponse(id=user.id, email=user.email)


@router.post("/token/exchange", response_model=AccessTokenResponse)
def exchange_oauth_code(
    body: OneTimeCodeExchange,
    request: Request,
    db: Session = Depends(get_db),
) -> AccessTokenResponse:
    code_hash = hash_one_time_code(body.code)
    statement = select(OAuthCode).where(OAuthCode.code_hash == code_hash).with_for_update()
    oauth_code = db.scalar(statement)
    if oauth_code is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired code")

    expires_at = oauth_code.expires_at
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    if expires_at <= datetime.now(timezone.utc):
        db.delete(oauth_code)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired code")

    user_id = oauth_code.user_id
    db.delete(oauth_code)
    db.commit()
    return _token_response(user_id, request)


async def _provider_user_info(provider: str, client, token: dict) -> tuple[str, str | None, bool]:
    if provider == "github":
        response = await client.get("user", token=token)
        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Identity provider could not verify the account")
        profile = response.json()
        email = profile.get("email")
        email_verified = False
        emails_response = await client.get("user/emails", token=token)
        if emails_response.status_code == 200:
            verified_email = next(
                (item for item in emails_response.json() if item.get("primary") and item.get("verified")),
                None,
            )
            if verified_email:
                email = verified_email.get("email")
                email_verified = True
        return str(profile["id"]), email, email_verified
    if provider == "facebook":
        response = await client.get("me?fields=id,email", token=token)
        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Identity provider could not verify the account")
        profile = response.json()
        return str(profile["id"]), profile.get("email"), bool(profile.get("email"))

    profile = token.get("userinfo")
    if not profile:
        profile = await client.userinfo(token=token)
    subject = profile.get("sub")
    if not subject:
        raise HTTPException(status_code=502, detail="Identity provider returned no stable account identifier")
    email = profile.get("email")
    verified = profile.get("email_verified") is True
    return str(subject), email, verified


@router.get("/{provider}/start")
async def start_provider_login(provider: str, request: Request):
    if provider not in configured_providers(request.app.state.provider_definitions):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sign-in method is not configured")
    client = request.app.state.oauth.create_client(provider)
    redirect_uri = f"{request.app.state.settings.public_api_url.rstrip('/')}/api/auth/{provider}/callback"
    authorization_params = {}
    if provider == "tara" and request.app.state.settings.tara_acr_values:
        authorization_params["acr_values"] = request.app.state.settings.tara_acr_values
    return await client.authorize_redirect(request, redirect_uri, **authorization_params)


@router.api_route("/{provider}/callback", methods=["GET", "POST"])
async def finish_provider_login(
    provider: str,
    request: Request,
    db: Session = Depends(get_db),
):
    if provider not in configured_providers(request.app.state.provider_definitions):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sign-in method is not configured")
    if request.query_params.get("error"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Sign-in was not completed")
    client = request.app.state.oauth.create_client(provider)
    try:
        token = await client.authorize_access_token(request)
        subject, email, verified_email = await _provider_user_info(provider, client, token)
    except OAuthError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identity provider sign-in failed",
        ) from exc

    identity = db.scalar(
        select(AuthIdentity).where(
            AuthIdentity.provider == provider,
            AuthIdentity.subject == subject,
        )
    )
    if identity is None:
        normalized_email = email.strip().lower() if email else None
        canonical_email = None
        if verified_email and normalized_email:
            existing_user = db.scalar(select(User).where(User.email == normalized_email))
            if existing_user is None:
                canonical_email = normalized_email
        user = User(
            id=str(uuid4()),
            email=canonical_email,
            password_hash=None,
            created_at=datetime.now(timezone.utc),
        )
        db.add(user)
        db.flush()
        identity = AuthIdentity(
            id=str(uuid4()),
            user_id=user.id,
            provider=provider,
            subject=subject,
            provider_email=normalized_email,
            created_at=datetime.now(timezone.utc),
        )
        db.add(identity)
    db.execute(delete(OAuthCode).where(OAuthCode.expires_at < datetime.now(timezone.utc)))
    raw_code = new_one_time_code()
    db.add(
        OAuthCode(
            code_hash=hash_one_time_code(raw_code),
            user_id=identity.user_id,
            expires_at=datetime.now(timezone.utc) + timedelta(seconds=90),
        )
    )
    db.commit()
    callback_url = f"{request.app.state.settings.frontend_url.rstrip('/')}/auth/callback"
    return RedirectResponse(f"{callback_url}#code={raw_code}", status_code=status.HTTP_303_SEE_OTHER)
