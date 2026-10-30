# 04_verify_handoff - verify and record handoff

One job: verify the implemented behavior against the brief and leave a usable handoff.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Working (this run): `../02_interface_plan/output/interface-plan.md`
- Working (this run): `../03_implementation/output/implementation-record.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/frontend-quality.md`

Do NOT load: other runs, unrelated stage outputs, or the whole `../../../../_shared` folder.

## Process
1. Stop if a required input is missing, unchecked, or failed.
2. Exercise each acceptance criterion in the running application or through the project's appropriate browser tests. Check relevant viewport, keyboard, focus, and assistive-technology behavior from the plan.
3. Record what was actually checked, the exact commands or manual steps, outcomes, and any known limitations.
4. Write `check.md` beside the report, with first line exactly `pass` or `fail: <why>`. A failed check stops the run; fix the issue and repeat verification.

## Outputs
- `release-handoff.md` -> `output` (start from `../../../../_templates/artifacts/release-handoff.md`)
- `check.md` -> `output`

## Check
The requester or reviewer confirms every acceptance criterion has evidence, relevant accessibility and responsive checks are recorded, and unresolved limitations are plainly stated. Write `pass` only when the change is accepted for handoff.
