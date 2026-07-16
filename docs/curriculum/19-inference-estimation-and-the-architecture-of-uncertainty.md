# Chapter 19. Inference, Estimation, and the Architecture of Uncertainty

## Opening

![CI width versus n.](../assets/figures/fig43_ci_width_n.png)

*CI width versus n.*

![Estimation and confidence intervals.](../assets/figures/fig21_estimation_ci.png)

*Estimation and confidence intervals.*

![Estimation culture: confidence intervals against MID.](../assets/figures/swarm_ch19_estimation_ci.png)

*Estimation culture: confidence intervals against MID.*

A CI is reported as 0.82-1.01 for a secondary endpoint. Before calling the trial negative or positive, separate estimation from dichotomania and read the absolute scale.


## The Pathology of Dichotomania in Clinical Research

Neurologic literature remains deeply afflicted by dichotomania—the compulsive categorization of continuous evidence into 'positive' or 'negative' bins based on an arbitrary mathematical boundary, typically alpha = 0.05. This cognitive distortion causes clinicians to equate a p-value of 0.04 with definitive truth and a p-value of 0.06 with statistical noise. The reality is that chance is a continuous threat to precision, and treating inferential statistics as a categorical verdict fundamentally misunderstands the architecture of uncertainty.

Statistical inference is an exercise in estimation, not adjudication. The goal of a clinical trial is not to prove that an effect is exactly zero or not zero, but to estimate the magnitude of the effect and quantify the precision of that estimate. By elevating the p-value above the confidence interval, readers systematically ignore the clinical importance of the point estimate and the plausible range of alternative truths contained within the data. A rigorously designed but imprecise study of absolute benefits is infinitely more useful for patient care than a highly significant, massively confounded artifact.

- Random error (chance) affects precision; systematic error (bias) corrupts validity.
- Hypothesis testing cannot rescue invalid estimates derived from confounded data.
- A 'nonsignificant' result does not prove equivalence or absence of effect.
- A 'statistically significant' result does not establish biologic importance or causal truth.

## Sampling Variation and the Illusion of Replication Failure

Assume a fixed, universal truth: a specific neuroprotectant reduces 90-day mortality by exactly 4.0 percentage points. If we were to theoretically execute 100 identical trials, each enrolling 300 patients from the exact same population, the observed risk differences would not uniformly be 4.0 percent. The estimates would scatter around the true value, yielding results like 1.2 percent, 7.8 percent, and perhaps −0.5 percent. This scatter is sampling variation. It is the inevitable consequence of measuring a sample rather than a census.

When two legitimate stroke trials report divergent point estimates, sampling variation is one possible explanation alongside differences in design, population, treatment delivery, measurement, and bias. Precision depends strongly on information and event count, not simply the total denominator. Compare studies with an explicit estimate and confidence interval for the between-study difference or a synthesis model; visual overlap of separate confidence intervals is not a formal heterogeneity test.

## Estimation Culture and Confidence Interval Interpretation

The standard error (SE) is the foundational metric of precision, approximating the standard deviation of the sampling distribution for a given statistic. It measures how wildly our estimate would fluctuate upon repeated sampling. A confidence interval (CI) operationalizes the standard error. For a 95% Wald interval, we essentially take the point estimate and extend roughly 1.96 standard errors in both directions. The frequentist definition of a 95% CI—that 95% of such intervals computed over infinite repetitions will capture the true parameter—is mathematically correct but clinically sterile.

For appraisal, adopt the compatibility interpretation: the confidence interval delineates the spectrum of effect sizes that are reasonably compatible with the observed data, conditional on the statistical model and its assumptions being flawless. Values clustered near the point estimate are highly compatible; values at the extreme limits are marginally compatible; values outside the interval are highly incompatible. This framework immediately neutralizes dichotomania.

Under estimation culture, an absolute risk reduction (ARR) of 3.0% (95% CI, −1.0% to 7.0%) is never dismissed as 'negative.' It is accurately characterized as structurally imprecise data compatible with both a clinically vital 7.0% absolute benefit and a trivial 1.0% absolute harm. Conversely, an ARR of 0.2% (95% CI, 0.1% to 0.3%) is statistically significant but clinically microscopic. Decision-making requires overlaying the interval against the minimum clinically important difference, not just the null value.

*Teaching figure (synthetic).* Interval A rules out both the null and an MCID miss—actionable if valid. Interval B is “nonsignificant” yet compatible with large benefit *and* small harm—imprecise, not negative. Interval C is significant but clinically tiny. Interval D keeps harm on the table. Dichotomania at p = 0.05 collapses these four distinct decision problems into two useless bins.

