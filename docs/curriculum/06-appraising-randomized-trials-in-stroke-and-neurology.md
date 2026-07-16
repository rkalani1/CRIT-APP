# Chapter 6. Appraising Randomized Trials in Stroke and Neurology

## Opening

![CONSORT-minded flow.](../assets/figures/fig26_consort_minded.png)

*CONSORT-minded flow.*

![Trial pathway overview.](../assets/figures/fig05_trial_pathway.png)

*Trial pathway overview.*
![Trial pathway teaching sketch.](../assets/figures/crit_fig_trial_pathway.png)

*Trial pathway teaching sketch.*


Journal club is an EVT RCT with beautiful Kaplan–Meier curves. Ask allocation concealment, crossover, and absolute functional gains before declaring a new standard for your ED.


## The Epistemology of the Randomized Trial in Stroke

The randomized controlled trial sits atop the evidence hierarchy not by historical tradition or arbitrary consensus, but due to a singular mathematical property: when executed flawlessly, randomization balances both measured and unmeasured baseline prognostic factors in expectation. This is the exclusive mechanism in clinical epidemiology that breaks the causal arrow between patient characteristics and treatment assignment. In observational data, a patient receives a therapy because a clinician predicted they would benefit, or because they were deemed physiologically capable of tolerating the intervention. This generates intractable confounding by indication, meaning the treatment assignment is hopelessly entangled with the underlying baseline risk of the outcome. Prediction is not causation. A machine learning model might flawlessly predict that stroke patients receiving mechanical ventilation have astronomically higher mortality rates, but that associational correlation contains zero causal information regarding the efficacy of the ventilator itself. Randomization replaces clinician intent and predictive assignment with a stochastic, mathematical coin flip.

Proper random assignment makes assignment independent of baseline potential outcomes under the allocation mechanism, so between-group outcome differences can estimate the effect of assignment when concealment, follow-up, outcome measurement, and analysis are valid. It does not make the realized groups identical, nor does it imply that an individual’s unobserved control outcome equals another participant’s observed outcome. Post-randomization co-interventions, missing outcomes, crossover, and measurement error can still bias the analysis or change the estimand.

The task of clinical appraisal is not to automatically accept the results simply because the word 'randomized' appears in the title. The task is to trace the causal architecture from the sequence generation all the way to the final intention-to-treat analysis, interrogating every phase where bias might have leaked back into the trial execution. Consider a surgical trial comparing early versus late decompressive hemicraniectomy for malignant middle cerebral artery infarction. Observational registries are fundamentally biased because neurosurgeons only operate on patients they predict will survive the procedure. Randomization removes this prediction-based assignment, but if surgical patients receive disproportionately intensive care unit rehabilitation while medical patients receive palliation, confounding has re-entered through the backdoor of co-interventions. True appraisal requires absolute skepticism of the post-randomization timeline.

## The Mechanics of Randomization: Breaking the Confounding Arrow

The physical mechanics of randomization shape the trial’s integrity and balance. Simple randomization can produce chance imbalances in smaller trials. Permuted blocks improve allocation balance, while stratified or minimization procedures can improve balance on selected prognostic factors. In acute-stroke trials, investigators may stratify on center or key prognostic factors and combine stratification with blocked or minimization procedures. Exact balance depends on the allocation algorithm, stratum size, and trial completion.

Stratification or minimization can improve balance on selected prognostic covariates, while chance imbalances remain possible elsewhere. A baseline difference does not by itself prove failed randomization. Examine the allocation process, then use prespecified adjustment for important prognostic variables when appropriate; such adjustment often improves precision but does not guarantee a narrower interval in every realized sample. Randomization supports exchangeability under the allocation mechanism, not identical observed groups.

Appraisers must explicitly differentiate true stochastic randomization from deterministic alternation. Assigning treatments based on alternate days of the week, odd or even hospital record numbers, or odd or even birth years is not randomization. These are entirely predictable, deterministic sequences. They fail the fundamental requirement of randomness and are acutely vulnerable to selection bias, as clinicians can easily predict the assignment and selectively enroll or exclude patients.

