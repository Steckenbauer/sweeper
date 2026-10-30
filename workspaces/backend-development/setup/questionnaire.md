# Project Setup - configure the backend workspace

One-time setup. Inspect repository manifests, service entry points, schemas, tests, and team conventions, then fill in [`../_shared/project-profile.md`](../_shared/project-profile.md). Preserve the current stack; do not add dependencies or migrate frameworks as part of this setup.

## Questions to answer

1. What runtime, language, framework, and package-manager versions does the project use?
2. Where are service entry points, API contracts, source files, tests, and migrations?
3. What exact commands start services, build, lint, type-check, test, and validate migrations?
4. Which databases, queues, caches, and external services are involved, and what are their local test conventions?
5. What authentication, authorization, data privacy, retention, and API compatibility rules apply?
6. What deployment, rollback, observability, performance, and release constraints apply?

If a value cannot be verified, leave it marked `Not configured` and ask the project owner before relying on it.
