# Chapter 12. Effect Sizes, Absolute Benefit, NNT, and Clinical Importance

## Opening

![Absolute vs relative by baseline.](../assets/figures/fig70_absrel_baseline.png)

*The same relative risk reduction produces a large absolute benefit at high baseline risk and a negligible one at low baseline risk.*

![ARR and NNT.](../assets/figures/fig08_arr_nnt.png)

*Absolute risk reduction and its reciprocal, the number needed to treat, translate a trial's effect into patients treated per event prevented.*

![NNT icon array.](../assets/figures/crit_fig_nnt_icon_array.png)

*Absolute benefit intuition.*


Marketing quotes a 25% relative reduction. Convert to absolute risk difference and NNT with the control-arm rate before counseling the next clinic patient.


## Conceptual Core: The Imperative of Absolute Effects

Clinical literature heavily favors relative measures of effect—relative risk reductions (RRR), odds ratios (OR), and hazard ratios (HR). There are structural, statistical, and psychological reasons for this dominance. Statistically, relative effects are often assumed to be more stable across populations with differing baseline risks. Models like logistic regression natively generate odds ratios, and Cox proportional hazards regression natively generates hazard ratios. Furthermore, relative risk reductions usually appear numerically larger than absolute risk reductions, making them highly attractive for abstracts, press releases, and pharmaceutical marketing.

Clinical decision-making requires the absolute scale. A relative risk reduction of 50% provides little actionable information in isolation. If the 90-day control risk is 20%, a transportable 50% relative reduction corresponds to 10 fewer events per 100 treated; if the control risk is 1%, it corresponds to 0.5 fewer events per 100. Treatment burden and per-patient cost may remain similar, while absolute harm can also vary by baseline risk; estimate benefits and harms separately in the target population.

Understanding treatment efficacy therefore requires translating a compatible relative estimate into local absolute benefits only after its transportability is justified. This conversion needs a credible control risk for the target population and horizon. Relative measures alone can make effects appear larger than their absolute clinical impact, so appraisal should report natural frequencies with and without treatment and quantify harms on the same horizon.

Relative metrics without absolute context are insufficient for clinical interpretation. Raw event rates, absolute differences, and absolute harms establish whether an effect is clinically important. This translation is foundational to evidence-based neurology.

## Quantitative Reasoning: Defining the Symbols and Metrics

To appraise literature, one must precisely define the mathematical structure of effect sizes. Let p_c denote the risk of the event in the control group (baseline risk), and p_t denote the risk of the event in the treatment group.

Risk Ratio (RR): The ratio of the probability of an event in the treated group to the probability in the control group (RR = p_t / p_c). If the event is harmful (e.g., recurrent stroke), an RR < 1 indicates benefit. The Relative Risk Reduction (RRR) is defined as 1 - RR. If a trial reports an RR of 0.80, the RRR is 20%. The RR is mathematically constrained; it cannot exceed 1 / p_c. It is easily understood but often misrepresented as a measure of absolute efficacy.

Odds Ratio (OR): Odds are defined as the probability of an event occurring divided by the probability of it not occurring: O = p / (1 - p). The odds ratio is the ratio of the odds in the treatment group to the odds in the control group: OR = [p_t / (1 - p_t)] / [p_c / (1 - p_c)]. A frequent statistical error in neurology is interpreting the OR as a Risk Ratio. When an outcome is rare (generally <10%), the OR closely approximates the RR. However, many stroke outcomes are common. For example, achieving functional independence (modified Rankin Scale 0-2) after acute ischemic stroke may occur in 40% to 60% of patients. In these ranges, the OR mathematically inflates the apparent effect size relative to the RR.

Consider a thrombectomy trial where the control group has a 40% chance of mRS 0-2 (p_c = 0.40) and the treatment group has a 60% chance (p_t = 0.60). The RR is 1.50 (0.60 / 0.40). The odds in the control group are 0.40/0.60 = 2/3 ≈ 0.667. The odds in the treatment group are 0.60/0.40 = 1.50. The OR is 1.50 / (2/3) = 2.25. Quoting an OR of 2.25 as a '125% increase in the probability of good outcome' is a severe mathematical failure. The probability increased by 50% relative, and 20% absolute. Never read an OR as an RR when events are common.

