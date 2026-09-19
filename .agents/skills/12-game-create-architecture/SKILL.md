---
name: 12-game-create-architecture
description: Specify the architecture of the agreed game through state ownership, system contracts, dependencies, and necessary decisions before implementation.
---

# 12 — Architecture specification

For the chosen digital stack, read applicable [engine and technology contracts](../00-game-preproduction/references/engine-profile-review.md). If services, analytics, or platform delivery are present, add [service and release contracts](../00-game-preproduction/references/service-and-release-planning.md). These refine existing scope; they do not select an engine, networking, or SDK automatically.

Role: technical architect. Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Produce D0 architecture specifications, not an engine project, code, prototype, or CI.

## Inputs and boundaries

Load the chosen profile, defaulting to `docs/preproduction/project-profile.json`. Resolve semantic `profile.sources` keys into actual relative-path lists, especially `architecture`, `decisions`, `risks`, `content`, `release`, current requirements, and the system map. Read documents and data within scope. Extend canonical sources. For a new project, use the [template rules](../00-game-preproduction/references/templates.md) to create minimal documents and register paths, not parallel specifications.

Take features and platforms from the profile and accepted requirements. In `profile.features`, distinguish `present`, `absent`, and `unknown`: `absent` permits N/A with a reason, source, and reopening condition; `unknown` remains open. Do not add networking, saves, campaigns, or an engine for a template. A full pass covers the entire agreed scope; early feasibility advice limits conclusions to its stated risk.

For non-digital games, architecture covers rules, information states, components, allowed actions, and delivery. Software layers, APIs, executable builds, and CI apply only to an actual digital component; their absence does not prevent product contracts.

Preserve the chosen stack, versions, and constraints. A version family is not a verified dependency set. Check material API and compatibility claims against official sources for actual versions, retaining URL and date. Unknown integration results remain unverified; stack-independent contracts can progress while those dependencies are unresolved.

## Work

1. Extract requirements for state, time, input, presentation, content lifecycle, and failures. Add synchronization, storage, platform services, and accessibility where applicable. Preserve IDs; introduce new IDs explicitly with source links. Assess coverage by requirements and units, not module counts.
2. Define module boundaries, a single owner for each mutable state, public operations, events, and permitted dependencies. Distinguish definitions from instances, ownership from access, and personal from shared data where relevant. Presentation must not gain authority that contradicts game rules.
3. Trace mandatory end-to-end flows: initialization, core actions, context changes, completion, and applicable failures/recovery. For each transition, identify order, initiator, before/after state, observable result, and final confirmation point. Cover repetition, cancellation, lateness, concurrency, and partial failure where possible.
4. Specify boundary contracts: commands/data, units and identifiers, preconditions, guarantees, errors, and recovery ownership. Documentary pseudocode is allowed. Implementation detail cannot replace a gameplay rule: animation duration or UI feedback does not determine an outcome unless its source requires that.
5. Connect budgets to simultaneous-load scenarios across the agreed product, units, and future measurements. Separate accepted limits, forecasts, and measured results. Identify decisions needing ADRs; direct unambiguous contracts do not need ADRs to meet a quota.
6. Describe the applicable content pipeline: source → validation → import/transformation → build → delivery. Cover versions, source-level diagnostics, repeatability, partial-failure recovery, and deletion/migration. Test hooks, controlled time/randomness/failures, and build infrastructure become future tasks when the process needs them. Send trust boundaries and material technical unknowns to 15a.

## Output and completion

Update canonical `architecture` documents. Give the traceability owner requirement → module/contract → ADR or basis for direct decision → future check, open decisions, and affected versions. The assigned coordinator owns shared logs under `profile.paths.state_dir`.

A missing mandatory contract is a gap; a planned integration check is not proof of compatibility. Continue to [13](../13-game-architecture-decision/SKILL.md), then [14](../14-game-architecture-review/SKILL.md). Send conflicts with agreed product rules through [16](../16-game-propagate-design-change/SKILL.md), with concrete options and impact.