```
THE ESTIMATION HEURISTIC
------------------------
1. Identify the point estimate on the absolute scale.
2. Identify the bounds of the 95% CI.
3. Locate the null value (0 for differences, 1 for ratios).
4. Locate the minimum clinically important difference (MCID).
5. Determine compatibility: Does the CI include the MCID? The null? Meaningful harm?
6. Conclude: Is the precision sufficient to alter clinical pathways, assuming zero bias?
```

## The P-Value: Mathematical Reality Versus Clinical Fiction

The p-value is perhaps the most chronically misunderstood metric in biomedicine. Formally, it is the probability of observing a test statistic at least as extreme as the one calculated, assuming that the null hypothesis is true and that all background assumptions of the statistical model are perfectly met. It is fundamentally a measure of data surprise under a highly specific, often implausible scenario (the sharp null).

The p-value does NOT represent the probability that the null hypothesis is true. It does NOT represent the probability that the finding is a 'fluke.' It provides absolutely no information regarding the magnitude, clinical relevance, or causal reality of the estimated effect. A p-value of 0.001 in an administrative database of five million patients can comfortably correspond to an effect size so minuscule it is irrelevant to human health. Conversely, a p-value of 0.15 in a trial of 80 patients may obscure a massive therapeutic signal drowning in random error.

When authors state 'there was no difference between groups (p = 0.30)', they overstate what the test establishes. The study did not reject the null under the specified test; inspect the effect estimate and confidence interval to distinguish compatibility with negligible effects from substantial imprecision. A large p-value does not confirm that the true effect is zero.

## Type I Errors, Type II Errors, and the Misuse of Power

In the Neyman-Pearson framework of hypothesis testing, a Type I error (alpha) occurs when a true null hypothesis is incorrectly rejected—a false positive. A Type II error (beta) occurs when a false null hypothesis fails to be rejected—a false negative. Statistical power (1 - beta) is the pre-study probability that the trial will successfully reject the null, assuming the true effect size is exactly as specified in the design phase.

Crucially, power is an architectural tool used before data collection to size the cohort. Once the data are collected and the confidence interval is calculated, power becomes entirely irrelevant for interpreting the results. Calculating 'post hoc power' using the observed effect size is a mathematical tautology that merely repackages the p-value; a non-significant p-value will unconditionally yield low post hoc power. If a trial fails to cross the alpha threshold, do not dismiss it as 'underpowered'—a term that implies the treatment works but the sample was too small. Instead, analyze the confidence interval to determine if the trial's precision formally excludes meaningful clinical benefit.

## The Multiplicity Penalty: Subgroups and Secondary Endpoints

If an investigator executes 20 independent tests under true null hypotheses at α = 0.05, the probability of at least one false positive is 1 − 0.95^20 ≈ 64%, not 100%. Correlation among tests changes that value, but unadjusted secondary endpoints and subgroups still inflate the family-wise error rate. Pre-specification and an appropriate multiplicity strategy—such as a testing hierarchy, alpha allocation, or a justified adjustment—are therefore essential.

Subgroup analyses are notoriously vulnerable. An overall trial may be flat, but the investigators discover a 'significant' benefit in right-sided occlusions treated between 3 and 4.5 hours. Without a formal test for interaction demonstrating that the treatment effect genuinely differs across the stratum, such findings are overwhelmingly likely to be statistical illusions born of sampling variation in tiny strata. Treat exploratory subgroup findings as hypotheses requiring independent replication, never as actionable clinical directives.

## Absolute Effects and the Arithmetic of NNT

Relative effects sometimes appear more stable than absolute effects across risk strata, but that stability is empirical—not mathematical—and must be justified in the target population. Odds ratios and hazard ratios are not fixed-horizon risk ratios and cannot be multiplied directly by baseline risk. Clinical translation should therefore report endpoint- and horizon-specific absolute risks, with uncertainty, rather than assuming a relative estimate transports unchanged.

The Number Needed to Treat (NNT = 1 / ARR) translates absolute probability into a frequency format. However, NNT point estimates presented without confidence intervals project a false certainty. When computing a confidence interval for an NNT based on an ARR interval that crosses zero, the math becomes non-linear and fractures through infinity. An ARR CI of −1.0% to 5.0% translates to an NNT interval encompassing benefit (NNT 20 down to infinity) and harm (Number Needed to Harm [NNH] of 100). Therefore, expressing the uncertainty primarily through absolute risk differences (e.g., 'between 1 more and 5 fewer events per 100 patients') is far more transparent than manipulating disjointed NNT ranges.

