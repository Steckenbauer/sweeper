from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="backend/login-service/.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str = "postgresql+psycopg://sweeper:sweeper@localhost:5432/sweeper"
    jwt_secret_key: str = Field(min_length=32)
    session_secret: str = Field(min_length=32)
    jwt_issuer: str = "sweeper-login-service"
    access_token_minutes: int = Field(default=15, ge=1, le=60)
    frontend_url: str = "http://localhost:5173"
    public_api_url: str = "http://localhost:8000"
    frontend_origins: str = "http://localhost:5173"
    cookie_secure: bool = True
    webauthn_rp_id: str = "localhost"
    webauthn_origin: str = "http://localhost:5173"

    google_client_id: str | None = None
    google_client_secret: str | None = None
    apple_client_id: str | None = None
    apple_client_secret: str | None = None
    microsoft_client_id: str | None = None
    microsoft_client_secret: str | None = None
    github_client_id: str | None = None
    github_client_secret: str | None = None
    facebook_client_id: str | None = None
    facebook_client_secret: str | None = None
    tara_client_id: str | None = None
    tara_client_secret: str | None = None
    tara_discovery_url: str | None = None
    tara_acr_values: str | None = None

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.frontend_origins.split(",") if origin.strip()]
