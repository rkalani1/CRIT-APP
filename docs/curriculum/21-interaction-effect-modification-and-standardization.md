# Chapter 21. Interaction, Effect Modification, and Standardization

## Opening
![Additive vs multiplicative interaction.](../assets/figures/swarm3h_interaction_scales.png)

*Additive vs multiplicative interaction.*


An interaction claim says the drug works only on one scale. Demand which scale, pre-specification, and absolute stratum effects.


## Interaction Versus Confounding: Structural Distinctions

In clinical epidemiology, interaction (effect modification) and confounding represent fundamentally different structural phenomena. Confounding is a form of bias that distorts the marginal estimate of an exposure-outcome relationship. It arises when a third variable is associated with both the exposure and the outcome, necessitating adjustment or weighting to isolate the causal effect. Effect modification, by contrast, describes a scenario where the magnitude or direction of an effect genuinely varies across strata of a third variable. It is a clinical reality to be documented and analyzed, not a bias to be eliminated.

The stroke literature frequently exhibits linguistic and analytical confusion between these concepts, typically manifesting in phrases such as 'we adjusted for interaction.' Proper methodology requires adjusting for confounders to estimate a uniform effect, and stratifying by effect modifiers to report heterogeneous effects. For example, if the recanalization efficacy of a specific stent retriever varies by clot composition (e.g., erythrocyte-rich versus fibrin-rich), clot composition acts as an effect modifier. Averaging the treatment effect across all clot types obscures essential procedural heterogeneity.

## Scale Dependence: Additive and Multiplicative Frameworks

![The same stratum-specific risks summarized on additive and multiplicative interaction scales.](../assets/figures/fig13_interaction_scales.png)

*An interaction can appear on one scale and not another, so the scale must be named before interpretation.*

Interaction is not an absolute property of the data; it is mathematically tethered to the scale of analysis. Two frameworks predominate: the additive scale (evaluating rate or risk differences) and the multiplicative scale (evaluating risk, odds, or hazard ratios). Data demonstrating perfect homogeneity on one scale often exhibit marked interaction on the other. This property routinely complicates the interpretation of trial data where baseline risks vary significantly.

Assume a trial of intensive lipid lowering in secondary stroke prevention yields a relative risk of 0.75 across all investigated subgroups. Multiplicative homogeneity is satisfied. However, if the baseline five-year stroke risk is 20% in patients with severe intracranial atherosclerosis and 8% in patients with cryptogenic stroke, the absolute risk reductions diverge (5.0% versus 2.0%, respectively). Although the multiplicative model detects no interaction, the additive scale demonstrates substantial effect modification.

Standard regression architectures (logistic, Cox proportional hazards) operate by default on the multiplicative scale. When authors report a non-significant interaction p-value, they typically mean the data do not reject multiplicative homogeneity. Relying exclusively on this metric ignores the additive scale, which dictates public health impact, number needed to treat, and bedside risk-benefit tradeoffs. Absolute risk differences govern clinical decisions.

## Methodological Traps in Subgroup Analysis

Subgroup claims in neurovascular literature require rigorous skepticism. Methodological discipline begins with pre-specification. Hypotheses delineated in the statistical analysis plan prior to data unblinding carry evidentiary weight; post-hoc exploratory cuts generate hypothesis-generating observations at best. The probability of falsely identifying a 'significant' interaction scales rapidly with the number of subgroups tested without multiplicity adjustment.

A frequent inferential error involves comparing within-stratum p-values to claim effect modification. Authors might observe a treatment effect in patients under age 70 (p=0.02) and no significant effect in those over age 70 (p=0.15), subsequently declaring age an effect modifier. This logic is mathematically invalid. The correct procedure requires a formal interaction test—an evaluation of the product term between the exposure and the stratifying variable—to determine if the effect sizes significantly differ. Disparate p-values often reflect asymmetrical statistical power across strata rather than biological divergence.

Furthermore, interaction estimates are highly vulnerable to misclassification of the modifier. If stroke etiology (e.g., cardioembolic versus large vessel) is misclassified in a subset of the cohort, any true interaction between etiology and therapeutic response will be attenuated. Appraisers must factor the inter-rater reliability of the stratifying variable into their assessment of the subgroup claim.

## Standardization of Rates for Comparative Epidemiology

![Direct standardization combining stratum-specific risks under a common target-population distribution.](../assets/figures/fig19_standardization.png)

*Standardization makes the target population—and its covariate distribution—explicit.*

