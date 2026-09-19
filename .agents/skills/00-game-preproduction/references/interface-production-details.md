# Interface, localization, and voice production details

Read applicable sections at stages 08/09/09a/10b for the agreed devices, languages, components, and accessibility commitments. Do not add a second language, voice-over, or screen reader support to satisfy a checklist. Resolve unknown applicability; unavailable tools do not remove an accepted requirement. Add results to canonical UX, accessibility/localization, narrative/audio, and QA sources.

## Precise interaction states

For each interaction pattern actually used, distinguish hover, focus, and selection. Specify activation on press/release, cancellation after pointer/focus leaves, repeat/hold, preview, and value confirmation. Check focus restoration when a window closes, an element is removed or disabled, and the available set becomes empty. For lists/grids, define edge behavior, wrapping or stopping, scrolling to focus, and responses to data changes. For drag-and-drop, provide an alternative action for supported input methods. For text fields, define entry/editing, submit/cancel, and transfer of control. Not every state applies to every component; state the specific applicability reason.

Stage 09 walks through these transitions against primary rules, including interruption and switching supported devices. A box diagram does not establish correct focus or activation behavior.

## Assistive interfaces

If screen reader or OS accessibility support is promised, interactive and informational elements need semantic names, roles, values, states, available actions, and a focus/reading order. Describe state-change announcements, priority/queuing, repetition suppression, and modal behavior. Distinguish ordinary voice-over, TTS, and a platform accessibility bridge: audio output alone does not establish an accessible interface.

Architecture selects a supported bridge for the actual version/platform and records unverified capabilities. QA plans checks with the declared assistive tool and participants suited to the research question; compatibility remains unconfirmed until tested.

## Writing systems and text input

Derive requirements from selected locales for bidirectional and mixed-direction strings, shaping/ligatures, fonts/fallbacks, line wrapping/breaking, and sorting/search where present. RTL does not mean mirroring everything: specify rules for navigation, diagrams, directional icons, numbers, and game spaces where reflection changes meaning.

If players enter text, describe IME composition, candidate selection, the virtual keyboard, submit/cancel, and focus restoration. Length limits must distinguish bytes, characters, and visible graphemes as appropriate to the operation; unfinished composition is not submitted text. Images with embedded text need an editable source, an owner for localized variants, and a criterion for matching the string registry. Future language QA covers these cases on the actual renderer/device, including mixed strings and dynamic variables.

## Voice-over production

For recorded lines, connect line/character/scene IDs to text, locale, version, playback conditions, context, emotional/directional intent, and pronunciation of significant names. Recording scripts, selected takes, and final files must preserve this connection; text changes reopen the affected recording/translation work.

If synchronized subtitles or lip-sync are promised, specify segmentation, timing, duration source, clipping/interruption rules, each locale's variant, and future verification. Do not invent recordings, performers, translations, or measured timing. Include delivery and rerecording work in assets/production while keeping character context in canonical narrative sources.
