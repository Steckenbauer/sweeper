from datetime import datetime, timedelta, timezone
from uuid import uuid4

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import Settings
from app.database import get_db
from app.main import create_app
from app.models import Base, OAuthCode, User
from app.security import hash_one_time_code


def make_client(**settings_overrides):
    settings = Settings(
        database_url="sqlite://",
        jwt_secret_key="test-jwt-secret-key-with-at-least-32-characters",
        session_secret="test-session-secret-key-with-32-characters",
        **settings_overrides,
    )
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    app = create_app(settings)
    app.state.session_factory = session_factory

    def override_get_db():
        yield from _session(session_factory)

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app), engine


def _session(session_factory):
    with session_factory() as session:
        yield session


def test_password_registration_login_and_profile():
    client, engine = make_client()
    try:
        registration = client.post(
            "/api/auth/password/register",
            json={"email": "Person@Example.com", "password": "secure-password-123"},
        )
        assert registration.status_code == 201
        token = registration.json()["access_token"]
        assert registration.json()["token_type"] == "bearer"

        profile = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert profile.status_code == 200
        assert profile.json()["email"] == "person@example.com"

        login = client.post(
            "/api/auth/password/login",
            json={"email": "person@example.com", "password": "secure-password-123"},
        )
        assert login.status_code == 200
        assert login.json()["access_token"]
    finally:
        engine.dispose()


def test_password_registration_rejects_duplicate_and_weak_password():
    client, engine = make_client()
    try:
        payload = {"email": "person@example.com", "password": "secure-password-123"}
        assert client.post("/api/auth/password/register", json=payload).status_code == 201
        assert client.post("/api/auth/password/register", json=payload).status_code == 409
        payload["email"] = "other@example.com"
        payload["password"] = "short"
        assert client.post("/api/auth/password/register", json=payload).status_code == 422
    finally:
        engine.dispose()


def test_password_login_has_generic_failure_and_protected_profile_requires_token():
    client, engine = make_client()
    try:
        response = client.post(
            "/api/auth/password/login",
            json={"email": "missing@example.com", "password": "incorrect-password"},
        )
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid email or password"
        assert client.get("/api/auth/me").status_code == 401
        assert client.get(
            "/api/auth/me",
            headers={"Authorization": "Bearer invalid"},
        ).status_code == 401
    finally:
        engine.dispose()


def test_provider_methods_require_credentials_and_tara_discovery_url():
    client, engine = make_client(
        google_client_id="google-id",
        google_client_secret="google-secret",
        tara_client_id="tara-id",
        tara_client_secret="tara-secret",
    )
    try:
        response = client.get("/api/auth/methods")
        assert response.status_code == 200
        assert response.json()["methods"] == ["password", "passkey", "google"]
        assert client.get("/api/auth/tara/start").status_code == 404
    finally:
        engine.dispose()


def test_all_requested_external_providers_are_configurable():
    client, engine = make_client(
        google_client_id="google-id",
        google_client_secret="google-secret",
        apple_client_id="apple-id",
        apple_client_secret="apple-secret",
        microsoft_client_id="microsoft-id",
        microsoft_client_secret="microsoft-secret",
        github_client_id="github-id",
        github_client_secret="github-secret",
        facebook_client_id="facebook-id",
        facebook_client_secret="facebook-secret",
        tara_client_id="tara-id",
        tara_client_secret="tara-secret",
        tara_discovery_url="https://tara.example/.well-known/openid-configuration",
    )
    try:
        assert client.get("/api/auth/methods").json()["methods"] == [
            "password",
            "passkey",
            "google",
            "apple",
            "microsoft",
            "github",
            "facebook",
            "tara",
        ]
    finally:
        engine.dispose()


def test_oauth_exchange_code_is_short_lived_and_single_use():
    client, engine = make_client()
    session_factory = client.app.state.session_factory
    user_id = str(uuid4())
    code = "one-time-code-value-that-is-long-enough-for-the-api"
    with session_factory() as session:
        session.add(
            User(
                id=user_id,
                email="oauth@example.com",
                password_hash=None,
                created_at=datetime.now(timezone.utc),
            )
        )
        session.add(
            OAuthCode(
                code_hash=hash_one_time_code(code),
                user_id=user_id,
                expires_at=datetime.now(timezone.utc) + timedelta(seconds=90),
            )
        )
        session.commit()
    try:
        exchange = client.post("/api/auth/token/exchange", json={"code": code})
        assert exchange.status_code == 200
        assert client.get(
            "/api/auth/me",
            headers={"Authorization": f"Bearer {exchange.json()['access_token']}"},
        ).json()["id"] == user_id
        assert client.post("/api/auth/token/exchange", json={"code": code}).status_code == 400
    finally:
        engine.dispose()


def test_passkey_authentication_options_and_registration_requires_login():
    client, engine = make_client()
    try:
        options = client.post("/api/auth/passkeys/authentication/options")
        assert options.status_code == 200
        assert options.json()["flow_id"]
        assert options.json()["publicKey"]["challenge"]
        assert client.post("/api/auth/passkeys/registration/options").status_code == 401

        registration = client.post(
            "/api/auth/password/register",
            json={"email": "passkey@example.com", "password": "secure-password-123"},
        )
        token = registration.json()["access_token"]
        registration_options = client.post(
            "/api/auth/passkeys/registration/options",
            headers={"Authorization": f"Bearer {token}"},
        )
        assert registration_options.status_code == 200
        assert registration_options.json()["flow_id"]
        assert registration_options.json()["publicKey"]["authenticatorSelection"]["residentKey"] == "required"
        assert (
            registration_options.json()["publicKey"]["authenticatorSelection"]["userVerification"]
            == "required"
        )
        assert client.get("/healthz").json() == {"status": "ok"}
    finally:
        engine.dispose()
