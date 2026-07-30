# Chapter 28. Systems of Care, Policy, and Patient Communication

## Opening

![Transportability.](../assets/figures/fig72_transportability.png)

*A trial's absolute benefit can shrink in your catchment when baseline risk, access, and case mix differ from the enrolled population.*

![Pathway decisions.](../assets/figures/fig41_pathway_decisions.png)

*Turning evidence into a pathway means deciding what to adopt, what to de-implement, and how to track access and equity.*

![One-hundred-person array with six persistent events, two events prevented by the strategy, and 92 people without the event.](../assets/figures/swarm_ch28_natural_frequencies.svg)

*Natural frequencies for systems and counseling.*

Policy meeting: absolute benefit looks large in trials but small in your catchment. Systems design must track access, equity, and communication—not only p-values.


## Pathway Change and De-Implementation

The integration of new evidence into institutional pathways requires more than simply writing novel orders. Often, the most formidable barrier in vascular neurology is de-implementation—the deliberate process of abandoning entrenched practices after current evidence and local review show that their harms, burdens, or opportunity costs exceed their benefits. Clinical pathways become deeply institutionalized. Candidate examples for review might include default broad hypercoagulable testing without a supported indication or correction-only insulin used as the sole continuing inpatient strategy. These examples are prompts for evidence review, not universal directives: the relevant population, indication, current guideline, and local safety data must be checked before a practice is changed.

De-implementation may require revising legacy order sets, multidisciplinary retraining, and confronting the cognitive bias of omission where clinicians fear that withdrawing an intervention equates to withholding care. Any EHR forcing function also creates new failure modes. Pathway reform therefore requires authorized governance, clinical and technical validation, audit and feedback, and a reversible implementation plan.

Operational checklist for a pathway change:

1. Name the decision (adopt, restrict, or retire a practice).
2. Attach absolute benefits and harms with time horizons.
3. State the validity caveats that would reverse the decision.
4. Identify the authorized governance body and the affected clinical, pharmacy, nursing, informatics, and patient-safety stakeholders.
5. Assign an accountable owner, balancing metrics, review date, and stop or rollback criteria.
6. Build and test proposed EHR changes in a non-production environment, including uncommon and safety-critical workflows.
7. Only authorized teams should release production changes; monitor the go-live and use the rollback plan if prespecified safety signals emerge.

## Transportability Across Hospital Settings

A pervasive error in guideline application is assuming that efficacy observed within highly selected populations at comprehensive stroke centers automatically ensures effectiveness in community or rural environments. This transportability gap is particularly acute in neurocritical care and complex endovascular therapeutics.

Transportability depends on the actual intervention protocol and co-interventions. An intensive blood-pressure strategy may require a specified monitoring frequency, trained nursing, rapid medication titration, and escalation capacity, but requirements such as 1:1 staffing or invasive monitoring are not universal across trials. Compare the protocol's delivery conditions with local capacity and measure fidelity and adverse events during implementation.

Critical appraisal must therefore evaluate not only the internal validity of a randomized trial but the contextual baseline required for its success. Clinicians and system directors must explicitly verify whether their institution possesses the structural fidelity needed to replicate the experimental conditions under which the benefit was achieved.

Transport questions to force onto the board:

- Who was excluded from the trial, and do those exclusions define our modal patient?
- Which co-interventions (imaging, ICU, transfer times, operator volume) carried the effect?
- If we cannot match the co-intervention package, what is the expected attenuation of ARR?
- Is a staged implementation (hub first, then spokes) safer than network-wide flip?

## Quality Metrics Versus High-Fidelity Evidence

Quality metrics, often enforced by national certifying bodies and pay-for-performance models, aim to standardize care delivery. However, rigid adherence to these targets can generate perverse incentives that conflict with nuanced, evidence-based medicine.

Door-to-needle time for intravenous thrombolysis is a useful example. Treatment benefit is time-sensitive for eligible patients, so eligibility assessment and treatment should proceed without avoidable delay under current guidelines and the local pathway. Complex or uncertain presentations may require focused evaluation, but eligibility assessment is not permission to delay once the indication and eligibility are established. A process metric should therefore promote rapid, appropriate treatment while preserving accountable review of genuine uncertainty.

