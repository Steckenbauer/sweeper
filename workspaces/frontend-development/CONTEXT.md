# Frontend Development Workspace - feature workflow

The repeating unit is one frontend feature or change. Copy the run starter, then move through scope, interface plan, implementation, and verification/handoff. Application code remains in the project source tree; run folders hold editable decisions and evidence.

| Stage | Job | Output |
|---|---|---|
| `01_scope` | Define the user outcome and acceptance criteria | `feature-brief.md` |
| `02_interface_plan` | Specify UI states, behavior, and responsive/accessibility needs | `interface-plan.md` |
| `03_implementation` | Implement the plan and record the code changes/checks | `implementation-record.md` |
| `04_verify_handoff` | Verify acceptance criteria and record handoff | `release-handoff.md`, `check.md` |

Start from [`_templates/feature-run/`](./_templates/feature-run/). Each stage contract names its exact inputs, output, and check. Stable constraints live in [`_shared/`](./_shared/); per-feature artifacts live under `runs/<feature-slug>/`. Stages 01–03 are complete when their output's `## Stage Check` says `pass`; stage 04 is complete when its `check.md` begins with `pass`. A failed or pending check blocks the next stage.
