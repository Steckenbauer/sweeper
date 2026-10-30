# Backend Quality Principles - reusable constraints

Apply these principles to every change. Follow the repository's existing patterns and the project-specific settings in [`project-profile.md`](./project-profile.md); this file does not prescribe a framework or architecture.

## Contracts and behavior

- Tie the change to the feature brief's outcome and observable acceptance criteria.
- Preserve existing API and event behavior unless the brief explicitly authorizes a change. Document compatibility and rollout implications.
- Validate untrusted input at system boundaries and return consistent, documented errors without leaking internals.
- Consider relevant not-found, conflict, unavailable-dependency, timeout, and partial-failure behavior.

## Data and reliability

- Preserve data integrity with the repository's transaction, constraint, and concurrency patterns.
- Make schema and data migrations safe for the configured deployment and rollback strategy; consider old and new application versions during rollout.
- Use retries, timeouts, idempotency, and caching only where appropriate to the existing system's semantics.
- Avoid unbounded work, queries, or payloads; follow configured performance and capacity constraints.

## Security and operations

- Enforce authentication and authorization on the server for every protected operation; do not trust caller-supplied identity or access decisions.
- Minimize sensitive data collection and exposure. Never log credentials, tokens, secrets, or unnecessary personal data.
- Keep secrets in the project's approved secret-management mechanism; do not hardcode them.
- Emit useful, appropriately redacted diagnostics using existing logging and observability conventions.

## Verification

- Run applicable configured lint, type, unit, integration/contract, and migration checks; record exact commands and outcomes.
- Test boundary validation, authorization, error paths, and data changes relevant to the acceptance criteria.
- Do not report unrun checks as passing. Record unavailable checks and unresolved risks in the handoff.
