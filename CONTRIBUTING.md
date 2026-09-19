# Contributing

Keep changes focused on reusable game preproduction instructions. Preserve stable skill names, stage IDs, relative links, and the distinction between documentation readiness and a tested game.

For a change, explain the concrete gap, affected stages, resulting behavior, and verification performed. Keep instructions in English and shared rules under `.agents/skills/00-game-preproduction`. Add domain detail where it changes a decision; avoid repeating generic guidance.

Run the checks listed in [README.md](README.md). If review semantics or routing change, also evaluate a realistic request in an isolated workspace using an independent reader. Report what was actually exercised and what remains untested.

Issues and pull requests should include the relevant skill, a minimal scenario, and expected versus observed behavior. Remove private game material and credentials from examples. Preserve attribution when adapting outside methods.
