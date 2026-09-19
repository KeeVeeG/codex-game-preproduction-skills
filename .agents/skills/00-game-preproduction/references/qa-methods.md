# Planning verification and using existing evidence

Read at stage 19 when choosing QA/playtest methods, and at 15a/17a when planning risks, debt, and team capacity. Creating tests, builds, or experiments and conducting research are outside D0. Existing results may be analyzed with their provenance and limitations intact.

## Match the method to the hypothesis

For each hypothesis, specify observable behavior, an appropriate test medium, participants/context, procedure, metric, and interpretation rule. Paper, tabletop, or flow walkthroughs can explore rules, choices, and comprehension; they cannot establish real-time feel, input latency, audiovisual feedback, or moving-camera comfort. Local play without network conditions cannot establish networked feel. Think-aloud can reveal reasoning but may change pacing. An unprompted first impression needs a participant who has not been taught the design or guided by the author. An author's own walkthrough does not replace that observation.

Choose representativeness according to the specific risk; neither maximum prototype fidelity nor a fixed tester count is universal. Before implementation, record the future method and limits of its conclusions. An unperformed check is not evidence of failure.

For earlier notes, preserve available build/revision, platform, devices/conditions, seed/configuration, participant composition/experience, procedure, and recording source. Unknown fields remain unknown. Distinguish observations, interpretations, participant preferences, and new hypotheses; conclusions apply only to the tested context. Route findings to design/balance, implementation defects, UX/polish, or another check according to their cause. A complaint is not automatically a proven code defect.

## QA planning and defect handling

Define entry criteria for each future check: required version/content, available functionality, test environment/data, observation tools, and known limitations. Connect exit criteria to required outcomes and risk, without universal bug or assertion counts.

A defect record distinguishes impact/severity from urgency/priority. Include expected and actual behavior, steps and preconditions, environment/version, reproduction frequency, evidence, and whether regression status is known. “Could not reproduce” does not mean “fixed.” Define ownership, triage, investigation/fix/verification/closure states, and transition criteria. Rechecking reproduction and related regressions must reference the appropriate revision. Status names may follow the project's process.

Capacity planning includes investigation, fixing, rechecking, queue aging, and recurring systemic causes. Test-count formulas and filenames do not establish quality. Distinguish automatable invariants, integration observations, platform checks, and subjective playtests; do not create tests that merely mirror implementation without a useful criterion.

## Technical and production debt

If an existing project contains debt or accepts a temporary compromise, record its category/area, manifestation and source, cost of leaving it and frequency of impact, risk, and repair cost/dependencies. Compare repayment with other priorities, and assign a review trigger, owner, and debt-reduction criterion. Distinguish observed costs from estimates; do not invent debt for a new project. Carry tasks into production planning and changes to accepted contracts through stage 16.

For the selected iteration process, define how to compare agreed scope/estimates with actual delivery, reasons for carryover, recurring obstacles, and successful repeatable practices. Check the outcome of previous action items before choosing a new action. Process changes need an owner and a future effectiveness check. If no iterations have occurred, record an observation plan, not a fictional retrospective. A fixed sprint cadence is not required.
