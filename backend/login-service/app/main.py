from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.auth import router as auth_router
from app.config import Settings
from app.database import create_session_factory
from app.passkeys import router as passkeys_router
from app.providers import create_oauth_clients


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings()
    app = FastAPI(title="Sweeper Login Service", version="1.0.0")
    app.state.settings = settings
    app.state.session_factory = create_session_factory(settings.database_url)
    app.state.oauth, app.state.provider_definitions = create_oauth_clients(settings)
    app.add_middleware(
        SessionMiddleware,
        secret_key=settings.session_secret,
        max_age=600,
        same_site="none",
        https_only=settings.cookie_secure,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["Authorization", "Content-Type"],
    )
    app.include_router(auth_router, prefix="/api/auth", tags=["authentication"])
    app.include_router(passkeys_router, prefix="/api/auth/passkeys", tags=["passkeys"])

    @app.get("/healthz", tags=["operations"])
    def healthcheck() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
