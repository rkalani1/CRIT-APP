# Chapter 11. Stroke Outcomes: mRS, Time-to-Event, and Competing Risks

## Opening
![mRS ordinal ladder.](../assets/figures/crit_fig_mrs_ladder.png)

*The modified Rankin Scale is an ordinal ladder of disability; where you cut it — 0–1, 0–2, or a full ordinal shift — changes whether an effect looks large or trivial.*


Outcome debate: mRS shift vs dichotomized independence vs home-time. Wrong endpoint can make a small effect look revolutionary—or hide disability that patients care about.


## Conceptual Core: Outcomes Encode Values and Statistical Power

Stroke research lives and dies by its endpoints. An intervention's success or failure is never an absolute truth; it is strictly conditional on the mathematical structure of the outcome variable chosen by the investigators. A neuroprotective trial can be deemed a massive success if disability is coded as modified Rankin Scale (mRS) 0-2 versus 3-6, yet utterly fail if the threshold is shifted to mRS 0-1 versus 2-6. Similarly, whether recurrent stroke is analyzed with death as a censoring event or as a competing risk fundamentally alters the absolute incidence reported to patients. Outcome choice is therefore both a profound values judgment and a strict methodologic design choice. Critical appraisal without endpoint literacy is merely cargo-cult evidence-based medicine: you will correctly recite intention-to-treat protocols and blinding checklists while entirely missing the fact that the primary endpoint is mathematically incapable of answering the clinical question at hand.

We must establish a fundamental epistemological boundary: prediction is not causation. Throughout this chapter and all subsequent analyses, remember that predicting a patient's 90-day mRS using their baseline NIH Stroke Scale (NIHSS) is an exercise in pattern recognition. In contrast, estimating the causal effect of tenecteplase on that same 90-day mRS requires evaluating counterfactuals—the difference between what happened and what would have happened under a different treatment assignment. You cannot intervene on baseline variables like age or initial infarct volume. Predictive models are optimized for accuracy regardless of mechanism, whereas causal inference is optimized to isolate the exact, unconfounded effect of an intervention. Confusing these two frameworks leads to lethal errors in clinical trial interpretation, such as adjusting for post-randomization variables or interpreting hazard ratios as direct causal parameters.

To formalize outcome definitions, modern clinical trialists rely on the ICH E9(R1) estimand framework. An estimand specifies the treatment conditions being compared, target population, outcome variable, handling of intercurrent events, and population-level summary measure. Ambiguity in any attribute can make the target and analysis difficult to interpret. Three common outcome paradigms in neurology are ordinal functional scales, time-to-event survival models, and competing-risk frameworks.

## The Modified Rankin Scale: Psychometrics, Measurement, and Hiding the Truth

The modified Rankin Scale (mRS) is the dominant functional outcome measure in stroke neurology. It ranges from 0 (no symptoms) through 5 (severe disability, bedridden, requiring continuous nursing care) to 6 (death). It is critical to understand that the mRS is a global scale of disability and societal participation, not a pure neurological impairment scale like the NIHSS. A patient with a devastating hemianopia might score a 2 or 3 on the mRS if they adapt and successfully manage their affairs, whereas the NIHSS would strictly penalize the visual field deficit. The strengths of the mRS are its global clinical interpretability, its historical continuity across decades of major trial programs (from NINDS rt-PA to the modern endovascular thrombectomy era), and its focus on holistic patient independence rather than isolated neuroanatomical deficits.

The mRS is ordinal, not interval-scaled: the human and clinical distance between adjacent categories is not constant. Patients and families can value the same transition differently, and residence is not determined by mRS alone. Utility-weighted mRS approaches assign numerical values to categories, but those weights depend on the population and elicitation method and should be reported rather than assumed universal.

