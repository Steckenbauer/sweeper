# Data Design

## Existing schema and access paths

None exists. SQLAlchemy sessions perform exact email, provider/subject, credential-ID, and expiry lookups.

## Proposed model

| Entity/table | Keys and relationships | Important constraints | Data lifecycle |
|---|---|---|---|
| `users` | UUID-string primary key | unique indexed nullable email | Account lifetime |
| `auth_identities` | user FK with cascade | unique provider + subject | Until identity/user deletion |
| `passkey_credentials` | user FK with cascade | unique credential ID | Public key and counter until credential/user deletion |
| `oauth_codes` | user FK; hashed code PK | indexed expiry | Single use; 90-second expiry |
| `passkey_challenges` | nullable user FK | indexed expiry/purpose | Single-use; 5-minute expiry; expired rows pruned on new flow |

## Read/write patterns and query design

Authentication uses indexed exact-match reads. Provider callbacks insert identities and one-use codes transactionally. Passkey verification locks challenge/credential rows when supported.

## Indexes and expected query plans

Unique email/provider-subject/credential indexes support point lookups. User FKs and expiry timestamps are indexed. Expect index seeks; initial dataset is small.

## Volume and growth assumptions

Unknown; initially small. Expired OAuth codes are cleaned on callbacks and expired challenges on new ceremonies. Add periodic cleanup if volume warrants it.

## Migration and backfill sequence

One initial additive Alembic migration creates five empty tables and indexes. No backfill.

## Compatibility, locks, and availability

No existing consumers or production data. Apply table creation before service startup; PostgreSQL lock duration is unmeasured.

## Recovery, rollback, or forward-fix strategy

Downgrade drops all auth data and is destructive once accounts exist. Use forward-fix and verified backups thereafter.

## Privacy, retention, and deletion impact

Email and provider subject identify users. No raw passwords or OAuth codes are stored. User deletion cascades auth records. User-record retention is unspecified.

## Acceptance-criteria mapping

| Criterion | Schema/query behavior | Verification |
|---|---|---|
| Uniqueness | Unique email index, provider-subject constraint, unique credential ID | API/model test and migration check |
| Ownership | User foreign-key cascades | Migration check |
| Versioning | Alembic initial migration | Upgrade, check, downgrade on disposable SQLite |

## Decisions and open questions

PostgreSQL is the runtime target. No PostgreSQL server or restore policy is configured; the deployment owner must verify migration and backups before production.

## Stage Check

pass
