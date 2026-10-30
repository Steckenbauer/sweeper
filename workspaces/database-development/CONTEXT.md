# Database Development Workspace - change workflow

The repeating unit is one database schema, query, data migration, or operational change. Copy the change starter, then move through requirements, data design, implementation, and verification/handoff. Schema and migration code remains in the project source tree; run folders hold editable decisions and evidence.

| Stage | Job | Output |
|---|---|---|
| `01_scope` | Define data requirements and acceptance criteria | `change-brief.md` |
| `02_data_design` | Specify model, access patterns, and migration strategy | `data-design.md` |
| `03_implementation` | Implement schema/query/migration and record checks | `implementation-record.md` |
| `04_verify_handoff` | Verify correctness, safety, and operational handoff | `release-handoff.md`, `check.md` |

Start from [`_templates/change-run/`](./_templates/change-run/). Each stage contract names exact inputs, output, and check. Stable constraints live in [`_shared/`](./_shared/); per-change artifacts live under `runs/<change-slug>/`. Stages 01–03 are complete when their output's `## Stage Check` says `pass`; stage 04 is complete when its `check.md` begins with `pass`. A failed or pending check blocks the next stage.
