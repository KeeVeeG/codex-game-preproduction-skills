---
name: 15a-game-technical-risk-review
description: Review applicable game risks in failures, load, compatibility, and content pipelines, and specify future evidence without implementation.
---

# 15a — Technical risk review

Check applicable risks against the [engine/technology profile](../00-game-preproduction/references/engine-profile-review.md) and [services, data, and delivery](../00-game-preproduction/references/service-and-release-planning.md). Use [QA and debt methods](../00-game-preproduction/references/qa-methods.md) for inherited debt and future experiment selection. Unknown applicability does not mean an absent feature.

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. This stage extends architecture from 12–15; an early limited pass can inform a risky decision. It creates contracts and an experiment plan, not implementation.

## Inputs and applicability

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Read `architecture`, `decisions`, `controls`, `risks`, `content`, `qa`, `release`, and primary requirements through `profile.sources`. Preserve chosen technologies and the full agreed product scope. Record review scope and source versions.

Use `profile.features` for applicable boundaries and scenarios. `absent` needs a reason, source, and reopening condition; `unknown` remains uncertainty. Do not presume networking, cloud, user-generated content, analytics, or voice. Add security measures, servers, or services only from requirements and justified risks.

For non-digital deliverables, technical risks may involve materials, component reproducibility, assembly, readability, and manufacturing constraints. Assess actual requirements. Software categories below receive specific N/A justification when there is no digital component; they do not require creating one.

## Review

1. **Trust and recovery.** For actual inputs, participants, and storage, identify trusted/untrusted data, authority owners, and invalid-input outcomes. Where applicable, trace repeated/spoofed commands, size/rate limits, invalid IDs, partial failures, saving/migration, interruption, and service unavailability. Distinguish protection of mandatory invariants from permitted user changes. Personal data, diagnostics, and recordings follow accepted project constraints; do not invent retention rules from reviewer preferences.
2. **Simultaneous load.** Choose representative and boundary scenarios for all applicable modes/spaces. Examine only used resources: computation, graphics, memory, input, audio, loading, physics, AI, network, or storage. Check units, limits, and budget composition; do not add parallel CPU/GPU phases as though sequential. Distinguish forecasts, allowed configurations, and measurements. Future experiments need configurations, duration, meaningful averages/peaks/percentiles, and comparison criteria.
3. **Pipeline and compatibility.** Trace the actual source-to-delivery chain: data/ID/reference validation, transformation, import, build, and packaging. Applicable operations need source-level diagnostics, repeatability, tool/data versions, deletion/migration, and partial-failure recovery. Verify dependency provenance and reproducible-delivery requirements. Plan future validators, build processes, and test tools as tasks; do not implement them now.
4. **Observability and external dependencies.** Every collected metric answers a testable question with a known source, receiving role, collection method, and access/retention limits. Verify material API/SDK capabilities and license terms against official sources for the relevant version and date. Keep unverified claims `UNVERIFIED`; do not assert either successful compatibility or impossible integration.
5. **Risk response.** Separate repairable mandatory-contract gaps from uncertainty requiring future gameplay measurement. For each risk, record cause, trigger, consequence, likelihood/impact with rationale, owner, prevention, and recovery/fallback. An unknown mandatory outcome cannot be hidden behind an experiment without specifying safe behavior.

## Output and checkpoint

Update canonical `risks`, or create a minimal register using [templates](../00-game-preproduction/references/templates.md). Each entry connects risk to requirement/scenario, uncertainty, owning role, measures, a `PLANNED` experiment, decision criterion, dependent ADRs/tasks, and status. Preserve numeric evidence status; documentary PASS is not a game measurement.

Send findings, versions, and required 13–15/17–20 rechecks to the coordinator. Changes to accepted rules pass through [16](../16-game-propagate-design-change/SKILL.md). After 15a, the coordinator conducts MR-TECH when `profile.review.required` requires it, using an independent Codex subagent under the [review protocol](../00-game-preproduction/references/subagent-review.md). Policy changes need a basis in the user's decision; unavailable delegation does not waive a required review. Missing evidence stays pending. Tool failures are not design defects and do not stop other useful corrections.
