# Chapter 18. Causation Frameworks, Bias, and Inference

## Opening

![E-value intuition (original).](../assets/figures/fig47_evalue.png)

*E-value intuition (original).*

![Counterfactual contrast (original).](../assets/figures/fig20_counterfactual.png)

*Counterfactual contrast (original).*
![Causal graph motifs used in appraisal (original).](../assets/figures/crit_fig_confounder_mediator_collider.png)

*Causal graph motifs used in appraisal (original).*


Someone cites Bradford Hill as if a checklist proves causation. Use the questions as probes, not a courtroom stamp.


## Learning objectives

- Define causal inference through the lens of counterfactual potential outcomes, recognizing the fundamental problem of causal inference.
- Deconstruct multicausality using the sufficient-component cause framework (causal pies) to evaluate preventative leverage.
- Differentiate confounding from structural selection bias and information bias using specific neurological and stroke examples.
- Apply Hill's viewpoints not as a definitive causal checklist, but as critical appraisal questions for observational literature.
- Identify common violations of temporality and exchangeability in stroke research, including reverse causation.

## Introduction: The Causal Gap in Neurological Literature

Clinical neurology is inherently a causal enterprise: we prescribe anticoagulants to prevent stroke, administer thrombolytics to salvage penumbra, and deploy immunomodulators to alter the trajectory of demyelinating disease. Yet the literature guiding these decisions frequently relies on observational data, where the leap from statistical association to causal inference is fraught. Authors often camouflage causal intent with associative language ('linked to,' 'associated with') in the methods, only to pivot to causal verbs ('reduces,' 'prevents') in the conclusion.

Critical appraisal requires a formalized approach to evaluate whether an association reflects a true causal effect. This chapter introduces foundational causal frameworks—counterfactuals, causal pies, and structural biases (confounding, selection bias, information bias)—and reclaims Hill's viewpoints as rigorous appraisal questions rather than a superficial checklist. Mastery of these concepts allows the reader to dissect whether a reported difference in outcomes stems from the treatment itself, flawed study architecture, or the intrinsic baseline differences among patients.

## Counterfactuals and Potential Outcomes

The counterfactual framework, or potential outcomes model, provides the theoretical scaffolding for modern causal inference. Imagine a patient with an acute M1 occlusion. Under this framework, the patient has two theoretical, mutually exclusive potential outcomes: Y(1), their 90-day modified Rankin Scale (mRS) if they undergo endovascular thrombectomy, and Y(0), their mRS if they receive medical management alone. The individual causal effect is the contrast between Y(1) and Y(0).

The fundamental problem of causal inference is that we can only ever observe one of these potential outcomes. If the patient undergoes thrombectomy, Y(1) is factual and observed, while Y(0) becomes counterfactual and unobserved. Because we cannot measure individual causal effects, we rely on population-level estimates, comparing the average outcome of a treated group against the average outcome of an untreated group.

For the untreated group to serve as a valid proxy for the counterfactual experience of the treated group, the two groups must be exchangeable. Exchangeability assumes that if the untreated patients had instead been treated, their risk of the outcome would be identical to that of the actually treated patients. Randomization achieves exchangeability in expectation by balancing both measured and unmeasured prognostic factors. In observational studies, exchangeability is an untestable assumption reliant on perfect covariate adjustment, which is rarely, if ever, achieved.

## Sufficient-Component Cause Intuition (Causal Pies)

Neurological diseases are rarely the product of a singular, isolated insult. The sufficient-component cause model (often visualized as 'causal pies') accommodates multicausality. A 'sufficient cause' is a complete mechanism (a full pie) that inevitably produces the disease. Each sufficient cause is comprised of multiple 'component causes' (the slices of the pie). For example, a specific sufficient cause for a cardioembolic stroke might require the simultaneous presence of atrial fibrillation, absence of anticoagulant therapy, a hypercoagulable state, and a lack of redundant collateral circulation. None of these components alone is sufficient to cause the stroke, but together they form a complete pathogenic pathway.

