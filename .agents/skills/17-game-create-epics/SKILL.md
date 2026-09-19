---
name: 17-game-create-epics
description: Decompose agreed game scope into connected code and content epics grounded in requirements, architecture, and production units, without executing the tasks.
---

# 17 — Create epics

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Produce a D0 delivery plan. Scheduling does not reduce the approved product; a template does not add a mandatory campaign or commercial release.

## Inputs and scope

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Resolve `architecture`, `decisions`, `controls`, `content`, `risks`, `production`, `release`, `epics`, `stories`, primary requirements, and traceability through `profile.sources`. Read the full or scoped 11a results; actual units/IDs matter more than software module names. Check for source changes since acceptance.

Scope can be the agreed product, a system, or a deliverable group. List the remainder for limited scope. Use `profile.features`: cover `present`; justify `absent` with a reason, source, and reopening condition; leave `unknown` open. Unknown catalogs do not mean zero content.

Extend existing epics and plans, preserving IDs and links. For new documents, use minimal canonical [templates](../00-game-preproduction/references/templates.md) and register actual relative paths in the profile without imposing a game folder structure.

## Work

1. Map each in-scope requirement to a module or discipline and an observable player/production outcome. Cover applicable implementation, content, spaces, visual/audio delivery, UI, languages, accessibility, tools, QA, and release. Non-code deliverables have production units and accepting roles, not fictional software modules.
2. Define epics with clear responsibility, outcomes, and boundaries. Do not duplicate one GDD without separating requirements. Assign owners and contracts to cross-cutting dependencies. Document later parts of the agreed scope now even if implementation comes later.
3. Order work by actual dependencies. A layer name does not replace input/output relationships. For cycles, identify the missing contract or decision; arbitrarily reordering rows does not establish a workable sequence.
4. Record each epic's goal, module/deliverable type, units and IDs, inclusions/exclusions, inputs/outputs, dependencies, owner and accepting role, applicable accepted decisions/controls, constraints, and observable future completion criteria. Link the current release plan where applicable. Do not invent requirement or ADR numbers.
5. Separate unique creation, reuse, adaptation, and integration. Reused units still cost work when adaptation or integration is required. Grouping is allowed with explicit coverage of each unit and a consistent delivery contract.
6. Check both directions: every requirement belongs to an epic, and every epic obligation has a source. Mark omissions, double counting, and unresolved new decisions `GAP`. Effort estimates stay provisional with their basis and numeric status. Epics with undefined mandatory outcomes stay draft.

## Output and next step

Update canonical `epics` and the current summary plan in `production`/`stories`. Each epic needs sources, coverage, gaps, and documentary status separate from future execution. The coordinator updates shared state/findings under `profile.paths.state_dir` from the reported results.

Next, [17a](../17a-game-production-readiness/SKILL.md) checks capacity and the production plan, then [18](../18-game-create-stories/SKILL.md) details epics in dependency order. Do not produce code, content, or infrastructure at this stage.