Furthermore, incorporating death as category 6 creates a statistical singularity. Death is an absorbing state that permanently terminates all functional assessment. Placing it on the identical continuum as functional disability forces the scale to model a joint distribution of survival and morbidity. A therapy that successfully prevents death but leaves all salvaged survivors bedridden (mRS 5) shifts the distribution from 6 to 5. Mathematically, this is an improvement on the ordinal scale. Clinically and ethically, many families would view prolonged survival in a permanently bedridden state as a fate equal to or worse than death. You must always inspect the mortality rate independently of the functional shift.

Ascertainment bias is the final peril of the mRS. Unstructured bedside interviews yield dismal inter-rater reliability, with kappa statistics frequently hovering around 0.4. Blinding is absolutely essential. In open-label endovascular or surgical trials, unblinded assessors frequently, albeit unconsciously, nudge patients across the primary dichotomy boundary (e.g., from an mRS 3 to an mRS 2) based on implicit therapeutic optimism. Rigorous trials must utilize structured instruments like the mRS-9q or the Rankin Focused Assessment (RFA) and employ central adjudication of video-recorded interviews to defend against systemic detection bias.

## Dichotomized mRS: Mathematical and Clinical Casualties

Historically, stroke trials collapsed the 7-level ordinal mRS into a binary outcome—most commonly 'good' (0-1 or 0-2) versus 'poor' (2-6 or 3-6) recovery. The advantages of this approach are simplicity of communication and the ability to easily calculate absolute risk reductions and Numbers Needed to Treat (NNT). The disadvantages are severe. Dichotomization throws away immense amounts of statistical variance. Mathematically, dichotomizing a continuous or finely graded ordinal variable at the median discards approximately 36 percent of the statistical information, which is computationally equivalent to throwing away a third of your enrolled patients. If the cutpoint is extreme (e.g., mRS 0-1), the power loss is even more catastrophic in severe stroke cohorts.

Cutpoint choice directly affects interpretation. A treatment that shifts patients from mRS 4 (unable to walk or attend to bodily needs without assistance) to mRS 3 (requires some help but walks without assistance) can produce little or no difference at an mRS 0–2 dichotomy even though the ordinal change matters. Inspect the full category distribution instead of equating one cut point with the entire treatment effect.

Using Odds Ratios (OR) for dichotomized outcomes when the event is common drastically overstates the clinical effect. If the control group achieves mRS 0-2 at a rate of 30 percent, and the treatment group achieves it at 40 percent, the Absolute Risk Reduction (ARR) is 10 percent, yielding an NNT of 10. The Risk Ratio (RR) is 40/30 = 1.33, a 33 percent relative increase in good outcomes. However, the Odds Ratio is (0.4/0.6) / (0.3/0.7) = 1.55. If this OR is naively communicated to the press or a patient as a '55 percent relative improvement in risk', it constitutes statistical malpractice. Always prefer absolute effects (ARR, NNT, NNH) over relative effects. Relative measures mask the baseline risk, making a 1 percent vs 2 percent difference look identical to a 40 percent vs 80 percent difference.

Finally, dichotomy shopping is a fatal threat to type I error control. If investigators pre-specify mRS 0-1, review the data, fail to achieve statistical significance, and subsequently publish the trial highlighting mRS 0-2 as a 'post-hoc responder analysis', they have invalidated the trial's inferential integrity. Rigorous appraisal requires verifying that the published primary endpoint matches the clinicaltrials.gov registration exactly.

*Teaching figure (synthetic).* The left panel moves substantial mass from mRS 4 to mRS 3; the right panel collapses the same data at the conventional mRS 0–2 cut point and nearly extinguishes the risk difference. Residence may change for some patients but depends on support and context, not the mRS score alone.

## Shift Analysis and the Proportional Odds Assumption

![Modified Rankin Scale distributions before and after an ordinal shift.](../assets/figures/fig30_mrs_shift.png)

*Shift analysis uses the full outcome distribution instead of discarding information at a single cut point.*

