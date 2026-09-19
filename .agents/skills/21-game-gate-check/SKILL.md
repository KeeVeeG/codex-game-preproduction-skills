---
name: 21-game-gate-check
description: Determine evidence-based readiness of all agreed game D0 documentation, including feature applicability, current reviews, and unresolved mandatory contracts.
---

# 21 — Final D0 readiness gate

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Use the full [coverage framework](../00-game-preproduction/references/coverage.md) and [workflow](../00-game-preproduction/references/workflow.json). Review the game's entire agreed scope. This skill neither changes the project stage to development nor starts implementation.

## Inputs and scope

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Resolve actual paths from `profile.sources`: primary requirements, `content`, `architecture`, `decisions`, `controls`, `risks`, `epics`, `production`, `stories`, `qa`, `release`, `reviews`, and other present disciplines. Read reports in `profile.paths.state_dir` and compare their versions with current sources. An old positive verdict does not cover changed documents.

Reconcile `profile.features` with the product: `present` needs coverage; N/A for `absent` needs a reason, evidence, and reopening condition; `unknown` remains unresolved applicability. Do not add campaigns, networking, storefronts, or languages by default. Unknown catalogs do not establish absent content.

## Review

1. Reconcile final coverage and 11a with the full agreed scope, actual catalogs, and mandatory entities in prose. Each applicable area/unit needs a concrete source, current substantive review, delivery plan, and acceptance. `MISSING`, `DRAFT`, `REVIEW_REQUIRED`, and `RECHECK_REQUIRED` do not close obligations. Limited audits show the remainder and cannot give overall readiness.
2. Confirm consistency of rules, numbers, states, contracts, and owners. Every mandatory requirement has a source, plan location, and verification method. Missing registries/specifications are gaps; fixed counts of ADRs, files, or rows are not quality criteria. Mandatory boundaries must not admit two incompatible implementations equally compliant with their text.
3. Review every present deliverable type: levels/spaces/routes, narrative, environment, UX, accessibility/languages, art/audio/animation, and individual content specifications. Derive scope from the profile and sources. Spatial requirements need precise plans and appropriate data; artistic perspective cannot prove geometry. Do not hide unique variants or later agreed content behind generic specifications.
4. Apply the [visual criteria](../00-game-preproduction/references/visual-references.md) to 10c when images belong to the agreed deliverable: actual saved files, views/states/panels, ID/version links, substantive observations, and independent acceptance. Prompts, missing files, and generic moodboards do not replace required images. A profile N/A cannot exclude images actually used; resolve the applicability mismatch first.
5. Check completeness and order of implementation, all content types, tools, QA, and applicable delivery tasks. Final 11a after 18/19 and 17a must reflect current scope; 15a must cover technical risks and future measurements. Under [handoff review](../00-game-preproduction/references/handoff-review.md), verify stage 20's sample composition, actual files/reader response, and closure of mandatory assumptions. Successful samples do not replace full story audit.
6. Separate undefined specifications from future hypotheses. An allowed untested gameplay assumption needs an owner role, method, decision criterion, checkpoint, and failure consequences; preserve numeric status. `PLANNED`/`PLANNED_RUNTIME` is not a completed test. No future build alone does not fail D0; unknown mandatory rules or production contracts are gaps.
7. Read independent reviews of all applicable disciplines, checking scope, versions, actual responses, and finding closure. Self-review or merely assigning an agent does not prove independent acceptance. Reread the weakest sources and failure flows and try to disprove the provisional verdict. Each material open finding needs concrete consequences and a closure condition.

## Independent subagent reviews

Under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md), verify required MR-DESIGN after the first full 11a, MR-TECH after 15a, and MR-HANDOFF after full 20 before 21, including affected rechecks. The reviewer is an actual independent Codex subagent (`profile.review.reviewer = codex_subagent`). Require substantive returned responses, current source versions, and disposition of findings, not just evidence that delegation was requested. Fresh reviewers receive sources and neutral scope without author conclusions or reasoning history.

`profile.review.required` and `profile.review.image_review_required` determine required checkpoint and image reviews; the default policy requires both. A different policy needs a documented basis in the user's decision. Do not waive review because of tool failure, elapsed time, or an obsolete log. A policy exception does not waive substantive and independent verification of the deliverable.

For used existing images and each new generation/artistic edit, verify file/version/panels → actual subagent viewing and observations → finding disposition → acceptance. A checkpoint review can cover multiple explicitly examined items; it cannot substitute for missing per-file coverage. Text-only responses, inaccessible images, or reviews of old hashes do not establish current viewing. Reuse current evidence only with verified source/viewing-copy hash and scope links. Rejected candidates remain in history and cannot fill a required accepted view. Unused historical archives are not automatically in scope.

Missing, failed, or obsolete required reviews exclude `READY_FOR_IMPLEMENTATION`; use `NEEDS_REVISION` with the delegation or image-access dependency. Tool failure is not a design defect and does not stop available corrections. Cancelled requirements remain historical, not successful reviews. Preserve substantive findings. Broad checkpoint consultation cannot replace stage 20's separate clean-context reader.

## Output

Update the existing final `reviews` report or `readiness-report.md` under `profile.paths.state_dir`: scope/versions, evidence by criterion, gaps, future hypotheses, limits, and verdict. Do not fill missing author specifications inside the gate merely to change status. Assign concrete fixes to owners and repeat affected checks.

- `READY_FOR_IMPLEMENTATION`: all agreed D0 scope is reviewed with no unresolved mandatory rules, contracts, or reviews.
- `NEEDS_REVISION`: specific repairs, updates, or remaining review are required.
- `NEEDS_USER_DECISION`: a genuinely unresolved product or external choice requires the user; list all other gaps too.

Send state/findings entries to the coordinator. When ready, conclude the documentation stage. Implementation needs a separate user instruction, which may be given in the same task.
