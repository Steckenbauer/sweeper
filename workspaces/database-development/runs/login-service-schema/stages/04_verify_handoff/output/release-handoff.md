# Database Change Handoff

## User- or system-visible data change

Adds persistent auth tables; no existing data changes.

## Acceptance criteria and evidence

| Criterion | How it was checked | Result |
|---|---|---|
| Uniqueness and relationships | Alembic schema compared with SQLAlchemy metadata | Pass |
| Versioned schema lifecycle | Upgrade and downgrade on disposable SQLite | Pass |
| Auth data writes | Password signup and OAuth-code tests using SQLite | Pass |

## Migration and rollout sequence

Provision PostgreSQL and set `DATABASE_URL`; apply `python -m alembic -c backend\login-service\alembic.ini upgrade head`; then deploy service. Verify against actual PostgreSQL before production auth is enabled.

## Expected lock, duration, and backfill behavior

Empty table creation/indexes; no backfill. PostgreSQL lock duration is not measured.

## Rollback or forward-recovery procedure

Before user data exists, downgrade drops all new tables. After accounts exist, prefer a forward-fix and restore only from a verified backup.

## Backup/restore, monitoring, and alerting

Backup/restore policy is not configured in the repository. Establish one before storing production accounts; monitor database health and migration failures.

## Checks run

| Check or manual steps | Environment | Result |
|---|---|---|
| Alembic upgrade, schema check, downgrade | Disposable SQLite file | Pass |
| Backend API tests | In-memory SQLite | 7 passed |

## Known limitations or risks

No PostgreSQL server or operational policy was available. SQLite does not validate PostgreSQL locking or deployment behavior.

## Handoff decision

Ready for PostgreSQL deployment rehearsal. Production rollout remains blocked on that rehearsal and backup/restore confirmation.