A component cause that appears in every possible sufficient-cause pie for a disease is deemed a 'necessary cause.' While necessary causes exist (e.g., SARS-CoV-2 is necessary for COVID-19 encephalopathy), most risk factors in neurology are neither strictly necessary nor sufficient on their own. Hypertension is not necessary for ischemic stroke, as normotensive individuals can infarct, nor is it sufficient, as many hypertensive patients never experience a stroke.

For the appraiser, this model clarifies preventative leverage. Intervening on a highly prevalent component cause (like hypertension) disables every sufficient-cause pie that requires it, leading to substantial public health benefit, even if other causal pathways remain untouched. It also demolishes the 'single cause' fallacy, reminding us that attributing a stroke to a single factor oversimplifies the interacting web of biological vulnerabilities.

## Structural Biases: Confounding, Selection Bias, and Information Bias

When an observed association deviates from the true causal effect, the discrepancy is typically driven by one of three systematic errors: confounding, selection bias, or information bias. Distinguishing among these is crucial for evaluating whether a study's methodology can support its conclusions.

### Confounding: The Open Backdoor Path

Confounding occurs when a third variable, the confounder, is a common cause of both the exposure and the outcome. This creates a spurious 'backdoor path' that mimics a causal relationship. For example, in an observational study evaluating a novel oral anticoagulant versus warfarin, older age and chronic kidney disease might independently dictate both the choice of the novel drug (exposure) and an increased risk of hemorrhagic transformation (outcome). If not rigorously adjusted for, the analysis will falsely attribute the adverse outcomes directly to the drug.

![E-value curve: how strong residual confounding must be to nullify an observed risk ratio (original teaching figure).](../assets/figures/cycle2_ch18_evalue_tipping.png)

*Teaching figure (synthetic).* The E-value translates an observed RR into the minimum confounder–outcome and confounder–exposure association that could fully explain the finding away. Modest RRs (≈1.2–1.5) evaporate under weak residual confounding; large RRs demand stronger alternative explanations. The metric is a sensitivity probe—not a causal proof and not a fix for selection or measurement bias.

### Selection Bias: Conditioning on a Collider

While confounding stems from common causes, structural selection bias often arises from conditioning on a common effect, known as a collider. If a study restricts its analysis to patients who survive the initial 30 days post-stroke (survivor bias), it conditions on survival. Because both intensive care therapies and unmeasured physiological resilience independently cause survival, analyzing only the survivors induces a non-causal association between the therapies and resilience. Selection bias also occurs in biomarker research when cohorts are restricted to those with complete MRI follow-up; patients who tolerate and complete MRIs systematically differ from those who drop out due to severe cognitive decline or death.

### Information Bias: Measurement and Misclassification

Information bias arises from systemic errors in how exposures or outcomes are measured, leading to misclassification. Non-differential misclassification (random error across all groups) typically biases the association toward the null, obscuring true effects. Differential misclassification is more insidious. For example, if patients prescribed a high-profile, novel anti-seizure medication are monitored with prolonged EEG more aggressively than those on legacy drugs, the novel drug cohort will appear to have a higher seizure frequency purely due to surveillance bias. Similarly, recall bias plagues case-control studies: patients who suffered a severe subarachnoid hemorrhage may retroactively over-report pre-morbid headaches compared to healthy controls, fabricating a spurious prodromal link.

## Hill's Guidelines as Appraisal Questions

![Bradford Hill viewpoints as appraisal questions, not a scorecard (original teaching figure).](../assets/figures/fig50_bradford_hill_questions.png)

*Hill's viewpoints are probes that expose weak causal claims; ticking boxes does not prove causation. Original teaching figure.*


