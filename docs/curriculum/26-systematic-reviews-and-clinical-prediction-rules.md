# Chapter 26. Systematic Reviews and Clinical Prediction Rules

## Opening

![Synthesis forest sketch (original).](../assets/figures/fig23_forest_meta.png)

*Synthesis forest sketch (original).*

![Prediction-rule lifecycle (original).](../assets/figures/fig46_cpr_lifecycle.png)

*Prediction-rule lifecycle (original).*

![Clinical prediction rule lifecycle (original).](../assets/figures/swarm_ch26_cpr_lifecycle.png)

*Clinical prediction rule lifecycle (original).*

A clinical prediction rule is proposed for ED triage. Inspect derivation, validation, calibration, and net benefit—not only AUC.


## Learning objectives

- Deconstruct systematic reviews as observational studies of primary literature, vulnerable to selection, publication, and aggregation biases.
- Appraise meta-analyses by interrogating between-study heterogeneity, the choice of fixed versus random effects, and the clinical peril of pooling uncombinable trials.
- Evaluate the methodological lifecycle of Clinical Prediction Rules (CPRs) across derivation, narrow/broad validation, and clinical impact phases.
- Distinguish mathematical overfitting and poor calibration in derivation cohorts from true transportability using classical stroke examples.
- Interrogate whether implementing a validated CPR actually improves patient outcomes or clinician behavior compared to baseline clinical gestalt.

## Systematic Reviews as Observational Studies of the Literature

A systematic review is not a magical truth-generating machine; it is an observational study where the subjects are primary research papers. Just as a clinical cohort is vulnerable to selection bias, a systematic review is vulnerable to retrieval and publication bias. If a search strategy restricts by language, skips grey literature, or relies entirely on a single database, the resulting 'cohort' of studies is compromised. Appraising a systematic review requires reading its methods section with the same skepticism applied to a retrospective chart review: Who was included, who was missed, and how did the investigators prevent their own priors from dictating the search string?

Publication bias—the file-drawer problem—is the foundational threat to any literature synthesis. Positive trials are submitted rapidly, published in high-impact journals, and cited frequently. Negative or inconclusive trials languish in file drawers or appear years later in obscure venues. When a systematic review aggregates only the published, accessible literature, it risks inflating the true effect of an intervention. Tools like funnel plots and formal asymmetry testing attempt to detect this, but they are underpowered when the number of studies is small. In neuroprotection literature, where dozens of small, positive animal and early-phase human trials evaporated in large Phase III testing, uncorrected systematic reviews of the early phases were spectacularly misleading.

## Meta-Analysis: The Arithmetic of Pooling and the Threat of Heterogeneity

Systematic review is the method of assembling the evidence; meta-analysis is the statistical arithmetic of pooling it. They are not synonymous. Many systematic reviews should conclude without a meta-analysis if the underlying studies are too disparate. Pooling uncombinable trials—giving thrombolytics at 3 hours versus 6 hours, or using different dosing regimens—creates an arithmetic mean of apples and oranges that represents no clinically real patient. Clinical heterogeneity (differences in patients, interventions, or outcomes) must dictate statistical choices.

When meta-analysis is justified, the choice of model matters. A fixed-effect model assumes a single true effect size across all studies, with variance arising only from sample size. This is almost never true in stroke neurology. A random-effects model assumes a distribution of true effects, accounting for between-study variance. While more conservative, a random-effects model does not fix the underlying sin of pooling garbage. A tight confidence interval around a pooled estimate derived from flawed primary trials is a dangerous illusion of certainty. Precision is not validity. Garbage in, precise garbage out.

Statistical heterogeneity (e.g., I-squared statistic) quantifies the proportion of variation across studies due to true differences rather than chance. A high I-squared (e.g., >50%) should halt reflex pooling and prompt subgroup analysis or meta-regression to explain the variance. If five trials show massive benefit and five show harm, the meta-analytic average of 'no effect' obscures the vital truth that the intervention's effect depends entirely on a yet-unidentified covariate.

## Clinical Prediction Rules: Derivation and the Trap of Overfitting

A Clinical Prediction Rule (CPR) quantifies the contributions of multiple variables to estimate diagnosis or prognosis. The CPR lifecycle demands three distinct phases: derivation, validation, and impact analysis. The derivation phase identifies predictors and fits a statistical model. The cardinal sin of derivation is overfitting—building a mathematical model that perfectly contours to the random noise of the local dataset but fails utterly when exposed to new patients. Overfitting occurs when investigators force too many variables into a model with too few outcome events. A classic rule of thumb requires at least 10 (and preferably more) outcome events per candidate predictor.

Stroke neurology is plagued by a surplus of derived, overfitted prediction models. A prognostic score for ICH expansion derived on 150 patients with 30 expansion events, which churned 20 variables through automated stepwise regression to find 4 'significant' predictors, is mathematical fiction. It has captured the idiosyncrasies of that specific cohort in that specific hospital in that specific year, not generalizable neurovascular biology.

