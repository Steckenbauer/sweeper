# Login service

FastAPI service for password, passkey, and configured identity-provider sign-in. PostgreSQL stores user accounts, external identities, passkeys, short-lived OAuth exchange codes, and passkey challenges.

## Run locally

1. Copy `backend/login-service/.env.example` to `backend/login-service/.env`; replace both signing secrets with independent random values of at least 32 characters. `COOKIE_SECURE=true` is required for cross-site OAuth callbacks, including Apple's form-post callback; browsers treat `localhost` as a secure context for local development.
2. Start PostgreSQL and create the database named in `DATABASE_URL`.
3. From the repository root, install and migrate:

   ```powershell
   python -m pip install -r backend/login-service/requirements-dev.txt
   python -m alembic -c backend/login-service/alembic.ini upgrade head
   python -m uvicorn app.main:app --app-dir backend/login-service --reload
   ```

4. Open `http://localhost:8000/docs` for the interactive API contract.

## Run with Docker

Build the image from the repository root:

```powershell
docker build -t sweeper-login-service backend/login-service
```

Run it on a Docker network that can reach PostgreSQL, passing the service environment file:

```powershell
docker run --rm --name sweeper-login-service --env-file backend/login-service/.env -p 8000:8000 sweeper-login-service
```

Set `DATABASE_URL` to the PostgreSQL hostname reachable from the container (for example, the database container's network name, not `localhost`). Apply migrations separately before starting the API:

```powershell
docker run --rm --env-file backend/login-service/.env --entrypoint python sweeper-login-service -m alembic -c alembic.ini upgrade head
```

The image runs as a non-root user and has a `/healthz` Docker health check. Secrets are supplied at runtime and are not copied into the image.

`GET /api/auth/methods` reports password and passkey plus only the external providers configured with client credentials. Configure each provider's registered callback as `PUBLIC_API_URL/api/auth/{provider}/callback`. Google, Apple, Microsoft, and TARA use OpenID Connect discovery; GitHub and Facebook use OAuth 2. Configure `TARA_DISCOVERY_URL` for the TARA environment registered to the service, and optionally set `TARA_ACR_VALUES` to request a TARA authentication context supported by that environment. Apple client secrets must be generated and rotated according to Apple's developer requirements.

OAuth callback redirects to `FRONTEND_URL/auth/callback#code=...`; the frontend must exchange that short-lived one-use code at `POST /api/auth/token/exchange`. The code is put in the URL fragment so it is not sent in HTTP requests or referrer headers. Password register/login and passkey verification return a 15-minute bearer token. All protected endpoints require `Authorization: Bearer <token>`.

Passkey enrollment requires an authenticated user: call `POST /api/auth/passkeys/registration/options`, pass its `publicKey` to `navigator.credentials.create`, then submit the resulting credential and `flow_id` to `/api/auth/passkeys/registration/verify`. Authentication uses `/authentication/options`, `navigator.credentials.get`, and `/authentication/verify`. Set `WEBAUTHN_RP_ID` to the frontend host and `WEBAUTHN_ORIGIN` to its exact origin.

Before deploying, set `COOKIE_SECURE=true`, allow only trusted frontend origins, use HTTPS, provision provider credentials, and apply migrations. Apply rate limits at the ingress for registration, password login, OAuth start, and passkey verification. Automatic account linking by email is deliberately disabled; external identities are keyed by provider subject. Do not log request bodies, passwords, codes, tokens, or provider responses.

## Verify

```powershell
python -m pytest backend/login-service/tests
python -m ruff check backend/login-service/app backend/login-service/tests backend/login-service/migrations
python -m alembic -c backend/login-service/alembic.ini check
```

Run the Alembic check with `DATABASE_URL` pointing to an isolated non-production database.
