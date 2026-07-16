# Chapter 26. Systematic Reviews and Clinical Prediction Rules

## Opening

![Synthesis forest sketch.](../assets/figures/fig23_forest_meta.png)

*Synthesis forest sketch.*

![Prediction-rule lifecycle.](../assets/figures/fig46_cpr_lifecycle.png)

*Prediction-rule lifecycle.*

![Clinical prediction rule lifecycle.](../assets/figures/swarm_ch26_cpr_lifecycle.png)

*Clinical prediction rule lifecycle.*

A clinical prediction rule is proposed for ED triage. Inspect derivation, validation, calibration, and net benefit—not only AUC.


## Systematic Reviews as Observational Studies of the Literature

A systematic review is not a magical truth-generating machine; it is an observational study where the subjects are primary research papers. Just as a clinical cohort is vulnerable to selection bias, a systematic review is vulnerable to retrieval and publication bias. If a search strategy restricts by language, skips grey literature, or relies entirely on a single database, the resulting 'cohort' of studies is compromised. Appraising a systematic review requires reading its methods section with the same skepticism applied to a retrospective chart review: Who was included, who was missed, and how did the investigators prevent their own priors from dictating the search string?

Publication bias—the file-drawer problem—is the foundational threat to any literature synthesis. Positive trials are submitted rapidly, published in high-impact journals, and cited frequently. Negative or inconclusive trials languish in file drawers or appear years later in obscure venues. When a systematic review aggregates only the published, accessible literature, it risks inflating the true effect of an intervention. Tools like funnel plots and formal asymmetry testing attempt to detect this, but they are underpowered when the number of studies is small. In neuroprotection literature, where dozens of small, positive animal and early-phase human trials evaporated in large Phase III testing, uncorrected systematic reviews of the early phases were spectacularly misleading.

## Meta-Analysis: The Arithmetic of Pooling and the Threat of Heterogeneity

Systematic review is the method of assembling the evidence; meta-analysis is the statistical arithmetic of pooling it. They are not synonymous. Many systematic reviews should conclude without a meta-analysis if the underlying studies are too disparate. Pooling uncombinable trials—giving thrombolytics at 3 hours versus 6 hours, or using different dosing regimens—creates an arithmetic mean of apples and oranges that represents no clinically real patient. Clinical heterogeneity (differences in patients, interventions, or outcomes) must dictate statistical choices.

When meta-analysis is justified, the choice of model matters. A common-effect model assumes that the studies estimate one shared effect; a random-effects model assumes a distribution of effects. A random-effects analysis is not automatically more conservative. As between-study variance grows, study weights become more similar, giving small studies more relative influence than under a common-effect model. Model choice should follow the clinical and statistical estimand, not a reflex rule. Neither model repairs biased or clinically incompatible primary studies.

I² describes the proportion of observed variability not explained by within-study sampling error, but it depends on study precision and is not a direct measure of clinical importance. Do not start or stop pooling at an arbitrary threshold such as 50%. Examine clinical compatibility, τ², the prediction interval, study quality, and prespecified explanations for heterogeneity; subgroup or meta-regression analyses may themselves be underpowered and exploratory.

## Clinical Prediction Rules: Derivation and the Trap of Overfitting

A Clinical Prediction Rule (CPR) combines multiple variables to estimate diagnosis or prognosis. Its lifecycle includes derivation, validation, and impact assessment. Derivation identifies predictors and fits the model; too many candidate parameters for the available information increases overfitting. The historical “10 events per variable” rule is only a rough starting point: required sample size is context-specific and should account for candidate predictor parameters, total sample size, event fraction, anticipated model fit and shrinkage, and precision of predicted risks.

Stroke neurology is plagued by a surplus of derived, overfitted prediction models. A prognostic score for ICH expansion derived on 150 patients with 30 expansion events, which churned 20 variables through automated stepwise regression to find 4 'significant' predictors, is mathematical fiction. It has captured the idiosyncrasies of that specific cohort in that specific hospital in that specific year, not generalizable neurovascular biology.

## Validation: Narrow, Broad, and the Limits of Transportability

