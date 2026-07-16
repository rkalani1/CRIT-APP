# Chapter 4. Internal Validity, External Validity, and Bias Taxonomy

## Opening

![Three bias families.](../assets/figures/fig27_three_bias_families.png)

*Three bias families.*

![Bias taxonomy map.](../assets/figures/fig02_bias_taxonomy.png)

*Bias taxonomy map.*

![Bias families versus transportability.](../assets/figures/swarm_ch04_bias_taxonomy.png)

*Bias families versus transportability.*

Quality meeting: someone proposes adopting an outside center protocol based on one observational paper. Demand the bias story—selection, confounding, measurement—before the order set is rewritten.


## Introduction: The Two-Part Promise of Validity

When clinicians and methodologists declare a study 'valid,' they frequently conflate two distinct questions. Internal validity asks whether the design and analysis identify the target estimand in the study population without important systematic distortion. External validity (often parsed into generalizability and transportability) asks whether an internally valid estimate is relevant to a different population, setting, or system of care. Design, measurement, and effect heterogeneity can affect both questions, so distinct does not mean wholly non-overlapping.

A landmark endovascular therapy (EVT) trial can be internally flawless in establishing a treatment effect for highly selected patients at comprehensive stroke centers, yet entirely fail to transport to a rural spoke hospital lacking advanced perfusion imaging and experiencing prolonged transfer delays. Conversely, a massive administrative claims analysis might possess perfect external validity regarding the demographic representation of an insured national population, while remaining completely internally invalid for a causal treatment effect due to intractable unmeasured confounding.

Critical appraisal must permanently sever these two concepts and score them separately. This chapter formalizes a rigorous bias taxonomy, defining the mathematical and structural threats to internal validity, and establishes the clinical frameworks required to evaluate transportability. We reject the amateur approach of compiling an undifferentiated list of 'limitations.' Instead, we provide the architectural diagnostic tools to locate exactly where a study's inferential chain breaks, allowing the clinician to render a definitive verdict on the utility of the evidence.

## Random Error versus Systematic Error (Quantitative Foundations)

Before deploying a taxonomy of biases, distinguish sampling variation from systematic error. Let $\theta$ represent the target estimand and $\hat{\theta}$ an estimator computed from a sample. Under a specified sampling and statistical model, repeated samples produce a distribution of $\hat{\theta}$ with variance $Var(\hat{\theta})$. Confidence intervals and p-values summarize particular features of that distribution under their assumptions; they do not measure design validity or every source of uncertainty.

For many well-behaved estimators, sampling variance decreases as effective sample size and event information increase, but this is estimator- and design-dependent and is not guaranteed merely by invoking the Law of Large Numbers. Bias can be expressed as $E[\hat{\theta}] - \theta$ for a specified data-generating process. Some finite-sample bias shrinks with sample size; a fixed identification failure from confounding, selection, or measurement can persist even as the interval becomes narrow. More observations do not by themselves repair a structurally unidentified contrast.

If an observational stroke registry systematically assigns patients with heavier baseline disability to the medical management arm rather than the interventional arm, a dataset containing five million electronic health records will not eliminate the confounding. It may produce a very narrow confidence interval centered on a biased estimate. In the era of big data and claims-based research, precision is a false friend. A study with a p-value of $10^{-12}$ and a confidence interval width of 0.01 can still be seriously biased. Critical appraisal must not allow statistical precision to silence structural bias concerns.

Different problems require different remedies, but the categories are not operationally exclusive. More informative sampling and measurement can improve precision and sometimes reduce estimable measurement error; design, data collection, causal assumptions, and analysis determine whether the target is identified. Uncontrolled multiplicity raises the probability of selective false-positive claims across a family of analyses. Prespecification and an error-rate procedure appropriate to that family address this selection problem, but they do not correct confounding, selection bias, or outcome mismeasurement.

## Internal Validity: Defining the Boundary

Internal validity is defined as the structural credibility of the causal inference for the exact population analyzed, under the exact design implemented. It asks a singular question: did the study accurately measure what it claimed to measure for the patients actually enrolled? For a randomized controlled trial (RCT), internal validity relies on the physical mechanisms of the experiment. This includes cryptographic allocation concealment to prevent selection bias at baseline, uncompromised randomization integrity to ensure baseline exchangeability, rigorous blinding of outcome assessors to prevent differential information bias, nearly complete follow-up to block attrition bias, strict adherence to the intention-to-treat (ITT) principle for evaluating the primary treatment policy estimand, and flawless protocol fidelity.

