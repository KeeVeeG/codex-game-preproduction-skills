---
name: 02-game-map-systems
description: Map a game's systems, rule owners, and directed dependencies. Use after diagnosis or changes to system boundaries to order specification work.
---

# 02 — Map systems and dependencies

Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Inputs through `profile.sources`: baseline, game loop, mechanics, system interactions, catalogs, and report 01. Continue an existing map and preserve its IDs. The map indexes decisions; it does not create a second GDD.

1. Identify explicitly selected systems and necessary supporting contracts. Each entry includes an ID, player purpose, source, specification owner, inputs/outputs, and definition status. Justify hidden dependencies with a concrete action: granting a permanent reward requires ownership and persistence rules. It does not authorize a shop, skill tree, or cloud saves. Genre associations do not prove a system is necessary.
2. Trace the product's actual loop, such as choice → action → consequence → new decision, round → result → next round, or exploration → discovery → changed options. Cover entry, normal use, complex or late states, exit, and recovery using only supported variants. Do not substitute a generic combat-and-loot loop.
3. For each edge, record direction, whether it is required, the specific data or event, contract owner, and source. Distinguish dependencies in rule definition, runtime data flow, production, and player presentation. Bidirectional events do not necessarily imply an impossible implementation order.
4. Find cycles, conflicting ownership, duplicated state, and nodes with many document dependencies. Resolve cycles through boundaries, event ordering, and coordinated specification work. Do not split a connected system artificially just to produce an acyclic diagram.
5. Connect systems to full content accounting: required unit or procedural family → specification → state/placement → future task → acceptance. A system map does not replace coverage of individual units. Route spatial contracts to 07b and narrative/onboarding to 07a. For inapplicable aspects, follow the profile's `absent` rules rather than creating empty mandatory entities.
6. Order documentation from defining rules to consumers. Explain priorities through player impact, uncertainty, and dependencies. Identify independent groups for parallel authors with non-overlapping files. Early priorities do not remove other agreed systems from scope.

Output: `systems-map.md` in `profile.paths.state_dir`, containing the registry, typed directed edges, cycles, owners, bottlenecks, revision order, and links to canonical documents. Send shared changes to the coordinator.

Completion: every system in the agreed baseline has an owner, material connections are explained, and cycles are accounted for. An independent technical or systems Codex subagent traces a normal and failure sequence under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Continue to [03](../03-game-scope-check/SKILL.md). A “next system” request selects the first unready node for [06](../06-game-design-system/SKILL.md). Recalculate affected ordering after a contract change.
