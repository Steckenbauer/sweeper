# Project Setup - configure the database workspace

One-time setup. Inspect repository manifests, schema definitions, migration history, test configuration, and operating procedures, then fill in [`../_shared/project-profile.md`](../_shared/project-profile.md). Preserve the current database technology; do not add dependencies or migrate engines as part of this setup.

## Questions to answer

1. Which database engine, version, topology, and hosting model are used in each environment?
2. Where are schemas, migrations, fixtures, and data-access code, and which tools own them?
3. What exact commands safely start/reset local databases, apply/roll back migrations, run tests, and detect schema drift?
4. What data volumes, important access patterns, query SLAs, and growth expectations should inform design?
5. What data classification, privacy, retention, deletion, and safe test-data rules apply?
6. What backup/restore, availability, lock-time, rollout, and production change-approval requirements apply?

If a value cannot be verified, leave it marked `Not configured` and ask the database owner before relying on it. Do not copy production data into a development environment unless an approved process explicitly permits it.
