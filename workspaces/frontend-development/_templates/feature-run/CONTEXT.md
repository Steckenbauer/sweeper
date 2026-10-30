# Feature Run - one frontend change

This folder is one run. Fill in `request.md`, then complete the stages in order. The repository's application source is the implementation target; this folder stores decisions and evidence, not duplicate application code.

| Stage | Input | Output |
|---|---|---|
| [`01_scope`](stages/01_scope/CONTEXT.md) | `request.md` | `feature-brief.md` |
| [`02_interface_plan`](stages/02_interface_plan/CONTEXT.md) | `01_scope/output/feature-brief.md` | `interface-plan.md` |
| [`03_implementation`](stages/03_implementation/CONTEXT.md) | Brief and interface plan | `implementation-record.md` |
| [`04_verify_handoff`](stages/04_verify_handoff/CONTEXT.md) | Brief, plan, implementation record | `release-handoff.md`, `check.md` |

For project-specific commands and constraints, read the root `../../_shared/project-profile.md` and `_shared/frontend-quality.md` files when a stage contract names them. Stop on missing inputs or failed checks; fix the current stage before proceeding.
