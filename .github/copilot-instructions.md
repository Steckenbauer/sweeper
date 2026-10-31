Before starting work in this repository, read `workspaces/AGENTS.md` and use it to route frontend, backend, and database tasks to the appropriate workspace instructions.

If a task needs a specialized workspace that is not listed there, ask the user whether they want that workspace created before creating one. If they decline, continue the task using the repository's existing conventions.

Put implementation code in the project's source tree, not under `workspaces/`. Keep frontend and catalog UI changes in the project-root frontend/catalog area, backend changes in the backend area, and schema, query, or migration changes in the database area. Follow the repository's existing directory layout and conventions; do not create a new source directory when the project already has an established location. The `workspaces/` directories are for workflow guidance and per-change planning and handoff artifacts only.