## Allocation Concealment: The Final Mile of Randomization

Allocation concealment protects the randomization sequence before the assignment occurs. Blinding protects the trial after the assignment is made. These are distinct concepts with distinct failure modes. Allocation concealment answers a singular question: could the enrolling investigator predict the next assignment before deciding to enroll the patient? If an investigator knows the next assignment is the active therapy, and they strongly predict a specific patient will benefit, they will aggressively enroll them. If they know the next assignment is the control, they might delay enrollment or find a trivial exclusion criterion to exclude a highly viable patient. This destroys the exchangeability of the groups.

Time pressure makes allocation procedures especially important. Small, fixed, unmasked blocks can make later assignments predictable, while poorly implemented envelopes can be opened or skipped. Centralized electronic allocation after irrevocable enrollment is a strong safeguard; properly prepared sequentially numbered, opaque, sealed envelopes can also conceal allocation when electronic systems are infeasible. Appraise what participants and recruiters could actually predict, not the technology label alone.

Inspect the baseline characteristics table for large or patterned imbalances and interpret them alongside the allocation process. Weak concealment plus suspicious enrollment patterns raises concern, but imbalance alone does not prove subversion. Examine sequence generation, concealment, enrollment chronology, and site-level patterns before attributing cause; then assess how any important imbalance affects precision and the prespecified analysis.

## Blinding: A Stakeholder-Specific Matrix

Blinding (or masking) is rarely a binary grade of 'double-blind' or 'open-label.' It is a highly specific matrix of stakeholders. Appraisers must explicitly define the blinding status of the patient, the treating clinician, the endpoint assessor, the adverse event adjudicator, the statistician, and the manuscript writer. Each unblinded role introduces a highly specific, mechanistically distinct bias pathway. You must specify how the lack of blinding in each role corrupts the specific estimand of interest.

Unblinded patients report systematically worse subjective outcomes in the control arm due to disappointment and lack of placebo effect. Unblinded clinicians provide differential co-interventions. If a clinician knows a patient received mechanical thrombectomy, they may target stricter blood pressure parameters, pursue more aggressive intensive care support, and order earlier physical therapy consultations. This performance bias conflates the isolated effect of the endovascular procedure with the unmeasured package of superior supportive care. Unblinded assessors systematically rate the intervention group more favorably on subjective scales like the modified Rankin Scale (mRS), subconsciously shifting borderline cases into favorable categories based on their belief in the treatment.

In mechanical thrombectomy and neurosurgical trials, blinding the proceduralist is structurally impossible. A neurosurgeon cannot be blinded to performing a craniectomy. This structural limitation does not doom the trial, but it exponentially heightens the strict requirement for blinded outcome assessors, highly objective endpoints, and rigidly protocolized, standardized co-intervention guidelines for both arms. The inability to blind the treating physician mandates zero tolerance for unblinded endpoint ascertainment.

## PROBE Designs and Adjudication Committees in Neurology

The Prospective Randomized Open-label Blinded-Endpoint (PROBE) design is highly prevalent in vascular neurology. Due to the logistical impossibility of blinding procedural interventions, trials heavily utilize PROBE frameworks. Unmasking can introduce outcome-measurement bias, especially for subjective endpoints, but randomization remains; judge the likely direction and magnitude of measurement bias rather than reclassifying the design.

Unblinding occurs rapidly via physical cues. In an endovascular trial, groin hematomas from arterial puncture, alopecia from fluoroscopic radiation, or visible craniectomy defects immediately unmask the supposedly blinded bedside assessor. Even without physical cues, patients frequently reveal their treatment assignment during standard conversation. Mitigation strategies must be aggressive. Centralized, blinded telephone assessments by personnel strictly segregated from the hospital, or structured video interviews evaluated by independent core labs, are mandatory structural defenses against unblinding.

