# Animation Development Workspace

Use this workspace to plan and create either web/UI animations or standalone 2D/3D animation deliverables. Choose the workflow based on the output; application code and rendered assets stay in the project's source or delivery tree, not in this workspace.

## Where things live

| Folder | What it holds |
|---|---|
| [`_shared/animation-principles.md`](./_shared/animation-principles.md) | Shared motion, clarity, and quality guidance |
| [`_shared/project-profile.md`](./_shared/project-profile.md) | Known web and standalone toolchain and delivery constraints |
| [`setup/questionnaire.md`](./setup/questionnaire.md) | One-time project/toolchain configuration |
| [`_templates/web-animation-run/`](./_templates/web-animation-run/) | Copyable web/UI animation workflow |
| [`_templates/standalone-animation-run/`](./_templates/standalone-animation-run/) | Copyable standalone 2D/3D workflow |
| `runs/<animation-slug>/` | Per-animation briefs, plans, and verification records |

## Route by task

| If | Go to |
|---|---|
| Animating a website, app, or interactive browser experience | Copy `_templates/web-animation-run/` to `runs/<animation-slug>/` |
| Creating a standalone 2D/3D animation or rendered sequence | Copy `_templates/standalone-animation-run/` to `runs/<animation-slug>/` |
| Creating an animation that needs both web integration and standalone production | Use both workflows; agree the asset/interface handoff and ownership before implementation |
| Configuring known tools or delivery requirements | Complete `setup/questionnaire.md` in `_shared/project-profile.md` |

Follow the selected run's `AGENTS.md` and stage checks in order. Do not assume a framework, animation library, DCC application, renderer, or export format that the project profile or requester has not specified.
