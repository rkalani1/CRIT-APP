# Chapter 20. Regression and Survival Analysis: Literacy for Paper Readers

## Opening

![Noncollapsibility sketch.](../assets/figures/fig67_noncollapsibility.png)

*Odds ratios and hazard ratios can shift when covariates are added even without any confounding — noncollapsibility, not bias.*

![Table 2 fallacy.](../assets/figures/fig55_table2_fallacy.png)

*The Table 2 fallacy reads every adjusted coefficient as a causal effect; only the exposure of interest was designed to be interpreted that way.*

![Time-to-event: events versus censoring.](../assets/figures/swarm_ch20_survival.png)

*Survival models weigh events against censoring over time; translate the hazard ratio into absolute risks at a horizon patients care about.*

A Cox model dump fills the supplement. Translate hazards into absolute risks over a clinically meaningful horizon before teaching the result.


## Mapping Clinical Outcomes to Regression Models

Regression quantifies conditional associations between an outcome and modeled predictors. It does not isolate a causal effect merely because covariates are included; causal interpretation additionally requires a defined estimand, an identifying design and adjustment set, correct temporal ordering, and adequate model specification. Choose the model and effect measure to match the outcome, time structure, and target question.

Linear regression models a continuous outcome’s conditional mean. Interpreting its coefficient requires a correctly specified mean structure and adequate control of confounding for the intended question; independent observations and appropriate variance estimation are also important. Normally distributed residuals are needed for some exact small-sample inference, not for unbiased ordinary-least-squares coefficients. Skewed outcomes may call for a transformation, robust inference, or a generalized model, depending on the estimand and residual behavior.

Logistic regression is employed for binary outcomes, modeling the log-odds of the event. Classic neurological applications include 90-day modified Rankin Scale dichotomies (e.g., mRS 0-2 vs. 3-6), symptomatic intracerebral hemorrhage, or 30-day readmission. The output is an odds ratio (OR). A frequent analytical failure is the misinterpretation of the OR as a risk ratio, particularly when the outcome is common. An OR of 3.0 for a rare event approximates a threefold increase in risk; for an event with a 40% baseline prevalence, an OR of 3.0 corresponds to a far smaller absolute risk increase.

Cox proportional hazards regression models time-to-event data. It is indicated when both the occurrence of an event and the timing of that event are clinically relevant, such as time to recurrent stroke, post-stroke epilepsy, or death. Unlike logistic regression, which treats all outcomes occurring within a fixed window as equivalent, Cox models account for varying lengths of follow-up and right-censoring.

## Survival Curves, Censoring, and Longitudinal Follow-Up

Right-censoring occurs when follow-up ends before the event is observed because of study completion, loss to follow-up, or withdrawal. Standard survival methods use each participant's event-free information up to censoring and require an appropriate independent-censoring assumption, often conditional on modeled covariates. If participants at higher event risk disproportionately drop out, Kaplan–Meier can overestimate event-free survival and underestimate cumulative incidence; more generally, direction depends on outcome coding and the censoring mechanism.

The Kaplan-Meier estimator provides a non-parametric method to plot the survival function over time, yielding the classic stair-step survival curve. Each vertical drop represents the occurrence of the primary event. Tick marks on the curve typically indicate censoring times. Readers must critically inspect the number at risk provided beneath the plot; confidence intervals widen drastically as the remaining at-risk pool shrinks. Large apparent separations at the tail of a Kaplan-Meier curve, driven by a handful of remaining subjects, should be viewed with extreme skepticism.

Competing risks require an estimand-specific analysis. A cause-specific Cox model may legitimately censor competing deaths to estimate the cause-specific hazard, but treating those deaths as ordinary censoring and then using 1 − Kaplan–Meier as the event probability overestimates cumulative incidence. Use an Aalen–Johansen cumulative-incidence estimate for absolute risk, with cause-specific or Fine–Gray regression when covariate effects on the corresponding scale are the target.

## Deconstructing the Hazard Ratio

The Cox model estimates a hazard ratio (HR), comparing instantaneous hazards among people still event-free and at risk. A hazard is a rate limit, not a probability or fixed-horizon risk. Under a proportional-hazards model, HR 0.50 means the modeled treatment hazard is half the comparator hazard at each time; translating that contrast to an absolute risk requires the baseline hazard, competing-event strategy, and time horizon.