To avoid the catastrophic information loss of dichotomization, modern acute stroke trials (e.g., IST-3, MR CLEAN, EXTEND-IA TNK) utilize ordinal shift analyses. A shift analysis asks a holistic question: does the intervention improve the entire distribution of functional scores across all levels of the mRS? The standard statistical engine for this is Proportional Odds Logistic Regression (POLR). Rather than fitting a single logistic curve, POLR fits a series of parallel curves for every possible cumulative cutpoint of the mRS.

The fundamental mathematical requirement of POLR is the proportional odds assumption. This assumption dictates that the treatment effect—the odds ratio—must be identical across all possible dichotomous splits of the scale. In formal terms, the odds ratio for achieving an mRS <= 0 versus > 0 must be exactly the same as the odds ratio for achieving mRS <= 1 versus > 1, mRS <= 2 versus > 2, and so on. When this assumption holds, the model yields a single, highly efficient 'common odds ratio'. For example, a common odds ratio of 1.5 implies that, regardless of where you draw the line of 'success' on the mRS, the odds of ending up on the better side of that line are increased by 50 percent.

In clinical reality, the proportional odds assumption frequently fails. Consider a craniectomy trial for malignant MCA infarction. The surgery reliably prevents brain herniation and death, shifting patients from mRS 6 to mRS 4 or 5. However, the surgery does absolutely nothing to repair the destroyed cortex, so it generates zero shifts from mRS 2 to mRS 1. Because the treatment effect is highly concentrated at the severe end of the scale and absent at the mild end, the proportional odds assumption is severely violated. When violated, the common odds ratio reported by the software becomes an uninterpretable, sample-size-weighted average of the cutpoint-specific odds ratios. It obscures the true biological action of the intervention.

Clinical translation rule: Inspect the full mRS distribution, but do not use a stacked-bar visual as a test of proportional odds. Formally assess model fit and proportionality, and use a prespecified alternative estimand or model—such as partial proportional odds, generalized odds, utility-weighted analysis, or a rank-based estimand—when one common odds ratio is inadequate. Applicability to a particular patient still requires attention to enrollment criteria and clinically relevant effect modifiers.

## Quantitative Reasoning: Time-to-Event and Censoring Mechanics

In longitudinal stroke research, predicting whether an event occurs is insufficient; we must measure exactly when it occurs. Time-to-event analysis requires strict formalization of its random variables. Let T denote the true, unobserved time to the clinical event of interest (e.g., recurrent ischemic stroke). Let C denote the true time to censoring (e.g., loss to follow-up, withdrawal, or administrative end of the study). The observable data for each patient consist of the observed follow-up time Y = min(T, C) and the event indicator delta = I(T <= C), where I is the indicator function returning 1 if the event was observed and 0 if the patient was censored.

From these variables, we define the Survival function S(t) = P(T > t), which represents the probability of surviving event-free beyond time t. We also define the Hazard function, lambda(t) = limit as dt approaches 0 of P(t <= T < t + dt | T >= t) / dt. The hazard function represents the instantaneous failure rate at time t, strictly conditional on the patient having survived event-free up to that exact moment. The cumulative hazard is Lambda(t) = integral from 0 to t of lambda(u) du, leading to the fundamental relationship S(t) = exp(-Lambda(t)).

The Kaplan-Meier product-limit estimator calculates the survival curve empirically. At each event time t_i, it multiplies the preceding estimate by (1 - d_i / n_i), where d_i is the number of events and n_i the number at risk just before t_i. Its interpretation requires independent censoring, either marginally or conditional on variables used in a correctly specified analysis. Assess the reasons and timing of censoring rather than assuming censored and observed participants have identical future risk.

Informative censoring can bias a Kaplan-Meier estimate. If deteriorating patients are transferred to hospice and then lost, the observed risk set may become systematically healthier and the event rate may be underestimated. Differential loss raises concern but is not proof of bias; examine reasons and timing, and use justified weighting, modeling, bounds, or sensitivity analyses.

## Hazard Ratios versus Risk Ratios: Interpretative Precision and Causal Bias

