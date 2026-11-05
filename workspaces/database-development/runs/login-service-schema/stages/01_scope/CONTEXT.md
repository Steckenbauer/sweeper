# 01_scope - define the data change

One job: turn the request into clear data requirements and testable acceptance criteria.

## Inputs
- Working (this run): `../../request.md`
- Reference (every run): `../../../../_shared/project-profile.md`

Do NOT load: other runs, unrelated stage outputs, production data, or the whole repository when a targeted inspection answers the question.

## Process
1. If the request is missing or unclear, stop and identify the specific gap.
2. Identify affected entities, data lifecycle, writers/readers, consumers, and relevant existing behavior.
3. Write observable acceptance criteria, including integrity, compatibility, volume, privacy, and failure cases where relevant. Flag destructive actions and unresolved data ownership.

## Outputs
- `change-brief.md` -> `output/` (start from `../../../../_templates/artifacts/change-brief.md`)

## Check
The requester or data owner confirms the need, affected consumers, scope, and acceptance criteria. Record accepted assumptions in the brief. Under `## Stage Check`, write `pass` or `fail: <why>`; do not proceed with unknown ownership or unresolved destructive scope.
