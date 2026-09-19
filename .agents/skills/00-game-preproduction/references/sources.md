# Sources and adaptation boundaries

The main methodological source is [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios/tree/984023ddac0d5e27624f2baacde6105e45de375f), pinned to `984023ddac0d5e27624f2baacde6105e45de375f`, under MIT. Its notice is retained in the portable [LICENSE](../LICENSE).

The [provenance map](provenance.json) preserves the source package's stage-to-source mappings and archived hashes. These identify historical method lineage; this edition does not claim a new exhaustive upstream audit, textual equivalence, or execution of the original studio workflow.

The method was generalized from project-specific preproduction work. This edition uses English instructions and independent Codex subagent consultation. Project facts and personal configuration are excluded. Source roles bind to an actual game profile; feature applicability determines the work. Numbers, technologies, content scope, and production budgets come from the game rather than examples.

The package covers preparation for implementation. Upstream implementation, builds, profiling, runtime tests, and publication are not relabeled as completed D0 checks. Their required inputs, future tasks, risks, and evidence belong in the relevant production plans.

## Related methods

The following ideas are expressed in this package's own instructions; their source packages are not bundled as dependencies.

| Source snapshot | Methodological influence |
|---|---|
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD/tree/94b6727b00c8316557828c8a8ff2a48ff60d60cc) | Requirements/architecture/story handoff coverage and testing for two incompatible interpretations of one contract. |
| [BMAD Game Dev Studio](https://github.com/bmad-code-org/bmad-module-game-dev-studio/tree/2486f5f5f3b8870baa6cee4615a870c0330f441c) | Connections between game intent, design documentation, production planning, and future verification. |
| [Anthropic doc-coauthoring](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/doc-coauthoring/SKILL.md) | A fresh reader reconstructing a contract from the actual delivery without author explanations. |
| [obra/superpowers](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797) | Bounded delegation, independent review, and realistic behavioral skill evaluations. |
| [gstack-game](https://github.com/fagemx/gstack-game/tree/7259ab9782fa9c17e45c16f1fb8347823ddb4379) | Preserving the intended player experience in tasks and acceptance criteria. |
| [claude-game-design-suite](https://github.com/baxatron-git/claude-game-design-suite/tree/5dd265ac2b143d13683766cdaae9695d3d871909) | Evidence for reopening decisions, sequential resource states, and narrative recovery. |
| [awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/tree/b105e1cf617adf0b68ed98790a716bbb60993179) | Turn/undo boundaries, information before irreversible transitions, and evidence for pixel, seam, and frame accuracy. |
| [fcsouza/agent-skills](https://github.com/fcsouza/agent-skills/tree/e0a3dde8c1d865ef5b430040caab8e533f16d28e) | Procedural reproducibility inputs, random-stream separation, and version compatibility. |

Instruction loading also draws on [OpenAI's guidance on skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): precise selection, task-relevant detail, and explicit completion criteria.

These links document attribution, not instructions to install or run upstream tools. Related source code, templates, and instruction text are not included as third-party distributions. Their licenses and trademarks remain their owners'. No endorsement is implied.
