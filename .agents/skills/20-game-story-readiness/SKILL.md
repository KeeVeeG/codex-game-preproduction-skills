---
name: 20-game-story-readiness
description: Independently check game task specifications, dependencies, and QA, including handoff of actual documentation to a fresh Codex subagent without author history.
---

# 20 — Story readiness

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Review D0 documentation; the report does not establish completed stories or a ready build. Do not edit stories while reviewing them.

## Inputs

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Read `profile.sources.stories`, `epics`, `architecture`, `decisions`, `controls`, `qa`, `content`, `risks`, `production`, `reviews`, and primary requirements. Use 11a, 15a, and current 17a results. Missing sources required by this checkpoint are `GAP`; narrow early passes may hand future work to its stage but cannot declare the whole game ready.

Scope is a story, epic, or `all`. For `all`, independently reconcile the full task plan with actual files, agreed scope, and content units. Record versions/hashes, coverage, and unread remainder. N/A under `profile.features` needs a reason, evidence, and reopening condition; `unknown` and “not yet documented” are not N/A.

## Review

1. Verify each requirement against a real ID/anchor and current source text. Criteria must be self-contained and observable; formatting and item counts do not prove completeness.
2. Check accepted decisions, control-manifest version, interfaces, state owners, and applicable technology constraints. Unverified or inaccessible normative references remain gaps. Rules must preserve source meaning, including whom they bind and which violation they prevent.
3. Check boundaries, roles, dependencies, and cycles. Predecessors can be unimplemented, but mandatory specifications/contracts must exist. Unaccepted, contradictory, or unresolved contracts block dependent tasks' documentary readiness; future execution order is assessed separately.
4. Map each criterion to a QA case and future evidence. Visual/audio results and game feel need observation methods and decision criteria; a path to a nonexistent evidence file is insufficient. Check preservation of required experience and detection of harmful simplification where applicable. Future game deliverables are allowed with sufficient specifications and explicit production tasks.
5. Preserve numeric and hypothesis status. Tuning with an owner, testable hypothesis, and revision criterion is allowed; unknown mandatory rules, outcomes, or authority are blockers. Missing future gameplay tests alone do not indicate a D0 defect.
6. Reconcile all agreed 11a content with code, content, tooling, verification, and applicable delivery tasks. Each unit needs an outcome, accepting role, dependencies, risks, and verification method. `PLANNED` cannot replace a missing specification. Send unsupported capacity or external waits to 17a; a correctly formatted story does not resolve them.

## Handoff without author history

Perform a separate [handoff review](../00-game-preproduction/references/handoff-review.md) on selected deliverables of every present type and unique risky contracts. An actual fresh Codex subagent receives only the real documentation files, their normative references, and a neutral request to reconstruct the contract. Do not pass author explanations, expected verdicts, reasoning history, or prior consultation conclusions. The reader must not inherit the author's conversation. For future game assets, review their actual specifications rather than imagined implementations.

Record the reader's actual response: reconstructed contract, required assumptions, and unreadable files. Fix unknown contracts in documentation; oral author explanations do not close them. Sampling supplements full story review and cannot replace it. If independent delegation is unavailable, record pending evidence and continue independent work; self-review is not independent acceptance. This clean-context reader is distinct from broader checkpoint consultation.

## Output

Update the existing `reviews` report or `story-readiness.md` under `profile.paths.state_dir`. Include scope/versions, each examined story's status, unreviewed remainder, handoff results, findings with paths/IDs, and closure conditions. Statuses: `READY` for sufficient specification; `NEEDS_WORK` for repairable gaps; `BLOCKED` for missing mandatory decisions/contracts. Do not extend a limited result to the whole game.

Return fixes to [18](../18-game-create-stories/SKILL.md)/[19](../19-game-qa-plan/SKILL.md). After full stage 20, the coordinator conducts MR-HANDOFF before [21](../21-game-gate-check/SKILL.md) when `profile.review.required` requires it, using an independent Codex subagent under the [review protocol](../00-game-preproduction/references/subagent-review.md). Policy changes need a basis in the user's decision, not reviewer convenience. Checkpoint consultation does not replace the separate fresh reader. Missing required responses remain pending while available fixes continue. Send shared entries to the coordinator; do not start implementation.