Independent adjudication committees evaluate secondary endpoints and critical safety events, such as symptomatic intracranial hemorrhage (sICH) or cause-specific mortality. Adjudicators should be shielded from treatment labels and avoidable procedure-specific metadata; when imaging itself necessarily reveals treatment-related findings, use prespecified objective definitions and report the remaining risk of unmasking.

## Estimands and Analysis Sets: ITT, Modified ITT, and the Per-Protocol Illusion

![ITT vs per-protocol: different questions.](../assets/figures/fig42_itt_vs_pp.png)

*Intention-to-treat answers the effect of assignment and preserves randomization; per-protocol answers an adherence-conditional question and often reintroduces confounding. Teaching figure.*


The estimand framework formally defines the target of estimation: the population, the strategies compared, the precise variable of interest, the handling of intercurrent events, and the population-level summary metric. In stroke trials, intercurrent events—such as crossover to rescue therapy, protocol non-adherence, or withdrawal of consent—are inevitable. How the analysis handles these events defines the fundamental causal meaning of the result.

Analysis by randomized assignment preserves the randomized comparison and commonly estimates an assignment or treatment-policy effect. It does not by itself solve missing outcomes, outcome-measurement bias, or departures from the prespecified estimand. Nonadherence may attenuate an assignment effect in some settings, but its direction is not guaranteed; report adherence and complementary estimand-aligned analyses.

Modified ITT labels are not standardized and require an exact definition. Per-protocol and as-treated analyses often restrict or reclassify participants using post-randomization information such as adherence, crossover, or treatment receipt. A naive comparison can therefore break randomization and introduce selection or time-varying confounding, but it does not inevitably condition on a collider. Causal per-protocol effects require a prespecified estimand, adequate longitudinal data, and methods such as inverse-probability weighting or other g-methods under explicit assumptions. Interpret discordant assignment-based and per-protocol results by their estimands, adherence patterns, missingness, and analytic methods rather than assigning either automatic primacy.

## Attrition, Missing Data, and Loss to Follow-Up

Differential missing outcomes—for example, 10% versus 2%—threaten the randomized comparison because bias depends on why outcomes are missing and their unobserved values. Report reasons by arm, compare missingness with event rates, and use prespecified imputation, bounds, or tipping-point analyses. A complete-case p-value alone cannot establish the original-population effect.

Missing Completely At Random (MCAR) is often implausible in stroke follow-up because outcome collection may depend on discharge destination, disability, cognition, or survival. Complete-case analysis can bias either arm's observed success rate and the treatment contrast; direction and magnitude depend on the missingness mechanism and unobserved outcomes. Report the reasons, timing, and amount of missingness by arm rather than assuming a direction.

Multiple imputation can be appropriate under a stated Missing At Random assumption conditional on included information. Tipping-point analyses and best-case/worst-case bounds show how conclusions change under progressively less favorable assumptions; extreme scenarios are informative bounds, not a universal pass/fail requirement. When missingness is large relative to the observed effect, the primary estimate needs prespecified sensitivity analyses and appropriately cautious interpretation.

## Competing Risks and Withdrawal of Life-Sustaining Therapy

For a full 90-day ordinal mRS endpoint, death is incorporated as category 6 rather than treated as a competing event. For a nonfatal endpoint such as recurrent stroke or recovery among survivors, death may instead preclude the event and change the estimand. Dichotomized mRS combines death with selected disability states by design; report the full outcome distribution and mortality separately so clinically different states are not obscured.

Withdrawal of Life-Sustaining Therapy (WLST) can act as a post-randomization mediator of mortality and disability. If clinicians know assignment, differential expectations could alter WLST timing and thereby affect outcomes. Unstandardized practice does not prove that WLST explains the treatment contrast, but trials should prespecify guidance where feasible, record timing and reasons, and report sensitivity analyses when differential WLST is plausible.

Prespecified WLST guidance can reduce avoidable variability but cannot eliminate individualized decisions or all clinician-level differences. Appraisal should examine whether mortality contrasts could be partly mediated by treatment biology, WLST practice, or both.

