# Database Change Run - one schema or data change

This folder is one run. Fill in `request.md`, then complete the stages in order. The repository's schemas, queries, and migrations are the implementation targets; this folder stores decisions and evidence, not duplicate database code.

| Stage | Input | Output |
|---|---|---|
| [`01_scope`](stages/01_scope/CONTEXT.md) | `request.md` | `change-brief.md` |
| [`02_data_design`](stages/02_data_design/CONTEXT.md) | `01_scope/output/change-brief.md` | `data-design.md` |
| [`03_implementation`](stages/03_implementation/CONTEXT.md) | Brief and data design | `implementation-record.md` |
| [`04_verify_handoff`](stages/04_verify_handoff/CONTEXT.md) | Brief, design, implementation record | `release-handoff.md`, `check.md` |

For project-specific commands and constraints, read the database workspace's `../../../../_shared/project-profile.md` and `_shared/database-quality.md` files when a stage contract names them. Stop on missing inputs or failed checks. Never run destructive or mutating checks against production without explicit authorization.
