# Codex Game Preproduction Skills

32 portable Codex skills for preparing game design and production documentation before implementation. One coordinator guides 31 specialist stages, preserves progress, and commissions independent Codex subagent reviews.

The deliverable is **documentation readiness for implementation (D0)**: agreed rules, content specifications, architecture, production tasks, and a QA plan. Game code, finished production assets, playtest results, performance measurements, and release execution are separate work.

## Install

Copy **all 32 folders** from [.agents/skills](.agents/skills) into your game's `.agents/skills` directory, preserving their names. Compare existing folders before replacing local changes. Shared references, the optional image helper, and attribution are included under `00-game-preproduction`; this repository's `docs` and `tools` are not runtime dependencies.

Open the game workspace in Codex and start a task with the skills available. If discovery is unavailable, give Codex the installed path to `.agents/skills/00-game-preproduction/SKILL.md` and ask it to read that file.

Requirements:

- Codex with local file access and subagent delegation for independent reviews.
- Image viewing for applicable visual references; image generation only when new raster concepts are needed.
- Python 3.10+ and Pillow only for the optional image preparation helper and its tests.

No third-party model service, API key, or proxy is required.

## Use

For a full pass:

```text
Use $00-game-preproduction to prepare the entire agreed game scope
for implementation. Preserve existing canonical sources, resolve
documentation gaps, obtain the required independent reviews, and save
progress. Report READY_FOR_IMPLEMENTATION only when the evidence supports
it. Do not start implementing the game.
```

For a new idea, include a short game description and known constraints. An existing project can start from its current documents.

To resume:

```text
Continue with $00-game-preproduction from the saved project state.
```

For a focused task, invoke a specialist such as `$07b-game-level-design`. This does not start the entire workflow or claim readiness for the whole game.

## Workflow

| Stages | Scope |
|---|---|
| 01–05 | Project profile, systems, scope, design review, and consistency |
| 06–07c | Mechanics, calculations, narrative, spaces, and spatial review |
| 08–09a | UX, interface review, accessibility, and localization |
| 10–11a | Art, environment, audio, visual references, assets, and content coverage |
| 12–16 | Architecture, decisions, implementation constraints, risks, and change propagation |
| 17–21 | Epics, production capacity, tasks, QA, handoff review, and the D0 verdict |

The [project profile](.agents/skills/00-game-preproduction/references/project-profile.md) binds semantic source roles to the game's existing files. It records scope, platforms, engine, languages, and feature applicability without assuming a genre or technology. Authored content is tracked by unit; procedural content by family, rules, boundaries, and test sets.

Every stage is considered in a full run. Inapplicable work requires an evidenced `N_A`; unknown requirements remain open. A draft, a filled template, or a missing tool cannot establish readiness.

See the [workflow graph](.agents/skills/00-game-preproduction/references/workflow.json), [20 coverage areas](.agents/skills/00-game-preproduction/references/coverage.md), and [artifact contracts](.agents/skills/00-game-preproduction/references/templates.md) for detailed requirements. Instructions load as needed for the current stage.

## Independent review

Consult fresh Codex subagents after design/content, after technical risk review, and before final handoff. Reviewers inspect explicit source versions and return findings for resolution. Applicable visual references require actual image inspection for each used file and new artistic candidate version. Stage 20 separately checks whether a fresh reader can work from the handoff package without the author's explanations.

The [review protocol](.agents/skills/00-game-preproduction/references/subagent-review.md) defines coverage, evidence, and rechecks. If delegation or image viewing is unavailable, required evidence stays pending while independent work continues. The default policy is stored in the profile; explicit user decisions can change it.

## Maintain and verify

From the repository root:

```sh
python tools/validate-package.py
python tools/test-package-validator.py
python -m pip install Pillow
python tools/test-image-transport.py
```

Checks cover package structure, source links, review configuration, portability, and local image preparation. They do not prove design quality or the readiness of a particular game. See [validation scope](docs/validation.md) and [contribution guidance](CONTRIBUTING.md).

## License and attribution

[MIT](LICENSE). Adapted methods include [Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios/tree/984023ddac0d5e27624f2baacde6105e45de375f); its copyright notice is retained. [Sources and adaptation boundaries](.agents/skills/00-game-preproduction/references/sources.md) and the [stage provenance map](.agents/skills/00-game-preproduction/references/provenance.json) document attribution.

This is an independent community project, not an official OpenAI product or an endorsed distribution of the upstream project.
