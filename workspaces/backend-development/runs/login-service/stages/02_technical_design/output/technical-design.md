# Technical Design

## Existing behavior and relevant components

No backend or database profile is configured. The React login view is in progress and remains untouched.

## Contract or interface changes

| Operation/event | Request/input | Response/output | Compatibility |
|---|---|---|---|
| `GET /api/auth/methods` | none | enabled method IDs | New API |
| `POST /api/auth/password/register`, `/login` | email/password | 15-minute bearer token | New API |
| `GET /api/auth/{provider}/start`, `GET/POST .../callback` | configured provider/identity response | redirect with one-use code in fragment | New API |
| `POST /api/auth/token/exchange` | one-use code | bearer token | New API |
| `POST /api/auth/passkeys/*` | WebAuthn ceremony data | options, registration result, or token | New API |
| `GET /api/auth/me` | bearer token | user ID/email | New API |

## Data and migration changes

Additive Alembic migration creates users, provider identities, passkey credentials, temporary OAuth codes, and passkey challenges. PostgreSQL is runtime target; SQLite is used only for isolated tests/migration checks.

## Validation and authorization

Normalize email; require 12-character minimum registration passwords; hash with Argon2; sign 15-minute JWTs; verify WebAuthn origin/RP/challenge/signature. Require bearer auth for profile and passkey enrollment. Provider email never auto-links identities. Do not store raw credentials or one-use codes.

## Errors, timeouts, and failure behavior

Generic invalid-password errors; 401 invalid bearer; 409 duplicate signup; 400 invalid/expired flows; 404 unconfigured providers; sanitized provider errors. Prune expired challenges as flows are created.

## Reliability, performance, and observability

SQLAlchemy sessions use pool pre-ping; Authlib performs provider requests. No credential logging. Deployers must enforce ingress rate limits.

## Rollout, compatibility, and rollback

Configure PostgreSQL, secrets, origins, RP ID, and providers; apply migration before service startup. Downgrade drops auth data; prefer forward fixes after user data exists.

## Acceptance-criteria mapping

| Criterion | Component or behavior | Verification |
|---|---|---|
| Methods/provider configuration | `/api/auth/methods` | All-eight-method test |
| Password/token auth | `/password/*`, `/me` | Registration/login and rejection tests |
| Passkeys | `/passkeys/*` | Option generation and auth enforcement tests |
| OAuth exchange | provider routes and token exchange | Config and replay tests |
| Schema | Alembic | Upgrade, schema check, downgrade on disposable SQLite |

## Decisions and open questions

Requester approved the design. TARA discovery and optional `acr_values` are deployment-provided. GitHub/Facebook use OAuth 2 profile APIs.

## Stage Check

pass
