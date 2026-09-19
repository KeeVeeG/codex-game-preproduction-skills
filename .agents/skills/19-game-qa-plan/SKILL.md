---
name: 19-game-qa-plan
description: Plan game QA, regression, and player-experience checks from actual requirements and tasks while separating future tests from evidence already obtained.
---

# 19 — QA plan

Choose the medium and procedure using [QA methods](../00-game-preproduction/references/qa-methods.md): paper checks, think-aloud sessions, and network playtests support different conclusions. Give applicable [technology contracts](../00-game-preproduction/references/engine-profile-review.md), [delivery/services](../00-game-preproduction/references/service-and-release-planning.md), and [languages/assistive interfaces/VO](../00-game-preproduction/references/interface-production-details.md) targeted future checks.

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. This stage writes QA documentation; it does not create or run the game, future tests, CI, or test scaffolding.

## Inputs and scope

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Read current `profile.sources.qa`, `stories`, `epics`, `architecture`, `controls`, `content`, `risks`, `production`, `release`, and primary rules/UX/content. Preserve existing QA IDs and criteria; connect duplicates instead of renumbering without cause. Use 11a results.

Scope can be the entire agreed product, an epic, system, or story. Record sources/versions, checked units, and exclusions. Use `profile.features`: cover `present`, justify `absent` with reason/evidence/reopening condition, and keep `unknown` open. Do not replace chosen genre, engine, devices, modes, or languages with a universal test matrix.

## Work

1. Establish requirements and stories; mark missing sources `GAP` and continue useful work on available ones. Distinguish missing rules from missing future test results. Limited scope cannot claim full coverage.
2. Map task types to criteria and risks: logic/data, integration, UI, visual/audio perception, and player experience as applicable. If a declared type hides another material risk, add the appropriate method and record the mismatch.
3. For each requirement, specify preconditions/data, action, expected result, edge cases, method, role, and future evidence. Invariants/calculations may be automated; subjective hypotheses need observation and decision criteria, not merely a future video path. Where sources establish a risk, acceptance must distinguish the required property from a functional simplification that destroys it.
4. Add game-specific end-to-end and regression flows: required outcomes, cancellation/failure/recovery, system interaction, and data boundaries. Include multiplayer, save migration, economy, campaigns, platform compatibility, and localization only where applicable. For limited scope, select affected flows and list the remainder.
5. Assign a future experiment for each unverified core quality and budget: owner role, conditions, method, acceptance/revision criterion, decision point, and failure consequences. Preserve numeric status; a proposed threshold does not establish balance or performance.
6. Check requirement → case and case → requirement. Every mandatory content unit/variant needs coverage or explicit justification for reusing cases. A generic case does not prove coverage of each unit's unique states.
7. Allocate future verification levels by risk: data/unit, integration, smoke, regression, performance, sustained load, and applicable delivery checks. Long-running checks need justified duration, starting load, checkpoints, and methods to detect drift/accumulation. Do not copy arbitrary standards or require identical infrastructure for every project.
8. Plan reproducibility needs: fixtures, controlled time/randomness/failures, and data/environment versions. Evidence connects criterion, build/content/schema or document version, conditions, actual result, artifact, and acceptance. Assess instability on comparable versions. Quarantining a future test needs an owner, return condition, and interim coverage. Link defect → reproduction → fix → targeted regression; broaden runs according to risk.

## Output and evidence

Use applicable [special checks](../00-game-preproduction/references/conditional-design-checks.md) for turn/undo boundaries, irreversible transitions, procedural reproducibility, and exact pixel/repeatable visual deliverables. Review documentary contracts now; future generator, animation, and game-import checks stay `PLANNED`.

Update canonical `qa` plans or create minimal ones with [templates](../00-game-preproduction/references/templates.md) and register paths. Include scope/versions, mapping, cases, roles, future infrastructure, exit criteria, and gaps. Future tests are `PLANNED`; document review of the plan does not mean the game passed.

Send proposals to story owners and [20](../20-game-story-readiness/SKILL.md), and shared state/findings to the coordinator under `profile.paths.state_dir`. Required new gameplay measurements remain next-stage tasks.
