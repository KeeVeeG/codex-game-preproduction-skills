# Handoff review without author history

At stage 20, a fresh reader reconstructs the contract from the actual delivery package. This supplements the full review of all stories and content; the sample does not replace that review.

The coordinator lists every story and delivery type present. Select at least one example of each type (such as logic, integration, board/location, visual asset, UI, audio, text, or release), plus unique or risky contracts and previously ambiguous packages. One example may cover several types. Record the full population, selected IDs, selection reasons, and unexamined scope.

Give a fresh Codex subagent the assignment, this method, actual delivery files, the profile and primary requirements, and accessible normative references. Do not supply author explanations, expected conclusions, discovered answers, prior reviewer conclusions, or discussion history. Use a fresh context when available (for Codex collaboration, `fork_turns="none"`). This describes a capability, not a promise that the tool exists. If no fresh subagent is available, label any self-check and leave required independent evidence pending under the [subagent review protocol](subagent-review.md).

Without coding or changing the materials, the reader:

1. Reconstructs the result, IDs/versions, initial states, operations, outputs, errors/recovery, dependencies, receiving role, and acceptance criteria. Links significant claims to files and sections.
2. Lists the inputs an implementer in that discipline needs: for spaces, scale/layout, placements or generation constraints, kits, and visual sheets; for text, variables/context/conditions; for logic, states/priorities/contracts. A future delivery is acceptable as an explicit dependency.
3. Explains how to distinguish an acceptable result from one that satisfies a checklist but undermines the core experience. Does not invent missing art rules or constants.
4. Records assumptions, conflicts, inaccessible references, and missing answers. Distinguishes an unknown mandatory contract from a hypothesis with a future measurement plan and from a reading error.

In the working directory's `story-readiness.md`, record the subagent identity/task and discipline, supplied files/versions/SHA, full and selected ID sets, references actually read, reconstructed contract, assumptions, findings and their disposition, verdict, and limitations. The author verifies findings against canonical sources and fixes the canon rather than answering only in conversation. After changes, repeat the affected scenario. A reader who already knows the answer cannot supply a new blind experiment; use a new fresh-context subagent when that evidence is required.

This independently written method draws on the reader-testing idea in [Anthropic doc-coauthoring](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/doc-coauthoring/SKILL.md). It does not adopt the source's permissions or installation instructions.
