# Process state, writing, and handoff

The coordinator reads this reference when starting or resuming a full run. Specialists read the section relevant to their delegation or evidence changes. D0 and loading rules are in the [protocol](protocol.md).

## Records and statuses

Create or continue the necessary records in `profile.paths.state_dir`. Installation does not create game records. A full run maintains all records below; a focused task saves its scope without claiming full workflow coverage.

| File | Contract |
|---|---|
| `state.md` | Goal and boundaries, profile location, stages and source revisions, active delegations, blockers, and the next concrete action. |
| `source-manifest.json` | Actual game paths, SHA-256, revision/date, and a recoverable baseline; include a commit when available. |
| `findings.md` | Stable ID, severity, source/field, scenario, consequence, owner, fix, and closure evidence. |
| `coverage-matrix.md` | COV-01–20, applicability and grounds, units/families, canonical sources, tasks, QA, and limitations. |
| `subagent-review.md` | Actual review assignments, source snapshots, reviewer identities, responses, failures, and finding dispositions. A pending assignment is not a received review. |

Keep stage reports here or at established profile locations. Canonical documents retain their own locations. When an artifact is missing, use its contract in [templates.md](templates.md) without loading unrelated templates.

Stage statuses: `NOT_STARTED`, `IN_PROGRESS`, `COMPLETE`, `N_A`, `BLOCKED`, `RECHECK_REQUIRED`. `COMPLETE` applies to a result and snapshot; `N_A` requires profile evidence; `BLOCKED` names the dependency. Reuse current, unaffected evidence.

Finding severity: `BLOCKER` for undefined mandatory behavior or a broken invariant; `MAJOR` for a substantial gap or risk; `MINOR` for local clarity. Finding statuses: `OPEN`, `FIXED_PENDING_REVIEW`, `VERIFIED`, `REJECTED_WITH_REASON`. An author's claim of a fix does not replace checking the scenario.

## Before writing and after changes

Before shared changes or transfer of write ownership, preserve affected text in `snapshots/<run>/<revision>/` with original paths, or a diff with a recoverable baseline. A Git commit covers only its committed content; uncommitted changes also need a recoverable baseline. A hash alone cannot recover text.

After changes, **before updating the source manifest**, mark changed sources and affected results `RECHECK_REQUIRED`, then record the new revision without erasing the old one. Only actual rechecking restores currency. Trace downstream effects through 16; [workflow.rechecks](workflow.json) defines required repeats. Do not repeat a current check just to increase iteration counts.

## Delegation

Assign one writer per file. The coordinator owns shared records, profile, snapshots, and integration. Delegate independent domain files in parallel within available agent capacity. Provide the exact SKILL.md, task and scope, current primary sources and relevant profile fields, acceptance criteria, write ownership, and expected result. Do not rely on inherited history. Provide shared protocol and relevant conditional instructions, not all skill bodies.

Receive and examine every result; spawning an agent is not completion. After a failure, inspect partial edits and unfinished work before reassigning writes. If responsibilities overlap, send proposed changes to the owner instead of overwriting. For significant reviews, provide requirements and the snapshot without desired verdicts or author justifications. Stage 20 uses a [fresh reader](handoff-review.md) without earlier consultation history.

## Resume and conclude

On resumption, compare the request, profile and policy, state, open findings, source manifest, and unfinished delegations. Check actual versions for the next work and dependencies. Changes reopen affected scope, not automatically the entire process. Incomplete or contradictory records require recovery of the relevant diagnostics. Global acceptance checks the full agreed scope.

Stage 21 issues `READY_FOR_IMPLEMENTATION` only when mandatory contracts, units, task/QA links, risks, and current independent evidence support it. A future hypothesis has an owner, method, verification point, criterion, and consequence of failure. An unknown mandatory rule cannot be hidden in a playtest plan.

`NEEDS_REVISION` records fixable gaps and missing required evidence. `NEEDS_USER_DECISION` identifies a consequential unresolved choice. Tool failure is not a design defect or a PASS. Continue independent work while preserving the dependency. The final `readiness-report.md` states the verdict, sources, corrections, limits, and next step; it does not start implementation, an automation, or a new user task.
