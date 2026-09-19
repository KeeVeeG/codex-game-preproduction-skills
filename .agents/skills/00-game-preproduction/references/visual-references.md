# Visual references sufficient for production

Stage 10c removes mandatory guesswork about appearance. Images support the specification's dimensions, states, and rules. Concept perspective does not change a location's geometry or establish that an asset works.

## Choose necessary coverage

From the current catalog and art direction, list visible units, families, variants, and states. For each, identify which questions need images and which views are sufficient. An unspecified “art” topic or a single moodboard does not define individual entities.

- For 3D forms as needed: silhouette, front/profile/rear/scale views, connection/material details, movement/states.
- For 2D: sprite or illustrated form, angles/layers, palette/on-screen size, required states and directions. Do not assign frame counts without a project reason.
- For environments: overview and necessary working views of modules, joins, palette/materials, scale, lighting, route readability, and family variants. Dimensioned level layouts remain a separate canonical source.
- For UI/typography: actual compositions at target formats, focus/states, density/localization, contrast, and links to actions. For precise SVG/HTML/fonts, prefer editable sources and verified renders.
- For printed components: dimensions, sides, bleeds/margins for the selected process, symbols, and states. Verify printer requirements separately.

Retain suitable existing references when rights, versions, and compliance with requirements are established. New images are unnecessary when the required appearance is already unambiguous. If raster concepts are needed, use available image generation within the assignment; a tool call alone does not produce approved game assets or approve the artistic direction.

For exact pixel art, seamless repetition, or frame consistency, read the [format-specific checks](conditional-design-checks.md). A compressed transport copy or artistic concept does not automatically establish grid, palette, join, or future animation accuracy.

## Generation and provenance

Read the active image-generation skill/tool instructions. Before editing, inspect the actual source image. For a new image, provide the agreed form, style, purpose, required views/states, format, constraints from canonical sources, and reference IDs. A prompt is a production input, **not an image**. A written prompt, an unviewed URL, or a missing output does not fulfill an image requirement.

Track rights and provenance for external sources; inspiration is not automatically a licensed production asset. Do not download third-party material to bypass display restrictions. Save the actual file returned by the generator in the profile's directory with a version; do not invent output paths or receipts. Resume a running job instead of creating a duplicate. Display local images using absolute paths when the environment requires them.

Use the built-in tool by default when available. A missing result does not authorize silently switching to a paid CLI/API or installing a tool. The chosen method must follow the assignment and current environment instructions.

## Generation failures

Read the actual response and distinguish content-policy refusals from technical failures such as unsupported dimensions/formats, unavailable services, or unfinished jobs. A refusal label such as `illicit` is not a legal finding about the project. If a permitted concept was ambiguous, clarify its permitted purpose and remove unnecessary ambiguous detail. Do not disguise a prohibited goal, bypass a refusal with euphemisms, or repeat an unchanged refused request.

Correct an established cause and make one justified retry. After a repeated refusal/failure, record the requirement, attempts, and exact dependency while continuing independent work. Resume when inputs or service conditions change rather than cycling endlessly through prompts. A failure neither counts as a generated image nor removes the requirement.

## Manifest and acceptance

Use the existing manifest at `profile.sources.visual_manifest`; if none exists, create an agreed index. Each entry contains:

`reference_id | unit/family IDs | view/panel/state | path | version | SHA-256 | source/rights/tool and actual receipt | prompt/inputs | normative requirements | decision/limitations | subagent visual review and acceptance`.

Many-to-many relationships are allowed: one sheet may cover several units, but every panel and version must be identifiable. Track variants, details, reuse, and uncovered questions separately. Procedural families need an appearance grammar, boundaries, and representative/extreme examples; a few images do not cover every possible generator output.

Useful statuses are `PLANNED`, `GENERATED_PENDING_REVIEW` or `EXISTING_PENDING_REVIEW`, `NEEDS_REVISION`, `ACCEPTED_REFERENCE`, and `REJECTED`. Preserve each new artistic version, including unsuccessful candidates, and have it reviewed by a fresh Codex subagent under the [subagent review protocol](subagent-review.md). Use `profile.review` with `required`, `image_review_required`, `reviewer: codex_subagent`, and `policy_source` to record the applicable review policy. Count only observations from the actual image and current version. A reviewer name or a returned response alone is insufficient evidence.

Give the subagent the image, primary requirements, relevant canonical sources, and a bounded review task. It must inspect characteristic form, readability at the intended scale, key states, consistency between sheets, visual accessibility, feasible joins/layers, and misleading geometry where applicable. Record its identity/task, source paths/versions/SHA, image content actually observed, findings, disposition, verdict, and visibility limits. One independent subagent may provide both visual observations and acceptance in the same review; an additional reviewer is unnecessary when that scope is covered. The author verifies findings against canonical requirements and records fixes or reasoned dispositions. If an independent subagent or necessary image-viewing tools are unavailable, label self-checks and leave required independent evidence pending.

An accepted reference has no unresolved mandatory appearance decision within its scope. Artistic changes or changed requirements invalidate affected reviews and specifications. Technical transport copies link to the source SHA and state visibility limits; they do not create a new artistic version. Until required review is complete, dependent visual deliveries cannot be `READY`; independent text/audio work may continue.