In 1965, Austin Bradford Hill proposed nine 'viewpoints' to help distinguish causal from non-causal associations. Decades later, these viewpoints are frequently misapplied as a deterministic checklist. Ticking boxes does not prove causation; robust associations can be robustly confounded. Instead, senior appraisers use Hill's criteria as an interrogative framework to expose vulnerabilities in observational claims.

- Temporality: The only non-negotiable criterion. Did the exposure definitively precede the outcome? Beware of reverse causation, such as declining physical activity 'causing' stroke when subclinical cerebrovascular disease was already restricting mobility.
- Strength of Association: Is the effect size large enough (e.g., hazard ratio of 3.0 rather than 1.1) that it is mathematically unlikely to be entirely explained by unmeasured residual confounding?
- Consistency: Has the association been replicated across different methodologies, diverse populations, and independent datasets? Shared biases (like healthy-adherer bias in pharmacy claims) can produce false consistency.
- Experiment: Is there quasi-experimental or randomized trial evidence supporting the mechanism? Does cessation of the exposure lead to a measurable drop in risk?
- Biologic Gradient (Dose-Response): Does increased exposure strictly correlate with increased outcome severity? Note that sicker patients receiving higher drug doses can artificially create this gradient through confounding by indication.
- Plausibility and Coherence: Does the claim align with established pathophysiology? While necessary for hypothesis generation, human storytelling is highly adaptable, and plausibility can be engineered for almost any outcome post hoc.

## Clinical Synthesis and Application

When dissecting a neurological study, the appraiser must strip away the rhetoric and identify the counterfactual question being asked. If the claim is causal, verify that the exposure is a distinct, actionable intervention rather than an immutable patient characteristic. Trace the study's architecture for open backdoor paths (confounding), inappropriate conditioning (selection bias), and corrupted data streams (information bias). Use Hill's viewpoints to systematically doubt the findings.

Ultimately, causal inference from observational data is a negotiation with uncertainty. A study may not flawlessly prove causation, but it may provide sufficient evidence to alter practice when randomized trials are unethical or impossible. The goal of critical appraisal is not to nihilistically dismiss observational research, but to calibrate our clinical confidence to the rigorousness of the study's design.


![fig80_icon_array.png original teaching graphic](../assets/figures/fig80_icon_array.png)

*Original teaching graphic (fig80_icon_array.png).*

## Chapter summary

Causal inference in neurology demands more than mere statistical association. The counterfactual framework clarifies that true causal effects require exchangeability between treated and untreated populations, a standard that randomized trials approximate but observational studies struggle to meet. The sufficient-component cause (causal pie) model illustrates that neurological events are multicausal, requiring the confluence of multiple factors, none of which may be singularly necessary or sufficient. When observational studies fail to estimate true causal effects, the error is typically rooted in structural biases: confounding (unblocked common causes), selection bias (conditioning on colliders), or information bias (misclassification and surveillance disparities). Hill's viewpoints should be deployed not as a checklist for proving causality, but as rigorous questions to stress-test observational claims, ensuring that only robust, well-defended associations influence patient care.

## Practice and reflection

1. Define the unobservable counterfactual for a patient who received intravenous thrombolysis for acute ischemic stroke.
2. Draw two distinct 'causal pies' for intracranial hemorrhage, illustrating how hypertension functions as a component cause in both.
3. Identify a clinical scenario where survivor bias (a form of selection bias) could artificially inflate the perceived efficacy of a neuroprotective agent.
4. Explain how surveillance bias (a type of information bias) could distort the comparative safety profile of a newly approved multiple sclerosis therapeutic.
5. Critique a hypothetical paper claiming that poor sleep architecture causes early-onset dementia, specifically addressing reverse causation and temporality.
6. Review a recent observational stroke paper. Map out its implicit causal claim, and list the unmeasured confounders that threaten exchangeability.

---

*Figures and tables in this chapter are original teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*


![Conceptual Diagram](../assets/figures/fig10_appraisal_loop.png)



## Advanced Application in Clinical Practice

