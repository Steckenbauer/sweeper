# 04_verify_handoff - verify browser behavior and hand off

One job: check the implemented animation against its acceptance criteria and leave a usable handoff.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Working (this run): `../02_motion_plan/output/motion-plan.md`
- Working (this run): `../03_implementation/output/implementation-record.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/animation-principles.md`

## Process
1. Stop if any required input is missing or unchecked.
2. Exercise each acceptance criterion in the browser or with configured project tests.
3. Verify reduced-motion behavior, relevant interaction/focus states, and target viewports.
4. Record exact checks, results, limitations, and any unrun checks.

## Outputs
- `release-handoff.md` -> `output/`
- `check.md` -> `output/` (first line `pass` or `fail: <why>`)

## Check
The requester or reviewer confirms acceptance evidence is complete and limitations are explicit. Write `pass` only when the deliverable is ready for handoff.
