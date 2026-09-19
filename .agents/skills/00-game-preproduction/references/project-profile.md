# Game profile and source bindings

The package defines the method; the profile defines the product. On the first full run, stage 01 checks the user-specified profile location, then `docs/preproduction/project-profile.json`. If absent, create it from [profile.template.json](profile.template.json), existing material, and the request. A focused task without a profile establishes only the bindings it needs and records the unknown remainder; it does not require a full stage 01 pass. Installing skills does not start this process. Read this guide when creating or changing the profile or resolving unclear bindings.

Extract known facts before asking questions; ask only what materially changes the next work. For a new idea, create a short brief and scope. For an existing project, preserve documents and IDs. An unknown engine need not block work on the game loop, but cannot justify an invented technical contract.

## Fields

- `project`: name, intended player experience, audience, and genres, using the project's language. Genre labels do not automatically establish mechanics.
- `scope`: assignment goal, target delivery, inclusions, exclusions, and constraints. A full game, module, expansion, or slice follows the actual request. Preserve the entire agreed scope; an early prototype does not replace it.
- `game`: platforms, engine and version, presentation, input, player counts and modes, content structure, and languages. Empty lists or `null` mean unknown, not absent. Do not default to a particular engine, 2D/3D, frame budget, multiplayer, or localization.
- `features`: applicability values `present`, `absent`, and `unknown`. Template keys aid discovery; extend them for domains such as VR, physical components, or modding. `present` enables checking; `unknown` requires resolution. Support `absent` with `feature_evidence[key]` containing `source`, `reason`, and `reopen_when`.
- `sources`: semantic role to a list of explicit paths relative to the game root. An empty list means the source has not been found or created. One document may serve several roles. Extend role names as needed; bind aliases such as `mechanics` and `systems` to the same source when appropriate instead of duplicating documents.
- `authority`: canonical source order and decision owners. Current user instructions take priority. Modification time does not establish authority; preserve unresolved conflicting claims and the decision needed.
- `paths.state_dir`: working records, default `docs/preproduction`. `paths.reference_dir`: actual images, default `assets/art-references`; preserve an existing suitable location. These paths are relative to the game, not the installed skill.
- `review`: consultation policy. Defaults are `required: true`, `image_review_required: true`, and `reviewer: codex_subagent`. Use fresh, independent Codex subagents without selecting a fixed model or external service. Record the policy's authority in `policy_source`. Explicit user decisions may change requirements; tool unavailability does not authorize weakening them. Details are in [subagent-review.md](subagent-review.md).

The template intentionally contains unknowns. It is neither a completed profile nor readiness evidence. Adapt it during bootstrap without replacing an existing populated profile. Do not store credentials or personal absolute paths in it.

## Applicability and coverage units

Consider every stage in a full run and perform its applicable work. A focused task establishes applicability for its scope and dependencies. `N_A` requires a reason, canonical source, and reopening event. Missing files, time, tools, staff, or decisions do not imply inapplicability. An evidenced `N_A` satisfies a workflow dependency; an unknown mandatory dependency does not. Partial applicability cannot make an entire stage `N_A`.

| Product | Questions to resolve |
|---|---|
| Grid puzzle | Cell rules, states, solvability, authored boards or generation contracts. Story and combat may be absent; input and feedback remain. |
| Visual novel | State graph, branches, variables, return/skip/save behavior, backgrounds, portraits, and text. A location does not imply 3D navigation. |
| Procedural cooperative game | Zone families, grammar and parameter ranges, determinism and versions, connectivity, resource bounds, future test seeds, state ownership, and recovery. |
| Board or primarily text game | Components, rules, information states, and play sequence; physical delivery where applicable; text and component accessibility. Rendering and CI are not automatic requirements. |

List every agreed finite authored unit. For procedural, unbounded, or user-created content, list families, rules, mandatory combinations and boundaries, test sets, and generation or moderation constraints. A sample with declared remaining coverage does not prove every possible outcome. Hybrid projects require both forms of accounting.

Relative links in SKILL.md resolve inside the package. Profile paths resolve from the selected game root. Keep game artifacts in that game, not in a separate skills repository.