The Hazard Ratio (HR) is defined as the ratio of two hazard functions: lambda_treatment(t) / lambda_control(t). Under a Cox proportional hazards model, this ratio is assumed to be constant over the entire follow-up period. In contrast, the Risk Ratio (RR) at a specific time horizon t is the ratio of cumulative failure probabilities: (1 - S_treatment(t)) / (1 - S_control(t)). It is a mathematical certainty that hazard ratios are not risk ratios. An HR of 0.50 does not mean that the absolute number of events is halved, nor does it mean the cumulative risk is halved. It strictly means that the instantaneous rate of events among those currently alive and at risk is halved.

Because later hazards condition on remaining event-free, a conventional hazard ratio is a risk-set contrast and need not equal a marginal causal effect. Its interpretation depends on design, estimand, censoring, competing events, and proportional-hazards assumptions. Differential depletion of susceptible participants can change risk-set composition over time, so pair the hazard ratio with time-specific absolute risks and curves.

Because the hazard at a later time conditions on remaining event-free until that time, a hazard ratio need not have a simple causal interpretation; causal interpretation requires an appropriate design, a clearly defined estimand, and additional assumptions. For bedside counseling, pair any HR with absolute risks at clinically predetermined time horizons. For example: 'At 1 year, the observed risk of recurrent stroke was 12 percent with standard care and 8 percent with the new agent, an absolute difference of 4 percentage points.' Whether that contrast is causal depends on the study design, adherence strategy, censoring, competing events, measurement, and identifying assumptions. Absolute effects are clinically interpretable, but they are not automatically causally identified or transportable.

## Competing Risks: When Death Alters the Estimand

![Competing-event pathways showing how death changes the probability of observing a later nonfatal outcome.](../assets/figures/fig31_competing_risks.png)

*Competing-risk methods separate questions about instantaneous event rates from questions about cumulative incidence.*

A competing risk is formally defined as an event that either precludes the occurrence of the primary event of interest or fundamentally alters the probability of its occurrence. In neurology, death is the ultimate, omnipresent competing risk. When evaluating recurrent ischemic stroke, dementia progression, or post-stroke epilepsy, a patient who dies from a myocardial infarction or systemic sepsis is permanently removed from the pool of individuals who can experience the neurological event.

When competing death is censored, 1 − Kaplan–Meier estimates a net-risk construct under assumptions that remove the competing event; it is not the observed-world cumulative incidence. Reporting it as the probability of recurrent stroke can overestimate that probability in high-mortality cohorts. Use Aalen–Johansen cumulative incidence for absolute real-world risk, while retaining cause-specific models when their hazard-scale estimand answers the question.

![Schematic cumulative-incidence curves for recurrent stroke under treatment and control over 24 months.](../assets/figures/fig59_cuminc_curve.png)

*Illustrative curves, not study data. Cumulative incidence reports absolute risk at a stated horizon; a credible comparison also requires uncertainty and appropriate handling of competing events.*

The cause-specific hazard is the instantaneous event rate among people who are still alive and event-free. It is useful for etiologic and event-process questions and contributes to the cumulative-incidence calculation, but it is not itself an absolute risk.

The Fine–Gray model instead relates covariates to the subdistribution hazard using an extended, censoring-weighted risk set that retains information after competing events. It can support model-based cumulative-incidence estimates; the cumulative incidence function can also be estimated directly with Aalen–Johansen methods. For prognosis and resource planning, report the cumulative incidence at named horizons. Choose cause-specific or subdistribution modeling according to the question, and do not interpret either hazard ratio as a risk ratio.

*Teaching figure (synthetic).* Treating death as ordinary censoring invents an immortal risk set and overstates nonfatal recurrence. Prefer the cumulative incidence function when counseling patients or powering secondary-prevention studies in high-mortality cohorts.

## Fully Worked Example: A Numeric Life Table and Subdistribution Calculation