This dynamic illustrates a limitation of target-driven measurement: optimizing a single process metric can obscure safety, access, or appropriateness. Review metric frameworks for legitimate clinical variance and balance speed with missed eligible treatment, safety outcomes, access, and diagnostic revision.

Metric hygiene for stroke leadership:

- Pair velocity metrics with balanced safety and access measures: sICH, missed eligible treatment, treatment delay by subgroup, diagnostic revisions such as mimics, and transfer outcomes. A mimic-treatment rate alone can incentivize undertreatment.
- Protect documented clinical pauses for high-uncertainty phenotypes.
- Expire order-set defaults that encode fragile early enthusiasm for a single trial.
- Report absolute outcomes alongside process compliance so “green dashboards” cannot hide harm.

## Shared Decision-Making and Absolute Risks

In the modern era of neurovascular therapeutics, ethical patient care requires shared decision-making grounded in transparent statistical communication. Presenting a relative risk reduction without the corresponding absolute risks can make benefit appear larger when baseline risk is low.

Use a named population, endpoint, and horizon. In [REDUCE](https://www.nejm.org/doi/full/10.1056/NEJMoa1707404), selected patients with cryptogenic stroke and PFO had recurrent ischemic stroke in 1.4% of the closure group versus 5.4% of the antiplatelet-only group over a median 3.2 years (crude ARR 4.0 percentage points; NNT 25). Atrial fibrillation or flutter occurred in 6.6% versus 0.4%, and serious device-related adverse events in 1.4% of closure recipients. Antithrombotic regimens after closure are trial-, device-, and guideline-specific; “lifelong antiplatelet therapy” is not a universal device requirement. Counseling should present these absolute outcomes and test whether the patient matches the enrolled population.

For preference-sensitive decisions such as unruptured intracranial aneurysm or asymptomatic carotid stenosis management, communication should include absolute benefits and harms at named horizons, uncertainty, and reasonable alternatives. Natural frequencies can help some people, while others may prefer percentages or visual aids; check understanding and align the discussion with the individual's goals and communication needs.

Bedside communication scaffold (teaching template):

```
For 100 people like you, over [time horizon]:
- Without the intervention: about A will experience [bad outcome]
- With the intervention: about B will experience [bad outcome]
- So about (A−B) fewer people experience [bad outcome]; about C experience [named harm]
- Uncertainty: plausible range spans ...
- Your priorities that change the threshold: ...
```

## From Paper to Policy: One-Page Systems Memo

```
SYSTEMS MEMO — EVIDENCE TO PATHWAY
==================================
Decision at stake:
Source paper(s) / date:
Absolute benefit (ARR, CI, horizon):
Absolute harm (ARI, CI, horizon):
Top validity / transport threats:
Metric implications (what not to game):
EHR / order-set changes:
Governance approval / affected stakeholders:
Test environment / safety scenarios:
Go-live monitoring / stop or rollback criteria:
Patient communication script (natural frequencies):
Owner / review date / dissent logged:
```


## Chapter summary

Systems of care convert appraisal into operations. De-implementation can be harder than adoption because habits are encoded in order sets and omission concerns. Transportability may be limited when trial co-interventions and staffing cannot be reproduced locally. Quality metrics can improve reliability but can also create gaming or selection pressure; pair speed measures with appropriateness and harm audits. Shared decision-making is clearer when relative effects are paired with absolute risks, natural frequencies, uncertainty, and patient-relevant outcomes. Close the loop with authorized governance, tested and reversible implementation, an owner, and a review date.

## Practice and reflection

1. Identify one stroke-unit habit that may merit de-implementation. State what evidence and local data would be needed, which governance body would decide, and how a proposed EHR change would be tested and rolled back. Do not alter a production system for this exercise.
2. Take a late-window EVT or intensive BP trial and write three transportability constraints for a primary stroke center.
3. Redesign a door-to-needle dashboard so it cannot improve while mimic-treatment harm rises unnoticed.
4. Rewrite a relative-risk counseling sentence for PFO closure or aneurysm treatment into a per-100 natural-frequency script.
5. Complete the systems memo template for a paper your service debated in the last month; assign an owner and review date.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
