# 01_scope - define the backend outcome

One job: turn the request into a small, testable feature brief.

## Inputs
- Working (this run): `../../request.md`
- Reference (every run): `../../../../_shared/project-profile.md`

Do NOT load: other runs, unrelated stage outputs, or the whole repository when a targeted inspection answers the question.

## Process
1. If the request is missing or unclear, stop and identify the specific gap.
2. Describe the caller or affected system, problem, desired behavior, in-scope behavior, assumptions, and exclusions.
3. Write observable acceptance criteria, including relevant boundary, failure, and compatibility cases.

## Outputs
- `feature-brief.md` -> `output/` (start from `../../../../_templates/artifacts/feature-brief.md`)

## Check
The requester or service owner confirms the outcome, scope, and acceptance criteria are correct and testable. Record accepted assumptions in the brief. Under `## Stage Check`, write `pass` or `fail: <why>`; do not proceed on unresolved scope.
