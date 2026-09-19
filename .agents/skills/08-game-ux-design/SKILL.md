---
name: 08-game-ux-design
description: Specify game interactions, screens, and HUD through exact states, navigation, and verifiable requirements before implementation. Use after mechanics and target devices are defined.
---

# 08 — Design UX

For used controls and selected support, read the applicable [interaction and language details](../00-game-preproduction/references/interface-production-details.md). Focus versus selection, activation/cancellation, and return of control need concrete outcomes.

Role: UX designer. Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. This stage establishes D0 documentation readiness. Interactive prototypes and in-game usability testing are separate work.

## Inputs and scope

Use `profile.sources`: `baseline`, `systems`, `mechanics`, `ux`, `accessibility_localization`, `art`, `architecture`, and required `content` catalogs. The default profile is `docs/preproduction/project-profile.json`. Read the existing UX specification before editing. If none exists, agree a canonical location with the coordinator and register the source. Do not create another independent UX document alongside an existing one.

Use selected platforms, devices, orientations, locales, and accessibility requirements. Do not add controllers, touch, VR, network menus, or a shop because another genre commonly uses them. Investigate unknown applicability; `N_A` requires a reason, source, and reopening condition.

## Work

1. Derive user intentions and journeys from the agreed game loop: launch, learning, main activity, completion/retry, and applicable settings, saves, social, or service scenarios. For each, specify entry state, inputs/outputs, interruptions, and recovery. A game without a campaign does not require a final boss; in an interface-driven game, the main working screen may itself be the play space.
2. Connect information hierarchy to areas and components. For each element, define visibility, data source, state owner, update conditions, and presentation of missing/stale data. Define a shared information budget, overlays, queues, safe areas, and scaling. Displaying a result does not make UI the owner of gameplay state.
3. For actions, specify input, immediate feedback, request/event, confirmed result, cancellation, and return of control. Cover normal, empty, unavailable, pending, and error states where applicable. When an external or network operation's result is unknown, the interface must not promise success before confirmation. An offline game does not need an artificial server step.
4. Maintain a shared catalog of actual patterns: buttons, focus, lists, fields, hints, dialogs, drag-and-drop, gestures, or other interactions. Specify states, input, feedback, transitions, and interruptions. Screens reference shared patterns and document differences. Check accessible alternatives, remapping, device disconnection/change, and text scaling/expansion for promised support.
5. Trace game-specific conflicts: concurrent actions, modals during required actions, pause, focus loss, loading, and return from interruptions. For multiplayer, include actual roles and ownership, late confirmations, and reconnection. For VR, include posture/view constraints; for touch, reachable areas and competing gestures. Apply only confirmed branches.

## Output and handoff

Update canonical UX rules and diagrams. `ux-design.md` in `profile.paths.state_dir` maps “requirement → scenario/state → section → future check.” Numerical targets require sources and confidence status under the protocol. A layout does not establish readability, latency, or comfort.

Hand off to independent [09 — UX review](../09-game-ux-review/SKILL.md) and [09a — accessibility/localization](../09a-game-accessibility-localization/SKILL.md). Send technical constraints to architecture without automatically selecting a UI framework. Return contradictions with mechanics to their owner; new interface copy cannot resolve conflicting rules.
