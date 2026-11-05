# 02_motion_plan - specify browser motion and fallbacks

One job: make the accepted brief implementable and reviewable before code changes.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Reference (every run): `../../../../_shared/animation-principles.md`
- Reference (every run): `../../../../_shared/project-profile.md`

Do NOT load unrelated runs or introduce unrequested product behavior.

## Process
1. Stop if the brief is missing, unchecked, or unclear.
2. Inspect relevant existing UI and motion conventions.
3. Specify triggers, sequence, timing, easing, states, and interaction behavior.
4. Define reduced-motion behavior, relevant viewport support, and how the motion will be checked.

## Outputs
- `motion-plan.md` -> `output/`

## Check
The requester or design owner approves the plan, including reduced-motion behavior and relevant interaction states. Record `pass` or `fail: <why>` under `## Stage Check`.
