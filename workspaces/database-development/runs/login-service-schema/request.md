# Database Change Request

## Data or operational problem

The new login service requires durable PostgreSQL storage for accounts, external provider subjects, passkey public credentials, and short-lived auth ceremony state.

## Requested outcome

Create a versioned additive schema migration for the login-service entities with uniqueness, foreign-key cascades, and indexes supporting authentication lookups and expiry cleanup.

## Affected systems and consumers

The FastAPI login service is the only known writer and consumer. No existing database or schema is configured.

## Known constraints

PostgreSQL is the selected runtime database. Do not store raw passwords, OAuth codes, access tokens, or WebAuthn private keys. Downgrading the initial schema is data-destructive.

## References

The requester selected PostgreSQL and approved the login-service design.