When translating these methodological principles to real-world clinical decision-making, it is essential to look beyond the surface-level metrics. In neurology and stroke care, outcomes are rarely binary. Patients experience a spectrum of recovery, and interventions often have multifaceted impacts on both quality of life and functional independence. 

### Critical Caveats for the Reader
1. **Contextualizing the Baseline Risk:** The absolute benefit of any intervention depends entirely on the baseline risk of the patient. A relative risk reduction of 50% might mean preventing 1 event in 1000 for a low-risk patient, but 1 event in 10 for a high-risk patient. Always convert relative metrics to absolute metrics before discussing with patients.
2. **The Fragility of Findings:** Consider how many events would need to be flipped from 'non-event' to 'event' to lose statistical significance. In many landmark trials, this number is surprisingly small.
3. **Transportability:** Just because an intervention worked in a highly controlled academic trial does not guarantee it will work in a community setting where system delays, differing demographics, and less rigid protocols exist.

### Methodological Deep Dive: The Architecture of Uncertainty
Every paper you read represents a single sample drawn from a hypothetical universe of infinite possible samples. The confidence interval gives us a range of values that are compatible with the data, given our background assumptions. However, this interval assumes zero systemic bias—which is never true in practice. Unmeasured confounding, selection bias, and measurement error can shift the true effect far outside the reported confidence interval. 

When evaluating evidence, ask yourself:
- What would happen if the unmeasured confounder was as strong as the strongest measured confounder?
- What if the patients lost to follow-up all experienced the worst possible outcome?
- Does the biological mechanism logically support the magnitude of the claimed effect?

### Integration into Patient Communication
How do we communicate this complexity? Use natural frequencies rather than percentages. "Out of 100 patients like you treated with this drug, 5 more will walk independently at 90 days, but 2 more will suffer a severe bleed." This framing avoids the cognitive distortions introduced by relative risk formats.

### Summary Checklist for this Domain
- [ ] Have I identified the precise estimand?
- [ ] Is the outcome measured reliably and is it clinically meaningful?
- [ ] Has the study accounted for competing risks (e.g., death before stroke recovery)?
- [ ] Are the confidence intervals narrow enough to rule out clinically meaningless effects?
- [ ] Is there biological plausibility aligned with the statistical findings?

### Conclusion
By adopting a structured, skeptical, yet open-minded approach to evidence appraisal, clinicians can protect their patients from both the harms of unproven therapies and the harms of delayed adoption of effective treatments. Critical appraisal is not about finding reasons to reject papers; it is about calibrating your confidence in their conclusions.


## Advanced Application in Clinical Practice

When translating these methodological principles to real-world clinical decision-making, it is essential to look beyond the surface-level metrics. In neurology and stroke care, outcomes are rarely binary. Patients experience a spectrum of recovery, and interventions often have multifaceted impacts on both quality of life and functional independence. 

### Critical Caveats for the Reader
1. **Contextualizing the Baseline Risk:** The absolute benefit of any intervention depends entirely on the baseline risk of the patient. A relative risk reduction of 50% might mean preventing 1 event in 1000 for a low-risk patient, but 1 event in 10 for a high-risk patient. Always convert relative metrics to absolute metrics before discussing with patients.
2. **The Fragility of Findings:** Consider how many events would need to be flipped from 'non-event' to 'event' to lose statistical significance. In many landmark trials, this number is surprisingly small.
3. **Transportability:** Just because an intervention worked in a highly controlled academic trial does not guarantee it will work in a community setting where system delays, differing demographics, and less rigid protocols exist.

### Methodological Deep Dive: The Architecture of Uncertainty
Every paper you read represents a single sample drawn from a hypothetical universe of infinite possible samples. The confidence interval gives us a range of values that are compatible with the data, given our background assumptions. However, this interval assumes zero systemic bias—which is never true in practice. Unmeasured confounding, selection bias, and measurement error can shift the true effect far outside the reported confidence interval. 

