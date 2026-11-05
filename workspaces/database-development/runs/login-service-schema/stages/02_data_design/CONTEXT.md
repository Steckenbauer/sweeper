# 02_data_design - design the schema and migration

One job: turn the accepted requirements into a reviewable data model, query, and migration design.

## Inputs
- Working (this run): `../01_scope/output/change-brief.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/database-quality.md`

Do NOT load: other runs, unrelated stage outputs, production row data, or the whole `_shared/` folder.

## Process
1. If the brief is missing, unchecked, or unclear, stop and identify the gap.
2. Inspect relevant schemas, migration history, data-access paths, and representative query plans. Map each criterion to a schema, query, constraint, or lifecycle change.
3. Specify keys, types, nullability, constraints, indexes, expected access patterns, estimated data scale, migration/backfill steps, compatibility window, lock/availability risks, and recovery strategy. Mark non-applicable items with a reason; identify unresolved decisions.

## Outputs
- `data-design.md` -> `output/` (start from `../../../../_templates/artifacts/data-design.md`)

## Check
The requester or database owner confirms the model serves known consumers, preserves required invariants, and has an acceptable migration and recovery plan. Resolve material data-loss, compatibility, privacy, or lock-risk questions before implementation. Under `## Stage Check`, write `pass` or `fail: <why>`.
