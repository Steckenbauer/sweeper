# 02_technical_design - design the service change

One job: translate the accepted brief into a reviewable API, data, and failure-behavior design.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/backend-quality.md`

Do NOT load: other runs, unrelated stage outputs, or the whole `_shared/` folder.

## Process
1. If the brief is missing, unchecked, or unclear, stop and identify the gap.
2. Inspect relevant existing handlers, contracts, schemas, and tests. Map each acceptance criterion to an interface, data, or behavior change.
3. Describe validation, authentication/authorization, error behavior, data integrity, compatibility and rollout, and relevant observability. Mark non-applicable items with a reason; identify unresolved decisions.

## Outputs
- `technical-design.md` -> `output/` (start from `../../../../_templates/artifacts/technical-design.md`)

## Check
The requester or service owner confirms the design satisfies the brief and fits system conventions. Resolve material contract, data, security, or rollout questions before implementation. Under `## Stage Check`, write `pass` or `fail: <why>`.
