---
name: 11a-game-content-coverage
description: Audit all agreed game content against specifications, consumers, production tasks, and acceptance, including procedural families and gaps hidden by shared specifications.
---

# 11a — Content coverage

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Use the full [coverage framework](../00-game-preproduction/references/coverage.md). This is a D0 audit, not a check for completed scenes, translations, audio banks, or game models.

## Inputs and passes

Use `profile.sources.baseline`, `systems`, `mechanics`, `content`, `levels`, `assets`, `art`, `environment`, `audio`, `ux`, `accessibility_localization`, `visual_manifest`, and existing plans. The first pass after 11 establishes scope for architecture and production. Repeat after 18/19 against epics, stories, and QA; a final pass is required before the readiness gate.

Derive categories from this game's commitments: levels, scenes, quests, entities, cards, dialogue, screens, sounds, locales, generator families, or other actual units. Do not add campaigns, bosses, items, or postgame content to fit another game's template. Inapplicability needs a reason, evidence, and reopening condition. Unknown content scope is not zero content.

## Review

1. Derive the expected set from primary catalogs **and** obligations in prose. Record the source of each count and ID. Empty or absent catalogs do not prove no need. Preserve distinctions between types, instances, variants, production units, and placements. For procedural games, enumerate finite families, rules, parameters, and constraints; separately plan representative/boundary checks of generated results. A few seeds do not cover every possible world.
2. Find each unit's rule, specification, allowed states/variants, consumers, dependencies, and acceptance criteria. Spatial content needs applicable plans, placements/generation rules, and assembly recipes; narrative needs branching, transitions, and recovery; UI needs states, devices, and strings. Read the content rather than checking only files or links.
3. Check both directions: expected units without specifications and specifications/deliverables/placements without authorized needs. Shared specifications can be inherited when links and differences are explicit and every inheritor is checked. Find duplicates, obsolete IDs, incompatible versions, and missing relationships. Do not silently add content to repair them.
4. Find game-relevant category gaps: late/rare branches without rules, variants without states, sounds without events, interactions without signals, assets without consumers, screens without strings/glyphs, generators without constraints, or recovery without an exit. For visible content, inspect `visual_manifest`: actual images/panels, essential details, and current acceptance under [10c](../10c-game-visual-reference-pack/SKILL.md). Each applicable image needs actual independent Codex subagent review under `profile.review`; a prompt or text description cannot replace viewing it.
5. After planning, map every mandatory unit to an epic/task and verification method. Independently enumerate actual stories and check task → authorized requirement/unit/coverage in reverse. Technical tasks without asset IDs still need justification. On the early pass, mark not-yet-created tasks `PENDING_PLANNING`; on the final pass, their absence is a gap. This deferral never permits undefined mandatory behavior.
6. Ask an independent reviewer to reconstruct the final sets from primary sources. In addition to full set comparison, trace actual risks such as edge variants, late branches, complex reuse, or unique paths. Sampled deep review does not replace complete set mapping. The coordinator updates shared coverage and findings; assigned authors repair canonical sources.

## Output and completion

Write `content-coverage.md` under `profile.paths.state_dir`: expected sets and ID/type → source → specification → placement/consumer → task → acceptance → status, category totals, and unconfirmed coverage. For families, state the enumerable boundary and generation test plan. Reference canonical data rather than copying it into another registry.

The first full pass hands defined scope to architecture and production and triggers MR-DESIGN when required by the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). The final pass after planning must not leave mandatory units missing or hidden behind a general positive verdict. Changed content/states reopen affected reviews under the protocol.
