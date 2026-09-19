---
name: 07a-game-narrative-design
description: Specify applicable narrative, characters, quests, dialogue, and onboarding as connected states and implementation materials. Support linear, branching, and systemic forms without requiring a story.
---

# 07a — Design narrative and onboarding

Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Inputs through `profile.sources`: baseline, game loop, existing canon, characters/scenes/quests, map 02, rules, UX, art, and audio. Preserve current IDs and canonical documents; detail serves the selected product.

Assess narrative and onboarding separately. A game without a story may still need to explain available actions. An embedded tutorial is not mandatory if another adequate method is selected. The stage is `N_A` only when all required parts are demonstrably inapplicable. `unknown` is not absence.

1. Inventory applicable entities: arcs/scenes, characters, quests, dialogue, player knowledge, and learning actions. Record each entry's canonical source, function, availability, execution, consequences, location/context, and status. Cover the full agreed content. For systemic narrative, cover authored elements, combination rules, constraints, and material outcome classes.
2. Define tone, player promise, causality, world facts, and the range of change caused by player actions. Distinguish world truth, character knowledge, player knowledge, and deliberate ambiguity. A material mystery needs an author-defined answer or a deliberate decision to leave it open. Specify endings, alternatives, and post-completion states where selected; do not impose a campaign and credits on endless or session-based play.
3. For applicable characters, define role, motivation, voice with examples, relationships, development, and links to appearance/voice assets. Scenes, quests, and dialogue need an initiator, preconditions, states, triggers, goal, permitted choices, success/failure/retry, consequences, and next node. Rewards and formulas reference their system owner. Dialogue lines need stable keys, speaker, text, context, variables, conditions, and priority; keys must match the selected localization approach.
4. Check skipping, interruption, revisiting, already-satisfied conditions, visit order, and loading where saves are supported. For branching, trace reachable flag combinations, branch merges, choice consequences, and impossible states. For networked products, specify whose choices and knowledge persist. Do not add branches to fill a table.
5. Define onboarding through “existing knowledge → introduction → safe practice → independent use → complex challenge → hint/recovery.” Cover the first use of every required new rule and supported return after a break. Separate information needed for the next action from optional lore. Explain how needed knowledge is recovered after skipping or interruption; this may use interface, environment, or text.
6. Connect scenes and hints to space in 07b, system states, text constraints, accessibility, and art/audio materials. Trace setup and payoff of significant promises, emotional load, and pauses. Reading pace, literary quality, and comprehension remain hypotheses with future verification plans.

Output: updated canonical narrative/onboarding materials, coverage registry, and acceptance scenarios. Create files as needed rather than imposing a fixed chapter list. Send shared indexes and findings to the coordinator.

Completion: required entities and transitions are covered. An independent narrative or QA Codex subagent traces sequences, branches, and knowledge recovery from primary documents under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Continue to [07b](../07b-game-level-design/SKILL.md) where applicable; after changes, repeat [05](../05-game-consistency-check/SKILL.md) and [04](../04-game-review-all-gdds/SKILL.md). The absence of narrative defects on paper does not establish player reception.
