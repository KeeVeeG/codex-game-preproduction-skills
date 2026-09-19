---
name: 01-game-project-stage-detect
description: Assess the actual state of a game's documentation, agreed scope, and gaps before implementation. Use as the initial diagnostic stage for an existing project or a new concept.
---

# 01 — Assess project readiness

For a new or undefined concept, or a project whose rules mainly exist in code or a prototype, use the relevant [foundation and evidence-recovery branch](../00-game-preproduction/references/foundation-and-adoption.md). Do not reopen an accepted concept without cause.

Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Use the full [coverage schema](../00-game-preproduction/references/coverage.md) for the initial assessment. Find the profile, defaulting to `docs/preproduction/project-profile.json`. Select sources by purpose from `profile.sources`; save reports under `profile.paths.state_dir`. Preserve the existing document structure.

Assess documentation readiness for the agreed product, rather than inferring a stage from file counts. Inputs include the concept or baseline, GDD or equivalent, catalogs, specifications, technical and production constraints, and previous reports. For a new game, start with the available concept and the minimum canonical foundation required by the protocol. Leave unknown product decisions open.

1. Record the scope under review, source revisions, selected platforms, interaction methods, and material constraints. Distinguish intent from confirmed decisions and existing implementation from its documentation. Missing code or prototypes neither fail D0 nor authorize creating them.
2. Reconstruct the coverage matrix across every area of the shared schema. For applicable areas, extract units from text and catalogs: systems, modes, spaces, screens, content types, and states. Section titles alone are insufficient. A missing required content catalog is a gap, not a successfully covered empty set. For procedural content, list families, generation rules, constraints, and required outcome classes rather than every possible instance.
3. Check applicability through `profile.features`: `present` requires substantive review; `absent` requires a reason, source, and reopening condition; `unknown` requires investigation or a decision. Genre alone does not establish the absence of narrative, networking, progression, or levels. Assess parts of an area separately: a game without a story may still need onboarding.
4. For each area, distinguish source availability, rule definition, verified consistency, open decisions, and future measurements. Detailed prose does not establish an unambiguous action outcome. Identify conflicting values, missing owners, and unspecified state transitions.
5. Give every gap an exact source or bounded search area, the affected player or implementer, a required outcome, and a next stage. Separate missing specifications, unavailable sources, product decisions, and future playtests. Readiness percentages require an explicit denominator of comparable units.
6. Check authoritative sources, IDs, registry links, and archives. Propose a dependency-based revision order. Previously completed stages retain their status only while their evidence remains current; list changes that require another pass.

Output: `stage-report.md` in the state directory, with reading scope, an “area → sources → established facts → gap → next action” matrix, limitations, and a recommended route. The coordinator owns the shared matrix and logs; for a standalone run, assign ownership under the protocol.

Completion means the entire agreed scope is accounted for and material gaps have an action. It is not a positive final D0 gate. An independent Codex subagent checks material conclusions against primary documents under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Continue to [02](../02-game-map-systems/SKILL.md); repeat 01 after a baseline change or discovery of an untracked area.
