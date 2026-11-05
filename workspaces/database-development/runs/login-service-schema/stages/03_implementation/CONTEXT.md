# 03_implementation - implement the database change

One job: implement the accepted schema, query, or migration design in the existing project.

## Inputs
- Working (this run): `../01_scope/output/change-brief.md`
- Working (this run): `../02_data_design/output/data-design.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/database-quality.md`

Do NOT load: other runs, unrelated stage outputs, production data, or the whole repository. Inspect only files needed to follow local patterns and make the change.

## Process
1. Stop if either working input is missing or has not passed its check.
2. Implement the smallest coherent schema/query/migration change using existing tooling. Do not introduce a new engine or dependency without approval; never rewrite applied migration history contrary to project policy.
3. Run applicable configured checks against a disposable or approved non-production database. Record exact commands, results, and any checks not run.
4. Record changed files, migration sequencing, estimated operational impact, recovery limitations, and remaining risks.

## Outputs
- `implementation-record.md` -> `output/` (start from `../../../../_templates/artifacts/implementation-record.md`)

## Check
The requester or database reviewer compares the diff with the brief and design, confirms checks are safe and applicable configured checks pass, and accepts any explicitly documented unavailable check or risk. Under `## Stage Check`, write `pass` or `fail: <why>`. Do not claim completion while a configured check is failing.