While interaction concerns subgroup effects within a single cohort, standardization techniques address the comparability of aggregate event rates across distinct populations. Crude rates (e.g., unadjusted regional stroke mortality) are inherently confounded by demographic composition. A region with a heavily aged demographic structure will manifest a higher crude stroke incidence than a younger region, rendering direct comparison of the unadjusted rates epidemiologically meaningless.

Direct standardization applies the stratum-specific rates observed in the study populations to the demographic distribution of a single, external reference standard. The resulting standardized rate isolates the difference in disease force by neutralizing the compositional variance. This technique is essential for comparing longitudinal incidence trends across decades where the underlying population age structure has shifted.

Indirect standardization reverses the architecture, applying the stratum-specific rates of a reference population to the demographic structure of the study cohort to calculate an expected number of events. The ratio of observed to expected events—the Standardized Mortality Ratio (SMR)—is utilized extensively in quality improvement dashboards and hospital benchmarking, particularly when small numerators make local stratum-specific rates statistically unstable.

## Worked Example: Reconciling Scales in Antiplatelet Efficacy

### Trial Data Architecture

Consider a multicenter trial randomizing patients with minor ischemic stroke to dual antiplatelet therapy (DAPT) versus aspirin alone for 21 days. The pre-specified analysis stratifies the cohort by the ABCD2 score into high-risk and low-risk tiers.

```
High-Risk Stratum (n = 1600)
Aspirin alone: 96 events / 800 patients (12.0%)
DAPT:          64 events / 800 patients (8.0%)
RR = 0.67 | ARR = 4.0% | NNT = 25

Low-Risk Stratum (n = 2400)
Aspirin alone: 36 events / 1200 patients (3.0%)
DAPT:          24 events / 1200 patients (2.0%)
RR = 0.67 | ARR = 1.0% | NNT = 100
```

### Appraisal and Net Clinical Benefit

A formal test for multiplicative interaction yields p > 0.05, meaning that it did not detect heterogeneity on the multiplicative scale; this is not proof of homogeneity. Under the synthetic assumptions, report 4.0 fewer ischemic events and 0.8 more major hemorrhages per 100 patients in the high-risk stratum, versus 1.0 fewer ischemic events and 0.8 more major hemorrhages per 100 in the low-risk stratum. Do not collapse these clinically different outcomes into a net-benefit verdict without uncertainty, severity or utility weights, and patient preferences.

## Checklist for Evaluating Interaction and Subgroups

- Verify Pre-specification: Identify whether the subgroup hypothesis was formally defined prior to data analysis or generated post-hoc.
- Check the Interaction Test: Confirm that a formal statistical test for interaction was performed, rather than inappropriate comparisons of subgroup p-values.
- Identify the Scale: Determine if the reported interaction test operates on the additive or multiplicative scale.
- Reconstruct Absolute Risks: Calculate the stratum-specific absolute risk reductions to determine if relative homogeneity masks additive heterogeneity.
- Model Net Benefit: Evaluate whether absolute harm profiles alter the clinical utility of the intervention across the proposed subgroups.


![Subgroup forest plot illustrating that different within-group p-values do not establish interaction.](../assets/figures/fig66_subgroup_forest.png)

*Teaching graphic (fig66_subgroup_forest.png).*

## Chapter summary

Effect modification occurs when the magnitude of an exposure-outcome association varies across strata of a third variable, representing biological or clinical heterogeneity distinct from confounding bias. Interaction analysis is fundamentally scale-dependent; subgroups often demonstrate homogeneity on a multiplicative scale (e.g., consistent risk ratios) while simultaneously exhibiting marked interaction on an additive scale due to differences in baseline event rates. Because clinical decision-making relies on absolute net benefit, neurologists must reconstruct absolute risk reductions and evaluate NNTs across strata before accepting subgroup claims. Rigorous appraisal also mandates checking for pre-specification, formal interaction testing, and adjusting for multiplicity. To ensure valid comparison of aggregate stroke rates across demographics, direct and indirect standardization techniques neutralize compositional confounding, providing accurate epidemiological and quality benchmarking.

## Practice and reflection

1. Analyze a recent stroke trial reporting 'consistent treatment effects across all subgroups.' Reconstruct the absolute risk reductions for two distinct subgroups to assess additive interaction.
2. Construct a synthetic dataset where the absolute risk difference is identical between two age strata, but a Cox regression model indicates significant multiplicative interaction.
3. Critique a journal article that relies on overlapping confidence intervals to conclude there is no interaction between stroke etiology and therapeutic efficacy.
4. A regional stroke system implements direct standardization for 30-day mortality. Explain how using a 1990 reference population versus a 2020 reference population might alter the absolute standardized rates.
5. Draft a structured peer-review comment challenging a manuscript's assertion of effect modification that was based entirely on disparate within-stratum p-values.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
