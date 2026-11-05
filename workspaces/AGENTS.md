# Development Workspaces

This folder contains separate, stack-agnostic workflows for frontend, backend, and database development. Each workspace owns its project profile, reusable guidance, and feature-run template.

| If the work is about | Go to |
|---|---|
| UI, browser behavior, or accessibility | [`frontend-development/AGENTS.md`](./frontend-development/AGENTS.md) |
| Creating web/UI or standalone 2D/3D animations | [`animation-development/AGENTS.md`](./animation-development/AGENTS.md) |
| APIs, services, or backend operations | [`backend-development/AGENTS.md`](./backend-development/AGENTS.md) |
| Schemas, queries, migrations, or database operations | [`database-development/AGENTS.md`](./database-development/AGENTS.md) |
| Creating or restructuring a workspace | [ICM Architect skill](../.github/skills/icm-architect/SKILL.md) |

## Cross-domain requests

For a request that spans multiple domains, use the relevant workspaces above and coordinate them in parallel when their work can be done independently:

1. Split the request into bounded packages with clear ownership, inputs, outputs, and checks. Each worker must read the `AGENTS.md` for its domain.
2. Resolve shared contracts and prerequisites first. Do not dispatch conflicting edits to the same files; assign shared files to one owner.
3. Use the available agent runtime to start independent packages concurrently. Wait for all workers, review their handoffs, integrate their changes, and run combined checks.
4. If parallel workers are unavailable, follow the same domain routing sequentially and state that parallel execution was unavailable.

Single-domain requests should go directly to that domain workspace. Keep plans and handoffs in the applicable per-change run; do not create a separate orchestration workspace.