When evaluating evidence, ask yourself:
- What would happen if the unmeasured confounder was as strong as the strongest measured confounder?
- What if the patients lost to follow-up all experienced the worst possible outcome?
- Does the biological mechanism logically support the magnitude of the claimed effect?

### Integration into Patient Communication
How do we communicate this complexity? Use natural frequencies rather than percentages. "Out of 100 patients like you treated with this drug, 5 more will walk independently at 90 days, but 2 more will suffer a severe bleed." This framing avoids the cognitive distortions introduced by relative risk formats.

### Summary Checklist for this Domain
- [ ] Have I identified the precise estimand?
- [ ] Is the outcome measured reliably and is it clinically meaningful?
- [ ] Has the study accounted for competing risks (e.g., death before stroke recovery)?
- [ ] Are the confidence intervals narrow enough to rule out clinically meaningless effects?
- [ ] Is there biological plausibility aligned with the statistical findings?

### Conclusion
By adopting a structured, skeptical, yet open-minded approach to evidence appraisal, clinicians can protect their patients from both the harms of unproven therapies and the harms of delayed adoption of effective treatments. Critical appraisal is not about finding reasons to reject papers; it is about calibrating your confidence in their conclusions.


## Advanced Application in Clinical Practice

When translating these methodological principles to real-world clinical decision-making, it is essential to look beyond the surface-level metrics. In neurology and stroke care, outcomes are rarely binary. Patients experience a spectrum of recovery, and interventions often have multifaceted impacts on both quality of life and functional independence. 

### Critical Caveats for the Reader
1. **Contextualizing the Baseline Risk:** The absolute benefit of any intervention depends entirely on the baseline risk of the patient. A relative risk reduction of 50% might mean preventing 1 event in 1000 for a low-risk patient, but 1 event in 10 for a high-risk patient. Always convert relative metrics to absolute metrics before discussing with patients.
2. **The Fragility of Findings:** Consider how many events would need to be flipped from 'non-event' to 'event' to lose statistical significance. In many landmark trials, this number is surprisingly small.
3. **Transportability:** Just because an intervention worked in a highly controlled academic trial does not guarantee it will work in a community setting where system delays, differing demographics, and less rigid protocols exist.

### Methodological Deep Dive: The Architecture of Uncertainty
Every paper you read represents a single sample drawn from a hypothetical universe of infinite possible samples. The confidence interval gives us a range of values that are compatible with the data, given our background assumptions. However, this interval assumes zero systemic bias—which is never true in practice. Unmeasured confounding, selection bias, and measurement error can shift the true effect far outside the reported confidence interval. 

When evaluating evidence, ask yourself:
- What would happen if the unmeasured confounder was as strong as the strongest measured confounder?
- What if the patients lost to follow-up all experienced the worst possible outcome?
- Does the biological mechanism logically support the magnitude of the claimed effect?

### Integration into Patient Communication
How do we communicate this complexity? Use natural frequencies rather than percentages. "Out of 100 patients like you treated with this drug, 5 more will walk independently at 90 days, but 2 more will suffer a severe bleed." This framing avoids the cognitive distortions introduced by relative risk formats.

### Summary Checklist for this Domain
- [ ] Have I identified the precise estimand?
- [ ] Is the outcome measured reliably and is it clinically meaningful?
- [ ] Has the study accounted for competing risks (e.g., death before stroke recovery)?
- [ ] Are the confidence intervals narrow enough to rule out clinically meaningless effects?
- [ ] Is there biological plausibility aligned with the statistical findings?

### Conclusion
By adopting a structured, skeptical, yet open-minded approach to evidence appraisal, clinicians can protect their patients from both the harms of unproven therapies and the harms of delayed adoption of effective treatments. Critical appraisal is not about finding reasons to reject papers; it is about calibrating your confidence in their conclusions.

