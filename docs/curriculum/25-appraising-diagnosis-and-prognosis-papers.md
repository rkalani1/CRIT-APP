# Chapter 25. Appraising Diagnosis and Prognosis Papers

<div class="disclaimer-banner" markdown="1">
**Web Edition — original teaching text.** Educational only; not medical advice. No commercial handbook prose, paper abstracts, or publisher figures.
</div>

## Web Edition clinical frame

It is mid-afternoon on a stroke unit. A fellow drops three PDFs into the team channel: an EVT selection paper with a dramatic relative-risk headline, a claims analysis of dual antiplatelet timing, and a prediction model for hemorrhage risk. Before anyone changes a pathway, this chapter forces a slower question: what exactly is being estimated, for whom, and with what absolute stakes?

## Learning objectives

- Apply the tripartite diagnosis and prognosis appraisal frameworks framework (Validity, Results, Applicability) to appraise diagnostic accuracy and prognostic studies in neurology.
- Detect validity threats in diagnostic research, including spectrum bias, partial verification bias, and incorporation bias in stroke pathways.
- Recognize validity threats in prognostic research, particularly inception cohort violations, incomplete follow-up, and absent adjustment for baseline confounding.
- Reconstruct diagnostic results from 2×2 tables to compute likelihood ratios (LRs), refusing to transport predictive values across differing prevalence landscapes.
- Interpret prognostic results through absolute risk and calibration slopes, demanding precision around time-horizons for neurologic outcomes.
- Evaluate the applicability of diagnostic tests and prediction rules by linking post-test probabilities or predicted risks to absolute clinical action thresholds.

## The Tripartite Framework: Validity, Results, Applicability

The diagnosis and prognosis appraisal frameworks to the Medical Literature established a discipline for critical appraisal that remains indispensable. Whether evaluating a prehospital stroke scale, an automated CTA algorithm, or a score forecasting intracerebral hemorrhage (ICH) expansion, the appraisal process breaks into three consecutive, unskippable questions: (1) Are the results of the study valid? (2) What are the results? (3) Will the results help me in caring for my patients? Skipping directly to the results—celebrating a high sensitivity or an impressive c-statistic—without first securing validity is the most pervasive error in journal club. If the methods cannot yield the truth, the numbers are mathematical fictions. If the numbers are valid but do not cross action thresholds in your local population, the tool is academically interesting but clinically useless. This chapter adapts the diagnosis and prognosis appraisal frameworks templates specifically for the diagnostic and prognostic literature in neurology.

## Appraising Diagnosis Part 1: Are the Results Valid?

Diagnostic validity hinges on the independent, blind comparison of an index test against a credible reference standard within a representative spectrum of patients. First, was there an independent, blind comparison with a reference standard? The reference (gold) standard must be applied regardless of the index test result, and the interpreters of each must be meticulously blinded to the other. In neurology, 'incorporation bias' is a frequent contaminant. This occurs when the index test (e.g., continuous EEG) forms part of the criteria for the reference standard (e.g., the consensus diagnosis of nonconvulsive status epilepticus). Agreement is mathematically guaranteed, inflating the test's apparent accuracy.

Second, did the patient sample include an appropriate spectrum of patients to whom the diagnostic test will be applied in clinical practice? Testing a large-vessel occlusion (LVO) scale by comparing devastating MCA syndromes against young healthy controls creates profound 'spectrum bias.' The test looks flawless on paper because the clinical gray zone—mild deficits, fluctuating aphasia, complex migraines, post-ictal paresis—has been surgically excised. A valid study enrolls consecutive patients suspected of having the target condition, exactly as they present in the chaotic emergency department or prehospital environment.

Third, did the results of the test being evaluated influence the decision to perform the reference standard? 'Verification bias' (or work-up bias) occurs when only patients testing positive on a bedside screen are sent for the definitive CTA or catheter angiography. The false negatives are never discovered, rendering the test artificially sensitive. If the reference standard is invasive or costly, authors must statistically adjust for the unverified patients or employ a dual-reference strategy, rather than ignoring them.

## Appraising Diagnosis Part 2: What Are the Results?

Once validity is established, extract the raw counts to reconstruct the 2×2 table: true positives, false positives, false negatives, and true negatives. Sensitivity (the proportion of diseased patients who test positive) and specificity (the proportion of non-diseased patients who test negative) are fixed test properties, but they are useless at the bedside because you do not yet know if the patient has the disease. Positive and negative predictive values (PPV and NPV) answer the bedside question, but they are fatally tethered to the study's prevalence. Transporting a PPV from a comprehensive stroke center cohort with a 30% LVO prevalence to a community EMS stream with a 5% prevalence is an epidemiological error dressed as evidence-based medicine.

