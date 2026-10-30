# Database Development Workspace

Use this workspace to plan, implement, and verify database changes. A completed run leaves a checked handoff; schema and migration code stays in the project source tree.

## Where things live

| Folder | What it holds |
|---|---|
| [`_shared/`](./_shared/) | Stable database profile and quality principles |
| [`_templates/`](./_templates/) | Copyable change-run and artifact starters |
| [`setup/`](./setup/) | One-time project configuration questionnaire |
| `runs/<change-slug>/` | Per-change requirements, designs, implementation records, and verification |

## Route by task

| If | Go to |
|---|---|
| Starting a database change | Copy [`_templates/change-run/`](./_templates/change-run/) to `runs/<change-slug>/`, fill in `request.md`, then follow its `AGENTS.md` |
| Continuing a change | Open that run's `AGENTS.md` and continue at its first incomplete stage |
| Configuring the project | Complete [`setup/questionnaire.md`](./setup/questionnaire.md) in [`_shared/project-profile.md`](./_shared/project-profile.md) |
| Checking the workflow | Read [`CONTEXT.md`](./CONTEXT.md) |

Preserve the existing database technology and conventions. Treat production data and migrations as sensitive, irreversible assets; do not proceed to the next stage until the current stage's check passes.
