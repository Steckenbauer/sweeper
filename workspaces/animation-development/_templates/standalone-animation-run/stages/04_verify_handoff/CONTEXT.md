# 04_verify_handoff - verify playback and delivery

One job: verify the rendered deliverable and leave clear source and export handoff details.

## Inputs
- Working (this run): `../01_scope/output/animation-brief.md`
- Working (this run): `../02_storyboard/output/storyboard.md`
- Working (this run): `../03_production/output/production-record.md`
- Reference (every run): `../../../../_shared/project-profile.md`
- Reference (every run): `../../../../_shared/animation-principles.md`

## Process
1. Stop if any required input is missing or unchecked.
2. Open and play the final export in the agreed target environment.
3. Check required dimensions, duration, frame rate, format, visual continuity, and audio/alpha where applicable.
4. Record exact commands/settings, playback checks, source and export locations, and limitations.

## Outputs
- `release-handoff.md` -> `output/`
- `check.md` -> `output/` (first line `pass` or `fail: <why>`)

## Check
The requester or reviewer confirms the deliverable opens and meets its agreed criteria, editable sources are accounted for, and limitations are explicit. Write `pass` only when it is ready for handoff.