The portable currency of diagnosis is the likelihood ratio (LR). The positive likelihood ratio (LR+ = sensitivity / [1 - specificity]) tells you how many times more likely a positive test occurs in diseased versus non-diseased patients. The negative likelihood ratio (LR- = [1 - sensitivity] / specificity) does the same for a negative test. An LR+ >10 generates large, often conclusive shifts in probability; an LR- <0.1 practically rules out disease. LRs between 0.5 and 2.0 rarely change clinical decisions.

For multilevel or continuous tests (like the NIHSS or an automated core volume), dichotomizing at a single 'optimal' cut-point destroys information. Demand interval likelihood ratios for strata (e.g., NIHSS 0-5, 6-10, 11-15). A high score might strongly rule in LVO, a low score strongly rule it out, while intermediate scores appropriately yield likelihood ratios near 1.0, preserving necessary clinical uncertainty rather than forcing a false binary.

## Appraising Diagnosis Part 3: Will the Results Help My Patients?

Applicability requires integrating the test's likelihood ratio with your patient's pre-test probability to generate a post-test probability via Bayes' theorem. Are your patients so different from those in the study that the LRs cannot apply? (Often, no—LRs transport reasonably well unless spectrum bias is severe.) Is the test available, affordable, and actionable in your setting? Most importantly: will the post-test probability cross a testing or treatment threshold? If a negative diffusion-weighted MRI (DWI) in a patient with a classic brainstem TIA syndrome lowers the probability of ischemia from 90% to 40%, but your threshold to prescribe dual antiplatelet therapy is 10%, the negative MRI is academically interesting but clinically irrelevant. It failed to cross the action threshold.

## Appraising Prognosis Part 1: Are the Results Valid?

Prognostic studies forecast the future. Their validity rests on unbiased cohort assembly and rigorous, relentless follow-up. First, was there a representative and well-defined sample of patients at a similar point in the course of the disease? This is the 'inception cohort' requirement. If a study evaluates post-stroke epilepsy but enrolls patients varying from one week to five years post-infarct, the survival curves are a meaningless blur. The clock must start at a uniform biologic moment (e.g., symptom onset, discharge, or 30 days post-hemorrhage).

Second, was follow-up sufficiently long and complete? Loss to follow-up is the Achilles heel of prognosis. Patients who drop out are rarely missing at random; they are often the most devastatingly disabled (unable to travel to clinic) or the most completely recovered (no longer feeling the need for medical contact). A rule of thumb: if assuming all lost patients suffered the worst outcome reverses the study's conclusion, the follow-up is fatally inadequate. Third, were objective and unbiased outcome criteria used? 'Functional decline' requires blinded modified Rankin Scale (mRS) adjudication, not a retrospective chart-review guess.

Fourth, was there adjustment for important prognostic factors? If a paper claims that early intensive rehab worsens prognosis, but the patients assigned to early rehab had significantly larger baseline infarct volumes, the claim is hopelessly confounded. Authors must use multivariable regression or propensity models to adjust for known baseline imbalances.

## Appraising Prognosis Part 2: What Are the Results?

Prognostic results should answer two pragmatic questions: How likely is the outcome, and how precise is the estimate? Seek absolute event rates at specific, clinical time horizons (e.g., '12% risk of recurrent stroke at 90 days'). Survival curves (Kaplan-Meier plots) provide the best visual summary, showing not just if an event occurs, but the tempo of when. For prognostic models or clinical prediction rules (CPRs), results are typically presented as discrimination (area under the ROC curve, or c-statistic) and calibration. Discrimination measures how well the rule separates those who have the event from those who do not. Calibration—often omitted but vastly more important—measures how closely the rule's predicted probabilities match the observed event rates across different risk strata. A poorly calibrated model that systematically overestimates risk will lead to massive overtreatment.

Precision is captured by 95% confidence intervals around these estimates. If the 90-day recurrent stroke risk is 12%, but the confidence interval stretches from 4% to 28%, the point estimate is a fragile illusion borne of a small sample size. Wide confidence intervals demand humility when applying the prognostic rule to the patient sitting in front of you.

## Appraising Prognosis Part 3: Will the Results Help My Patients?

To apply a prognostic rule, ask: Were the study patients similar to my own? If an ICH expansion score was derived purely in academic comprehensive centers with rapid blood pressure protocols, it may severely misestimate expansion risk in a rural spoke hospital with prolonged transfer times. Will the results lead directly to selecting or avoiding therapy? Prognosis is only useful if it dictates decisions or meaningfully anchors patient counseling. If a score predicts a 5% versus 15% risk of malignant edema after MCA territory stroke, but both probabilities compel continuous ICU monitoring and neurosurgical consultation, the score changes absolutely nothing. Finally, are the results useful for reassuring or counseling patients? Sometimes, delivering a highly certain, narrow confidence interval around a devastating prognosis is the definitive, compassionate action that empowers families to transition to palliative goals.

