# Backend Development Workspace

Use this workspace to plan, implement, and verify backend changes. A completed run leaves a checked handoff; application code and migrations stay in the project source tree.

## Where things live

| Folder | What it holds |
|---|---|
| [`_shared/`](./_shared/) | Stable project profile and backend quality principles |
| [`_templates/`](./_templates/) | Copyable feature-run and artifact starters |
| [`setup/`](./setup/) | One-time project configuration questionnaire |
| `runs/<feature-slug>/` | Per-feature briefs, designs, implementation records, and verification |

## Route by task

| If | Go to |
|---|---|
| Starting a backend change | Copy [`_templates/feature-run/`](./_templates/feature-run/) to `runs/<feature-slug>/`, fill in `request.md`, then follow its `AGENTS.md` |
| Continuing a change | Open that run's `AGENTS.md` and continue at its first incomplete stage |
| Configuring the project | Complete [`setup/questionnaire.md`](./setup/questionnaire.md) in [`_shared/project-profile.md`](./_shared/project-profile.md) |
| Checking the workflow | Read [`CONTEXT.md`](./CONTEXT.md) |

Preserve the stack and existing service conventions. Do not proceed to the next stage until the current stage's check passes.
