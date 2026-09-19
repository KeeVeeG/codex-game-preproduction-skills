---
name: 03-game-scope-check
description: Compare game documentation with the agreed scope to find missing requirements and hidden additions. Use for the initial package and subsequent changes.
---

# 03 — Check scope and completeness

Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Inputs through `profile.sources`: agreed baseline and exclusions, map 02, specifications, and catalogs. For a change, include the known starting revision and current edits. Preserve the full agreed scope, whether it is a small game, an expansion, or a larger product.

1. Extract verifiable commitments, counts, and explicit exclusions. Distinguish product scope, gameplay invariants, unconfirmed ideas, and starting settings. If the baseline is unavailable or contradictory, continue independent inventory work but do not issue a comparative verdict against invented boundaries.
2. Map every commitment to its canonical specification and a coverage row: covered, partial, missing, or contradicts the baseline. Include applicable modes, spaces/boards, characters, quests, items, screens, generation rules, and production units. Before a negative finding, search the whole declared area; a missing name in one file does not prove a requirement was lost.
3. Check `present/absent/unknown` against the profile. N/A needs support in the agreed product and a reopening condition. Future implementation does not make a required unit's design inapplicable; unknown content is not zero content. Procedural games require coverage of promised families and constraints rather than every possible world.
4. Classify additions as clarification of selected behavior, a necessary supporting contract, a new product commitment, or an exploratory alternative. Refunding an unused resource on cancellation may clarify an existing action; a new trading system expands the product. A technical validation plan does not become a mandatory D0 prototype.
5. Explain the effects of additions and omissions on the player, content, integration, and verification. Count comparable units; do not combine screens, text lines, and mechanics into a misleading percentage. Tie schedule estimates to assumptions about the team and production pipeline.
6. Complete missing detail within the authorized scope. For disputed product decisions, identify the owner, alternatives, and affected dependencies. Do not shrink the agreed game to a prototype for convenience or expand a small project to fill a template.

Output: `scope-review.md` in `profile.paths.state_dir`, with the baseline source, commitments, additions/omissions, sources on both sides, consequences, and correction route. A partial review explicitly limits its conclusion.

Completion: the reviewed scope has no unexplained additions or lost commitments; disputed decisions are visible and have owners. An independent production or game-design Codex subagent distinguishes clarification from expansion under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Continue to [04](../04-game-review-all-gdds/SKILL.md); repeat 03 after changes to the baseline or product content. The coordinator updates shared logs.
