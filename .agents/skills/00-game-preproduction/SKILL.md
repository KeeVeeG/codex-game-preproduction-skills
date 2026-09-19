---
name: 00-game-preproduction
description: "Prepare or resume a game's documentation for implementation, coordinating the full preproduction workflow and saving progress. Use for a full-cycle request; route a focused domain task to its specialist skill."
---

# 00 — Prepare a game for implementation

Deliver reviewable documentation for the **entire agreed scope**, with a stage 21 verdict. Continue available work toward that result; a first draft does not complete the assignment. Implementing the game is a separate task.

Follow the [shared protocol](references/protocol.md). Choose the appropriate entry below; reuse instructions already read unless they change or leave context.

| Task state | Next action |
|---|---|
| First full run | Locate the game root and profile, normally `docs/preproduction/project-profile.json`. Run [01](../01-game-project-stage-detect/SKILL.md) to establish the profile, sources, and full applicability matrix. |
| Resume | Read the actual profile, state, open findings, source versions, and unfinished delegations using [session-state.md](references/session-state.md). Check changed sources and immediate dependencies. Do not restart current diagnostics merely because the session is new. |
| Focused domain task | Use the relevant SKILL.md without starting the whole workflow; keep the result's scope local. |

Choose the next stage from `stages` in [workflow.json](references/workflow.json), current dependencies, and applicability. Read the selected skills, relevant `rechecks`, and due `subagent_reviews`, rather than loading every skill body. The final gate requires the full route and `completion` criteria. Workflow resource paths start at this directory; game paths start at the game root.

Numbers preserve the first-pass order; dependencies and changes determine repeats. An evidenced `N_A` satisfies a dependency; an unknown does not. Partial applicability retains the relevant work. Early feasibility checks and independent design, UX, art, or audio tasks can run in parallel when their inputs are defined. All stages and content units must be accounted for before 21.

Read the exact SKILL.md before executing or delegating a stage. The coordinator owns shared records and integrates every worker's result; use [session-state.md](references/session-state.md) for writing, snapshots, delegation, and recovery. Route shared contract changes through [16](../16-game-propagate-design-change/SKILL.md) and affected workflow rechecks, preserving current unaffected evidence.

Consult independent **Codex subagents** at MR-DESIGN after the first full 11a, MR-TECH after 15a, and MR-HANDOFF after the full 20 and before 21. Read [subagent-review.md](references/subagent-review.md) when a checkpoint is due. The default profile also requires actual visual inspection of every used image and every new artistic candidate version before visual acceptance. [10c](../10c-game-visual-reference-pack/SKILL.md) loads image generation and preparation details when needed. Unavailable delegation or image viewing leaves required evidence pending; continue independent work. Stage 20 uses a fresh reader without author or previous review history.

For `NEEDS_REVISION`, fix specific gaps. For `NEEDS_USER_DECISION`, present the consequential unresolved choice with a recommendation and continue independent work. Complete the full assignment with a justified `READY_FOR_IMPLEMENTATION` from [21](../21-game-gate-check/SKILL.md), or save the exact blocking dependency and next step. Future playtests and measurements remain hypotheses with owners and criteria, not proven game quality.
