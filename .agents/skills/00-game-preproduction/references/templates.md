# Minimum artifact contracts

These fields check completeness. They do not mandate a folder structure or empty document templates. Extend the existing canon through `profile.sources` first. Create new files only during actual work when needed, and register their paths in the profile. Preserve project IDs and statuses. Names below are examples for a new project.

## Foundation and source map — 01–05

`brief.md`: experience promise, audience/play conditions, loop, distinctive decisions, criteria, and open questions.

`scope.md`: current user objective and delivery, included/excluded scope, constraints, role of prototypes/early validation, decision owners, and approval source.

`systems-map.md`: system ID → purpose/gameplay result → inputs/outputs → state/owner → dependencies/events → canonical references.

`source-registry.md`: fact/ID/field → single authoritative source → derived text/data → synchronization rule → value status and change. Record conflicting sources before resolving them; do not silently merge them.

## System specification — 06/07

`ID, version/status, player experience, scope/exclusions, sources, states, entry/preconditions, rules and event order, outputs, cancellation/error/recovery, cross-system contracts, data/formulas/units/bounds, visible feedback, applicable modes, acceptance, risks/verification method, related tasks`.

To change an accepted decision: previous rule/rationale → new evidence/counterexample → why the previous rationale no longer applies → affected sources/checks. Do not reopen settled disputes solely because a new author prefers another option.

Calculations: inputs and their status, formulas/rounding, scenarios/edges, sensitivity, results, and limitations. Carry remaining resources and state between sequential content nodes. For procedural content, specify distributions, constraints, and validation cases. Calculations cannot establish enjoyment.

## Content and space — 07a–07c

Narrative unit: `ID → entry state/conditions → participants/actions/text and context → variables/outputs → branches/cancellation/retry/save → links to mechanics/spaces → acceptance`.

Authored space/board: purpose and gameplay path; units/scale/coordinates and orientation; measurable bounds; topology/entries/exits; placement layer with stable IDs; routes/challenges/resources; recovery/return; required states; kit/reference links; future construction criteria. The project selects diagram/data formats, such as SVG+JSON, a tilemap table, graph, or diagram. Text, plans, and data share IDs and remain consistent.

Procedural family: grammar/modules, parameters/distributions/bounds, connectivity and solvability invariants, placement/resource-balance rules, seed/version/determinism where needed, forbidden combinations, failed-generation fallback, and representative/extreme future checks. A fixed validation set does not prove every possible world.

## UX, art, environment, and audio — 08–11

UX flow: context/goal/entry → actions and visible states → empty/error/cancellation/recovery → input/focus/devices → accessibility/text → transitions/data → acceptance.

Art contract: visual principles with positive/negative examples, viewing scales, product-specific palette/shape/light/materials, variants/states, permitted reuse, production constraints, and exceptions. Actual images and their acceptance follow a [separate contract](visual-references.md).

Kit/assembly: component IDs, dimensions/joins/layers, uses/prohibitions, delivered files, assembly order, applicable collisions/overlaps/lighting, variation/dirt/wear only where needed, dependencies, defect checks, and effort estimates.

Audio event: ID, source/trigger/conditions, start/repeat/interruption/end, priority/variants, project-specific spatialization and audibility, music state, accessible alternative, format/channels/delivery/budget, and acceptance.

Production unit: ID and covered entities/states, authoritative requirements, reviewed visual versions or justified inapplicability, dimensional/technical contract, sources/exports/metadata, variants/reuse, dependencies, owner/effort, and observable acceptance. Do not label a concept as a production-ready model or finished sound.

Content row: `unit/family ID | requirement | specification | view/state | placement/use | asset/delivery ID | epic/story | QA | evidence | gap`. Tasks/QA may truthfully remain `pending` during the first 11a pass. Before 20/21, these must be actual links across all applicable scope.

## Architecture, decisions, rules, and risks — 12–16

Architecture: goals/constraints → context/integrations → modules/owners → states/flows/schemas → errors/recovery → compatibility/budgets → accepted decisions → future verification. Distinguish required behavior from implementation freedom.

ADR: ID/status/context, requirement and evidence, alternatives with tradeoffs, decision/rationale, mandatory consequences, compatibility/migrations, owners/dependencies, reconsideration criteria, and verification. Not every local choice requires an ADR.

Control manifest: `rule ID | bound role/layer | exact rule | incompatibility prevented | authoritative reference/version | check | exceptions/owner`. Extract accepted decisions without introducing hidden requirements.

Risk: scenario/cause/consequence, likelihood/impact with rationale, accepted mitigation and alternatives, owner, state, evidence method/timing/criterion, and failure cost/replanning. Separately identify whether a decision is needed now or measurement of the future product is needed later.

Change: recoverable before baseline → reason/decision → exact affected sources/IDs → changes/migrations → invalidated evidence → completed rechecks → remaining risks.

## Production and QA — 17–21

Epic: player/production outcome, boundaries/exclusions, requirements and all applicable content, dependencies, deliverables/owners, acceptance, and risks. Scheduling order does not remove later agreed content.

Story/task: implementer and outcome, exact current sources/IDs, starting conditions, contract and delivery files/formats, dependencies/blockers, main/edge/recovery scenarios, observable acceptance, player-experience link, prohibited simplification, estimates/assumptions, and future evidence. Package links must let another implementer find every required decision.

Capacity: role/available capacity/source, deliverables, optimistic/likely/pessimistic estimates with assumptions, parallelism/dependencies/critical path, rework/tools/licenses, and confidence limits. An unknown team is an unresolved estimating assumption, not an invented schedule.

QA case: `ID | requirement/story/unit | configuration/state | actions | observable expected result | data/edges | method/owner | planned/executed | actual evidence`. A playtest hypothesis also needs a question, audience/scenario, observation method, decision criterion, and consequences.

Readiness: agreed scope/snapshot; verdict; all COV areas and finite units/procedural families; current independent Codex subagent reviews; closed/open findings; task/QA/capacity dependencies; hypotheses with plans and failure costs; justified exclusions; next action. Page count alone cannot establish readiness.
