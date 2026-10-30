# 03_implementation - build the planned change

One job: implement the accepted interface plan in the existing application.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Working (this run): `../02_interface_plan/output/interface-plan.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/frontend-quality.md`

Do NOT load: other runs, unrelated stage outputs, or the whole repository. Inspect only files needed to follow local patterns and make the change.

## Process
1. Stop if either working input is missing or has not passed its check.
2. Implement the smallest coherent change in the project's existing source tree. Do not introduce a new framework or dependency without approval.
3. Run applicable configured checks from the project profile. Record exact commands, results, and any checks not run.
4. Record changed files, notable implementation decisions, and remaining risks.

## Outputs
- `implementation-record.md` -> `output` (start from `../../../../_templates/artifacts/implementation-record.md`)

## Check
The requester or code reviewer compares the diff with the brief and plan, confirms applicable configured checks passed, and accepts any explicitly documented unavailable check or risk. Under `## Stage Check`, write `pass` or `fail: <why>`. Do not claim completion while a configured check is failing.
