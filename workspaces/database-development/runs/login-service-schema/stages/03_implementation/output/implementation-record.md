# Database Implementation Record

## Changed files

Added SQLAlchemy models and Alembic config, environment, and revision `0001_create_auth_tables`.

## Schema and migration decisions

Five tables with foreign-key cascades, uniqueness, and indexes. OAuth codes are stored as hashes. Alembic reads `DATABASE_URL` from process environment or `backend/login-service/.env`.

## Commands run

| Check | Exact command | Environment | Result |
|---|---|---|---|
| Upgrade and schema check | `python -m alembic -c backend\login-service\alembic.ini upgrade head`; `python -m alembic -c backend\login-service\alembic.ini check` | Disposable SQLite file | Pass; no metadata differences |
| Rollback | `python -m alembic -c backend\login-service\alembic.ini downgrade base` | Same disposable SQLite file | Pass |
| Model/API checks | `python -m pytest backend\login-service\tests -q --tb=short` | In-memory SQLite | 7 passed |

## Checks not run and why

No PostgreSQL service was available. SQLite does not replace a PostgreSQL deployment rehearsal.

## Migration duration, locks, or backfill notes

Creates empty tables and indexes; no backfill. Duration/locks not measured on PostgreSQL.

## Recovery limitations and remaining risks

Downgrade is destructive and unsuitable after accounts are created. Rehearse on target PostgreSQL and verify backup recovery.

## Stage Check

pass