## Endpoints: The Modified Rankin Scale and Beyond

The modified Rankin Scale (mRS) is the dominant functional endpoint in acute stroke research. It is a strictly ordinal scale from 0 (no symptoms) to 6 (death). Historically, trials relied on dichotomizing the mRS, typically at 0-2 (functional independence) versus 3-6. Dichotomization discards immense statistical power and willfully ignores massive clinical shifts. A treatment that moves a patient from mRS 5 (bedbound, requiring constant nursing) to mRS 3 (requiring help with complex tasks but walking independently) is a profound clinical victory, yet it registers as a total failure in a 0-2 dichotomized analysis.

Ordinal logistic regression can use the full mRS distribution, but its common-odds interpretation depends on the proportional-odds model. If the treatment effect differs materially across cut points, one common odds ratio can conceal clinically important heterogeneity and becomes model-dependent. Inspect proportional-odds diagnostics and supplement the common odds ratio with the full mRS distribution, cut-point-specific effects, or an alternative estimand.

Utility-weighted mRS assigns numerical values to categories using an elicited preference set; spacing varies by population and method and must not be assumed universal. Time horizons are equally critical. Assessing outcomes at 90 days captures acute stabilization, but assessing at one year captures long-term neuroplasticity and rehabilitation effects. You must verify that the endpoint timeframe aligns with the biological mechanism of the intervention.

## Multiplicity, Interim Looks, and Early Stopping

The family-wise error rate represents the probability of making at least one Type I error (false positive) when conducting multiple hypothesis tests. Testing five secondary endpoints, three timepoints, and four anatomical subgroups inflates the false positive probability far beyond the nominal alpha of 0.05. Statistical rigor demands alpha-splitting techniques (e.g., Bonferroni correction) or strict hierarchical testing sequences, where the trial is only permitted to test mortality if, and only if, it first achieves significance on the primary mRS shift endpoint.

When prespecified interim looks are used, alpha-spending or group-sequential boundaries control Type I error; the boundary depends on the design and information fraction. Independent monitoring can also address safety and futility according to the protocol, but interim efficacy analyses are not universal requirements.

Trials stopped early for benefit can overestimate effects on average, particularly with few events. Interpret the estimate and repeated confidence interval in light of the stopping rule, information fraction, event count, and total evidence rather than applying an automatic discount.

## Subgroup Fishing and the Illusion of Heterogeneity

Subgroup fishing is the post-hoc search for a 'responder' population after a trial misses its primary endpoint. Repeated slicing by age, sex, baseline ASPECTS, occlusion site, or time window can generate nominal p-values by chance. Such findings are exploratory rather than automatically meaningless; credibility depends on prespecification, multiplicity control, interaction estimates with uncertainty, biological rationale, and replication.

A formal interaction estimate with uncertainty is the appropriate direct comparison of effects across strata; separate within-subgroup p-values do not test effect modification. Prespecification and multiplicity control strengthen credibility, but many trials have limited precision for interactions, so replication and clinical plausibility remain important.

Absence of a statistically significant interaction does not prove homogeneity, and overlap between subgroup confidence intervals or with the overall estimate is not a formal interaction test. Do not withhold an otherwise indicated therapy on the basis of an underpowered, post-hoc stratum result; integrate the interaction estimate, its uncertainty, prior evidence, applicability, and replicated findings.

## Quantitative Reasoning: Absolute Effects and the 2x2 Table

Relative risks and odds ratios do not communicate baseline risk on their own; an OR can also diverge substantially from an RR when outcomes are common. If a drug reduces an event from 2 per 10,000 patients to 1 per 10,000, the RR is 0.5 but the ARR is 0.0001 and the NNT 10,000 over the stated horizon. Reporting only “50% reduction” withholds the absolute scale needed for a clinical decision.

