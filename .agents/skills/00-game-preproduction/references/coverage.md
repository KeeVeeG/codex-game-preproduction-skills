# Coverage of the agreed game

Assess every area against the profile and sources. The matrix records ID, applicability and rationale, concrete units or families, canonical sources, missing contracts, owner, tasks, QA, and current evidence. Headings and completion percentages do not prove quality. Never replace `unknown` with `N_A`.

## COV-01 — Concept and scope

Experience promise, audience, game loop and session/match duration, product and agreed delivery, constraints, exclusions, success criteria, and source authority. Verify relevant market or pricing claims against current sources rather than assigning them from a template.

## COV-02 — Game loop, learning, and feedback

Action → understandable result → next choice; input, timing/spatial windows, game feel, errors, learning, and retries. Games without stories still need a way to learn. Check action availability and preservation of the core experience in future tasks.

## COV-03 — Rules and cross-system contracts

States, events, preconditions, ordering, inputs/outputs, errors, priorities, constraints, data ownership, and recovery. Account for simultaneous rules and text that permits two plausible but incompatible implementations.

## COV-04 — Gameplay entities, challenges, and encounters

Every applicable opponent, task, puzzle, card, obstacle, or other interactive challenge: experiential role, behavior, available responses, states, variants, failure/retry, observable cues, and placement. Do not create combat, bosses, or AI where absent.

## COV-05 — Economy, difficulty, and progression

Applicable resources, scores, limits, and unlocks: sources, costs, remaining amounts, saturation, exploits, edge cases, and calculation sensitivity. For puzzles, learning/difficulty curves; for finite routes, resource state at each node; for generators, distribution boundaries. Future gameplay balance remains a hypothesis.

## COV-06 — Narrative, text, and world

Within applicable scope: event/branch graphs, characters, conditions, variables, quests, dialogue, resolutions, skipping, return, recovery, and text data. Do not impose a campaign, lore, or post-credits state on a game without them.

## COV-07 — Spaces, boards, and generation

Every authored location/board or generation family: scale/coordinate system, measurable rules, topology, routes/access, placements, readability, hazards, and recovery. Reconcile text, diagrams, and structured data in the selected format. Procedural content needs grammar, ranges, connectivity/solvability, versions, and future validation cases rather than an infinite map inventory.

## COV-08 — Environment production and assembly

Applicable 2D, 3D, or physical kits; dimensional contracts, joins, materials, assembly/layer rules, collisions/overlaps, dependent assets, variants, organization, and effort estimates. A future implementer can reproduce the space without guessing. D0 does not require a finished scene.

## COV-09 — Visual language and references

Silhouettes, shape, color, light, composition, readability, states, and animation/VFX as the product requires. Actual images and required views/variants follow the [visual contract](visual-references.md), with rights/provenance and links between versions and acceptance. Review every applicable file/panel under the policy; one mood board cannot define every unit.

## COV-10 — Sound, music, and voice

Direction, events/conditions/priorities, variants, music states, mix/spatialization, interruption, recovery, delivery format, and project-specific budgets. Functional cues need accessible alternatives. Do not add voice-over or middleware from a template.

## COV-11 — UX, input, and accessibility

All interface/information flows and states, devices and switching, focus, errors/empty states, confirmation of irreversible actions, understandable cues, and actual audience barriers. Cover first entry, normal play, retries, and recovery. Ground numerical targets in the product.

## COV-12 — Languages and text workflow

Agreed languages and writing directions, formatting/plurals/wrapping/fonts, IDs/context/variables, editing, and verification. A single-language game still needs consistent text; a second translation is not mandatory. Separate localizable text from logic in an applicable format.

## COV-13 — Architecture and integrations

Requirements → modules/components → contracts, ownership, states/data, and necessary ADRs. Use only the selected stack and versions; verify material compatibility. A physical game needs component and manufacturing specifications rather than imposed software layers.

## COV-14 — Reliability, trust, and recovery

Save/load or session-resumption rules, migrations, corrupted data, failures, and recovery. For networking, authority, reconnection, synchronization, and abuse; for user-generated content, input boundaries and moderation; for payments/data, applicable constraints. Do not invent a server for a single-player product.

## COV-15 — Budgets and measurements

Target devices/conditions, applicable time/memory/loading/size budgets, peak scenarios, instruments, and future measurement points. Physical products need their own measurable manufacturing constraints. Initial budgets are not achieved results.

## COV-16 — Data, tools, and pipeline

Schemas, units, validation, import/export, versions and ownership, minimum necessary content-authoring tools, build/packaging/manufacturing, licenses, and delivery. Do not import another project's polygon count, file format, or mandatory JSON requirement.

## COV-17 — Content and traceability completeness

Authored catalog and/or generated content families/boundaries: requirement → rule/appearance → placement or use → production unit → task → QA. Include variants, states, and reuse. The first 11a pass records links awaiting tasks; final 11a after 18/19 verifies actual links.

## COV-18 — QA and evidence

Deterministic scenarios, invariants/edges, accessibility, platforms, recovery, playtest hypotheses, and regressions. Each needs state, action, observable result, dependencies, and `planned/executed` status with actual evidence. A prepared plan is not passed testing.

## COV-19 — Production and handoff

Epics/tasks across all disciplines, dependencies, three-point estimates with assumptions, role capacity, reuse/rework, critical path, and acceptance criteria. Preserve the full agreed scope; do not derive a schedule from an invented team. Review every story and additionally give actual packages to independent Codex subagents without author history.

## COV-20 — Release and support

Agreed delivery method, packaging, metadata, rights, QA/acceptance, release recovery, and support/analytics/updates only where applicable. A public storefront, monetization, live operations, and commercial release are not universal requirements. Verify current external requirements before accepting a decision.
