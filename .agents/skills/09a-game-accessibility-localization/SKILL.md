---
name: 09a-game-accessibility-localization
description: Specify and review accessibility and localization workflows for selected game devices, languages, and audiences. Connect requirements to actions, text, signals, and future acceptance.
---

# 09a — Design accessibility and localization

For promised screen readers, writing systems/text input, and voice-over, use the relevant [production contracts](../00-game-preproduction/references/interface-production-details.md). A general “RTL supported” or “voice-over included” label does not replace checks of semantics, the renderer/platform bridge, and localized deliverables.

Roles: accessibility specialist and localization lead. Follow the [protocol](../00-game-preproduction/references/protocol.md), including its source-loading rules. This pass extends beyond screens to gameplay actions and meaningful signals. Work remains within D0.

## Inputs

Use `profile.sources.baseline`, `ux`, `accessibility_localization`, `mechanics`, `content`, `art`, `audio`, and `architecture`. If 08 is unavailable, reconstruct the screen/action inventory from primary sources. Preserve existing documents and numerical values without multiplying canonical copies.

The project defines locales, source language, devices, and promised support. A monolingual game does not require another translation; absence of localization does not remove the need to check source-text readability. Record `N_A` with justification and a reopening condition. Unknown audiences or languages require a decision rather than silent exclusion.

## Work

1. Build a matrix: “screen/action/signal → visual, motor, auditory, or cognitive barrier → requirement/constraint → verification method.” Cover the agreed product, including rare states, settings, errors, and release materials where in scope. Naming an accessibility level without concrete commitments does not close a row.
2. Check promised input methods: reachability, remapping and persistence, conflicting actions, device disconnection/change, precision, hold/repeat behavior, and accessible alternatives. An alternative must preserve the mechanic's essential meaning or become a separately agreed mode. Do not silently change timers or ownership through UX.
3. Define scaling, contrast, shape in addition to color, flashes, shake, text speed, and renewed access to information. Numerical sources and verification status are required. When using an external standard, verify the primary source and its platform applicability. Reading a document does not establish certification.
4. Map meaningful audio cues to accessible alternatives and important visual cues to alternatives within the agreed support scope. For captions/subtitles, define speaker, context, direction where needed, queues, timing, background, and placement. Distinguish recorded speech, sound-effect descriptions, and live communication; automatic transcription and text-to-speech are not implied commitments. For games built around one sensory channel, explicitly examine accessibility limits and agreed modes.
5. Record the source language and target locales. The string registry covers all required categories, with stable key, source/context, text, variables/types, layout constraints, version, and translation status. Define fallback, language switching, font coverage, number/time formats, grammar, and terminology. Apply plural/gender rules, RTL, CJK, layouts, and cultural adaptation according to actual languages rather than a universal checklist. User-entered text remains data.
6. Specify translator context, export/import, and checks for variables and stale/missing strings. Assign owners for applicable string freeze, pseudolocalization, native-speaker review, voice-over, and translation of revisions. D0 does not present unverified translations as tested in-game or require freezing unfinished text.

## Output and completion

Update the canonical `accessibility_localization` specification. An independent Codex subagent writes `accessibility-localization-review.md` in `profile.paths.state_dir` under the [subagent review protocol](../00-game-preproduction/references/subagent-review.md): coverage denominator, sources, findings, limitations, and D0 verdict. Label self-checks explicitly; they do not replace required independent review, which remains pending if unavailable.

Send corrections to [08](../08-game-ux-design/SKILL.md), [10b](../10b-game-audio-design/SKILL.md), and architecture; send future verification criteria to QA. Completion requires coverage of all promised actions, signals, and locales. Future device, translation, and comfort checks remain planned until evidence exists. Propagate shared changes through 16.
