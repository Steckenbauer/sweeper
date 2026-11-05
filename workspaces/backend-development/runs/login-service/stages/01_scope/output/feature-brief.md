# Backend Feature Brief

## Caller or affected system and problem

Sweeper's login UI needs an API that can authenticate users using the requested password, passkey, and identity-provider methods.

## Desired behavior

Provide a deployable FastAPI service that persists accounts in PostgreSQL, securely verifies credentials, and returns short-lived bearer tokens.

## In scope

- Password registration/login with normalized email and Argon2 hashes.
- WebAuthn passkeys.
- Google, Apple, Microsoft, and TARA OIDC; GitHub and Facebook OAuth 2.
- Single-use OAuth code exchange, authenticated profile lookup, provider configuration, and an initial migration.

## Out of scope

- Frontend edits/token storage, provider application setup, and production deployment.
- Account linking, refresh tokens, password reset, and ingress rate limiting.

## Acceptance criteria

- [x] Methods API returns password/passkey and only configured external methods; all six providers can be configured.
- [x] Password signup enforces policy; password login returns a bearer token; invalid credentials are generic and profile access requires a valid token.
- [x] Passkey registration requires authentication; WebAuthn options and verification are provided.
- [x] OAuth/OIDC callbacks issue short-lived, single-use codes.
- [x] PostgreSQL schema is migration-managed and auth tests cover validation and failure paths.

## Assumptions and open questions

Requester approved FastAPI + PostgreSQL, self-registration, WebAuthn, OAuth/OIDC, and TARA's OIDC discovery setup. Provider credentials and service origins are deployment-provided.

## Stage Check

pass
