# Backend Release Handoff

## User- or system-visible change

Adds a FastAPI login API for password registration/login, WebAuthn passkeys, and configured Google, Apple, Microsoft, GitHub, Facebook, and TARA sign-in.

## Acceptance criteria and evidence

| Criterion | How it was checked | Result |
|---|---|---|
| Available methods | Test asserts all eight configured method IDs | Pass |
| Password/JWT | Signup, login, invalid login, duplicate signup, weak password, and profile tests | Pass |
| Passkeys | Authentication/registration options and unauthenticated enrollment test | Pass |
| OAuth exchange | Provider configuration and one-use/replay test | Pass |
| Schema | Upgrade, Alembic check, downgrade on disposable SQLite | Pass |

## API, event, or client compatibility

New `/api/auth` API; frontend is not modified. OAuth redirects to `FRONTEND_URL/auth/callback#code=...`; the client exchanges the fragment code and uses the returned bearer token.

## Data migration, rollout, and rollback

Set `backend/login-service/.env`, provision PostgreSQL/provider registrations, then run `python -m alembic -c backend/login-service/alembic.ini upgrade head`. Downgrade deletes all auth data; use forward recovery after accounts exist.

## Operational signals and alerts

`/healthz`; rate-limit signup, password login, provider start, and passkey verification at ingress. Never log credentials, tokens, codes, or provider responses.

## Checks run

| Check or manual steps | Result |
|---|---|
| `python -m pytest backend\login-service\tests -q --tb=short` | 7 passed |
| `python -m ruff check backend\login-service\app backend\login-service\tests backend\login-service\migrations` | Passed |
| Alembic upgrade/check/downgrade on disposable SQLite | Passed |
| `python -m pip install -r backend\login-service\requirements-dev.txt` | Passed |

## Known limitations or risks

No live PostgreSQL server, provider credentials, or browser authenticator was available. Provider callbacks and full WebAuthn ceremonies need deployment testing. The frontend preview is not wired to the API.

## Handoff decision

Ready for deployment configuration and frontend integration; do not enable production sign-in until callbacks, HTTPS, secrets, CORS, database, and ingress limits are configured.
