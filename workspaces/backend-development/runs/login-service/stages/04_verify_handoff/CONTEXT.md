# 04_verify_handoff - verify and record handoff

One job: verify the service behavior against the brief and leave an operationally useful handoff.

## Inputs
- Working (this run): `../01_scope/output/feature-brief.md`
- Working (this run): `../02_technical_design/output/technical-design.md`
- Working (this run): `../03_implementation/output/implementation-record.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/backend-quality.md`

Do NOT load: other runs, unrelated stage outputs, or the whole `_shared/` folder.

## Process
1. Stop if a required input is missing, unchecked, or failed.
2. Verify each acceptance criterion with appropriate unit, integration, contract, migration, or manual checks. Exercise relevant validation, authorization, and error paths.
3. Review compatibility, migration and rollback implications, and operational signals. Record exact commands or manual steps, outcomes, and known limitations.
4. Write `check.md` beside the report, with first line exactly `pass` or `fail: <why>`. A failed check stops the run; fix the issue and repeat verification.

## Outputs
- `release-handoff.md` -> `output/` (start from `../../../../_templates/artifacts/release-handoff.md`)
- `check.md` -> `output/`

## Check
The requester or reviewer confirms every acceptance criterion has evidence, relevant compatibility and operational concerns are documented, and unresolved limitations are plainly stated. Write `pass` only when the change is accepted for handoff.