For observational research, internal validity hinges on whether the analytical design successfully emulates a coherent target trial. This requires precise alignment of index time (time zero), appropriate and accurate classification of the exposure, and the rigorous statistical control of the major confounding and selection processes that render the exposure groups nonexchangeable. Failure at any of these nodes destroys internal validity. Observational studies using prevalent users instead of incident (new) users, or studies defining exposure based on events that occur in the future relative to the index time, suffer from catastrophic internal validity failures before the first regression model is even specified.

Crucially, internal validity is entirely relative to the specified estimand. An instrumental variable analysis might be perfectly internally valid for computing a Local Average Treatment Effect (LATE) among marginal patients whose treatment assignment was altered by the instrument, but it would be profoundly invalid if interpreted as an Average Treatment Effect (ATE) for the entire population. During any journal club or morbidity and mortality conference, asserting that a study is 'internally valid' is an incomplete sentence. The mandatory professional completion is: 'Internally valid for what specific target estimand?'

Finally, one must never confuse internal validity with clinical magnitude or clinical importance. A perfectly executed, internally flawless RCT may yield an absolute risk reduction of 0.5%, translating to a Number Needed to Treat (NNT) of 200. That finding is valid, but it may be clinically trivial for a high-risk, high-cost surgical intervention. Conversely, a deeply flawed observational study might claim an absolute risk reduction of 25%, but if the internal validity is compromised by indication bias, the magnitude is a statistical hallucination. Decision-making requires the integration of both the structural validity grade and the absolute effect size.

## External Validity and Transportability

External validity asks whether the causal conclusions derived from a internally valid study hold true beyond the highly specific, restricted context of its execution. Modern epidemiologic nomenclature enforces a precise distinction between generalizability and transportability. Generalizability is the ability to apply findings to the broader target population from which the study sample was formally and probabilistically drawn. Transportability, which is the far more common clinical requirement, is the ability to apply findings to a completely different population with distinct covariate distributions, unmeasured environmental factors, and distinct care processes. For the practicing stroke neurologist, the operational question is direct: if we enact this intervention in our specific stroke center on a Tuesday morning, should we anticipate identical absolute benefits and absolute harms?

Case-mix and system-mix are two useful domains for transportability. Case-mix includes distributions of prognostic factors and effect modifiers; system-mix includes treatment versions, expertise, timing, co-interventions, and access. An absolute effect from a rapid academic-hub workflow should not be assumed unchanged in a network with long transfers, but the transported effect requires data or an explicit model rather than a qualitative penalty alone.

Mathematical transportability depends on both baseline risk and effect stability. If an RR of 0.70 were justified and transportable, a 10% control risk would imply a 7% treated risk, ARR 3 points, reciprocal 33.3, and a rounded-up NNT of 34. At a 2% control risk, it would imply a 1.4% treated risk, ARR 0.6 points, and NNT 167. Harm may follow a different pattern. These are projections under assumptions, not a license to apply a published RR directly without checking effect modifiers, outcome definitions, and local risk estimation.

