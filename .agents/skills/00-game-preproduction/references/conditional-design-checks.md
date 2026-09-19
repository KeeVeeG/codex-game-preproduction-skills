# Checks for specific mechanics and formats

Read only applicable sections. These checks clarify an already selected mechanic; they do not add genre features to scope. At D0, specify rules and future QA scenarios without implementing the game.

## Turn boundaries and undo

When an action starts several board or rule resolution phases, define the start and end of one turn, effect order, and completion condition. Specify when to spend the turn, evaluate victory or defeat, and accept the next input. For example, the final available turn may complete an objective only after a chain of effects: the specification must determine the outcome independently of animation order.

Only when undo is in scope, list everything it restores: board state, scores and resources, counters, objective flags, and relevant randomness. Define undo during an unfinished action and replay after undo. Give stage 19 scenarios for the final turn, interrupted chains, and restoration of the complete state contract. Do not add undo, cascades, or input blocking to a game that does not require them.

Related method: [puzzle](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/b105e1cf617adf0b68ed98790a716bbb60993179/skills/genres/puzzle/SKILL.md).

## Irreversible spatial transitions

For a one-way transition, closed route, or loss of access, describe what the player can understand **before acting**, which objectives and resources are affected, and how recovery works. A reachable ending does not prove the choice is understandable. If an unexpected route closure is intentional, record the decision and check it against the intended experience and tutorial; a warning dialog is not mandatory. Stages 07c and 19 must examine the specific action using information available to the player, not just the route graph.

Related method: [level-design](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/b105e1cf617adf0b68ed98790a716bbb60993179/skills/disciplines/level-design/SKILL.md).

## Procedural reproducibility

If the project promises a reproducible world, session, or replay, a seed alone is not a complete contract. Record generator and rule versions, parameters, relevant inputs, and the order of random choices. Specify the random state needed to resume, or a reproducible way to recover it. With stage 12, decide which results are stored and which are regenerated; both may coexist if the source of truth and version checks are explicit.

Define whether decoration changes or chunk loading order may affect gameplay results. If they must not, separate random streams or identifiers, or specify another verifiable isolation method. Give stage 19 scenarios for restart, resume, and changing non-gameplay decoration while gameplay inputs stay fixed. Define compatibility, migration, or explicit rejection for a new version; an identical seed cannot conceal a version mismatch.

Related ideas on separate random streams and versioning: [procedural-gen](https://github.com/fcsouza/agent-skills/blob/e0a3dde8c1d865ef5b430040caab8e533f16d28e/plugins/game-dev/design/procedural-gen/SKILL.md). Its code and database instructions are not incorporated.

## Exact pixel art and repeating surfaces

For a reference claimed to be exact pixel art, specify its grid, palette, and scale, then inspect the lossless original at native size. If a magnified view is needed, use integer scaling without smoothing. JPEG compression and filtered resizing can change pixel boundaries and colors: a transport preview alone cannot prove these properties. Supply an accessible original PNG or explicitly linked detail views; the independent subagent review must identify the criteria actually visible.

When a surface or tile reference promises seamless repetition, inspect adjacent copies and the required edges and corners. For an animation sheet, check declared anchors and shape consistency across frames. If only a concept exists, record these requirements for delivery and future acceptance in stages 11 and 19; do not claim to have verified nonexistent frames, tiles, or imports.

Related method: [create-game-assets](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/b105e1cf617adf0b68ed98790a716bbb60993179/skills/disciplines/create-game-assets/SKILL.md). Its text and helpers are not copied. The stated limitations of [image review and transport](subagent-review.md) still apply.