Senior clinical appraisal requires independent computation from raw data. Define the baseline risk of the control group (P0) and the risk in the treated group (P1). The Risk Difference (RD), or ARR, is precisely P0 - P1 (or P1 - P0, depending on the outcome valence). The Number Needed to Treat (NNT) is the inverse of the absolute risk difference: NNT = 1 / RD. The Number Needed to Harm (NNH) is calculated identically using the absolute increase in adverse events.

In stroke neurology, absolute effects are essential for bedside decisions. An NNT of 10 for functional independence and an NNH of 100 for fatal intracranial hemorrhage provide two essential inputs for informed consent, but do not by themselves establish net clinical benefit; outcome severity, uncertainty, competing events, applicability, and patient values still matter. An isolated odds ratio of 1.8 is insufficient without anchoring event probabilities and a horizon.

## Fully Worked Example: Deconstructing a Reperfusion Trial

To demonstrate absolute quantitation, consider an invented multicenter trial of anterior-circulation large-vessel occlusion at 6–24 hours. It compares EVT plus medical therapy with medical therapy alone using 90-day mRS 0–2. The table below is synthetic and exists only to practice arithmetic; it is not a primary-publication appendix.

```
Hypothetical Reperfusion Trial: Primary Endpoint (mRS 0–2 at 90 days)
                             mRS 0–2     mRS 3–6     Total
EVT + Medical Therapy          528         672      1,200
Medical Therapy Alone          384         816      1,200

Risk in Treated (P1) = 528 / 1200 = 0.440
Risk in Control (P0) = 384 / 1200 = 0.320
Risk Difference (RD) = 0.440 − 0.320 = 0.120 (12.0 absolute percentage points)
Number Needed to Treat (NNT) = 1 / 0.120 = 8.33
Risk Ratio (RR) = 0.440 / 0.320 = 1.375
Odds Ratio (OR) = (528/672) / (384/816) = 0.7857 / 0.4705 = 1.669
```

Clinical translation: the absolute increase in mRS 0–2 is 12.0 percentage points, with reciprocal NNT ≈8.3 under the synthetic assumptions. If sICH occurs in 5.0% versus 2.0%, the absolute increase is 3.0 points and reciprocal NNH ≈33.3. A careful natural-frequency statement is: “Per 100 treated in this invented example, about 12 additional people achieve mRS 0–2 and about 3 additional sICH events occur.” A real interpretation must add intervals and the trial’s exact sICH definition; reciprocal measures are averages, and sICH is not synonymous with every “severe hemorrhage.”

## Harms, Co-Interventions, and the Evolving Medical Comparator

