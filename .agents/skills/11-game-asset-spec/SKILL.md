---
name: 11-game-asset-spec
description: Specify game production units, variants, dependencies, technical delivery, and observable acceptance criteria without producing the game assets.
---

# 11 — Asset specifications

Role: production specialist with art/audio direction and technical expertise. Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Work is limited to D0 specifications; the project determines delivery formats, not a preferred engine.

## Inputs and identity

Use `profile.sources.assets`, `art`, `audio`, `environment`, `visual_manifest`, `ux`, `accessibility_localization`, `content`, `levels`, `mechanics`, and `architecture`. A full pass requires applicable results from 10/10a/10b/10c. Start with the existing registry and specifications. If absent, reconstruct it from requirements and register one canonical source through the coordinator.

Preserve existing IDs, owners, relationships, and schema. Distinguish gameplay entities, production units, files, variants, and placements; do not invent duplicate numbering for a template. Typography, procedural materials, data tables, music, 2D sprites, and 3D models need different contracts. Explain inapplicable fields; an unknown format is not proof of inapplicability.

## Work

1. Collect explicit and implied needs in scope, including transitions, failures, and feedback. Map each to an existing production unit or registry gap. Check shared components, materials, rigs, banks, and assemblies before adding a deliverable. For procedural content, specify generator inputs, allowed families, and result criteria rather than an infinite list of files.
2. Describe each unit's purpose and required differences: form/color/material, sound character, text limits, or data structure as appropriate. Visible content references specific current 10c reference IDs, files, panels, and versions. Check actual independent Codex subagent image review under `profile.review` and current acceptance for each used image. Return missing essential views/states or required reviews to 10c.
3. Specify source/export files, formats, naming, units, reference points, and integration parameters as applicable: grid/alpha/atlas/frames/bounds for 2D; geometry/materials/rig/collision/LOD for 3D; states/glyphs/scale/locales for UI/text; schema/stable keys/validation for data. Do not require FBX or LOD on every specification. Use current standards and preserve their evidence status.
4. Link animation/effect states, transitions, interruption, events, and variants to mechanics. For audio, specify groups/variants, playback, mix priority, and an accessible alternative for critical meaning. Check joints and assembly dependencies for modular environments. Contracts must distinguish neighboring deliverables instead of repeating generic paragraphs.
5. Name an owner and observable artistic, technical, and QA acceptance criteria. Future checks of import/integration, size/format, references, placement, and peak load need conditions and timing. Provenance/license of future material is a requirement, not an acquired right. Return art/budget conflicts with sources and a proposed resolution.
6. Ask an independent reviewer to check need → unit → specification → dependency → acceptance and justify each entry in reverse. Check ID uniqueness, file/variant count distinctions, dependencies, and cycles. Missing future game files are planned deliverables; missing mandatory rules are D0 gaps. In existing projects, no text reference does not prove an unused asset: consider actual resources, importers, scenes, addressing, and dynamic references of the relevant environment.

## Output

Update canonical specifications and registry links. Its assigned owner makes shared edits during parallel work. Record scope, input versions, the mapping, violations, and remaining checks in `asset-spec-review.md` under `profile.paths.state_dir`. A Markdown file alone does not improve specification status.

Completeness applies to the entire agreed scope. Hand off to architecture, production, and [11a](../11a-game-content-coverage/SKILL.md). Route gaps to 10/10a/10b/10c/09a owners. Adding another entity does not repair a missing relationship or obsolete ID.
