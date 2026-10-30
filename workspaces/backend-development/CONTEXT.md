# Backend Development Workspace - feature workflow

The repeating unit is one backend feature or change. Copy the run starter, then move through scope, technical design, implementation, and verification/handoff. Application code and schema changes remain in the project source tree; run folders hold editable decisions and evidence.

| Stage | Job | Output |
|---|---|---|
| `01_scope` | Define the user/system outcome and acceptance criteria | `feature-brief.md` |
| `02_technical_design` | Specify API, data, compatibility, and failure behavior | `technical-design.md` |
| `03_implementation` | Implement the design and record code changes/checks | `implementation-record.md` |
| `04_verify_handoff` | Verify behavior and record operational handoff | `release-handoff.md`, `check.md` |

Start from [`_templates/feature-run/`](./_templates/feature-run/). Each stage contract names exact inputs, output, and check. Stable constraints live in [`_shared/`](./_shared/); per-feature artifacts live under `runs/<feature-slug>/`. Stages 01–03 are complete when their output's `## Stage Check` says `pass`; stage 04 is complete when its `check.md` begins with `pass`. A failed or pending check blocks the next stage.
