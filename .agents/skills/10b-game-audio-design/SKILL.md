---
name: 10b-game-audio-design
description: Specify game audio events, musical states, mixing, accessibility, and technical delivery before sound production and integration.
---

# 10b — Audio design

For recorded speech, use the [VO production contract](../00-game-preproduction/references/interface-production-details.md): recording script, IDs/context/pronunciation, localized takes, and accepted synchronization requirements. This branch does not add voice acting to the game.

Roles: audio director and sound designer with technical and accessibility reviewers. Follow the [protocol](../00-game-preproduction/references/protocol.md) and its source-loading rules. Do not create recordings, music, or middleware integrations at this stage.

## Inputs and applicability

Use `profile.sources.baseline`, `mechanics`, `systems`, `content`, `levels`, `ux`, `art`, `audio`, `assets`, `accessibility_localization`, and `architecture`. Accepted IDs, formats, banks, buses, and counts stay in their canonical sources; audio design connects them to behavior.

Determine SFX, music, recorded speech, and live communication separately. No voice chat does not mean no audio design. A completely silent game may justify `N_A`, with a reason, evidence, and reopening condition. Unknown audio scope remains open. Do not add voices, spatial mixing, or licensed music without an agreed need.

## Work

1. Define audio identity through player intent and sound's role. For applicable music, specify character, contexts, states/layers, silence, transitions, and interruption. Describe only reference excerpts actually heard, with explicit borrowing limits; a screenshot provides no listening evidence.
2. Build a complete requirement/state → event → asset ID/group → required accessible alternative catalog. Cover agreed action, interface, and content categories, including errors, transitions, and rare states. Deliberate silence needs a reason. Distinguish events, variation groups, delivered files, and playback instances. Matching names do not prove reuse.
3. For each event, specify trigger/start/stop, source of truth, cancellation, loop lifecycle, audible range/position where applicable, duration, variation, repetition, concurrency, and priority. Audio does not own a gameplay timer. For network or external confirmation, separate immediate local feedback from confirmed events and trace repeats, late responses, disconnection, and recovery. Do not add network contracts to a local game unnecessarily.
4. Specify routing, competition, masking of critical signals, dynamic range, clipping/headroom, and user settings. Use ambience/reverb/occlusion, spatialization, ducking, and mono/downmix only where the design calls for them. Examine the game's actual maximum combination of effects, speech, music, and warnings, rather than an arbitrary player count.
5. For live speech, define channels, devices, mute, delivery rules, duplicate-playback prevention, missing microphone, interruption/resumption, and personal settings. For recorded speech, connect lines, context, locales, variants, and interruption. With [09a](../09a-game-accessibility-localization/SKILL.md), check captions/subtitles and essential meaning under perception constraints. Do not promise automatic transcription or a required microphone without an accepted requirement.
6. Specify verifiable provenance/rights requirements, formats, dependencies, and architectural memory/loading constraints. New middleware or incompatible formats require a decision. Plan listening checks on declared devices, peaks, repetition, transitions, quiet settings, and maximum load. Rhythm or audio-led games need future latency/accuracy checks. Documentation does not prove final mix or synchronization quality.

## Output and handoff

Update canonical `audio`: direction, events/states, mixing contracts, dependencies, coverage, and acceptance criteria. Record independent review in `audio-design-review.md` under `profile.paths.state_dir`; label self-review explicitly. Link to source data and propagate shared changes through 16.

Hand off to [11](../11-game-asset-spec/SKILL.md), architecture for technical decisions, and QA for future checks. Completion means defined audio needs and testable contracts, not an existing bank or a reviewed final mix.
