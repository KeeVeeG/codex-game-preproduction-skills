---
name: 17a-game-production-readiness
description: Assess whether the agreed game has a feasible production plan through deliverable scope, role capacity, estimates, dependencies, and applicable release or support plans.
---

# 17a — Production readiness

For selected release, support, live operations, and analytics, use the [detailed contracts](../00-game-preproduction/references/service-and-release-planning.md) and include their content, roles, and acceptance in estimates. Use [QA/process-learning methods](../00-game-preproduction/references/qa-methods.md) for debt, defect queues, and past iterations where such evidence or obligations exist.

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. This stage estimates and plans; it does not hire people, purchase deliverables, produce assets, or publish the game.

## Inputs and applicability

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Read current `production`, `release`, `epics`, `stories`, `content`, `risks`, `qa`, and primary requirements from `profile.sources`. Use 11a and actual units/deliverables rather than file counts or sums of unlike quantities. Record source versions and limited/full scope.

The project determines team, platforms, distribution, languages, and support duration. In `profile.features`, `absent` permits N/A with a reason, evidence, and reopening condition; `unknown` remains open. Do not assume a storefront, campaign, online service, or commercial model.

## Review

1. Map the entire agreed scope and existing delivery phases to all epics/units: implementation, content, integration, verification, and handoff. Find omissions and double counting. Separate unique creation, adaptation, reuse, and assembly work. Early slices must retain a visible remainder of the agreed game.
2. Refine optimistic/most-likely/pessimistic estimates or another justified method by work package and role. Record method, confidence, and basis: own measurement, comparable example, catalog, or expert assumption. Include integration, rework, repeated acceptance, and applicable support. Unknown velocity, salaries, or supplier prices do not become facts. Preserve provisional and derived numeric status.
3. Build dependencies and role-availability scenarios, including one person covering multiple disciplines. Assess critical path, production throughput, queues, and external waits. Separate effort from calendar time; dividing total work by headcount does not establish a reliable date. State availability and contingency, and explain shared causes of correlated risks.
4. Plan calibration: which representative deliverable measures velocity, who records actual work/rework, when remaining estimates are recalculated, and what triggers revision. Offer capacity-shortfall options with consequences. Scope reduction needs an explicit decision and cannot be hidden in an estimate; option analysis can finish while that decision is pending.
5. Check applicable external dependencies: supplier/role, expected result, confirmed availability, license/provenance, cost, and schedule with source/date or `UNVERIFIED`. Documentation does not establish a team not yet formed or a contract not yet ordered.
6. Specify acceptance for the chosen delivery method: product/content/schema versions, future build reproducibility, release candidate, go/no-go, rights, and supporting materials. Plan data migration, updates/rollback, maintenance, defects, and communications where the product requires them. Missing applicable contracts are gaps; inapplicable services receive justified N/A rather than new scope.
7. Check production and QA task connections. Every outcome needs an accepting role and verification method; every risk needs an owner and dependent tasks. After 18/19, recalculate affected work packages. Previous conclusions do not automatically cover changed scope.

## Output

Update canonical `production` estimates as a calculation appendix to the authoritative delivery plan. If missing, create a minimal structure using [templates](../00-game-preproduction/references/templates.md) and register paths. Include coverage, estimates/assumptions, capacity scenarios, critical path/queues, external decisions, risks, acceptance, and task links. Every gap has an owner, closure method, and impact.

Send plan changes to its owner, tasks to [17](../17-game-create-epics/SKILL.md)/[18](../18-game-create-stories/SKILL.md), and checks to [19](../19-game-qa-plan/SKILL.md)/[20](../20-game-story-readiness/SKILL.md). Give the coordinator conclusions for 21 and shared logs under `profile.paths.state_dir`. Documentary feasibility is neither a completed release nor proven team productivity.