## Validation: Narrow, Broad, and the Limits of Transportability

Internal validation (e.g., bootstrapping, split-sample testing) is mathematically necessary but clinically insufficient. True transportability requires external validation: testing the derived CPR in a different patient population, at a different institution, or in a different era. Narrow validation tests the rule in a similar setting (e.g., another academic stroke center in the same region). Broad validation tests it in disparate settings (e.g., community EDs, different countries) to define its generalizability.

Validation must assess both discrimination and calibration. Discrimination (measured by the c-statistic or AUROC) asks if the rule correctly ranks patients: does the patient who died have a higher score than the patient who lived? Calibration asks if the predicted absolute risks match the observed absolute risks across deciles. A mortality score derived in 1995 might discriminate perfectly today (higher scores still mean higher risk), but its calibration will be terrible because overall stroke mortality has plummeted. Miscalibrated scores lead to erroneous shared decision-making, counseling families with outdated absolute risk profiles.

## Impact Analysis: Does the Rule Actually Change Care for the Better?

Impact analysis is the final, most neglected phase of CPR methodology. Even if a rule is perfectly derived and broadly validated, does deploying it in the clinic improve patient outcomes or resource allocation compared to standard clinical gestalt? Impact analyses require randomized trials or rigorous quasi-experimental designs where clinicians, not just patients, are assigned to use the rule or rely on intuition.

Consider the ABCD2 score for TIA triage. Derived and validated to predict short-term stroke risk, it became ubiquitous. But impact analyses and subsequent prospective cohorts revealed its operational flaws: it often misclassified patients with critical carotid stenosis or atrial fibrillation as 'low risk' because those etiologies don't neatly align with age or blood pressure points. When a CPR replaces a senior clinician's physiologic reasoning with an oversimplified arithmetic checklist, the impact on care can be negative. A rule that predicts well on paper is useless if it falsely reassures the clinician or fails to alter management trajectories.

## Appraising the Intersection: When Systematic Reviews Evaluate CPRs

The modern literature is saturated with systematic reviews of prediction models. A systematic review evaluating prognostic models for functional outcome after ischemic stroke will typically find dozens of competing scores. The appraisal conclusion is almost universally identical: most models are derived, few are externally validated, almost none have undergone impact analysis, and methodology is highly biased by missing data and overfitting.

When reading these reviews, the critical takeaway is rarely to adopt the 'winning' score. The takeaway is to recognize that we do not need more derivation studies. The field requires head-to-head external validation of existing scores on large, independent, modern datasets, followed by rigorous trials of their clinical impact. Until then, use CPRs to augment, not replace, clinical judgment, and always verify if the absolute risks predicted by the score match the current era of care.


![fig74_ps_overlap.png original teaching graphic](../assets/figures/fig74_ps_overlap.png)

*Original teaching graphic (fig74_ps_overlap.png).*

## Chapter summary

Systematic reviews are rigorous observational studies of the literature that require strict search methodologies to avoid selection and publication biases. Meta-analyses provide the statistical arithmetic to pool these studies, but demand careful navigation of clinical and statistical heterogeneity; pooling uncombinable, biased trials produces falsely precise, misleading estimates. Clinical Prediction Rules evolve through derivation, external validation, and impact analysis. Derivation is highly susceptible to statistical overfitting when variables outnumber events. External validation must prove not only discrimination but also calibration, ensuring predicted absolute risks match current clinical reality. Ultimately, an impact analysis is required to demonstrate that implementing the CPR improves patient outcomes compared to clinical gestalt. In neurovascular practice, we must resist the proliferation of unvalidated prognostic scores and demand evidence of true clinical impact.

## Practice and reflection

1. Find a meta-analysis in stroke neurology. Identify whether fixed or random effects were used and critique this choice based on the clinical heterogeneity of the included trials.
2. Locate the original derivation paper for a Clinical Prediction Rule you use frequently (e.g., ABCD2, ICH Score). Calculate the events-per-variable ratio to assess the risk of overfitting.
3. Review an external validation study of a neurologic prediction score. Did the authors report both calibration (e.g., Hosmer-Lemeshow or calibration plot) and discrimination (c-statistic)?
4. Explain to a junior resident why a meta-analysis pooling three small, highly biased RCTs with a narrow confidence interval provides less trustworthy evidence than a single large, rigorous RCT.
5. Propose a clinical impact analysis trial design for a widely used stroke scale (e.g., a pre-hospital LVO screening tool). Define the intervention, the control arm, and the patient-centered outcome.
6. Identify a clinical scenario where a well-validated prediction score (e.g., a TIA risk score) might lead a clinician to an incorrect management decision if they ignore the underlying pathophysiology.
7. Examine the funnel plot in a systematic review of a neuroprotectant or neurointervention. Discuss what asymmetry in the plot might suggest about the underlying evidence base.

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