For a transparent discrete-time illustration, consider 1,000 patients followed in two intervals and assume all events occur at each interval’s end. The event of interest is recurrent ischemic stroke; death before recurrence is competing. Exact continuous-time Kaplan–Meier and Aalen–Johansen estimates require individual event times, so the arithmetic below is an interval approximation.

Interval 1 begins with 1,000 at risk: 40 recurrent strokes and 60 competing deaths leave event-free survival 1 − (40 + 60)/1,000 = 0.900, and recurrent-stroke cumulative incidence 0.040.

Interval 2 begins with 900 alive and event-free: 25 recurrent strokes and 30 competing deaths. Under the stated interval-end convention, the conditional recurrent-stroke probability is 25/900 = 0.02778 and event-free survival through the interval is 1 − 55/900 = 0.93889.

The approximate net-risk calculation that censors deaths is 1 − [(1 − 40/1,000)(1 − 25/900)] = 1 − (0.960 × 0.97222) = 0.06667, or 6.67%.

The approximate observed-world cumulative incidence is 0.040 + 0.900 × (25/900) = 0.0650, or 6.50%.

The 6.67% net-risk construct is slightly higher than the 6.50% cumulative incidence in this synthetic cohort. The gap can be larger when competing mortality is common. Report which estimand was calculated and do not label 1 − Kaplan–Meier as real-world cumulative incidence when competing events are present.

## Composite Endpoints, Net Clinical Benefit, and Stroke-Specific Traps

Trials often bundle outcomes into composites such as nonfatal stroke, nonfatal myocardial infarction, and vascular death. The composite hazard is the sum of component cause-specific hazards, so the composite effect reflects component frequencies, timing, dependence, and treatment effects over evolving risk sets; it is not generally a simple weighted average of component hazard ratios.

A frequent, less important component can dominate a composite even when more serious components show little benefit or possible harm. Interpretability is strongest when components are clinically coherent and effects directionally similar; always report component counts and effects rather than relying on the composite alone.

![Illustrative component frequencies showing how a frequent, less severe event can dominate a composite endpoint.](../assets/figures/fig58_composite_endpoint.png)

*The percentages are synthetic and illustrate relative frequency, not additive incidence: participants and event types may overlap. Inspect each component's importance, timing, and treatment effect.*

Net Clinical Benefit (NCB) frameworks attempt to solve this by mathematically weighing ischemic prevention against hemorrhagic harm. However, these weights are intrinsic value judgments. Is one symptomatic ICH mathematically equal to three minor ischemic strokes, or five? When reading an NCB analysis, you must determine whether the specific utility weights were pre-specified in the protocol and whether sensitivity analyses demonstrate that alternative, equally valid weights would reverse the trial's conclusions.

## Pitfalls and Failure Modes in Stroke Endpoints

- Dichotomy Shopping: Declaring victory on a post-hoc mRS 0-2 dichotomy after the protocol-specified mRS 0-1 primary endpoint fails to achieve statistical significance, destroying type I error control.
- Proportional Odds Blindness: Interpreting a common odds ratio from a shift analysis without visually inspecting the stacked bar charts to verify that the shift occurs at clinically meaningful cutpoints.
- Hazard Ratio as Risk Ratio: Explaining a hazard ratio of 0.70 to a patient as a '30 percent reduction in your total risk of having a stroke', completely conflating instantaneous rates with cumulative probabilities.
- Kaplan-Meier for Nonfatal Events: Utilizing standard Kaplan-Meier survival curves for recurrent stroke or symptomatic hemorrhage in high-mortality cohorts, thereby treating death as independent, non-informative censoring.
- Immortal Time Bias: In observational cohort studies evaluating the timing of interventions (e.g., delayed anticoagulation post-stroke), defining exposure groups such that patients must survive long enough to receive the intervention, guaranteeing a spurious survival advantage for the treated group.
- Crossing Hazards: Applying a standard Cox proportional hazards model to an intervention that causes upfront periprocedural harm but long-term benefit (e.g., carotid stenting versus endarterectomy), yielding a meaningless, time-averaged hazard ratio near 1.0.
- Composite Dilution: Celebrating a positive MACE endpoint when the statistical significance is entirely driven by a reduction in minor, non-disabling events, masking a null or detrimental effect on fatal stroke.
- Prediction Conflated with Causation: Asserting that because baseline infarct volume strictly predicts 90-day mRS, intervening to lower the apparent infarct volume will causally improve the mRS by the exact predictive coefficient.
- Unblinded Ascertainment: Permitting local, unblinded clinical investigators to ascertain 90-day mRS in open-label device trials, injecting severe detection bias at the exact boundary of the primary dichotomy.
- Excluding Dead Patients: Analyzing 'functional outcome among survivors' by dropping mRS 6 from the denominator, creating massive, unresolvable selection bias if the treatment differentially affects mortality.