Internal validation is necessary to estimate optimism, but a single split sample is often inefficient; bootstrapping or repeated cross-validation generally uses the development data more effectively. External validation in relevant populations, institutions, and eras is then needed to evaluate calibration, discrimination, and transportability. Narrow validation examines a similar setting; broader validation deliberately tests more distinct clinical contexts.

Validation must assess both discrimination and calibration. Discrimination (measured by the c-statistic or AUROC) asks if the rule correctly ranks patients: does the patient who died have a higher score than the patient who lived? Calibration asks if the predicted absolute risks match the observed absolute risks across deciles. A mortality score derived in 1995 might discriminate perfectly today (higher scores still mean higher risk), but its calibration will be terrible because overall stroke mortality has plummeted. Miscalibrated scores lead to erroneous shared decision-making, counseling families with outdated absolute risk profiles.

## Impact Analysis: Does the Rule Actually Change Care for the Better?

Impact analysis asks whether deploying a rule improves decisions, outcomes, or resource use compared with an explicit alternative. Randomized assignment may occur at the patient, clinician, unit, or site level; cluster assignment is useful when individual randomization would cause contamination, but it is not universally required. Rigorous quasi-experimental designs can also inform impact when randomization is infeasible.

Consider the ABCD2 score for TIA triage. Derived and validated to predict short-term stroke risk, it became ubiquitous. But impact analyses and subsequent prospective cohorts revealed its operational flaws: it often misclassified patients with critical carotid stenosis or atrial fibrillation as 'low risk' because those etiologies don't neatly align with age or blood pressure points. When a CPR replaces a senior clinician's physiologic reasoning with an oversimplified arithmetic checklist, the impact on care can be negative. A rule that predicts well on paper is useless if it falsely reassures the clinician or fails to alter management trajectories.

## Appraising the Intersection: When Systematic Reviews Evaluate CPRs

The modern literature is saturated with systematic reviews of prediction models. A systematic review evaluating prognostic models for functional outcome after ischemic stroke will typically find dozens of competing scores. The appraisal conclusion is almost universally identical: most models are derived, few are externally validated, almost none have undergone impact analysis, and methodology is highly biased by missing data and overfitting.

When reading these reviews, the critical takeaway is rarely to adopt the 'winning' score. The takeaway is to recognize that we do not need more derivation studies. The field requires head-to-head external validation of existing scores on large, independent, modern datasets, followed by rigorous trials of their clinical impact. Until then, use CPRs to augment, not replace, clinical judgment, and always verify if the absolute risks predicted by the score match the current era of care.


## Chapter summary

Systematic reviews require reproducible searching, selection, extraction, and risk-of-bias assessment. Meta-analysis is optional and does not repair incompatible or biased studies. Prediction rules progress from development through internal and external validation to impact evaluation. External validation estimates discrimination and calibration with uncertainty in a specified setting; it cannot prove universal performance. Before routine deployment, assess whether using the rule improves a defined decision or outcome compared with current practice and monitor performance after implementation.

## Practice and reflection

1. Find a meta-analysis in stroke neurology. Identify whether fixed or random effects were used and critique this choice based on the clinical heterogeneity of the included trials.
2. Locate the original derivation paper for a Clinical Prediction Rule you use frequently (e.g., ABCD2, ICH Score). Calculate the events-per-variable ratio to assess the risk of overfitting.
3. Review an external validation study of a neurologic prediction score. Did the authors report both calibration (e.g., Hosmer-Lemeshow or calibration plot) and discrimination (c-statistic)?
4. Explain to a junior resident why a meta-analysis pooling three small, highly biased RCTs with a narrow confidence interval provides less trustworthy evidence than a single large, rigorous RCT.
5. Propose a clinical impact analysis trial design for a widely used stroke scale (e.g., a pre-hospital LVO screening tool). Define the intervention, the control arm, and the patient-centered outcome.
6. Identify a clinical scenario where a well-validated prediction score (e.g., a TIA risk score) might lead a clinician to an incorrect management decision if they ignore the underlying pathophysiology.
7. Examine the funnel plot in a systematic review of a neuroprotectant or neurointervention. Discuss what asymmetry in the plot might suggest about the underlying evidence base.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
