---
name: 10-game-art-bible
description: Define reproducible rules for a game's visual style, form, color, motion, and technical delivery, tied to player needs and content production.
---

# 10 — Art bible

Role: art director working with UX and technical art. Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Refine the approved aesthetic; a new direction is a design decision, not a side effect of filling a template. Do not produce game assets at this stage.

## Inputs and applicability

Read `profile.sources.baseline`, `art`, `ux`, `assets`, `content`, `levels`, and `architecture`, plus the actual current references. Current decisions take precedence over early concepts. View images before drawing visual conclusions; captions alone limit what can be observed. A still frame cannot establish animation or sound.

Use the game's actual medium: illustration, pixel art, 3D, vector shapes, interface, typography, or a combination. A text game may need typography and hierarchy without character sheets. No visual output may justify `N_A`, with a reason, evidence, and reopening condition. An unknown medium is not an absent one.

## Work

1. Turn accepted aesthetic principles into observable decisions: silhouette/composition, line quality, proportions, contrast, materials, palette, typography, and motion as applicable. Give each a testable question for the artist and examples of acceptable/unacceptable variation where needed. Mood words alone are insufficient.
2. Connect visual decisions to player tasks and product contexts. Define recognition of roles, interaction, threats, states, and depth; separate decoration from necessary information. Check the actual light/dark, quiet/busy, and other used states. Do not require combat, biomes, or cinematics unless they belong to the agreed game.
3. Specify applicable categories: characters, objects, environment, backgrounds, UI, text, animation, and effects. Cover states/transitions, reuse, variation limits, and quality targets. Distinguish cosmetic substitution from new behavior: a color variant neither creates a mechanic nor becomes a free completed deliverable.
4. Check how key actions read in the actual camera/view: contact, selection, movement, transformation, interaction, or other game actions. Essential points, directions, and states must be understandable without guesswork or color alone. Explain which features must match across views or cameras. Make the priority of gameplay signals over decoration testable.
5. Reconcile art rules with applicable technical contracts: resolution and scale, pixel grid, color space, alpha, fonts, materials, geometry, rigs, export, and import. Do not impose universal polygon, LOD, or frame counts. Numeric budgets need sources and evidence status. Resolve conflicts between appearance, readability, and load explicitly or record an open question.

## Output and handoff

Update the canonical `art` source. Record category coverage, changed rules, reference provenance, borrowing limits, conflicts, and future artistic/technical acceptance criteria in `art-bible-review.md` under `profile.paths.state_dir`. A link to someone else's work does not establish usage rights.

Send applicable spatial requirements to [10a](../10a-game-environment-production/SKILL.md), audio to [10b](../10b-game-audio-design/SKILL.md), and unresolved visual details to [10c](../10c-game-visual-reference-pack/SKILL.md). Actual images require [subagent visual review](../00-game-preproduction/references/subagent-review.md); an art standard does not replace a reference showing the required detail. Then prepare [11](../11-game-asset-spec/SKILL.md). Return changes affecting perception to 09/09a.