## Clinical and Epidemiologic Notes

Clinical Note: Bedside Communication. Never use hazard ratios or relative risks during patient counseling. A relative risk reduction of 50 percent sounds staggering, but if the baseline risk is 2 percent, the absolute risk reduction is a negligible 1 percent (NNT = 100). Always convert literature findings into absolute risk differences at strict time horizons. 'Without this medication, your risk of a stroke over the next year is 10 percent. With it, the risk is 6 percent. That means out of 100 people like you, we prevent 4 strokes over exactly one year.' This language is mathematically true and cognitively accessible.

Clinical Note: Discussing mRS Transitions. Anchor category descriptions in function: mRS 4 means unable to walk or attend to bodily needs without assistance; mRS 3 means requiring some help but walking without assistance. Home disposition may change for some patients but depends on caregivers, housing, and services. Present absolute category percentages and avoid converting a score directly into a residence prediction.

Epidemiologic Note: Missing Data Mechanisms. The handling of missing 90-day mRS data depends entirely on the mechanism of missingness. Missing Completely At Random (MCAR) means the missingness is independent of both observed and unobserved data; a simple complete-case analysis is unbiased but inefficient. Missing At Random (MAR) means missingness depends on observed covariates (e.g., older patients drop out more); multiple imputation can recover unbiased estimates. Missing Not At Random (MNAR) means the missingness depends on the unobserved outcome itself (e.g., patients with severe aphasia drop out because they cannot complete the phone interview). MNAR requires complex pattern-mixture models; standard multiple imputation will fail and produce biased estimates.

Epidemiologic Note: Transportability. Neither absolute nor relative effects are automatically transportable. A trial conducted in academic comprehensive stroke centers with an average door-to-needle time of 35 minutes and highly selected participants cannot have its absolute ARR seamlessly transported to a rural critical access hospital. A hazard ratio depends on risk-set composition and the baseline hazard and cannot simply be combined with a local baseline risk to recalculate ARR. Transport fixed-horizon risks or effects only with a justified model and explicit uncertainty.

## Named Framework: The TRIPP-Outcome Appraisal Checklist

To operationalize endpoint literacy on clinical service, utilize the TRIPP-Outcome (Timing, Risk, Incidence, Proportionality, Power) appraisal checklist when reviewing any stroke literature. This framework enforces strict methodologic discipline.

- Timing: Is the outcome assessment schedule biologically appropriate? Does a 90-day mRS fully capture the delayed recovery trajectory for intracerebral hemorrhage, or is administrative censoring artificially truncating the true treatment effect?
- Risk (Absolute): Does the abstract report absolute risk differences and numbers needed to treat (NNT/NNH), or does it hide behind impressive-sounding relative hazard ratios and odds ratios?
- Incidence (Competing): For a nonfatal event with competing death, did the authors report cumulative incidence (for example, Aalen–Johansen)? Cause-specific and Fine–Gray regression answer different questions and should be selected according to the estimand, not treated as interchangeable requirements.
- Proportionality: For ordinal shift analyses, is the proportional odds assumption met? If not, did the authors provide partial proportional odds models or non-parametric rank-based metrics? For time-to-event data, do the Kaplan-Meier curves cross, violating the proportional hazards assumption?
- Power and Precision: Was the trial powered for the specific dichotomy or ordinal shift chosen? If a composite endpoint is used, are the component-specific point estimates directionally consistent with the overarching composite conclusion?
- Intercurrent Events: How exactly are intercurrent events handled according to the ICH-E9(R1) estimand framework? Is death treated as an absorbing state (mRS 6), a competing risk, or erroneously deleted from the analytic dataset?
- Ascertainment Blinding: Was the primary functional outcome assessed by a blinded adjudicator using a structured interview tool (mRS-9q or RFA) to prevent detection bias?

