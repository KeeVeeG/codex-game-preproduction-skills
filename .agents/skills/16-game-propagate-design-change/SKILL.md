---
name: 16-game-propagate-design-change
description: Trace and synchronize the documentary impact of changes to game rules or scope across data, UX, content, architecture, and production tasks, with or without Git.
---

# 16 — Propagate a design change

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Use this procedure at any stage when rules, interfaces, tuning, or scope change. It covers agreed D0 documentation and does not start implementation.

## Inputs

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Resolve the changed rule and applicable `content`, `architecture`, `decisions`, `controls`, `risks`, `epics`, `production`, `stories`, `qa`, `release`, and `reviews` through `profile.sources`. Early passes use the system map and primary documents; mark future consumers as planned rather than existing.

Require the changed document/catalog and a verifiable before-state: snapshot, explicit diff, previous file, or precise revision in an existing Git repository. Git is optional; do not initialize a repository or create a branch merely for comparison. If the before-state is unavailable, analyze current dependencies and explicitly limit claims about completeness of detected changes.

Compare proposals with previously accepted, rejected, and superseded options. For a returning option, record the previous rationale and what changed: evidence, context, or the user's current decision. Failure to find history does not prove a previous rejection. Current instructions may revise an old choice without another permission request.

## Work

1. Record provenance, versions, and comparison boundaries. Preserve a recoverable before-state before planned edits, following the protocol. Do not modify snapshots, original reviews, or receipts; new evidence belongs to a new version.
2. Identify affected requirements, states, formulas, content units, and acceptance criteria for each change. Preserve IDs and numeric status: recalculate derived values with their inputs; hypotheses do not become measurements. Reassess affected N/A entries and reopening conditions when `profile.features` changes. `unknown` is not `absent`.
3. Trace direct and downstream relationships through all applicable disciplines and future deliverables. Confirm dependencies in actual files/fields, not just links. No explicit link does not prove no impact: inspect shared entities, states, and end-to-end flows.
4. For each consumer, record its old assumption, new rule, evidence, owner, and `STILL_VALID`, `NEEDS_UPDATE`, `NEEDS_DECISION`, or `UNKNOWN` status. Show cascades and cycles. Do not resolve contradictions by choosing the convenient version; explain why unaffected contracts remain valid.
5. Synchronize authorized documentary consequences in dependency order. Respect one writer per file; hand other authors their changes instead of overwriting parallel work. For product choices outside current authorization, identify the concrete question and options. After editing, reread affected sections and search for stale values or incompatible outcomes.
6. Assess unique/reused deliverables, tools, role effort, queues, critical path, external dependencies, and QA/release impact. Update canonical sources and send estimates to 15a/17a/19. Future regression remains `PLANNED`.
7. Mark affected reviews `RECHECK_REQUIRED`. Under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md), repeat only the changed subject with an independent Codex subagent. Changed image artwork, selected panels, or material requirements need current per-file evidence. Technical copies do not create an endless chain of artistic versions. Reuse unaffected reviews only with verified version and scope links.

## Output

Update the existing change-impact report or create it under `profile.paths.state_dir`. Include scope, versions, changes/consumers, completed synchronization, open decisions, unreviewed remainder, required rechecks, and next owner. Each material entry references a real path and section/ID. This is an impact report, not another authoritative decision log.

Send state/findings/coverage entries to the coordinator. Continue with targeted consistency, architecture, content, QA, or story-readiness checks. Broad impact warrants broad rechecking; every wording edit does not.
