# Contracts for the selected engine

Read at stages 12–15a only for the digital portion and selected stack. If the engine is undecided, compare options against requirements and risks; do not make every branch mandatory. For another engine or a custom stack, apply the relevant questions to its equivalents. This is D0 specification work, not an implementation guide.

## Common record

In canonical architecture, record actual engine, language/runtime, package, and target platform versions; include rendering, input, UI, storage, loading, and delivery methods where applicable. For each significant capability, record its requirement, chosen mechanism, data and resource owner/lifetime, constraints, alternative, primary source for the relevant version, and future verification. Do not infer language, native binding, ABI, export, or platform compatibility from an engine name or old example. Check official documentation; unavailable facts remain `UNVERIFIED` with a resolution action.

Do not import universal prohibitions or numerical budgets from source agents. A 2 ms limit, 20 Blueprint nodes, mandatory GAS/ECS, zero allocations, or a particular renderer is not a requirement for every game. Architecture choices must follow the product, team, and verifiable constraints.

## Godot

- Separate scenes/nodes, shared Resource definitions, and mutable instances. Describe creation, loading, scene changes, cancellation of pending operations, and cleanup. Signals, persistent subscriptions, and background tasks need an owner and defined behavior when their target is destroyed. Identify global state and editor execution scopes where needed.
- Define GDScript/C#/GDExtension boundaries for each significant system using authoring and testing needs, call and marshaling costs, memory, and export support. Check the C# runtime and native toolchain against **every** selected platform; a desktop example does not establish web, mobile, or console support.
- For native extensions, describe binary registration and delivery, version and architecture compatibility, object/buffer ownership, safe transfer of results between threads, editor reload, and failure recovery. Justify native code through a risk and measurement plan, not a fixed call count.
- Check the renderer against materials, particles, post-processing, and the minimum device. A missing capability needs an accepted visual alternative or delivery decision. Source assets, import, UIDs/references, shared versus per-instance data, and resource deletion belong in the pipeline contract.

## Unreal

- Justify Blueprint/C++ boundaries, designer controls, communication, UObject and non-UObject ownership, and subscription/async cleanup. Graph size alone does not choose a language. For content, trace hard/soft references, loading/unloading, cooking, package separation, and data availability after delivery.
- **If GAS is selected:** specify ownership of the Ability System and Attribute Sets, a shared tag vocabulary, base/current values, costs/cooldowns, stacking/duration/removal, activation/commit/end/cancel, and async task interruption. For networking, separately define authority, prediction/correction, and effect visibility; combat alone does not require GAS or prediction.
- **If replication is used:** map messages and states to owners, recipients, relevancy conditions, updates, and dormancy/wake behavior. Define late joining and restoration of required state; do not replace persistent state with a one-time event without a recovery contract.
- **If UMG/CommonUI or an equivalent is used:** connect screen layers/stacks to focus, input consumption, data sources, widget/view-model lifetimes, reuse, and reset. Localized text, accessibility, and update costs follow UX requirements; do not assign a UI framework automatically.

## Unity

- For GameObject/MonoBehaviour and selected data-oriented tools, define ownership boundaries, update order, scene lifecycle, input/UI/render pipeline, and content integration. ECS, Burst, and Jobs are not defaults.
- **If Entities/Jobs are selected:** define read/write access, system order and job dependencies, structural change points, native allocation lifetimes, synchronization, and the hybrid boundary. Data preparation and package support must match the selected versions; a future performance test remains separate from an estimate.
- **If Addressables or streamed delivery is selected:** trace handle/resource ownership and release, grouping by shared use, shared dependencies and duplication, and local/remote catalogs. Describe partial loading, caching, incompatibility, fallback, and atomic version switching. Plan fresh installation, ordinary updates, and skipped-version updates. Addressables does not imply mandatory networking or remote bundles.

## Cross-cutting technologies

For network contracts, define authority, message schema/version, units/precision, frequency and size limits, delivery/order guarantees, retries/stale data, validation, and recovery. Prediction, rollback, migration, and reconnect follow the agreed model; if required recovery is absent, specify the resulting player experience.

For networked sessions, describe topology, participant identification/authorization, creation, discovery, joining, and leaving; include lobbies and matchmaking only when selected. Loss of the host either ends the session or starts an agreed migration with a clear outcome; do not promise migration automatically. Smoothing/prediction, visibility, and state correction must fit the trust model and planned network test conditions.

AI needs observable states/decisions, designer parameters, and a load scenario. Shaders need quality/variant budgets, authoring parameters, and fallbacks for selected devices. Optimization and profiling remain future work. Carry conclusions into ADRs/controls, technical risks, and QA as “contract → versioned source → unknown → verification method → criterion,” without claiming the integration works already.

For selected AI behavior, describe available information, perception/memory and forgetting, action selection/interruption, and responses to unreachable or changed routes. Group roles and coordination apply only when required. Connect telegraphs to the player's ability to understand decisions, and future diagnostics to states, paths, and reasons for choices. Select behavior trees, utility systems, or another algorithm from the contract; do not grant AI hidden knowledge merely for implementation convenience.
