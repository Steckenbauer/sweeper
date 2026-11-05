# Implementation Record

## Changed files

Added FastAPI app, settings, SQLAlchemy models, password/JWT security, Authlib providers, WebAuthn endpoints, Alembic migration, environment example, requirements, README, and tests under `backend/login-service/`.

## Implementation decisions

Argon2 passwords; 90-second OAuth codes stored only as hashes; 15-minute JWTs; external identities are not auto-linked by email; only fully configured providers are advertised.

## Data or migration notes

Initial additive migration creates five auth tables. It was applied, schema-checked, and downgraded on disposable SQLite; PostgreSQL remains the runtime target.

## Checks run

| Check | Exact command | Result |
|---|---|---|
| API tests | `python -m pytest backend\login-service\tests -q --tb=short` | 7 passed |
| Lint | `python -m ruff check backend\login-service\app backend\login-service\tests backend\login-service\migrations` | Passed |
| Migration apply/check/rollback | PowerShell set `DATABASE_URL=sqlite:///temporary test file`; run Alembic upgrade, check, downgrade | Passed; temporary database removed |
| Dependencies | `python -m pip install -r backend\login-service\requirements-dev.txt` | Passed |

## Checks not run and why

No PostgreSQL server or live provider credentials were supplied. Real provider callbacks and full browser authenticator ceremonies were not exercised.

## Remaining risks or follow-up

Configure and test providers, especially TARA discovery/`acr_values` and Apple's form-post callback. Connect frontend to methods and code exchange APIs. Enforce ingress rate limits and HTTPS.

## Stage Check

pass
