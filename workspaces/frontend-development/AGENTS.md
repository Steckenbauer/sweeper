# Frontend Development Workspace

Use this workspace to plan, implement, and verify frontend changes. A completed run leaves a checked release handoff; application code stays in the project source tree.

## Where things live

| Folder | What it holds |
|---|---|
| [`../../_shared`](./_shared/) | Stable project profile and frontend quality principles |
| [`../../_templates`](./_templates/) | Copyable feature-run and artifact starters |
| [`../../setup`](./setup/) | One-time project configuration questionnaire |
| `runs/<feature-slug>/` | Per-feature briefs, plans, records, and verification |

## Route by task

| If | Go to |
|---|---|
| Starting a feature | Copy [`../../_templates/feature-run`](./_templates/feature-run/) to `runs/<feature-slug>/`, fill in `request.md`, then follow its `AGENTS.md` |
| Continuing a feature | Open that run's `AGENTS.md` and continue at its first incomplete stage |
| Configuring the project | Complete [`setup/questionnaire.md`](./setup/questionnaire.md) in [`_shared/project-profile.md`](./_shared/project-profile.md) |
| Checking the workflow | Read [`CONTEXT.md`](./CONTEXT.md) |

Keep the stack and existing project conventions; do not move to the next stage until the current stage's check passes.
