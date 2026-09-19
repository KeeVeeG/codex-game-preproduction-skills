---
name: 15-game-create-control-manifest
description: Derive concise implementation rules from accepted game architecture, preserving scope, source, prevented violation, and version for production tasks.
---

# 15 — Implementation control manifest

Role: technical architect. Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. The control manifest is a derived implementation reference; rationale and authority to change a rule stay with its canonical source.

## Inputs and prerequisites

Load the profile, defaulting to `docs/preproduction/project-profile.json`. Read actual `architecture`, `decisions`, `controls`, `risks`, current architecture reviews from `reviews`, and accepted requirements through `profile.sources`. Send significant changes made after review or unresolved blocking conflicts to [14](../14-game-architecture-review/SKILL.md). A draft reference does not become authoritative.

Extract `Accepted` ADRs; `Proposed` decisions remain open and `Superseded` records are history. Accepted direct contracts are allowed without ADRs. A proposed risk experiment does not become a required API or proven guarantee. External constraints need a source and version.

Respect `profile.features` applicability. N/A needs a reason, evidence, and reopening condition; unknown decisions cannot be excluded as inapplicable. Extend existing canonical documents. For new ones, use [templates](../00-game-preproduction/references/templates.md) and register actual paths.

## Work

1. Extract mandatory actions, prohibitions, interface guarantees, identifiers, data owners, limits, and recovery. Each rule must say whom or which modules it binds, what it requires, when it applies, and which observable violation it prevents. If the source cannot answer, return the gap to 12/13 and 14 rather than inventing a decision in the manifest.
2. Preserve each requirement's force and scope. Recommendations do not become prohibitions; rejected alternatives are not banned beyond an ADR's rationale. Organize rules by the project's actual layers and systems, without imposing a new directory structure. Cross-cutting rules retain one ID with references from multiple areas.
3. Carefully compare applicable invariants for ownership/authority, atomicity, result confirmation, cancellation/recovery, input, and accessibility. Use the game's actual commands and participants rather than a fixed cooperative or single-player template.
4. For budgets, record units, scope, load scenario, numeric evidence status, and measurement method/timing. Distinguish accepted limits, provisional values, calculations, and measurements. Unknown compatibility is not a prohibition; target frame rate is not an achieved result.
5. Preserve each rule's exact source path/section/ADR, source version, and future verification method. Check both directions: all significant accepted obligations are represented and every manifest rule has a source. Resolve differences in the source through the usual review cycle, not through independent manifest exceptions.
6. Include accepted content delivery, validation/import, version/migration, test-hook, and trust-boundary rules where applicable. Naming a future tool does not establish its existence. After 15a, update only rules whose source decisions actually changed and were reviewed.

## Output and completion

Update canonical `controls` with status, manifest version, date, source snapshot, covered decisions, and rule tables. Versions must distinguish changes made on the same day. On repeat passes, list added, changed, and retired entries; keep old links traceable.

Readiness requires checking every rule against its source and the entire accepted obligation set against the manifest. Significant new rules need independent review under the protocol; label self-review explicitly. Send version and impact to story owners and the coordinator for `profile.paths.state_dir`. Continue to [15a](../15a-game-technical-risk-review/SKILL.md), consistency checks, and [17](../17-game-create-epics/SKILL.md). Do not create code or tools at this stage.
