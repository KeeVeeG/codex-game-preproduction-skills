---
name: 10c-game-visual-reference-pack
description: Resolve visual uncertainties with actual reference images, required views and states, and independent Codex subagent review of every used image and new artistic version.
---

# 10c — Create and accept visual references

Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Read the [visual package criteria](../00-game-preproduction/references/visual-references.md) and [subagent review protocol](../00-game-preproduction/references/subagent-review.md). Before generation, read the available ImageGen skill and follow its tool requirements. Create D0 reference material; game applications, 3D assets, and engine import are outside this stage.

## Inputs and representation

Use `profile.sources.baseline`, `art`, `assets`, `content`, `levels`, `environment`, `ux`, `accessibility_localization`, `architecture`, `visual_manifest`, and existing references. Read actual files and reviews, not only names or index status. Preserve good current images; an attractive early concept does not override accepted rules.

Choose a medium that resolves the uncertainty: existing image, ImageGen raster concept, vector/dimensioned diagram, mockup, or typography sample. Abstract, text, and vector games do not require 3D concepts. No need for raster generation does not remove appearance documentation or review of images actually used. Complete `N_A` requires evidence that visual direction is unnecessary, a reason, and a reopening condition. Unknown needs remain gaps.

## Work

1. Expand visible content into a unit/family/variant/state → required views and details → actual image/panel → observation → gap matrix. For procedural content, cover visual grammar, combination constraints, representative examples, and boundaries; do not claim to enumerate every seed. A shared sheet does not prove visibility of every module or essential state. Shared specifications need explicit inheritors and differences.
2. View selected images with an available image-viewing tool. Record verified style, proportion, and palette anchors and input usage limits. Order work by dependencies: core reference → families/kits → variants/states → required scenes. Image count follows unresolved questions, not quotas or one-image-per-ID rules.
3. For a justified AI raster concept, call built-in ImageGen with current inputs and a precise task: what to show, preserve, and resolve. Use suitable tools for vector or exact dimensioned material; an attractive concept cannot replace a measurable diagram. Prompts do not satisfy an actual-image requirement. Record reuse when accepted references are already sufficient.
4. For failures or `illicit`, follow [error handling](../00-game-preproduction/references/visual-references.md). `illicit` may indicate a model-policy rejection, not established illegality. For an allowed task, clarify benign intent or remove an optional problematic detail without hiding prohibited intent or bypassing a restriction. Address technical failures by cause. After one justified retry, stop retrying without new evidence, record the gap, and continue independent work. Wait for a running call instead of duplicating it; do not silently switch APIs or CLIs.
5. Inspect the whole result and each meaningful panel: shape, proportions, material/texture, color, joints, states, camera, and readability as applicable. Fix specific defects with appropriate tools; use ImageGen to edit generated raster art. Canonical spatial/gameplay specifications take precedence over composition. Send contradictions to their owner. Each new artistic result is a new version.
6. Save every new result, including rejected candidates, as explicit versioned project files. Record provenance, input versions/scope, task/prompt, actual output, hashes, limits, and requirement links in canonical `visual_manifest`. Do not overwrite old versions or confuse copying with selection or acceptance.
7. Have an actual independent Codex subagent review every used existing image and every new generation/artistic edit under `profile.review`. Give the reviewer primary requirements, image files, required panels, and exact scope without author conclusions or reasoning history. It must actually view the images and return observations per file/version. Text descriptions, collection-level comments without file coverage, or unavailable image access do not establish acceptance. Missing required review remains pending evidence; continue other useful work.
8. When smaller viewing copies are needed, use [prepare-review-images.py](../00-game-preproduction/scripts/prepare-review-images.py) under the [transport rules](../00-game-preproduction/references/subagent-review.md), with explicit files, project `--root`, and an in-project `--output-dir`. Preserve originals and source/viewing-copy SHA links. Verify critical detail readability and provide a precise crop with context if needed. Compression without artistic changes does not create an endless version/review cycle. Script budgets are local settings, not provider limits.
9. Obtain independent art/technical acceptance against primary requirements and actual images, and address findings. One focused subagent review can cover both detailed image checks and package acceptance when it explicitly examines each obligation; do not duplicate reviews merely for ceremony. Keep selection, review, and final approval within project authority and do not invent user approval. Routine fixes proceed within scope; significant new creative choices return to the coordinator.

## Output and completion

Deliver actual references, an updated index/`visual_manifest`, and `visual-reference-review.md` under `profile.paths.state_dir`. Link units, versions, panels, original/viewing files, reviews, and acceptance; retain rejected candidates and their outcomes. Use the existing schema or the minimal shared structure, not a second registry.

Complete when applicable rows have current accepted materials and production-relevant appearance is defined. Required missing images/reviews remain gaps. Hand off to [11](../11-game-asset-spec/SKILL.md) and [11a](../11a-game-content-coverage/SKILL.md); changed inputs or artistic versions trigger affected rechecks. The assigned coordinator updates shared logs.