Transportability is not a binary switch. For example, [EXTEND-IA TNK](https://www.nejm.org/doi/full/10.1056/NEJMoa1716405) found more substantial reperfusion before thrombectomy with tenecteplase 0.25 mg/kg than with alteplase 0.9 mg/kg (22% vs 10%) among thrombectomy-eligible large-vessel occlusions treated within 4.5 hours. That result should not be rewritten as generic equivalence or superiority across every dose, population, endpoint, and workflow. Local implementation also requires auditing treatment times, eligibility, and hemorrhage outcomes.

## The Core Bias Taxonomy

A practical, clinically operational taxonomy groups systematic errors into four non-overlapping domains: selection bias, confounding, information bias, and reporting bias. While the specialized epidemiological literature contains dozens of eponymous biases (immortal time bias, lead time bias, spectrum bias, ascertainment bias, length-time bias), memorizing these names is analytically useless for the practicing clinician. The senior clinical epidemiologist maps these specialized terms to the underlying causal structure within the four core domains.

Selection bias occurs when the mechanism of entering the study or remaining in the analytical cohort distorts the estimated association between exposure and outcome. Confounding occurs when the exposure groups are inherently nonexchangeable at baseline due to shared common causes. Information bias occurs when the exposure, outcome, or covariates are measured with error. Reporting bias occurs when the publication or emphasis of results is systematically driven by the magnitude or direction of the findings.

In a twenty-minute protocol review or journal club preparation, this four-bin taxonomy provides a practical first-pass framework for scanning major threats. The bins can overlap—for example, selection can also alter measurement or reporting—and they are not collectively exhaustive for every estimand. The objective is to identify the dominant mechanisms that could materially distort the central claim and to assess their likely direction and magnitude.

## Selection Bias: Mechanisms and Stroke Examples

*Teaching figure (synthetic).* Left: severity opens a backdoor path treatment ← severity → outcome—block with pre-exposure adjustment. Right: restricting to patients who enter the analytic sample (S=1) when both exposure and outcome-related factors cause inclusion invents a non-causal association. Naming the structure prevents the amateur habit of calling every problem “confounding.” Absolute transport (ARR/NNT in *your* case-mix) is a separate question after internal validity.

Selection bias is a structural flaw that can arise when inclusion in the analyzed dataset is influenced by exposure- and outcome-related causes. In a causal graph, conditioning on a selected stratum can amount to conditioning on a collider. If exposure and outcome-related causes both influence selection, that conditioning can open a noncausal path and induce an exposure–outcome association. Its magnitude and direction depend on the causal structure and parameter values; it is not guaranteed in every numerical configuration.

In randomized trials, baseline selection into the trial affects transportability, but differential attrition—selection out of the trial after randomization—destroys internal validity. If missing 90-day mRS scores are more common in the surgical arm because patients with severe strokes die or withdraw consent, the remaining patients are a biased, structurally healthier subset. Analyzing only the 'completers' induces massive selection bias that invalidates the ITT principle.

In observational stroke research, selection bias is pervasive and often fatal. Consider a study utilizing a telestroke registry to evaluate outcomes of transient ischemic attack (TIA). Inclusion requires an emergency department physician to trigger a telestroke consult. Consults are heavily biased toward patients with severe, atypical, or stuttering symptoms, while clear, mild TIAs are managed locally without a consult. The analytical cohort is structurally selected for severity, rendering estimates of TIA recurrence completely untransportable to the general population.

Another classic mechanism is immortal time bias, which operates as a hybrid of selection and index-time errors. If researchers seek to compare patients who undergo acute inpatient rehabilitation to those who do not, they must recognize a structural truth: receiving inpatient rehabilitation requires surviving the acute hospital stay. The rehabilitation cohort is 'immortal' during the waiting period between admission and transfer. Comparing their overall survival from admission to a non-rehabilitation cohort that includes early catastrophic deaths induces a massive, artificial survival benefit for rehabilitation. The required architectural fix is the strict alignment of index time (time zero) to the moment of discharge, or treating rehabilitation as a time-varying covariate. Failure to do so guarantees a profoundly biased estimate.

## Confounding and Confounding by Indication

Confounding is the presence of a common cause structure that renders the exposure groups nonexchangeable. In causal inference notation, to estimate the causal effect of treatment $A$ on outcome $Y$, we require the assumption of conditional exchangeability: $Y^a \perp A \mid L$. This states that the potential outcome $Y^a$ is independent of the actual treatment assignment $A$, conditional on a sufficient set of measured pre-treatment covariates $L$. If unmeasured confounding $U$ exists (such that $U$ causes both $A$ and $Y$), this assumption fails entirely, and the estimated association is a mixture of the true causal effect and the backdoor path through $U$.

Confounding by indication is the signature, apex threat of all clinical observational research. It occurs because the indication for the treatment is intrinsically linked to the patient's baseline prognosis. Physicians are extensively trained to administer aggressive, risky therapies to patients they expect to benefit, and to withhold them from patients deemed too frail or for whom treatment is physiologically futile (confounding by contraindication). Consequently, patients receiving aggressive treatment differ systematically and profoundly from those who do not, on variables that directly determine survival and recovery.

In acute stroke, evaluating the effectiveness of EVT using unadjusted observational data is scientifically meaningless. Patients who receive EVT have confirmed large vessel occlusions (LVOs), high NIHSS scores, and favorable core-to-penumbra mismatch on advanced imaging. Their baseline prognosis for severe disability without treatment is extraordinarily high compared to the general stroke population. A naive, unadjusted comparison to a cohort of medically managed stroke patients (which includes lacunar infarcts, minor cortical strokes, and TIA mimics) will make EVT appear to cause massive harm. Conversely, in secondary prevention, neurologists routinely withhold oral anticoagulation from patients with a history of falls, cerebral amyloid angiopathy, poorly controlled hypertension, or suspected non-compliance. Patients discharged on anticoagulation are inherently healthier and at lower baseline risk for hemorrhagic complications. An unadjusted analysis will artificially inflate the safety profile of the drug.

The analytical responses to confounding include multivariable regression, propensity score matching, inverse probability of treatment weighting (IPTW), and instrumental variable analysis. It is critical to understand that regression and propensity scores are mathematically identical in their reliance on the assumption of no unmeasured confounding. They possess zero magic. If an administrative claims database lacks the NIHSS, the ASPECTS score, and collateral grading, no mathematical transformation of the ICD-10 comorbidities will balance the exposure groups. Unmeasured confounding remains. Confounding control is a conceptual, clinical task before it is a computational one. Adjustment variables must be true pre-exposure confounders. Adjusting for variables measured after the exposure is initiated is a catastrophic error.

## Information Bias: Misclassification in Neurology

Information bias stems from the flawed measurement of the exposure, the outcome, or the confounding covariates. Misclassification can be differential (where error rates differ systematically between the exposure or outcome groups) or non-differential (where error rates are uniform across groups). A common, dangerous epidemiological aphorism states that non-differential misclassification always biases estimates toward the null. This rule is only mathematically guaranteed for binary exposures and binary outcomes under strict conditions. In complex models involving continuous variables, categorical variables with more than two levels, or correlated measurement errors, non-differential misclassification can easily generate spurious effects away from the null. Do not recite that slogan uncritically.

In clinical neurology, measurement error is profound. Exposure misclassification frequently occurs in retrospective claims-based pharmacological adherence studies: a filled prescription for dual antiplatelet therapy (DAPT) tracked via a pharmacy database does not guarantee the patient actually ingested the medication at home. Outcome misclassification is notorious when relying on administrative ICD-10 codes. The positive predictive value (PPV) of an ICD-10 code for 'acute ischemic stroke' can be highly variable; it may inadvertently capture TIA, complicated migraine, functional neurological disorder, or old encephalomalacia coded improperly by billing departments. If a study evaluates a novel neuroprotectant and utilizes unadjudicated ICD-10 codes as the primary endpoint, the inclusion of non-stroke events dilutes the true outcome density, destroying statistical power and pulling relative effects toward the null.

Covariate misclassification occurs when structured, vital metrics like the NIHSS are either completely omitted, extracted from free-text clinical notes using faulty natural language processing, or imputed with unacceptably high variance. Appraisal questions regarding information bias must be highly aggressive: Were the outcome assessors rigorously blinded to the treatment assignment? (Unblinded assessment of the mRS via phone call is notoriously subjective and heavily biased toward the intervention). Were the definitions of symptomatic intracranial hemorrhage (sICH) pre-specified and strictly aligned with established, validated criteria (e.g., ECASS III or SITS-MOST)? Was a formal validation subsample utilizing gold-standard chart review performed to confirm the PPV of the administrative codes used in the primary analysis?

## Reporting Bias and Spin

Reporting bias corrupts the broader evidence ecosystem, making it impossible to synthesize the true state of the science. It includes publication bias (the systemic suppression of null or negative trials by authors or journals), selective outcome reporting (publishing only the secondary endpoints that achieved statistical significance while obscuring or minimizing the null primary endpoint), and spin. Spin is the intentional or unintentional use of rhetorical strategies to overstate causal certainty, distract from severe methodological limitations, or falsely elevate the clinical importance of the findings.

In the high-stakes, highly industry-funded landscape of stroke devices, novel antithrombotics, and proprietary imaging software, reporting bias directly determines what reaches your inbox and what is presented at international conferences. A strict defense mechanism requires cross-referencing the published manuscript against the prospective trial registry (e.g., ClinicalTrials.gov). Did the primary endpoint shift during the trial? Was the sample size arbitrarily truncated before the pre-specified power was reached? Did the statistical analysis plan change post-hoc to favor a specific subgroup?

Furthermore, one must relentlessly police the language of abstracts. Abstracts frequently deploy causal verbs ('reduces,' 'prevents,' 'causes,' 'drives') for strictly observational, associational designs. Critical appraisal demands translating these verbs back to their associational reality. An abstract claiming 'Statins reduce mortality in our hospital registry' must be mentally translated to 'Statin prescription at discharge was associated with lower mortality, heavily confounded by the fact that we only prescribe statins to patients who survive to discharge and are capable of swallowing.' Finally, reporting bias often manifests as asymmetrical emphasis: relative risk reductions (which sound massive) are heralded in the abstract for efficacy endpoints, while harms (e.g., major hemorrhage) are buried in the supplementary appendix and reported only as absolute risks to make them appear optically smaller.

## Collider Stratification Bias (Conceptual Core)

Collider stratification bias is a conceptually difficult but important error in clinical research. A collider is a variable that is causally influenced by two or more other variables. In a directed acyclic graph (DAG), it represents a node where two causal arrowheads collide ($A \rightarrow C \leftarrow Y$). Conditioning on a collider—by stratification, restriction, or regression—can open a noncausal path between its causes and induce an association. Whether that conditioning biases a particular estimate depends on the full graph and target estimand; do not add a collider to an adjustment set merely because it predicts the outcome.

Post-treatment variables require particular care because their role depends on the graph and target effect. Consider a hypothetical observational study evaluating EVT ($A$) and 90-day functional outcome ($Y$). Final infarct volume ($C$) may mediate part of EVT's effect and may also be affected by unmeasured baseline brain resilience or collateral status ($U$), which affects outcome. Adjusting for final infarct volume therefore changes the question away from the total effect; in this graph it can also open the path $A \rightarrow C \leftarrow U \rightarrow Y$. A mediation or controlled-direct-effect analysis needs a corresponding estimand and additional identification assumptions rather than routine covariate adjustment.

Restriction to survivors or complete cases can create a related problem when inclusion is affected by treatment and prognostic factors. In the stated drug example, analyzing survivors alone may select different frailty distributions across treatment groups. For a total-effect analysis, construct the baseline adjustment set from the causal graph and avoid routine adjustment for variables caused by treatment. Baseline prognostic variables need not all be common causes, and specialized longitudinal, mediation, or principal-stratification methods can sometimes address post-treatment variables under explicit assumptions. The adjustment set must match the estimand; a blanket 'adjust for every predictor' rule is not valid.

## Fully Worked Example: Appraising a Claims Study of EVT Effectiveness

Let us operationalize this entire taxonomy on a highly representative manuscript. Assume a paper published in a major journal titled 'Real-World Effectiveness of Endovascular Therapy in Large Vessel Occlusion: A National Claims Analysis.' The authors analyzed a dataset of 25,000 patients with ICD-10 codes for ischemic stroke and LVO. They compared patients who received EVT procedure codes against those who received only medical management. Using a multivariable logistic regression adjusted for age, sex, Elixhauser comorbidities, and hospital teaching status, they report an adjusted odds ratio of 0.65 for 30-day mortality in the EVT group. The abstract enthusiastically concludes: 'EVT is highly effective in routine practice and should be universally adopted across all centers.' Your health system is utilizing this paper to justify a massive expansion of auto-launch transfer criteria. We must deploy the structured appraisal.

1. Estimand Reconstruction: The authors are implicitly claiming an Average Treatment Effect (ATE) of EVT on 30-day mortality in the broad population of all LVO patients. The index time is ambiguous: is it the time of admission, or the time of the procedure? If eligibility and follow-up begin at admission but the EVT group is defined by a later procedure, the pre-procedure interval is at risk of being misclassified as immortal time unless treatment timing is handled explicitly.

2. Random Error: With $N=25,000$, sampling error may be smaller than in a modest cohort, but precision depends on event counts, model specification, clustering, missingness, and effective sample size. Inspect the reported interval rather than assuming it is microscopic. Large samples reduce some random error; they do not eliminate it or rescue systematic bias.

3. Selection Bias: Patients who reach an EVT-capable comprehensive center and actually undergo the procedure are profoundly selected. They are selected for geographical proximity, rapid presentation (arriving within the time window), and baseline physiological stability capable of surviving inter-facility transport. Many patients in the medical management arm may have died in the emergency department before imaging could even be completed.

4. Confounding by Indication: EVT selection depends on NIHSS, ASPECTS, collateral status, occlusion anatomy, time, frailty, and goals of care—variables that a claims-only analysis may not capture. Age and comorbidity codes are unlikely to form a sufficient adjustment set. Residual confounding could be large and its direction depends on competing selection mechanisms, so the odds ratio of 0.65 cannot identify the causal EVT effect in the stated broad population.

5. Information Bias: ICD-10 coding for 'LVO' without angiographic confirmation has poor sensitivity and specificity. Misclassification of the exposure and outcome adds further noise, though it is overshadowed by the confounding.

6. Collider Caution: Did the authors adjust for 'length of stay' or 'ICU admission'? If so, they conditioned on post-treatment colliders, further skewing the math away from a true causal effect.

7. External Validity: The dataset is highly representative of national demographics, but because the internal validity is fundamentally destroyed by indication bias, transportability is completely moot. You cannot transport a systematically biased estimate to your local hospital.

Conclusion: The study demonstrates severe, irremediable indication confounding and selection bias. The causal verb 'effective' in the abstract is blatant spin. This paper describes national utilization patterns; it possesses absolutely zero validity for establishing causal treatment efficacy or altering inter-hospital transfer criteria. The correct action is to discard the paper for clinical decision-making.

## Frameworks and Checklists: The Structured Validity Assessment

To prevent critical appraisal from devolving into unstructured skepticism or a disorganized airing of grievances, use a rigorous validity worksheet. Integrate it with the estimand framework in Chapter 3 whenever a paper is evaluated for a pathway update.

Part A: Estimand and Random Error.
- What is the exact causal target (population, exposure, comparator, outcome, time horizon)?
- Are there sufficient events to power this primary endpoint?
- Is the confidence interval width clinically acceptable for decision-making?
- Are there multiplicity concerns (unadjusted multiple comparisons)?

Part B: Internal Validity Threats (The Taxonomy).
- Selection Bias: Are there differential attrition or structural barriers to cohort entry?
- Confounding: Is there confounding by indication? Are the critical pre-exposure clinical variables (NIHSS, ASPECTS, time-last-known-well) actually measured and balanced?
- Information Bias: What is the PPV of the outcome definition? Were assessors blinded?
- Index Time: Is there immortal time bias?
- Colliders: Did the authors inappropriately adjust for post-treatment variables?

Part C: External Validity and Transportability.
- Case-Mix: How do the baseline characteristics of the study deviate from our local population?
- System-Mix: Can our hospital replicate the protocol logistics (e.g., time-to-needle, imaging speed)?
- Absolute Risk: Given our local baseline risk, does the absolute risk reduction remain clinically meaningful?

Part D: The Actionable Synthesis.
- Internal Validity Grade: (High / Medium / Low).
- Transportability Grade: (High / Medium / Low).
- Actionable Output: What exact clinical policy, protocol, or counseling language will change based on this paper? If the answer is none, the appraisal is complete.

## Pitfalls and Failure Modes in Validity Appraisal

Clinical readers frequently succumb to specific, recurring failure modes during appraisal. The first is confusing prediction with causation. An observational study may develop an exceptionally accurate machine learning model to predict which stroke patients will die at 30 days based on their admission lab values and demographics. High predictive accuracy does not mean the variables in the model are causal. Altering a predictive variable (e.g., pharmacologically lowering an inflammatory biomarker) will not necessarily change the outcome. Causation requires structural exchangeability; prediction merely requires mathematical correlation. Do not base interventions on predictive models without causal design.

The second failure mode is confusing precision with lack of bias. Physicians routinely accept findings from massive database studies simply because the $p$-value has six zeroes, completely ignoring that the point estimate is structurally detached from the truth due to unmeasured confounding. Precision around a biased estimate is dangerous.

The third failure mode is assuming relative-effect stability without verifying absolute impact. If a fixed-horizon risk ratio of 2.0 were justified and transportable, raising major bleeding from 5% to 10% gives an ARI of 5 percentage points (NNH 20), whereas raising it from 0.1% to 0.2% gives an ARI of 0.1 point (NNH 1,000). A hazard ratio of 2.0 does not support this arithmetic; use group-specific fixed-horizon risks or cumulative-incidence estimates.

## Clinical and Epidemiologic Notes

In acute stroke neurology, the intensity of confounding by indication is unmatched in internal medicine. Our primary therapies (intravenous thrombolysis, endovascular thrombectomy, dual antiplatelets, therapeutic anticoagulation) possess massive physiological power, capable of causing dramatic neurological recovery or lethal intracranial hemorrhage. Consequently, neurologist selection behavior is intensely and appropriately calibrated to baseline prognosis. We do not treat randomly. This clinical excellence at the bedside is precisely what creates catastrophic epidemiological confounding in observational data. This is why randomized controlled trials were absolutely mandatory to prove the efficacy of reperfusion therapies, and why observational 'real-world effectiveness' claims must be scrutinized with extreme prejudice.

Furthermore, in diagnostic stroke pathways, spectrum bias is a constant threat. The diagnostic accuracy (sensitivity, specificity, PPV, NPV) of a modality like CT Perfusion is frequently established in enriched cohorts with a high prevalence of true LVOs. When that same imaging modality is subsequently deployed in a general emergency department population dominated by dizziness, complex migraine, and toxic-metabolic encephalopathy (a low-prevalence spectrum), the false-positive rate will explode. This is mathematically driven by Bayes' theorem and the altered spectrum of disease. External validity in diagnostic testing is highly sensitive to the pre-test probability of the cohort. A diagnostic tool validated in a quaternary hub may fail spectacularly when transported to a community spoke.

## Cross-Links to Other Chapters

This chapter's validity framework assumes that the target question and estimand have first been defined in Chapter 3. Chapter 5 develops causal diagrams and target-trial thinking; Chapters 6 and 7 apply the framework to randomized and observational designs; Chapters 8 and 9 apply related validity questions to diagnosis and prediction. Chapter 19 returns to random error, estimation, and uncertainty.


![Branching analysis tree showing how multiple endpoints and subgroups multiply false-positive opportunities.](../assets/figures/fig45_multiplicity_tree.png)

*Teaching graphic (fig45_multiplicity_tree.png).*

## Chapter summary

Internal validity and external validity (transportability) answer distinct inferential questions and should be graded separately, even though some design and measurement choices affect both. Random error reflects finite sampling and generally shrinks with larger effective sample sizes, whereas systematic error can persist in massive datasets. Precision is not validity. A practical taxonomy comprising selection, confounding, information, and reporting mechanisms supports rapid review without claiming that the bins are mutually exclusive or exhaustive. Collider stratification explains one way that conditioning on selected post-treatment variables or survival can open noncausal paths; the consequence depends on the graph and estimand. Transportability requires reassessing absolute effects for the target case-mix, treatment delivery, and system of care. Structured validity assessments should yield graded, policy-relevant conclusions rather than unstructured lists of limitations.

## Practice and reflection

1. Retrieve a high-impact observational study assessing the 'real-world' outcomes of Tenecteplase versus Alteplase. Identify the index time and list three critical variables required to control for confounding by indication.
2. Explain the mathematical difference between random error and systematic error to a junior resident, utilizing the concepts of variance and expected value.
3. Draw a simple Directed Acyclic Graph (DAG) demonstrating confounding by indication for the decision to start therapeutic anticoagulation in a patient with a recent cardioembolic stroke.
4. Define immortal time bias. Design a flawed observational study evaluating the efficacy of outpatient physical therapy on 1-year mortality after stroke that falls victim to this bias.
5. Calculate the absolute risk reduction (ARR) and Number Needed to Treat (NNT) for a hypothetical intervention that has a Relative Risk (RR) of 0.5 in a high-risk population (baseline risk 20%) versus a low-risk population (baseline risk 2%).
6. Identify a paper in the stroke literature that utilizes a massive administrative claims database. Analyze the width of the confidence intervals and critique the study's vulnerability to unmeasured confounding despite its precision.
7. Explain collider stratification bias using the example of adjusting for 'symptomatic intracranial hemorrhage (sICH)' when assessing the effect of door-to-needle time on 90-day mRS.
8. Differentiate between generalizability and transportability. List three specific system-mix variables in your local hospital that might prevent a landmark EVT trial's results from transporting perfectly.
9. Locate a published meta-analysis of a neurosurgical intervention. Scrutinize the funnel plot and methods section for an assessment of publication/reporting bias.
10. Review an abstract of a strictly observational stroke registry that utilizes causal verbs ('decreases', 'prevents'). Rewrite the abstract conclusion using strictly associational language.
11. Draft a formal department policy detailing the specific thresholds of internal validity and absolute risk reduction required to adopt a novel secondary prevention agent to the local formulary.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
