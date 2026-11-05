import json
from datetime import datetime, timedelta, timezone
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from webauthn import (
    generate_authentication_options,
    generate_registration_options,
    options_to_json,
    verify_authentication_response,
    verify_registration_response,
)
from webauthn.helpers import (
    base64url_to_bytes,
    bytes_to_base64url,
)
from webauthn.helpers.exceptions import WebAuthnException
from webauthn.helpers.structs import (
    AuthenticatorSelectionCriteria,
    PublicKeyCredentialDescriptor,
    ResidentKeyRequirement,
    UserVerificationRequirement,
)

from app.database import get_db
from app.models import PasskeyChallenge, PasskeyCredential, User
from app.schemas import (
    AccessTokenResponse,
    PasskeyAuthenticationVerification,
    PasskeyRegistrationVerification,
)
from app.security import get_current_user, issue_access_token

router = APIRouter()
CHALLENGE_LIFETIME = timedelta(minutes=5)


def _challenge_response(db: Session, user_id: str | None, purpose: str, challenge: bytes) -> dict:
    flow_id = str(uuid4())
    now = datetime.now(timezone.utc)
    db.execute(delete(PasskeyChallenge).where(PasskeyChallenge.expires_at < now))
    db.add(
        PasskeyChallenge(
            id=flow_id,
            user_id=user_id,
            challenge=bytes_to_base64url(challenge),
            purpose=purpose,
            expires_at=now + CHALLENGE_LIFETIME,
        )
    )
    db.commit()
    return {"flow_id": flow_id}


def _take_challenge(db: Session, flow_id: str, purpose: str) -> PasskeyChallenge:
    challenge = db.scalar(
        select(PasskeyChallenge).where(
            PasskeyChallenge.id == flow_id,
            PasskeyChallenge.purpose == purpose,
        ).with_for_update()
    )
    now = datetime.now(timezone.utc)
    if challenge is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired passkey flow")
    expires_at = challenge.expires_at
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    if expires_at <= now:
        db.delete(challenge)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired passkey flow")
    return challenge


def _rp_id(request: Request) -> str:
    return request.app.state.settings.webauthn_rp_id


def _origin(request: Request) -> str:
    return request.app.state.settings.webauthn_origin.rstrip("/")


@router.post("/registration/options")
def registration_options(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    credentials = db.scalars(
        select(PasskeyCredential).where(PasskeyCredential.user_id == user.id)
    ).all()
    options = generate_registration_options(
        rp_id=_rp_id(request),
        rp_name="Sweeper",
        user_id=user.id.encode("utf-8"),
        user_name=user.email or user.id,
        user_display_name=user.email or "Sweeper user",
        exclude_credentials=[
            PublicKeyCredentialDescriptor(id=base64url_to_bytes(item.credential_id))
            for item in credentials
        ],
        authenticator_selection=AuthenticatorSelectionCriteria(
            resident_key=ResidentKeyRequirement.REQUIRED,
            user_verification=UserVerificationRequirement.REQUIRED,
        ),
    )
    response = _challenge_response(db, user.id, "registration", options.challenge)
    response["publicKey"] = json.loads(options_to_json(options))
    return response


@router.post("/registration/verify", status_code=status.HTTP_201_CREATED)
def verify_registration(
    body: PasskeyRegistrationVerification,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, str]:
    flow = _take_challenge(db, str(body.flow_id), "registration")
    if flow.user_id != user.id:
        db.delete(flow)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired passkey flow")
    try:
        verified = verify_registration_response(
            credential=body.credential,
            expected_challenge=base64url_to_bytes(flow.challenge),
            expected_rp_id=_rp_id(request),
            expected_origin=_origin(request),
            require_user_verification=True,
        )
    except (WebAuthnException, ValueError, TypeError, KeyError, AttributeError) as exc:
        db.delete(flow)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passkey registration failed") from exc

    credential_id = bytes_to_base64url(verified.credential_id)
    db.add(
        PasskeyCredential(
            id=str(uuid4()),
            user_id=user.id,
            credential_id=credential_id,
            public_key=bytes_to_base64url(verified.credential_public_key),
            sign_count=verified.sign_count,
            display_name=body.display_name.strip() if body.display_name else None,
            created_at=datetime.now(timezone.utc),
        )
    )
    db.delete(flow)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        credential_exists = db.scalar(
            select(PasskeyCredential.id).where(PasskeyCredential.credential_id == credential_id)
        )
        db.execute(delete(PasskeyChallenge).where(PasskeyChallenge.id == str(body.flow_id)))
        db.commit()
        if credential_exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Passkey is already registered",
            ) from exc
        raise
    return {"status": "registered"}


@router.post("/authentication/options")
def authentication_options(request: Request, db: Session = Depends(get_db)) -> dict:
    options = generate_authentication_options(
        rp_id=_rp_id(request),
        user_verification=UserVerificationRequirement.REQUIRED,
    )
    response = _challenge_response(db, None, "authentication", options.challenge)
    response["publicKey"] = json.loads(options_to_json(options))
    return response


@router.post("/authentication/verify", response_model=AccessTokenResponse)
def verify_authentication(
    body: PasskeyAuthenticationVerification,
    request: Request,
    db: Session = Depends(get_db),
) -> AccessTokenResponse:
    flow = _take_challenge(db, str(body.flow_id), "authentication")
    credential_id = body.credential.get("id")
    if not isinstance(credential_id, str):
        db.delete(flow)
        db.commit()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passkey authentication failed")
    stored = db.scalar(
        select(PasskeyCredential)
        .where(PasskeyCredential.credential_id == credential_id)
        .with_for_update()
    )
    if stored is None:
        db.delete(flow)
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Passkey authentication failed")
    try:
        verified = verify_authentication_response(
            credential=body.credential,
            expected_challenge=base64url_to_bytes(flow.challenge),
            expected_rp_id=_rp_id(request),
            expected_origin=_origin(request),
            credential_public_key=base64url_to_bytes(stored.public_key),
            credential_current_sign_count=stored.sign_count,
            require_user_verification=True,
        )
    except (WebAuthnException, ValueError, TypeError, KeyError, AttributeError) as exc:
        db.delete(flow)
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Passkey authentication failed") from exc

    stored.sign_count = verified.new_sign_count
    db.delete(flow)
    db.commit()
    token, expires_in = issue_access_token(stored.user_id, request)
    return AccessTokenResponse(access_token=token, expires_in=expires_in)
