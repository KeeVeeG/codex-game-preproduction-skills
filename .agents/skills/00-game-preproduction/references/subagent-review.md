# Independent Codex subagent consultation

Use Codex's available subagent tools for consultation. The default `profile.review` policy requires three checkpoints and visual review of each applicable image, with `reviewer: codex_subagent`. No external model, proxy, or model-specific adapter is required. Use the environment's configured model settings unless the user specifies otherwise.

Create a fresh reviewer context without the author's conversation, proposed verdict, or prior review conclusions. Supply the task, current primary requirements, explicit source files and versions, relevant profile fields, and acceptance criteria. Keep review assignments read-only; return findings to the responsible author. Use the actual tool interface available in the environment, not assumed command names. If delegation is unavailable, record the required review as pending and continue independent work. Self-review can assist a draft but cannot satisfy independent evidence.

Installation does not run consultations. User decisions may change review requirements when recorded in `policy_source`; missing tools are not such a decision.

## Checkpoints

| ID | Timing | Review scope |
|---|---|---|
| MR-DESIGN | After the first complete 11a | Player experience, mechanics and difficulty, applicable narrative and spaces, UX, art/audio, and content coverage. |
| MR-TECH | After 15a | Architecture, mandatory contracts, compatibility, data, reliability, budgets, and testable risks. |
| MR-HANDOFF | After the full 20, before 21 | Task completeness, dependencies and production capacity, requirement/content/QA links, and limits of the final verdict. |

Split a large checkpoint into bounded related disciplines with explicit coverage. A general response does not cover files the reviewer did not inspect. One subagent may cover several related items when each is evidenced; do not add duplicate reviews merely to fill roles. Stage 20's fresh-reader handoff remains a separate test of what an implementer can recover from the delivery alone.

After material changes, repeat the affected review scope. Reuse evidence only for unchanged sources and criteria whose coverage is established. Preserve old reviews as history, not current approval.

## Every applicable image

Before acceptance in 10c/11, give a reviewer access to **the actual images**: every used existing image and each new generated or artistically edited candidate version. Include unsuccessful new candidates in the ledger; unused historical archives need not be reviewed. Account for images embedded in documents, contact sheets, and variants, linking each panel to its source and version. A general MR-DESIGN response cannot replace per-image inspection.

The reviewer must open the images with available visual tools and list inspected files/panels, visible observations, and limits. Ask about silhouette and form, visible dimensions and joins, materials and lighting, composition, states, readability/accessibility, and deviations from specific requirements. A prompt, text description, filename, or unsupported claim that an image looks good cannot establish `visual_inspection: confirmed`.

For each image, record source SHA-256, viewed file and SHA-256, panels, assignment and response, reviewer identity, observations, and `confirmed`, `unsupported`, or `unconfirmed`. The coordinator checks findings against the original and canonical requirements; accepting advice does not automatically amend the canon. If the reviewer cannot view the file, required visual evidence remains incomplete. Do not issue `ACCEPTED_REFERENCE` before confirmed inspection and resolution of material findings.

An independent image reviewer may also assess reference acceptance when explicitly assigned both criteria. The author still integrates the findings. Artistic edits require new version evidence. Technical viewing copies map to the original and their visibility limits; they do not create an endless sequence of artistic versions requiring new reviews.

## Large images

Prefer direct inspection of original files. When viewing limits require smaller copies, use the optional [prepare-review-images.py](../scripts/prepare-review-images.py) with Python 3.10+ and Pillow. It runs locally and never contacts a service. Example from a game with this package installed:

```text
python .agents/skills/00-game-preproduction/scripts/prepare-review-images.py --root . --output-dir docs/preproduction/image-transport/run-001 --max-edge 1024 --quality 82 --max-image-bytes 500000 --max-batch-bytes 580000 --max-images 8 assets/art-references/example-v01.png
```

Replace the example with real explicit inputs and an output directory under the profile's state directory. With another installation location, resolve the script from this reference while keeping `--root` pointed at the game. These are adjustable preparation budgets, not tool limits; account for actual image count, dimensions, encoding, and any attachment overhead.

The helper preserves the full frame and aspect ratio, avoids upscaling, applies EXIF orientation, preserves alpha through PNG, and produces JPEG for opaque images. Embedded ICC is converted to sRGB; a corrupt profile fails. Content-based names and manifests preserve originals and refuse to overwrite different existing output. Manifests record dimensions, hashes, settings, and preparation batches with `prepared_local_only` and `not_sent`. Preparing a copy does not establish that a reviewer opened it.

Resizing and JPEG may obscure text, joins, or detail. Supply a usable original or explicitly identified detail panels with an overview for those criteria. Do not claim inspection of invisible features. The helper does not crop, render SVG, or handle animation/multiple frames. Render vectors separately with a suitable tool and retain their source link. Do not use image generation for technical resizing. Adjust budgets or grouping without dropping required coverage.

## Review record and findings

In the game's `subagent-review.md`, record the checkpoint or subject, date, reviewer task/agent identifier, independence and context supplied, exact assignment, explicit source files and hashes, image panels, scope, and a link to the actual response or failure. Use `pending`, `obtained`, `failed`, `uncertain`, or `recheck_required`. Wait for the existing assignment and inspect partial results before retrying; do not count dispatch as completion.

Connect each finding to the findings ledger and a disposition: `accepted`, `rejected_with_reason`, `needs_evidence`, or `needs_user_decision`, with supporting evidence and recheck results. `obtained` means a substantive response was received, not that every conclusion is correct or every finding is resolved. Missing required consultation prevents readiness; record a tool dependency separately from a design defect.