Evaluating benefit without quantifying absolute harm is incomplete. Symptomatic intracranial hemorrhage definitions differ across stroke trials. In the [NINDS rt-PA trial](https://www.nejm.org/doi/full/10.1056/NEJM199512143332401), sICH was any CT-documented intracranial hemorrhage temporally related to clinical deterioration; the protocol did not define it as a formal ≥1-point NIHSS threshold. [ECASS III](https://www.nejm.org/doi/full/10.1056/NEJMoa0804656) required hemorrhage judged the predominant cause of a ≥4-point NIHSS worsening or death. Different definitions yield different event rates, so cross-trial harm comparisons require the definition, time window, raw counts, and—when possible—a harmonized reanalysis.

Differential co-interventions operate as silent confounders. If the treating critical care teams are unblinded to assignment, they may subconsciously push aggressive normoglycemia protocols, strict temperature management, and intensive physical therapy exclusively for patients in the active surgical arm, while relegating the control arm to standard floor care. This pervasive performance bias conflates the isolated efficacy of the tested drug with the unmeasured, massive benefit of superior supportive care.

The comparator is central to the trial question, and 'best medical therapy' can change over time. A historical control regimen is not automatically obsolete; compare its components with current target practice and ask whether new co-interventions modify baseline risk or treatment effect. When contemporary care is materially more effective, the historical incremental absolute benefit may be smaller, but its direction and magnitude require evidence rather than assumption.

## Advanced Designs: Non-Inferiority and Adaptive Trials

Non-inferiority trials ask whether a new treatment is not worse than an active comparator by more than a prespecified margin, often because the new option may offer logistical, financial, or safety advantages. The margin is a pivotal design choice and should preserve a clinically acceptable fraction of the active comparator's effect using relevant historical evidence and clinical judgment. A wide or poorly justified margin can permit a clinically important loss of efficacy while still meeting the statistical criterion.

Nonadherence and crossover can attenuate observed differences in some settings, but assignment-based analysis is not invariably conservative in superiority trials or anti-conservative in non-inferiority trials. Non-inferiority conclusions should be robust across prespecified assignment-based and appropriately defined adherence-based estimands, with missing-data and protocol-deviation sensitivity analyses; neither analysis automatically establishes assay sensitivity.

Platform trials evaluate multiple interventions under a shared infrastructure and may add or drop arms over time. Some use response-adaptive randomization, while others retain fixed allocation; neither feature defines every platform trial. Appraise prespecified adaptation rules, concurrent controls, calendar-time effects, estimands, and the multiplicity procedure appropriate to the claims. Family-wise error control is one possible error-rate strategy, not a universal requirement for every platform objective.

## Checklists and Frameworks: The CONSORT-Minded Sequence

Memorizing the 25-item CONSORT checklist numbers is pedagogical waste. Advanced clinicians must instead internalize the structural causal sequence. When dissecting a publication, enforce this chronological framework:

- 1. Target Population & Setting: Who was excluded? Does the strict eligibility criteria match the physiology of the patient in your ED?
- 2. Assignment & Concealment: Was sequence generation genuinely random, and was the next assignment operationally unpredictable before irrevocable enrollment?
- 3. Strategies & Co-interventions: What precise protocols dictated the comparator arm? Were unblinded rescue therapies permitted differentially?
- 4. Blinding Matrix: Construct the grid. Who knew the assignment, when did they know it, and exactly how could that knowledge alter the measurement?
- 5. Analysis Sets & Estimands: Is the primary p-value strictly generated from an intention-to-treat population? Are missing data bounded by imputation?
- 6. Absolute Quantitation: Ignore the abstract. Extract the raw counts. Compute RD, NNT, NNH, and place the trade-off in plain language.

## Pitfalls and Failure Modes in Trial Appraisal

The landscape of trial appraisal is saturated with specific failure modes that trap junior clinicians. The primary failure mode is conflating 'randomized' with 'unbiased'. Assuming that a pristine sequence generation immunizes the trial from the devastation of differential attrition, unblinded assessment, and outcome reporting bias is a catastrophic analytical error.

The second failure mode is the Per-Protocol Apology: adopting a therapy from a favorable naive per-protocol or as-treated secondary analysis after a null assignment-based primary analysis. Such a comparison may be distorted by post-randomization selection or confounding unless it targets a prespecified estimand with appropriate adjustment and sensitivity analysis.

The third failure mode is Subgroup Hallucination. This involves declaring that a drug 'works brilliantly in severe strokes' based entirely on a post-hoc, exploratory subgroup analysis yielding a nominal p-value of 0.04, completely lacking a formal test for interaction. It represents the total surrender of statistical discipline.

The fourth failure mode is Relative Risk Theater. Communicating a '50% reduction in stroke mortality' to a patient's family without explicitly disclosing that the absolute baseline risk dropped from 2 in 10,000 to 1 in 10,000. It is statistically accurate but ethically manipulative.

## Clinical and Epidemiologic Notes

Clinical Note: When reading a newly published stroke trial, draft the clinical summary sentence before looking at the author's abstract conclusions. Compute the NNT and NNH independently from the raw event counts in the appendix. Formulate the precise absolute trade-off. Never adopt an abstract conclusion that you cannot mathematically reconstruct and defend with raw data.

Epidemiologic Note: Internal validity is distinct from external transportability. A well-executed trial such as DAWN estimates effects for the population it enrolled. Applying DAWN alone to a different core-size or clinical-severity phenotype would be a transportability error; however, dedicated large-core randomized trials now provide direct evidence for selected large-core populations. Appraise the target patient against the eligibility, workflow, endpoint, and uncertainty of the trial that actually studied that phenotype.

Industry Note: Scrutinize the data sharing statement and the precise role of the commercial sponsor. When the sponsor holds exclusive access to the raw data, dictates the statistical analysis plan, and authors the first draft of the manuscript without independent academic verification, the threshold for adopting marginal or subgroup-driven findings must rise exponentially. Methodological skepticism must scale with financial conflict.


![Scatterplots showing exposure measurement error attenuating a regression slope toward zero.](../assets/figures/fig77_regression_dilution.png)

*Teaching graphic (fig77_regression_dilution.png).*

## Chapter summary

Randomized trials are powerful because concealed random allocation supports baseline exchangeability in expectation, including for unmeasured prognostic factors. That advantage can be undermined by allocation subversion, differential missing outcomes, post-randomization co-interventions, and analyses that do not match the target estimand. Analysis by randomized assignment commonly targets a treatment-policy effect and preserves the randomized comparison for participants with observed outcomes, but it is not automatically unbiased when outcomes are missing or other identifying assumptions fail. Naive per-protocol or as-treated comparisons lose the protection of randomization and can introduce post-randomization confounding; causal per-protocol effects require a prespecified estimand, adequate longitudinal data, and appropriate adjustment. In PROBE trials, blinded outcome assessment reduces measurement bias, while open treatment assignment can still permit performance bias. Multiplicity, interim stopping boundaries, and post-hoc subgroup selection can generate exaggerated evidence. Appraisal should translate relative effects into endpoint- and horizon-specific absolute risks, risk differences, NNTs or NNHs when appropriate, and their uncertainty. A CONSORT-minded chronological review helps readers distinguish the randomized question from post-randomization departures and reporting spin.

## Practice and reflection

1. Extract the raw 2x2 event counts from the primary publication of the MR CLEAN or DAWN trial. Independently compute the Risk Difference, Relative Risk, Odds Ratio, and NNT for functional independence.
2. Draw a plausible DAG in which restricting an analysis to adherent participants opens a post-randomization selection path. State which arrows make the restriction biasing, explain why collider bias is possible rather than automatic, and name a design or analysis strategy that could target a per-protocol effect.
3. Select a recent Prospective Randomized Open-label Blinded-Endpoint (PROBE) trial in neurology. Map the blinding matrix for all stakeholders and identify the specific physical cues that could unmask the outcome assessor.
4. Locate a stroke trial stopped early for efficacy. Explain why stopping at a favorable interim fluctuation can create upward bias on average, then assess the stopping boundary, information fraction, event count, and uncertainty in that specific trial.
5. Contrast the NINDS and ECASS III definitions for symptomatic intracranial hemorrhage (sICH). Calculate how applying the more restrictive ECASS III definition mathematically alters the Number Needed to Harm (NNH).
6. Identify a trial that failed its primary intention-to-treat endpoint but highlights a 'positive' finding in a specific subgroup in the abstract. Determine if a formal interaction p-value was reported and interpret its validity.
7. Analyze a non-inferiority stroke trial (e.g., comparing tenecteplase to alteplase). State the non-inferiority margin in absolute terms and evaluate whether that exact margin is clinically acceptable in your local practice.
8. Explain why nonadherence can make treatment groups more similar in some non-inferiority trials, while noting that assignment-based analysis is not universally anti-conservative. State why prespecified assignment- and adherence-based estimands, missing-data analyses, and assay sensitivity all matter.
9. Evaluate a trial comparing a surgical intervention to 'best medical therapy' from a decade ago. Define the exact components of that historical medical therapy and argue whether the trial results remain transportable to modern optimized care.
10. Draft a standardized, 3-sentence informed consent script for a patient eligible for acute endovascular reperfusion, communicating the efficacy and safety profiles strictly using absolute frequencies (e.g., 'X out of 100') rather than relative percentages.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