## A Worked Example: Diagnosis (LVO Triage)

Scenario: A novel prehospital stroke scale claims 85% sensitivity and 80% specificity for detecting LVO. The local EMS pre-test probability (prevalence of LVO among stroke alerts) is 15%.

Validity (Are the results valid?): The study enrolled consecutive EMS dispatches (preventing spectrum bias), CTA was performed universally upon arrival (preventing verification bias), and the CTA readers were blinded to the field score. Validity is robust.

Results (What are the results?): Calculate LRs. LR+ = 0.85 / (1 - 0.80) = 4.25. LR- = (1 - 0.85) / 0.80 = 0.1875.

Applicability (Will they help my patients?): Convert pre-test probability (0.15) to odds (0.15/0.85 = 0.176). Post-test odds for positive = 0.176 × 4.25 = 0.75. Post-test probability = 0.75 / (1 + 0.75) = 43%. Post-test odds for negative = 0.176 × 0.1875 = 0.033. Post-test probability = 0.033 / 1.033 = 3.2%. If regional protocol dictates diversion to a comprehensive center when LVO probability exceeds 25%, a positive test clears the threshold (initiate diversion), and a negative test securely routes the patient to a primary center (leaving only a 3.2% residual risk).

## A Worked Example: Prognosis (ICH Expansion)

Scenario: A new clinical score predicts 24-hour hematoma expansion using baseline ICH volume, the CTA spot sign, and time from symptom onset.

Validity (Are the results valid?): The cohort was a true inception cohort (all scanned within 6 hours of onset), the 24-hour follow-up CT was 98% complete, and analysts were blinded. Validity is high.

Results (What are the results?): The authors provide absolute risk strata. Low score: 5% risk (95% CI 2-8%). Medium: 25% (20-30%). High: 65% (55-75%). Calibration slope is near perfect.

Applicability (Will they help my patients?): You apply the score to a patient in the ED; they map to the High stratum. The 65% risk of expansion crosses your aggressive action threshold, triggering ultra-early intensive blood pressure lowering, reversal of antithrombotics, and immediate transfer to a neuro-ICU capable of surgical evacuation. The prognostic rule directly catalyzed a treatment pathway.

## Chapter summary

The diagnosis and prognosis appraisal frameworks templates force critical appraisal into three unskippable phases: Validity, Results, and Applicability. For diagnosis, validity requires an independent, blinded comparison against a gold standard in a clinically relevant spectrum of patients, systematically avoiding verification and incorporation biases. Diagnostic results should be translated from sensitivity and specificity into portable likelihood ratios, which safely update local pre-test probabilities into actionable post-test probabilities via Bayes' theorem. For prognosis, validity demands an inception cohort with near-complete follow-up and rigorous adjustment for baseline confounding. Prognostic results must highlight absolute risks at defined time horizons, with calibration holding vastly more clinical weight than mere discrimination (AUC). Ultimately, applicability asks a binary question: does the post-test probability or predicted absolute risk actually cross a decision threshold that alters patient management, triage, or counseling in your specific clinical environment?

## Practice and reflection

1. Apply the diagnostic Validity template (spectrum, verification, incorporation, blinding) to a recent paper evaluating deep learning for LVO detection on non-contrast CT.
2. Calculate the positive and negative likelihood ratios for a diagnostic test with 90% sensitivity and 70% specificity.
3. Take the likelihood ratios from the previous exercise. If your local pre-test probability is 10%, calculate the precise post-test probability for both a positive and negative result.
4. Identify a prognostic prediction rule used in your practice (e.g., ABCD2, ICH score, HEAT score). Evaluate its original derivation paper strictly using the inception cohort and loss-to-follow-up criteria.
5. Explain to a junior resident why transporting a Positive Predictive Value (PPV) from a tertiary referral center study to a community primary care clinic is mathematically dangerous.
6. Define an explicit action threshold for transferring a suspected TIA patient to the hospital. How low must the predicted 48-hour stroke risk be to allow safe discharge home from the ED?
7. Identify a clinical situation where a negative diagnostic test has an excellent negative likelihood ratio (e.g., 0.05), but the post-test probability remains too high to withhold treatment. (Hint: consider very high pre-test probabilities).
8. Describe a clinical scenario where highly precise prognostic information changes patient counseling or family expectations, even if it does not alter the medical treatment plan.

---

*Figures and tables in this chapter are original teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*

