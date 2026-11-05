# 04_verify_handoff - verify and record database handoff

One job: verify the data change and leave a safe operational handoff.

## Inputs
- Working (this run): `../01_scope/output/change-brief.md`
- Working (this run): `../02_data_design/output/data-design.md`
- Working (this run): `../03_implementation/output/implementation-record.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/database-quality.md`

Do NOT load: other runs, unrelated stage outputs, production row data, or the whole `_shared/` folder.

## Process
1. Stop if a required input is missing, unchecked, or failed.
2. Verify each acceptance criterion against an isolated, representative database. Check constraints, expected and invalid data behavior, migration apply, relevant rollback/forward recovery, and query plans as applicable.
3. Assess lock duration, backfill progress/resumability, compatibility, backup/restore impact, and monitoring. Record exact commands or manual steps, outcomes, and known limitations.
4. Write `check.md` beside the report, with first line exactly `pass` or `fail: <why>`. A failed check stops the run; fix the issue and repeat verification.

## Outputs
- `release-handoff.md` -> `output/` (start from `../../../../_templates/artifacts/release-handoff.md`)
- `check.md` -> `output/`

## Check
The requester or database owner confirms evidence covers the acceptance criteria, rollout and recovery are understood, and operational risks are documented. Write `pass` only when the change is accepted for handoff. Do not run checks that mutate production without explicit authorization.
