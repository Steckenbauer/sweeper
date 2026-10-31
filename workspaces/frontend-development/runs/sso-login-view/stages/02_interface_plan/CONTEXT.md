# 02_interface_plan - plan states and interactions

One job: translate the accepted brief into a reviewable interface and behavior plan.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/frontend-quality.md`

Do NOT load: other runs, unrelated stage outputs, or the whole `../../../../_shared` folder.

## Process
1. If the brief is missing, unchecked, or unclear, stop and identify the gap.
2. Inspect only the relevant existing UI and project conventions. Map each acceptance criterion to a screen, state, or interaction.
3. Specify relevant loading/empty/error/success states, responsive behavior, keyboard interaction, and accessible names. Mark items that do not apply with a reason.

## Outputs
- `interface-plan.md` -> `output` (start from `../../../../_templates/artifacts/interface-plan.md`)

## Check
The requester or design owner confirms the proposed behavior and states satisfy the brief and fit the existing product. Resolve material design or behavior questions before implementation. Under `## Stage Check`, write `pass` or `fail: <why>`.