Internalizing this checklist fundamentally alters how you consume medical literature. The phrase 'positive on a shift analysis' becomes an immediate cue to demand the stacked bar charts. The phrase 'significantly reduced recurrent stroke' instantly triggers a mental audit of the competing mortality rate. This rigorous skepticism is the foundation of independent clinical epidemiology.

## Cross-Links to Other Chapters

- Chapters 4–5: Bias taxonomy, causal diagrams, confounding, and target-trial thinking.
- Chapter 6: Randomized-trial estimands, assignment-based analyses, and missing outcomes.
- Chapter 12: Effect sizes, absolute benefit, NNT, and clinical importance.


## Chapter summary

Stroke outcomes encode clinical values and mathematical structure. Dichotomized mRS loses information and depends on the chosen cut point. Ordinal analyses use more of the distribution, but a common-odds interpretation requires model assessment and may need an alternative estimand when proportionality is inadequate. Time-to-event methods require explicit censoring assumptions; hazard ratios compare event rates within evolving risk sets and are not cumulative risk ratios. Death competes with nonfatal endpoints, so report cumulative incidence rather than treating death as ordinary non-informative censoring. Pair model-based relative effects with time-specific absolute risks, uncertainty, and the assumptions needed for causal or bedside interpretation.

## Practice and reflection

1. From the original NINDS rt-PA stroke trial publication, extract the exact mRS distribution data. Calculate the Absolute Risk Reduction and Number Needed to Treat (NNT) for both an mRS 0-1 dichotomy and an mRS 0-2 dichotomy. Explain the clinical implications of the numeric difference.
2. Define immortal time bias. Construct a hypothetical observational study design comparing 'early versus late' decompressive hemicraniectomy for malignant MCA syndrome that structurally guarantees an immortal time bias favoring the late intervention group.
3. A junior colleague states, 'The hazard ratio for recurrent stroke was 0.60, meaning the treatment prevented 40 percent of strokes over two years.' Write a calm, mathematically precise correction distinguishing between instantaneous hazards and cumulative absolute risk.
4. Using the toy life-table example from this chapter, recalculate the 365-day Cumulative Incidence Function for recurrent stroke assuming the number of deaths in Interval 1 increases from 60 to 200. Contrast this new CIF with the correspondingly recalculated naive Kaplan-Meier estimate.
5. Draw a causal Directed Acyclic Graph (DAG) demonstrating informative censoring. Show exactly how an unmeasured variable (e.g., silent clinical deterioration) causing both trial dropout and impending fatal stroke biases the resulting survival estimate.
6. Review the DEFUSE 3 trial's primary endpoint methodology. Identify the specific statistical test used for the ordinal shift analysis. Explain why the authors might have chosen this precise test over a standard proportional odds logistic regression.
7. Define a 'competing risk' using strict epidemiologic terms. Explain precisely why death from pneumonia is a competing risk for evaluating the time to recurrent ischemic stroke, but is NOT a competing risk for evaluating all-cause mortality.
8. You are evaluating a novel neuroprotectant that significantly reduces mortality (shifts mRS 6 to 5) but has absolutely zero effect on mild or moderate disability. Predict how this specific treatment effect will alter the common odds ratio in a proportional odds logistic regression model. Will the single numeric model output adequately capture the true clinical effect?

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
