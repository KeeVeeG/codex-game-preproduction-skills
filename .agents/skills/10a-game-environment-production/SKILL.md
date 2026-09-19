---
name: 10a-game-environment-production
description: Plan reproducible production of game spaces and environments from approved layouts and art direction, including reuse, assembly, and future pipeline validation.
---

# 10a — Environment production

Roles: environment artist and technical artist with the spatial designer. Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Start after applicable results from 07b and 10. Produce D0 production contracts, not scenes, meshes, tilesets, or editor tools.

## Inputs and medium

Use `profile.sources.baseline`, `levels`, `environment`, `art`, `assets`, `mechanics`, `content`, and `architecture`. Read existing assembly recipes and placement data first. The source map identifies the owner of coordinates and dimensions; do not create a second editable copy.

Adapt to the medium: 3D modules, 2D tiles, illustrated backgrounds, boards, diagrams, rooms, or procedural families. For interface spaces, check whether 08/11 already covers component production. Do not turn UI into a mandatory 3D level. If there is no separate environment, record `N_A` with a reason, evidence, and reopening condition. Unknown applicability remains open.

## Work

1. Map every agreed space/family to shared elements, variants, and unique landmarks. Count source parts, assembled units, and placed instances separately. Find an existing production ID or a justified gap for each need. Verify differences and compatibility before claiming reuse.
2. Define the smallest kit that supports the stated situations. Specify units, measurements, dimensions, origin/pivot or anchors, orientation, seams/boundaries, allowed transforms, layers, and connections as applicable. Consider pixel grid, transparency, and sorting for 2D; export axes, collision, and surfaces for 3D; perspective, action zones, and state changes for backgrounds. Derive values from current design and technical contracts rather than a universal grid.
3. Separate gameplay structure, movement/interaction constraints, and decoration. Protect areas where decoration could obscure actions, views, text, or routes. For generation, separate mandatory constraints from cosmetic variation. Design owns seeds, allowed parameters, forbidden combinations, reachability/solvability checks, and failure recovery. Decorative generation must not add unapproved systems.
4. Trace spaces through boundary states of actual participants/objects: movement, turning, interaction, maximum size, carrying, camera, overlap, and recovery as applicable. Check state/solution reachability for puzzles, dimensions/access for routes, and character/pose/text combinations for dialogue scenes. Decoration cannot repair an undefined or impossible gameplay rule.
5. Write a recipe for each handcrafted area or procedural family: inputs, dependencies, part IDs, anchors, layers, materials/light/audio where applicable, exclusion zones, and assembly order. Reference canonical placement IDs or generation rules. Explain how final assets replace placeholders without changing gameplay boundaries, how rebuilding avoids duplicates, and how manual exceptions survive. Requirements for a future tool are not its implementation.
6. Plan a representative source → assembly → import/connection → gameplay check → measurement sequence before mass production. Choose it from actual risks, including reuse and exceptions; unique pipelines need their own criteria. Include seams, scale, references, readability, and target load. Do not mark future tests as completed.

## Output

Update canonical `environment` and `levels` recipes. In `environment-production-review.md` under `profile.paths.state_dir`, connect spaces/families, kits, dependencies, gaps, and future evidence. Handcrafted maps and procedural possibility spaces have different coverage denominators.

Hand off to [11](../11-game-asset-spec/SKILL.md), architecture, and production planning. Return spatial contradictions to 07b/07c, art issues to [10](../10-game-art-bible/SKILL.md), and missing visual details to [10c](../10c-game-visual-reference-pack/SKILL.md). Audio can proceed in parallel with separate file owners.
