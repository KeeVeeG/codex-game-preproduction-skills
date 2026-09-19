---
name: 05-game-consistency-check
description: Reconcile shared entities, states, values, and formulas across game documents and data, maintaining a canonical source registry. Use after shared-rule changes or for consistency audits.
---

# 05 — Reconcile sources and values

Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. Inputs through `profile.sources`: baseline, specifications, structured data, system map, and current changes. Use the project's existing formats, whether Markdown, JSON, spreadsheets, or another representation; conversion to fit a template is unnecessary.

Modes: full reconciliation; a bounded entity/system; or changes since a verified revision, including suppliers and consumers. If the starting revision is unknown, check the entire assigned area. Include uncommitted changes. Git is not required.

1. Find the existing source registry or build one from current materials. An empty registry is not a successful pass. Each entry includes a stable ID/name and aliases, category, canonical path and exact section/pointer, shared attributes, units, definition status, and consumers. The registry indexes facts; a dated value snapshot does not become another canonical copy.
2. Apply source authority established by the profile and accepted decisions. The baseline owns scope and invariants; designated specifications own details. A newer date or machine-readable format alone does not give priority. Record unresolved ownership as a conflict.
3. Find repeated IDs, names, states, formulas, and values throughout the review scope, including entities missing from the old registry. Compare equivalent contexts: mode, phase, category, content version, participant count, and other supported dimensions. Check types, units, ranges, rounding, and condition boundaries.
4. Distinguish invariants, chosen starting settings, calculated results, and hypotheses using the project's labels. Recalculate derived examples. For probabilities, check normalization, independence or conditioning, and what each percentage means. For time, check the common timescale, ticks/frames/seconds, and interval boundaries where used.
5. Reread each candidate in material context. Distinguish contradictions, outdated snapshots, synonyms, valid derived values, and references with insufficient data. Check backlinks and orphaned IDs in applicable catalogs. A missing required catalog remains a coverage gap.
6. Change the defining source only with a decision-based justification, then update consumers. Do not silently choose a convenient number. Send conflict history, shared registry changes, and affected dependencies to the coordinator. Do not mix review with another author's concurrent edits.

Output: the existing registry or `source-registry.md`, plus `consistency-report.md` in `profile.paths.state_dir`. Include scope, checked entries/files, conflicting source pairs, calculations, corrections, and remaining limitations. An independent Codex subagent checks material corrections against primary data under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md).

Completion: shared facts in the assigned scope are accounted for; material conflicts are resolved or explicitly limit the relevant conclusion. Continue to [06](../06-game-design-system/SKILL.md). After revisions, repeat 05 along affected dependencies; after a series of changes, repeat [04](../04-game-review-all-gdds/SKILL.md). Partial coverage cannot support an overall positive verdict.