Hazard Ratio (HR): A hazard is the instantaneous event rate among people still at risk. In a proportional-hazards model, an HR compares treatment and control hazards and assumes their ratio is constant over time. An HR is not a ratio of cumulative risks: an HR of 0.70 does not by itself mean 30% fewer people experience the event by a given horizon. The corresponding cumulative risks depend on the baseline hazard, follow-up horizon, competing events, censoring, and whether proportional hazards is plausible; extract risks from survival or cumulative-incidence estimates rather than guessing from the HR.

Absolute Risk Reduction (ARR): The arithmetic difference in event probabilities between the control and treatment groups (ARR = p_c - p_t). This metric operates on the natural scale and directly quantifies the number of events prevented per treated patient. If p_c is 0.10 and p_t is 0.06, the ARR is 0.04, or 4 percentage points.

Absolute Risk Increase (ARI): The analogous metric for adverse events, calculated as the risk of harm in the treated group minus the risk of harm in the control group (ARI = p_t(harm) - p_c(harm)). If a drug increases bleeding from 1% to 3%, the ARI is 2%.

## The Bridge: Baseline Risk and the Algebra of Absolute Risk Reduction

![Same relative effect yields different NNTs across baseline risk.](../assets/figures/fig32_nnt_vs_baseline.png)

*With a constant relative risk (RR = 0.75), NNT falls as control-event rate rises—absolute benefit tracks baseline risk. Teaching figure.*

The algebraic relationship between relative and absolute risk dictates the logic of precision medicine. Assuming the relative risk (RR) is constant and transportable across different patient populations, the Absolute Risk Reduction can be calculated as: ARR = p_c * (1 - RR).

This equation is the bridge. It demonstrates mathematically that the absolute benefit of any therapy is a direct linear function of the baseline risk (p_c). The higher the baseline risk, the greater the absolute benefit, provided the relative efficacy holds.