The standard Cox model assumes a constant covariate hazard ratio over follow-up. When effects vary over time—for example, early procedural harm followed by later benefit—a single constant HR is a model-dependent average that can obscure both phases. Check proportional-hazards diagnostics, then report clinically meaningful landmark risks and consider time-varying coefficients, piecewise effects, flexible survival models, or restricted mean survival time according to the question.

## Model Assumptions and the Table 2 Fallacy

Regression models are engines for statistical adjustment, but they cannot manufacture causal inference from inherently flawed observational data. A multivariable model isolates the association of an exposure with the outcome, conditional on the other variables in the model. This is distinct from isolating the true causal effect. If unmeasured confounders exist, or if the investigators inappropriately adjust for colliders or intermediates in the causal pathway, the resulting adjusted coefficient will remain biased.

The Table 2 fallacy occurs when every coefficient in one adjusted model is interpreted causally. Adding subsequent symptomatic hemorrhage to a treatment-outcome model conditions on a post-treatment variable: it changes the question away from the total effect and may also induce selection bias. The treatment coefficient represents a controlled direct effect only under additional causal and modeling assumptions. Each exposure requires its own estimand and adjustment strategy; even the prespecified primary coefficient is causal only if its design and identification assumptions are defensible.

## Critical Appraisal Checklist for Regression Models

When evaluating a clinical stroke paper that heavily relies on multivariable regression, apply the following rigorous checks:

- Verify Model Appropriateness: Does the model match the outcome? (Linear for continuous, Logistic for binary, Cox for time-to-event).
- Assess Information Relative to Complexity: Count candidate parameters, not just named variables, and assess event frequency, anticipated model fit, penalization, shrinkage, and target precision. A fixed 10–15 events-per-variable threshold is not a universal sample-size rule.
- Demand Absolute Metrics: Never accept an isolated OR or HR. Require absolute risk differences, numbers needed to treat (NNT), or marginal predicted probabilities.
- Check the Proportional Hazards Assumption: If a Cox model is used, did the authors explicitly test for and report PH compliance?
- Scrutinize Censoring: In survival analyses, is the drop-out rate acceptable, and is there evidence that censoring is non-informative?
- Identify Competing Risks: For time-to-event outcomes in populations with high mortality (e.g., severe stroke), were competing risks properly modeled?
- Avoid the Table 2 Fallacy: Refuse to interpret the adjusted coefficients of structural covariates as independent causal effects.


## Chapter summary

Statistical literacy for modern neurology requires the ability to deconstruct linear, logistic, and Cox regression models. Linear regression models a conditional mean, logistic regression models binary outcomes on the odds scale, and Cox regression models an instantaneous event rate ratio. Time-to-event analyses require non-informative censoring, either unconditionally or conditional on the modeled covariates. When proportional hazards is not credible, a constant Cox HR is difficult to interpret rather than automatically invalid; use diagnostics and an estimand that represents the time-varying effect or absolute survival difference. Readers should also avoid the Table 2 fallacy and demand absolute-risk estimates to supplement relative regression outputs.

## Practice and reflection

1. A study reports a hazard ratio of 0.60 for a new antiplatelet agent in preventing recurrent stroke over 5 years. The Kaplan-Meier curves cross at 6 months. Critique the reporting of a single HR for this cohort.
2. Explain why right-censoring a patient who drops out of a stroke rehabilitation trial due to severe depression violates the assumption of non-informative censoring.
3. Contrast the interpretation of a beta coefficient of -2.5 in a linear regression model of length-of-stay versus an odds ratio of 2.5 in a logistic model of 90-day mortality.
4. A paper's Table 2 shows that 'intensive blood pressure control' and 'discharge to a skilled nursing facility' both have significant adjusted ORs for poor 90-day outcome. Why is it an error to interpret the SNF coefficient as a causal effect?
5. Identify the appropriate regression model for an analysis where the outcome is time to first unprovoked seizure following a spontaneous intracerebral hemorrhage, accounting for patients who die before experiencing a seizure.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
