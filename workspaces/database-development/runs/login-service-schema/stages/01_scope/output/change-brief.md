# Database Change Brief

## Data need and affected consumers

The login service needs persistent users and authentication material. It is the only known reader/writer.

## Desired outcome

An Alembic-managed PostgreSQL schema for accounts, external identities, passkey public credentials, OAuth codes, and passkey challenges.

## In scope

Create constraints and indexes; enforce identity and email uniqueness; cascade owned records when users are deleted; expire and remove one-time flow data.

## Out of scope

Existing data migration, production operations, backups, and provider ingestion; no existing schema is present.

## Data lifecycle and sensitivity

Store password hashes, public passkey keys, provider subject/email values, and temporary flow records. OAuth code values are stored as hashes. Expired flow data is removed as subsequent flows are created. Auth data is sensitive.

## Acceptance criteria

- [x] Constraints prevent duplicate email, provider subject, and passkey credential identifiers.
- [x] Foreign keys associate credentials and identities with users and cascade deletion.
- [x] Migration can upgrade/downgrade an isolated database and matches SQLAlchemy metadata.

## Assumptions and open questions

Requester selected PostgreSQL. Data volume is initially small; no existing data or production schema exists. PostgreSQL runtime verification remains a deployment check.

## Stage Check

pass
