---
name: 09-game-ux-review
description: Independently review game interface and interaction documentation for scenario coverage, consistent states, and decisions that an implementer would otherwise have to invent.
---

# 09 — Independently review UX

Review selected patterns against [exact interaction states](../00-game-preproduction/references/interface-production-details.md), including disappearing elements, preview/commit, and interrupted input. Apply language and assistive branches according to promised support.

Role: an independent UX reviewer using a fresh-context Codex subagent under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Review D0; a paper scenario is not a successful user test.

## Inputs and coverage

Use `profile.sources.baseline`, `ux`, `mechanics`, `systems`, `accessibility_localization`, `art`, `architecture`, and related data. `profile.paths.state_dir` defines report paths. Required devices, locales, and player roles come from the profile and accepted sources; one mockup does not expand promised support.

Independently inventory screens, gameplay interactions, HUD states, and shared patterns first. This is the review denominator; the author's report is secondary evidence. For a partial assignment, explicitly limit the conclusion to the selected area. `N_A` requires a reason, evidence, and reopening condition. An unknown scenario is not absent.

## Review

1. Connect mechanics requirements to observable interactions and data. Check entry/exit points, player context, state sources, and action results. Justified absence of an element is acceptable; missing information needed for a player decision is a gap.
2. Walk through the main loop and applicable rare or late scenarios from the actual game: first launch, failure, retry, completion, return to a save, interruption, and recovery. For procedural play, check state-family constraints; for endless play, repeated cycles and accumulation; for narrative play, branches and transitions. Record steps where choosing behavior requires a new decision.
3. Check empty, pending, blocked, error, and partially completed states, cancellation, timers, and message priority. Where network/external operations exist, trace uncertain results, retries, and participant conflicts. Do not require artificial network logic when these operations are absent.
4. Trace every promised input method: element reachability, focus order/return, remapped labels, gestures, device changes, and modal exit. Required gameplay actions must not disappear because of a menu. Assess readability, meaning without a single color or sound, and reduced motion against accepted commitments. Record additional capabilities as proposals, not accepted requirements.
5. Check simultaneous HUD, warning, subtitle, and hint presentation at the maximum specified information load. Ensure the pattern catalog covers components actually used. Read diagrams and view images; a link or caption does not replace visual inspection. Even reviewed mockups do not prove working controls.

## Output

Write `ux-review.md` in the state directory: scope, source revisions, coverage matrix, concrete scenarios, and findings with severity, location, consequence, and verifiable corrections. Follow the protocol for verdicts and limitations. Unchecked scenarios receive no positive status; unavailable independent review remains pending.

Do not edit the canonical rules under review during the independent pass. Send findings to [08](../08-game-ux-design/SKILL.md), then recheck changed scenarios and dependent states. The separate [09a](../09a-game-accessibility-localization/SKILL.md) matrix remains required according to applicability. Send visual requirements to [10](../10-game-art-bible/SKILL.md) and implementation constraints to architecture.
