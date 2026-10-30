# Database Quality Principles - reusable constraints

Apply these principles to every change. Follow the repository's existing patterns and the project-specific settings in [`project-profile.md`](./project-profile.md); this file does not prescribe a database engine or schema architecture.

## Data modeling and queries

- Tie every schema or query change to a named data requirement, reader/writer, and acceptance criterion.
- Preserve referential integrity and domain invariants with the strongest appropriate constraints; document intentional exceptions.
- Choose keys, types, nullability, indexes, and relationships for actual access patterns and lifecycle needs.
- Avoid unbounded scans, accidental fan-out, and unnecessary indexes; inspect representative query plans and data volumes where relevant.

## Migrations and data safety

- Follow the configured migration tooling and never modify an already-applied migration unless project policy explicitly allows it.
- Assess existing data, backfills, constraints, locks, table rewrites, duration, and failure recovery before applying a change.
- Prefer staged, backward-compatible migrations when application versions overlap; document expand/contract sequencing and rollback or forward-recovery limits.
- Test migration apply and recovery against a disposable, representative database. Never run destructive or mutating checks against production data without explicit authorization.
- Keep credentials and sensitive data out of source, fixtures, logs, and handoff artifacts; use approved local test data.

## Reliability and operations

- Match transactions and isolation to the invariants being protected; consider races, retries, and idempotency.
- Account for replication lag, connection limits, storage growth, and backup/restore implications where relevant.
- Document operational observability and a safe response if a migration or backfill is slow or fails.

## Verification

- Run applicable configured schema, migration, database, integration, and query-plan checks; record exact commands and outcomes.
- Verify both expected data behavior and relevant invalid, duplicate, boundary, and failure cases.
- Do not report unrun checks as passing. Record unavailable checks and unresolved risks in the handoff.