Named trials illustrate why endpoint and horizon must stay attached to the arithmetic. In [NASCET](https://www.nejm.org/doi/full/10.1056/NEJM199108153250701), patients with recently symptomatic 70–99% stenosis had a 2-year ipsilateral-stroke risk of 26% with medical therapy versus 9% with carotid endarterectomy (ARR 17 percentage points; NNT about 6). In [ACAS](https://doi.org/10.1001/jama.1995.03520420037035), asymptomatic stenosis ≥60% had a 5-year composite risk of ipsilateral stroke plus any perioperative stroke or death of 11.0% with medical management versus 5.1% with surgery (ARR 5.9 points; NNT about 17). These trials studied different populations, eras, horizons, and endpoints; neither estimate should be reconstructed by assuming one common RR.

Perioperative harm must not be subtracted twice from a composite that already includes it, as the ACAS endpoint did. Modern decisions also require contemporary medical-therapy risk, age and life expectancy, stenosis measurement, surgical complication rates, and patient preferences. The broader lesson survives: use trial-specific absolute event risks with their exact endpoint and horizon, and verify that the local procedural-harm rate is compatible with the evidence.

## Number Needed to Treat (NNT) and Number Needed to Harm (NNH)

The Number Needed to Treat (NNT) translates the ARR into a frequency format. It represents the average number of patients who must receive the treatment to prevent one additional adverse outcome. The formula is simple: NNT = 1 / ARR, where ARR is expressed as a decimal, not a percentage.

If a trial reports an ARR of 0.04 (4 percentage points), the reciprocal NNT is 25. This means about four fewer events per 100 similar patients treated over the stated horizon if the estimate transports; it does not guarantee exactly one prevented event in every group of 25.

An NNT is uninterpretable without a stated time horizon. NNT 25 at 90 days and NNT 25 at 5 years are different horizon-specific estimates, but horizon alone does not establish potency, timing, or mechanism. Compare them only with the endpoint, population, competing risks, censoring, and event-time curves attached. Always report the duration (for example, “NNT 25 over 90 days”).

The Number Needed to Harm (NNH) applies the exact same mathematics to adverse events. NNH = 1 / ARI. Evaluating any stroke intervention requires juxtaposition of the NNT and NNH. If a potent antithrombotic regimen yields an NNT of 40 to prevent one ischemic stroke over 90 days, but generates an NNH of 80 for causing one major intracranial hemorrhage over the same period, the clinician faces a quantitative tradeoff. Because intracranial hemorrhages often carry higher morbidity than recurrent minor ischemic strokes, a simple numerical comparison (40 vs 80) is insufficient. One must formally weight the severity of the outcomes.

A common failure in literature is presenting the NNT as a single point estimate without its confidence interval. Because NNT is the reciprocal of the ARR, its confidence interval is calculated by taking the reciprocals of the ARR confidence limits. If the ARR is 0.04 with a 95% CI of [0.02, 0.06], the NNT is 25 with a 95% CI of [17, 50] (since 1/0.06 = 16.6 and 1/0.02 = 50).

When the ARR confidence interval crosses zero (e.g., ARR 0.02, 95% CI [-0.01, 0.05]), the NNT confidence interval crosses infinity. It ranges from an NNT of 20 (benefit) to infinity, to an NNH of 100 (harm). Reporting an NNT point estimate without acknowledging that the CI includes potential harm is deceptive.

Finally, NNT calculations are subject to competing risks. If the time horizon is 5 years, a patient may die of unrelated causes (e.g., cancer, myocardial infarction) before realizing the benefit of stroke prevention. In populations with high competing mortality, naive NNTs calculated from unadjusted Kaplan-Meier estimates will overestimate the absolute benefit.

## Confidence Intervals: Compatibility and Clinical Importance Thresholds

A 95% Confidence Interval (CI) is frequently mischaracterized as having a 95% probability of containing the true effect size. Strictly speaking, under frequentist statistics, the true effect is fixed, and the interval either contains it or does not. A more precise and clinically useful interpretation is that the CI represents a range of effect sizes that are highly compatible with the observed data, given the statistical model and its assumptions.

Appraisal requires examining the limits of the confidence interval against the Minimal Clinically Important Difference (MID or MCID). The MID is the smallest effect size that patients or clinicians consider large enough to justify the costs, risks, and burdens of the treatment. For a cheap, safe drug like aspirin, the MID might be an ARR of 0.5%. For an invasive, risky procedure like a craniectomy, the MID for functional independence might be an ARR of 10% or higher.

When a trial reports a statistically significant result, the CI strictly excludes the null value (e.g., an ARR CI that excludes zero). However, statistical significance does not equate to clinical importance. We categorize trial results into four distinct scenarios based on the CI and the MID:

1. Compatible Effects Are Clinically Important: The entire interval lies above the MID. Assuming a valid design and model, even the smallest effect compatible with this interval exceeds the prespecified importance threshold.

2. Statistically Detectable but Below the MID: The interval excludes zero but lies below the MID (for example, ARR 0.2%, 95% CI 0.1% to 0.3%). The estimate may be incompatible with no effect under the model yet still fail the prespecified clinical-importance threshold; adoption also depends on harms, cost, burden, and patient values.

3. Uncertain Clinical Importance: The interval excludes zero but crosses the MID. The data are compatible with effects on both sides of the importance threshold, so statistical significance does not settle clinical utility.

4. Broadly Inconclusive: The interval crosses both zero and the MID. The data may be compatible with harm, negligible effect, and clinically important benefit; report that range rather than reducing it to a positive/negative label.

5. Clinically Important Benefit Excluded at the Interval Level: The interval includes zero but its upper benefit limit is below the MID. Under the study and model assumptions, the interval excludes benefits at or above that threshold, while it may still include no effect or harm.

Never look solely at the point estimate. The width and location of the confidence interval relative to your patient's minimal important threshold dictate the decision.

## P-values versus Estimation and Clinical Importance

The p-value estimates the probability of obtaining data at least as extreme as those observed, assuming that the null hypothesis is true and all methodological assumptions hold exactly. It is a measure of statistical surprise. It does not measure the size of the treatment effect, nor does it measure the probability that the null hypothesis is false, nor does it measure the probability that the results were due to chance.

A fundamental failure in medical education is conflating the Fisherian p-value (a continuous measure of evidence against a null model) with the Neyman-Pearson alpha threshold (a rule for minimizing false positive errors over long-run industrial repetitions). Forcing p-values into a dichotomous 'significant' (p < 0.05) or 'non-significant' (p > 0.05) framework strips them of nuance and encourages cognitive cliffs, where p = 0.049 is a breakthrough and p = 0.051 is a failure.

Furthermore, the p-value conflates effect size and sample size. A trivial ARR of 0.1% in a trial of 100,000 patients will yield a p-value of 0.001. A massive ARR of 20% in a trial of 20 patients might yield a p-value of 0.15. Relying on p-values forces the reader to ignore the magnitude of the potential benefit.

Estimation centers the effect size and its uncertainty. In acute stroke trials, small samples can produce wide intervals even when the point estimate is large. Evaluate absolute and relative effects with confidence intervals and prespecified importance thresholds; report p-values for their stated tests without treating either side of 0.05 as a verdict.

## Named Framework: The Absolute Effect Translation Checklist

When reading a trial abstract, results section, or meta-analysis, deploy this sequential checklist to strip away relative framing, avoid spin, and establish the absolute clinical reality. Memorize this sequence.

1. Identify the Metric: Is the primary result reported as an RR, OR, HR, or IRR? Verify that the authors are not calling an OR a Risk Ratio.

2. Extract the Baseline Risk (p_c): Locate the exact event rate in the control group for the primary endpoint. Do not accept a relative summary without this denominator.

3. Calculate the Absolute Risk Reduction (ARR): Compute p_c * (1 - RR), or manually subtract the raw event rates if provided (p_c - p_t).

4. Determine the Number Needed to Treat (NNT): Invert the ARR (1 / ARR).

5. Establish the Time Horizon: Over what exact duration does this NNT apply? (e.g., 90 days, 1 year, 5 years).

6. Evaluate Precision: Examine the 95% CI of the absolute difference. Does it cross zero? Does it cross your predetermined Minimal Clinically Important Difference (MID)?

7. Extract Harm Data: Identify the primary safety endpoint (e.g., symptomatic intracranial hemorrhage, major bleeding). Extract its baseline risk, calculate the ARI, and invert it to find the NNH over the same time horizon.

8. Synthesize the Trade-off: State the core absolute contrast in natural frequencies. 'Over X days, we treat Y patients to prevent one [Efficacy Outcome], while one additional [Harm Outcome] occurs per Z patients treated.' The decision also requires precision, outcome severity, applicability, competing events, and patient values.

## Fully Worked Example 1: Dual Antiplatelet Therapy in Minor Ischemic Stroke

The following fully synthetic scenario—not POINT or CHANCE data—demonstrates absolute-effect arithmetic for secondary prevention after minor ischemic stroke or high-risk TIA.

Synthetic scenario (all event rates below are invented for arithmetic only): an RCT compares 21 days of aspirin plus clopidogrel followed by a single agent with aspirin alone, with 90-day follow-up. Recurrent ischemic stroke occurs in 5.0% versus 7.5%; major hemorrhage occurs in 0.9% versus 0.4%. In a real appraisal, confidence intervals and the prespecified analysis would be required before interpretation.

Step 1: Efficacy Translation. Control baseline risk (p_c) = 0.075 (7.5%). Treatment risk (p_t) = 0.050 (5.0%). Absolute Risk Reduction (ARR) = 0.075 - 0.050 = 0.025 (2.5 percentage points). Number Needed to Treat (NNT) = 1 / 0.025 = 40. Time horizon = 90 days.

Step 2: Safety Translation. Control harm risk (p_c_harm) = 0.004 (0.4%). Treatment harm risk (p_t_harm) = 0.009 (0.9%). Absolute Risk Increase (ARI) = 0.009 - 0.004 = 0.005 (0.5 percentage points). Number Needed to Harm (NNH) = 1 / 0.005 = 200. Time horizon = 90 days.

Step 3: Synthesis and Clinical Decision. In this synthetic scenario, treating 1,000 similar patients corresponds to 25 fewer recurrent ischemic strokes and 5 additional major hemorrhages over 90 days. Counts alone do not establish a five-to-one net benefit: recurrent strokes and hemorrhages vary in severity, may overlap, and carry different patient values. A decision analysis should preserve outcome severity and uncertainty, confirm that the patient matches the modeled population, and avoid labeling all prevented strokes “minor.”

Step 4: Baseline Risk Stratification (Advanced). Suppose a patient has an estimated 2.0% 90-day recurrence risk. You may project an absolute benefit only from a fixed-horizon risk ratio—or from a model that estimates fixed-horizon risks—not by treating an HR as though it were an RR. If a risk ratio of 0.65 were justified and transportable, the projected ARR would be 0.02 × (1 − 0.65) = 0.007 and the NNT 143. If the projected major-bleeding increase were 0.5 percentage points, the NNH would remain 200. This synthetic sensitivity analysis would correspond to about 7 fewer recurrent strokes and 5 additional major bleeds per 1,000 treated. It is a prompt to revisit assumptions and outcome severity, not proof that net benefit has vanished for every low-risk patient.

## Fully Worked Example 2: Thrombolysis in Acute Ischemic Stroke

Consider ECASS III alteplase at 3–4.5 hours. Its primary endpoint was a favorable 90-day outcome, defined as mRS 0–1 (no symptoms or no significant disability).

Reported efficacy: mRS 0–1 was achieved in 52.4% of the alteplase group and 45.2% of the placebo group (OR 1.34, 95% CI 1.02–1.76; p = 0.04). In the primary report, symptomatic intracranial hemorrhage occurred in 10/418 (2.4%) alteplase recipients and 1/403 (0.25%) placebo recipients (OR 9.85, 95% CI 1.26–77.32; p = 0.008). See the [primary ECASS III report](https://www.nejm.org/doi/full/10.1056/NEJMoa0804656).

Notice that the outcome is common. Using the OR of 1.34 as a relative risk is a trap. Control baseline probability of good outcome (p_c) = 0.452. Treatment probability of good outcome (p_t) = 0.524. The true Relative Risk of good outcome is 0.524 / 0.452 = 1.16. The OR (1.34) inflates the RR (1.16). Absolute Benefit (Absolute Increase in Good Outcome) = 0.524 - 0.452 = 0.072 (7.2 percentage points). NNT for one additional patient to achieve mRS 0-1 = 1 / 0.072 = 14.

Safety translation from the raw counts: control harm risk = 1/403 = 0.00248; treatment harm risk = 10/418 = 0.02392. The absolute risk increase is approximately 0.0214 (2.14 percentage points), and the NNH is approximately 47 over 90 days. Because there were only 11 sICH events, the relative estimate is very imprecise, as its wide confidence interval shows.

Synthesis: In the trial average, treating 100 eligible patients with alteplase between 3 and 4.5 hours corresponded to about 7 additional excellent functional outcomes and about 2 additional symptomatic intracranial hemorrhages. Those outcomes differ in severity and cannot be valued by a simple 7:2 count alone. The NNT of 14 is an average over the enrolled population and treatment times. Do not infer a time-specific NNT within the window without time-by-treatment-effect evidence and an appropriate model.

## Pitfalls and Failure Modes

Failure Mode 1: Reporting RRR without control risks. Abstracts frequently declare a '33% reduction in stroke.' Without the baseline risk, this is a mathematically void statement designed for marketing. A 33% reduction from 3% to 2% yields an ARR of 1% (NNT 100). A 33% reduction from 30% to 20% yields an ARR of 10% (NNT 10). Reject any presentation or protocol that relies solely on relative percentages.

Failure Mode 2: Misinterpreting Odds Ratios as Risk Ratios. As detailed heavily in this chapter, this error structurally exaggerates efficacy when outcomes are common (such as mRS 0-2). Always verify the metric. If an OR is provided for an outcome with an incidence >10%, extract the raw counts and calculate the absolute risk difference directly.

Failure Mode 3: Prediction is not Causation. You cannot calculate an actionable NNT from an observational registry simply by taking the absolute risk difference between treated and untreated groups. Observational data encode confounding. The treated group may have a lower risk because they were younger, had less severe strokes, or had better baseline collateral flow (confounding by indication). Unless robust causal inference techniques (e.g., inverse probability weighting, instrumental variables, target trial emulation) have successfully isolated the causal effect, an observational ARR is merely an association. Inverting an observational association yields a mathematically invalid NNT.

Failure Mode 4: Ignorance of Time Horizons. Cox models generate Hazard Ratios that integrate the effect over the entire follow-up period. Generating an ARR by subtracting cumulative Kaplan-Meier estimates at a specific landmark (e.g., 5 years) requires understanding that the NNT applies strictly to that 5-year boundary. Extrapolating NNTs assuming linear risk accumulation over time is flawed because neurological hazard functions are non-linear (e.g., stroke recurrence is heavily front-loaded in the first 14 days).

## Clinical and Epidemiologic Notes in Stroke Neurology

Note 1: The Illusion of Constant Relative Effects. Epidemiologists model relative risk as constant across subgroups out of mathematical convenience, not biological certainty. When calculating local ARRs based on trial RRs, we assume the RR is transportable. If the biological mechanism of effect differs in your local population (e.g., treating intracranial atherosclerosis versus extracranial cardioembolism), the RR itself may shift, invalidating the ARR calculation.

Note 2: Interaction on Additive versus Multiplicative Scales. Subgroup analysis frequently relies on testing for statistical interaction. Most software tests for interaction on the multiplicative scale (checking if the RR differs between groups). However, for clinical practice, interaction on the additive scale (checking if the ARR differs between groups) is far more important. Two subgroups can have identical RRs but drastically different ARRs if their baseline risks differ. A non-significant multiplicative interaction test does not mean the absolute benefits are identical across subgroups. Always evaluate subgroup differences based on absolute risk reductions.

Note 3: Thrombectomy and the NNT. In the [HERMES individual-patient meta-analysis](https://doi.org/10.1016/S0140-6736(16)00163-X), the common odds ratio for a better 90-day mRS category was 2.49, and the reported number needed to treat for at least a one-category mRS improvement was 2.6. That is not an NNT for functional independence. In the pooled data, mRS 0–2 occurred in 46.0% versus 26.5% (crude difference 19.5 points; reciprocal 5.1, or an integer NNT of 6 when rounded up). Every NNT must name its outcome, horizon, analysis, and population; do not transport it unchanged to a different core size, time window, or physiologic state.

## Cross-Links to Other Chapters

Chapter 9 (Prediction Models): Details how to calculate personalized baseline risks (p_c) using validated scoring systems, which serves as the foundation for individualized ARR calculations.

Chapter 10 (Systematic Reviews and Meta-Analysis): Discusses how to pool relative effects across multiple trials while recognizing heterogeneity and transportability limits.

Chapter 11 (Outcomes and Time-to-Event Data): Provides a deeper dive into the mechanics of the Cox proportional hazards model, the proportional hazards assumption, and Kaplan-Meier estimation.

## Chapter Summary

Relative measures (RR, OR, HR) describe different proportional contrasts. Their stability across populations is an empirical assumption, not a mathematical property, and none conveys clinical impact without a baseline risk and time horizon. For a binary causal risk-ratio estimand at a fixed horizon, risk difference = p_c × (1 − RR); an OR or HR cannot generally be substituted into that formula. ARR/ARI and NNT/NNH should therefore be computed from compatible group-specific risks or survival/cumulative-incidence estimates, with uncertainty and horizon stated.

Confidence intervals must be interpreted as continuous gradients of data compatibility, evaluated against a Minimal Clinically Important Difference (MID), rather than dichotomized around zero. P-values measure statistical surprise, not effect size, and should be relegated below point estimates and precision in any serious appraisal. Mastering the translation of relative metrics into absolute, time-bound natural frequencies is the defining skill of a mathematically literate neurologist.

## Practice & Reflection Prompts

1. Select a randomized antithrombotic trial. Extract group-specific fixed-horizon event risks (or survival/cumulative-incidence estimates), calculate the absolute risk difference and NNT, and explain why the HR alone is insufficient.

2. Using the same trial, calculate the ARI and NNH for major hemorrhage. Draft a two-sentence natural frequency statement comparing the absolute benefits and harms.

3. Explain mathematically why an Odds Ratio of 0.65 for a common outcome (e.g., 50% baseline incidence) cannot be interpreted as a 35% relative risk reduction.

4. A trial reports an ARR of 1.5% with a 95% CI of [0.1%, 2.9%]. If your clinical MID for this costly intervention is 3.0%, how do you interpret these results? Is the trial 'positive'?

5. Why does an NNT of 15 for endovascular thrombectomy in a late-window trial not apply to a patient with a baseline ASPECTS of 2?

6. Describe a scenario where interaction exists on the additive scale (different ARRs) but not on the multiplicative scale (same RR).

7. A registry study reports an absolute risk reduction of 4% for a new procedure compared to medical management. Why can you not invert this to an NNT of 25?

8. Find a trial where the p-value is > 0.05, but the upper limit of the confidence interval includes a massive absolute benefit. Why is it incorrect to conclude the treatment is ineffective?

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
