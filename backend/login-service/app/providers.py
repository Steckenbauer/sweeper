from dataclasses import dataclass

from authlib.integrations.starlette_client import OAuth

from app.config import Settings


@dataclass(frozen=True)
class ProviderDefinition:
    client_id: str | None
    client_secret: str | None
    discovery_url: str | None = None
    authorize_url: str | None = None
    access_token_url: str | None = None
    api_base_url: str | None = None
    scope: str = "openid email profile"
    oidc: bool = True


def provider_definitions(settings: Settings) -> dict[str, ProviderDefinition]:
    return {
        "google": ProviderDefinition(
            settings.google_client_id,
            settings.google_client_secret,
            discovery_url="https://accounts.google.com/.well-known/openid-configuration",
        ),
        "apple": ProviderDefinition(
            settings.apple_client_id,
            settings.apple_client_secret,
            discovery_url="https://appleid.apple.com/.well-known/openid-configuration",
            scope="openid email name",
        ),
        "microsoft": ProviderDefinition(
            settings.microsoft_client_id,
            settings.microsoft_client_secret,
            discovery_url="https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration",
        ),
        "github": ProviderDefinition(
            settings.github_client_id,
            settings.github_client_secret,
            authorize_url="https://github.com/login/oauth/authorize",
            access_token_url="https://github.com/login/oauth/access_token",
            api_base_url="https://api.github.com/",
            scope="read:user user:email",
            oidc=False,
        ),
        "facebook": ProviderDefinition(
            settings.facebook_client_id,
            settings.facebook_client_secret,
            authorize_url="https://www.facebook.com/dialog/oauth",
            access_token_url="https://graph.facebook.com/oauth/access_token",
            api_base_url="https://graph.facebook.com/",
            scope="email",
            oidc=False,
        ),
        "tara": ProviderDefinition(
            settings.tara_client_id,
            settings.tara_client_secret,
            discovery_url=settings.tara_discovery_url,
            scope="openid email profile",
        ),
    }


def create_oauth_clients(settings: Settings) -> tuple[OAuth, dict[str, ProviderDefinition]]:
    oauth = OAuth()
    definitions = provider_definitions(settings)
    for name, definition in definitions.items():
        if not definition.client_id or not definition.client_secret:
            continue
        if definition.oidc and not definition.discovery_url:
            continue
        oauth.register(
            name=name,
            client_id=definition.client_id,
            client_secret=definition.client_secret,
            server_metadata_url=definition.discovery_url if definition.oidc else None,
            authorize_url=definition.authorize_url,
            access_token_url=definition.access_token_url,
            api_base_url=definition.api_base_url,
            client_kwargs={"scope": definition.scope},
        )
    return oauth, definitions


def configured_providers(
    definitions: dict[str, ProviderDefinition],
) -> list[str]:
    return [
        name
        for name, definition in definitions.items()
        if definition.client_id
        and definition.client_secret
        and (not definition.oidc or definition.discovery_url)
    ]