## Manual Derivation: Exposing the Inferential Machinery

To demystify the black box of statistical software, we manually derive a risk difference and its confidence interval. Consider a hypothetical trial evaluating a neuroprotectant against standard care. The outcome is mortality at 90 days.

```
OBSERVED DATA
-------------
Control Group (R0): 45 deaths / 250 patients = 0.180 (18.0%)
Treatment Group (R1): 30 deaths / 250 patients = 0.120 (12.0%)

ESTIMATES
---------
Absolute Risk Reduction (ARR) = R0 - R1 = 0.180 - 0.120 = 0.060 (6.0%)
Point NNT = 1 / 0.060 = 16.7

STANDARD ERRORS (SE = sqrt[ p*(1-p) / n ])
---------------
SE(R0) = sqrt[ 0.180 * 0.820 / 250 ] = sqrt[ 0.0005904 ] = 0.0243
SE(R1) = sqrt[ 0.120 * 0.880 / 250 ] = sqrt[ 0.0004224 ] = 0.0206

SE(ARR) = sqrt[ SE(R0)^2 + SE(R1)^2 ]
SE(ARR) = sqrt[ 0.0005904 + 0.0004224 ] = sqrt[ 0.0010128 ] = 0.0318

95% CONFIDENCE INTERVAL (ARR +/- 1.96 * SE)
-----------------------
Margin of Error = 1.96 * 0.0318 = 0.0623
95% CI = 0.060 +/- 0.0623
95% CI = -0.0023 to 0.1223 (-0.2% to 12.2%)
```

This calculation yields an estimated 6.0-percentage-point benefit with a 95% CI from 0.2 points of harm to 12.2 points of benefit. The interval is compatible with effects from trivial harm to substantial benefit and does not exclude the prespecified clinically important benefit. A confidence interval is not, by itself, a likelihood ranking over every enclosed value. Decisions about further study should consider the full compatibility or likelihood profile, prior evidence, feasibility, and clinical value rather than labeling the study simply “positive” or “negative.”


![Calibration plot comparing predicted and observed risk by decile against the ideal 45-degree line.](../assets/figures/fig64_calibration_deciles.png)

*Teaching graphic (fig64_calibration_deciles.png).*

## Chapter summary

Statistical inference in neurology must abandon the binary constraints of hypothesis testing in favor of continuous parameter estimation. Sampling variation dictates that repeated observations of a true phenomenon will yield disparate point estimates; confidence intervals quantify this structural scatter. P-values assess the surprise of the data under a strict null hypothesis, failing entirely to measure the magnitude or clinical reality of an effect. Concepts like statistical power and Type I/II errors are architectural tools for trial design, utterly devoid of utility for interpreting post-hoc findings. Unregulated multiplicity in subgroups and secondary endpoints severely degrades evidentiary integrity. Absolute effects, particularly the Absolute Risk Reduction, must anchor clinical interpretation, as relative measures inherently camouflage the magnitude of patient-level impact. The ultimate mandate of appraisal is prioritizing validity over precision: an infinitely narrow confidence interval surrounding a structurally biased estimate is nothing more than a precise lie.

## Practice and reflection

1. Calculate the absolute risk reduction, the standard error of the difference, and the 95% confidence interval for a hypothetical trial where Control mortality is 22% (N=400) and Treatment mortality is 18% (N=400).
2. Draft a formal critique of a peer-reviewed abstract that concludes a neuroprotectant 'does not work' based strictly on a primary endpoint p-value of 0.07.
3. Differentiate between the mathematical definition of a frequentist 95% confidence interval and the clinical application of the 'compatibility interval' framework.
4. Examine a recent endovascular trial and catalog all unadjusted secondary endpoints and subgroup analyses; calculate the probability of at least one false positive assuming a family-wise null.
5. Translate a relative risk of 0.60 (95% CI, 0.45-0.85) into absolute risk reductions assuming a baseline event rate of 2%, and again assuming a baseline event rate of 25%. Discuss the divergent clinical imperatives.
6. Articulate the logical fallacy of calculating 'post hoc power' for an primary endpoint that failed to achieve statistical significance.
7. Explain the non-linear discontinuity that occurs when attempting to calculate a Number Needed to Treat (NNT) confidence interval derived from an ARR interval that crosses the null.
8. Construct an argument for why a highly significant p-value (p < 0.001) in an observational registry of 500,000 patients provides functionally zero evidence of a causal relationship.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
