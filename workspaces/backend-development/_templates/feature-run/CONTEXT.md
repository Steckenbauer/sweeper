# Backend Feature Run - one backend change

This folder is one run. Fill in `request.md`, then complete the stages in order. The repository's application source, API schemas, and migrations are the implementation targets; this folder stores decisions and evidence, not duplicate service code.

| Stage | Input | Output |
|---|---|---|
| [`01_scope`](stages/01_scope/CONTEXT.md) | `request.md` | `feature-brief.md` |
| [`02_technical_design`](stages/02_technical_design/CONTEXT.md) | `01_scope/output/feature-brief.md` | `technical-design.md` |
| [`03_implementation`](stages/03_implementation/CONTEXT.md) | Brief and technical design | `implementation-record.md` |
| [`04_verify_handoff`](stages/04_verify_handoff/CONTEXT.md) | Brief, design, implementation record | `release-handoff.md`, `check.md` |

For project-specific commands and constraints, read the backend workspace's `../../../../_shared/project-profile.md` and `_shared/backend-quality.md` files when a stage contract names them. Stop on missing inputs or failed checks; fix the current stage before proceeding.
