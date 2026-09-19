---
name: 18-game-create-stories
description: Specify testable future implementation and content-production tasks from game epics, requirements, and architecture contracts, covering the selected scope completely.
---

# 18 — Implementation and delivery stories

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Produce D0 task specifications; do not create code, game assets, test scaffolding, or builds at this stage.

## Inputs

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Read actual `profile.sources.epics`, `stories`, `architecture`, `decisions`, `controls`, `content`, `risks`, `production`, `qa`, and primary requirements. Use current dependency order and 11a results, not epic names without content. Preserve current IDs/versions; an unread link is not a verified requirement.

Scope can be an epic, a group of epics, or the whole agreed product. State it and the remainder. Use `profile.features`: `absent` needs a reason, source, and reopening condition; `unknown` remains open. Do not add content types, network modes, platforms, or languages for a template.

## Work

1. Decompose requirements into complete, testable changes to behavior, data, or presentation. Each task defines outcomes, input states, responsibility boundaries, and neighboring contracts. Split by verifiable results rather than arbitrary durations.
2. Give each criterion a real source/ID or verified anchor and preserve the rule in a self-contained statement. Mark missing contracts `GAP`; do not invent requirement or ADR numbers. A title such as “build the system” does not specify its states and exceptions.
3. Identify verification types: logic/data, integration, interface, visual/audio results, game feel, or other applicable deliverables. Mixed tasks retain every required check. Link accepted decisions, control-manifest version, interfaces, and material technology constraints. N/A explains applicability, not a missing document.
4. Use Given–When–Then or equivalent observable criteria: initial state, action, result, boundary cases, and recovery as applicable. Experience/perception needs a reference or observation method, accepting role, and decision criterion. Where functional simplification could destroy the required experience, identify the preserved property, canonical source, an example of that simplification, and its observable difference. Do not invent effects or prohibitions without sources.
5. List dependencies by actual paths/task IDs, predecessor outputs, and order. Distinguish documentary readiness from execution: a predecessor can be unimplemented, but its mandatory contract must exist and be consistent. “Clarify during development” cannot replace an unknown interface.
6. Preserve the status of provisional, calculated, and invariant numbers. Give work estimates a method and basis. Cover every requirement and unit of the epic, including later agreed content. Do not postpone mandatory specifications until a prototype.
7. For non-code deliverables, state unit/ID, relevant source/export contents, variants/states, integration, dependencies, and accepting role. Group only homogeneous procedures with explicit coverage of every ID; do not hide unique deliverables in generic tasks. Applicable tools, diagnostics, test hooks, and packaging get future tasks rather than implementation now.

## Output and handoff

Update existing `stories`, their epics, and the summary plan. If missing, create a minimal canonical structure with [templates](../00-game-preproduction/references/templates.md) and register actual paths. Every story needs sources, contract versions, criteria, dependencies, future evidence, and documentary status separate from execution. Mark future tests/artifacts `PLANNED`; do not claim they exist.

Prepare [handoff without author history](../00-game-preproduction/references/handoff-review.md): the story, actual existing documentation files, and verified normative references must let a new implementer reconstruct the contract without author explanations. For future game assets, supply their specifications and production tasks, not imaginary finished files.

Continue to [19](../19-game-qa-plan/SKILL.md), then [20](../20-game-story-readiness/SKILL.md). Send a summary to the coordinator for `profile.paths.state_dir`. Implementation does not begin automatically.
