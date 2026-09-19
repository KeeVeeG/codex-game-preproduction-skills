---
name: 14-game-architecture-review
description: Independently audit game architecture documentation for requirement coverage, ambiguous system contracts, conflicting decisions, and unsupported technical assumptions.
---

# 14 — Independent architecture review

Role: an independent Codex subagent with technical review expertise. Follow the [protocol](../00-game-preproduction/references/protocol.md), its source-loading rules, and the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Review D0 documentation; missing future builds or tests must not be replaced with code or invented PASS results. If delegation is unavailable, record pending independent evidence and continue useful checks without presenting self-review as independent acceptance.

## Inputs and completeness

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Resolve `profile.sources.architecture`, `decisions`, `controls`, `risks`, `content`, and primary requirements to actual paths. On later passes, add `epics`, `stories`, `qa`, `production`, and current `reviews`. Read linked content, not just link tables. Give a fresh reviewer sources and scope without author conclusions or reasoning history.

Record scope, source versions/hashes, requirements actually examined, and unreviewed remainder. A full pass covers the entire agreed scope; limited review cannot give a project-wide verdict. Preserve IDs between passes. Use `profile.features`: absence needs a reason, source, and reopening condition; unknown applicability is not N/A.

For non-digital games, review rules, information states, participants, and physical components. Do not demand software modules or APIs without a digital component. Testing for incompatible interpretations still applies.

An initial review may precede the 15a risk register and stories. Hand future consumers to their stages without claiming final readiness. Missing sources required by this current stage are gaps.

## Review

1. Independently extract requirements and check source → requirement → owner/contract → ADR where needed → dependent task/check. Distinguish full/partial coverage, gaps, and justified N/A. Accepted direct contracts are allowed without separate ADRs.
2. Compare overlapping decisions about ownership, interfaces, authority, event order, time, storage, budgets, and errors. For every mandatory cross-system contract, try to construct two incompatible implementations that both comply with its text. If possible, show both interpretations, their observable difference, and the missing rule. Different internals satisfying the same external contract are allowed. Agreement between files alone does not prove unambiguity.
3. Check dependency order, cycles, missing prerequisites, and compatible ADR statuses. Reverse the mapping: every module and significant decision must serve a requirement rather than silently expand the product.
4. Trace core actions and dangerous end-to-end flows: normal paths, cancellation, repetition, lateness, and partial failures where possible. Identify preserved invariants and confirmation points. Choose appropriate scenarios for actual asynchronous operations, shared state, saves, or external services; do not invent network tests for an offline product.
5. Verify material API/SDK/format claims against official sources for the actual version. Unknown support is neither proven available nor prohibited. Separate documented capabilities from unverified integration.
6. Check combined budgets, simultaneous load, pipeline repeatability, diagnostics, and recovery. Material unknowns need an owner, `PLANNED` experiment, decision criterion, and dependent tasks. An absent optional service, technology, or tool is not a defect.
7. On later passes, connect contracts to epics, stories, controls, and QA; planned tests are not completed tests. Recheck previous reviews after changes rather than applying an old positive verdict to new sources.

## Output and decision

Write the scoped `architecture-review.md` under `profile.paths.state_dir` or the existing `reviews` location. Include sources/versions, coverage, incompatible interpretations, conflicts, dependencies, evidence limits, and closure conditions. Do not create competing reports. D0 architecture verdicts are `PASS`, `CONCERNS`, or `FAIL`; uncovered mandatory contracts and invariant violations exclude `PASS`.

Do not edit author specifications during this review. Send repairs to [12](../12-game-create-architecture/SKILL.md)/[13](../13-game-architecture-decision/SKILL.md), and requirement changes through [16](../16-game-propagate-design-change/SKILL.md). Give shared entries to the coordinator. After affected contracts are rechecked, accepted architecture proceeds to [15](../15-game-create-control-manifest/SKILL.md).
