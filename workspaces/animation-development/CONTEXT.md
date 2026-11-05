# Animation Development - choose a workflow by deliverable

One job: guide an animation request into the right workflow and checked deliverable.

## Inputs
- Working (this run): the user's animation request and relevant project state
- Reference (every run): `AGENTS.md`
- Reference (every run): `_shared/animation-principles.md`
- Reference (when needed): `_shared/project-profile.md`

Do NOT load both run templates unless the request needs both web integration and standalone production. Do NOT infer unspecified tools, platforms, or delivery formats.

## Process
1. Identify whether the deliverable is browser-integrated motion, a standalone 2D/3D animation, or both.
2. Copy the corresponding run template into `runs/<animation-slug>/` and fill in its `request.md`.
3. Follow that run's stages in order; get each named check before proceeding.
4. Create implementation code or animation assets only in the agreed project source or delivery tree. Keep the run folder for plans and handoffs.
5. Verify the deliverable against the request, applicable accessibility/performance or render/export requirements, and record unrun checks and limitations.

## Outputs
- A checked web/UI animation, standalone animation, or coordinated pair of deliverables
- A run-folder handoff with decisions and verification evidence

## Check
The requester or reviewer confirms the correct workflow was used, the deliverable meets the request, applicable checks passed, and limitations are explicit.
