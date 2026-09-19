---
name: 13-game-architecture-decision
description: Record or refine a game architecture decision with alternatives, scope, dependencies, compatibility evidence, and a future verification plan.
---

# 13 — Architecture decision

Role: architect or relevant technical specialist. Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. An ADR documents a choice; acceptance does not mean integration is complete or gameplay tests have passed.

## Inputs

Load the chosen profile, defaulting to `docs/preproduction/project-profile.json`. Read `architecture`, `decisions`, `controls`, `risks`, and primary requirements for the decision from `profile.sources`. Read an existing ADR in full; preserve its ID, meaning, status, and history. Use [templates](../00-game-preproduction/references/templates.md) and register the actual path when a canonical document is missing.

First find decisions about the same data, interfaces, and dependencies, including ID mentions outside the ADR directory. Different number padding does not create a different decision. Do not issue a second incompatible `Accepted` contract. One canonical source owns a rule; summaries and manifests refer to it.

Derive applicability from `profile.features` and sources. `unknown` is not N/A; for `absent`, retain reason, evidence, and reopening condition. Do not reselect the approved engine, genre, or release method without an instruction covering that change.

## Work

1. Define the problem through requirements, affected modules, constraints, and concrete consequences of leaving it unresolved. Separate accepted foundations from new choices. ADRs serve significant decisions, not document quotas.
2. Compare realistic alternatives by cost, capabilities, failure modes, and consequences. Explain an already approved choice without inventing another approval step. Rejecting an alternative in one contract does not ban it throughout the project.
3. Verify claims that determine the choice—APIs, packages, formats, and platforms—against official sources for the selected version. Record date, URL, established behavior, and uncertainty. An available library does not prove a ready integration, reproducible delivery, or a successful future experiment.
4. Specify state owners, participants, commands/results, preconditions, guarantees, errors, and recovery. State dependencies, what the decision enables or blocks, and effects on data, performance, UX, and content as applicable. For replacement, cover migration, reversibility, and the previous ADR.
5. Link the contract to stable requirements and observable verification criteria. Separate completed source/document checks from future implementation checks, each with an owning role and decision point. Explain N/A for absent migration or external dependencies rather than leaving fields blank.
6. For material risks, record the cause of uncertainty, trigger, prevention, recovery/fallback, dependent tasks, and reopening condition. External deliverables need sources for provenance, version, and license terms. Mark unknowns `UNVERIFIED`. Introduce a service or tool from a justified requirement, not a list of popular products.

## Output and status

Update the existing `decisions` document or create one ADR in the canonical location and register it. Minimum content: ID/status/date, context and requirements, decision/contracts, alternatives, dependencies, compatibility/evidence, consequences, and verification.

`Proposed` means an open choice. `Accepted` means an approved foundation or decision within authorized scope, with its basis recorded. `Superseded` preserves history and links to the replacement. Changing an ADR does not turn a previous review into evidence for the new version. Ask for a new user choice only where current authorization genuinely leaves it unresolved.

Propagate impact through [16](../16-game-propagate-design-change/SKILL.md), then obtain [14](../14-game-architecture-review/SKILL.md) review of affected contracts and dependencies. Send shared-log entries to the coordinator for `profile.paths.state_dir`. Do not begin implementation.
