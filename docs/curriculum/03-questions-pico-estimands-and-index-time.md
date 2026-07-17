# Chapter 3. Questions, PICO, Estimands, and Index Time

## Opening

![Validity and transportability.](../assets/figures/fig25_validity_transport.png)

*Validity and transportability.*
![Two claim templates for paper claims.](../assets/figures/crit_fig_prediction_vs_causation.png)

*Two claim templates for paper claims.*


A family already saw the press release. Your job is translation: map the paper to a prediction template or a causal template, then decide whether anything at the bedside should change today.


## Conceptual Core: The Linguistic Chaos of Clinical Medicine

Most literature chaos begins as linguistic chaos. In neurology morbidity and mortality conferences, a trainee or attending might ask, 'Is endovascular therapy effective for large core infarcts?' or 'Do patients do better with early clinic follow-up?' or 'Is tenecteplase superior to alteplase?' These are vital curiosities, but they are not answerable research or appraisal questions. They lack a defined population, a specific contrast, a temporal origin, a measured outcome, and a defined summary metric. Critical appraisal does not start with attacking statistics; it starts with repairing the question. If you cannot define what is being estimated, debating the p-value is pure theater. The initial duty of the clinical epidemiologist is to force the clinician to speak in specific, falsifiable causal contrasts.

A cardinal rule that governs all critical appraisal is this: prediction is not causation. This distinction cannot be compromised. A prediction question asks, 'Given that a patient has characteristic X, what is the probability of outcome Y?' A causal question asks, 'If we intervene to change X to X*, how does the probability of outcome Y change?' The clinical query 'Is endovascular therapy beneficial in large core stroke?' is strictly causal. It implies an intervention. If an investigator attempts to answer this with a predictive model showing that large core patients treated with EVT have a 20% chance of functional independence, they have committed a category error. They predicted an outcome under a single condition without contrasting it against the counterfactual condition (medical management alone). Prediction observes the state of nature; causation requires a forced contrast between states.

A well-formed clinical question performs three precise jobs. First, it dictates which papers are actually relevant to your decision. Second, it specifies exactly what numerical estimate you need to extract from those papers. Third, it identifies 'neighbor' questions that masquerade as answers but should not drive your decision. In stroke neurology, neighbor questions are ubiquitous and dangerous. Early neurologic improvement at 24 hours is a neighbor of 90-day functional independence. The mere prescription of an antiplatelet is a neighbor of sustained adherence to an antiplatelet. Door-to-needle process time is a neighbor of patient-centered neurologic recovery. Recognizing a neighbor question prevents you from altering your practice based on off-target surrogate data.

This chapter provides the fundamental scaffolding for question generation and appraisal. We use PICO and PECO for structural anatomy; target population logic for evaluating transportability; the ICH E9(R1) estimand framework for analytic precision; index time (t0) for temporal discipline; and eligibility criteria for defining the exact boundaries of the causal target. Immortal time bias is introduced early because it represents the most dramatic consequence of getting time zero wrong—a recurrent theme that destroys the validity of countless observational studies in our field.

You cannot critically appraise what you have not clearly defined. Until the question is repaired, the literature search will yield noise, the journal club will descend into divergent arguments, and the resulting clinical pathway will be incoherent. Clarity in question design is conflict resolution technology for evidence-based medicine.

## The Target Population, the Study Sample, and the Analytic Set

The population in a clinical question is rarely a monolithic entity. It exists in three distinct layers that frequently diverge, and tracing their divergence is a core task of appraisal. The target population is the group of patients about whom you want to learn or for whom you intend to make a clinical decision. It is defined by the realities of your clinic or emergency department. The study sample consists of the individuals who were actually recruited, consented, or captured in the data source. The analytic set comprises the patients who actually contributed to the final statistical estimate after all exclusions, missing data omissions, and protocol violations were handled.

Consider a standard acute stroke dilemma. Your target population might be all patients presenting to your regional spoke hospitals with an internal carotid artery or proximal middle cerebral artery (M1) occlusion within 24 hours of last known well. You find a landmark trial. However, the trial's study sample only includes patients successfully transferred to academic hub centers who passed highly restrictive perfusion imaging screens and provided legal consent. The analytic set is further narrowed, excluding those who lacked a 90-day modified Rankin Scale (mRS) assessment or crossed over to another therapy. The trial remains internally valid for its specific analytic set, but it answers your target population question only partially.

- Target population: Defined by your clinical decision context. These are the patients you will treat on your next shift.
- Study sample: Defined by recruitment logistics, consent mechanisms, data capture limits, and formal inclusion criteria.
- Analytic set: Defined by the prespecified analysis population and handling of missing outcomes, protocol deviations, and exclusions (for example, randomized/ITT, modified ITT, per-protocol, or complete case).
- Transportability assessment: Compare the study and target populations, effect modifiers, treatment delivery, and setting; quantify transported effects only when an explicit model and supporting data permit it.

This distinction is exceptionally critical in observational claims research, where the layers blur dangerously. The claimed 'population' might be 'all hospitalizations with an ICD-10 code for ischemic stroke.' This is a data-available population, not a biologic one. Further exclusions for continuous fee-for-service Medicare enrollment create an analytic set with a fundamentally different socioeconomic and comorbidity profile than a safety-net hospital's target population. If your center serves primarily underinsured, younger stroke patients, an enrollment-continuous Medicare analysis may mislead you entirely, regardless of how sophisticated the confounding adjustment appears.

When designing your own research, reverse the standard error: define the target population and the estimand first, and only then select a data source capable of approximating them. A vast graveyard of failed observational neurology projects begins with a convenient, massive dataset, followed by retrofitting a question that the dataset fundamentally cannot support. The appraisal of others' work and the design of your own share this exact discipline.

## Named Frameworks: PICO, PECO, and the Architecture of Clinical Contrasts

PICO is the classical scaffolding for interventional clinical questions: Population, Intervention, Comparator, Outcome. PECO adapts this framework for exposure-based questions that dominate observational epidemiology: Population, Exposure, Comparator, Outcome. While both are technically incomplete as full causal estimands, they serve as exceptional first-pass compression tools. They force the user to articulate the absolute minimum components required to assess a clinical contrast. If you cannot write a complete PICO sentence, you do not have a question.

- Population: Must be anatomically and temporally specific. 'Adults with anterior-circulation LVO presenting 6-24 hours after last known well with target mismatch.'
- Intervention/Exposure: Requires operational granularity. 'EVT plus standard medical care' or 'High-dose atorvastatin loaded prior to discharge.'
- Comparator: Must reflect a realistic alternative state. 'Medical care without EVT' or 'No statin initiation prior to discharge.'
- Outcome: Patient-important, temporally bound. '90-day mRS ordinal shift' or 'Recurrent ischemic stroke within 30 days.'

Write PICO and PECO frameworks as complete sentences, not as telegraphic fragments. Writing 'Population: stroke' is intellectually lazy and clinically useless. Writing 'Population: adults with non-cardioembolic minor ischemic stroke (NIHSS <= 5) or high-risk TIA randomized within 24 hours of onset, without an existing indication for systemic anticoagulation' provides a falsifiable perimeter. The sentence structure forces you to recognize missing pieces. This exact sentence becomes the first line of your formal appraisal checklist.

The PICO structure is not restricted to randomized drug trials. You must write a PICO for a health systems intervention (e.g., bundled door-to-puncture process improvements versus standard operations) or for a diagnostic strategy (e.g., CTA-first versus MRI-first screening for late-window EVT candidates), provided the paper evaluates these strategies against patient outcomes. For pure prediction questions, a modified scaffold applies: Population, Index predictors, Comparator model or default clinical heuristic, and Outcome. This still forces clarity regarding the exact moment of prediction and the time horizon.

Common PICO failures in neurology involve unspecified comparators and composite outcomes. Asking 'Is EVT beneficial?' is meaningless without specifying 'beneficial compared to what specific era of medical therapy?' Composite outcomes, such as a combined endpoint of 'stroke, myocardial infarction, or vascular death,' frequently hide the specific component that patients actually care about. If a trial claims success based on a composite, but the entire effect is driven by a reduction in asymptomatic troponin leaks while stroke rates remain static, the PICO architecture reveals the deception. When you identify these structural failures in an abstract, your critical appraisal is largely complete.

## The Estimand Framework: ICH E9(R1) in Neurologic Practice

![PICO mapped to estimand components (ICH E9(R1) spirit; original teaching figure).](../assets/figures/fig24_pico_estimand.png)

*PICO anatomy flows into the five estimand components (population, treatment conditions, variable, intercurrent-event strategy, population-level summary). Teaching figure.*


An estimand is the precise mathematical and clinical target of estimation. Introduced formally to the clinical trial community via the ICH E9(R1) addendum, the estimand framework demands that researchers explicitly define what they are trying to measure before they measure it. Modern trial methodology relies heavily on estimands because two completely different statistical analyses can yield different numbers while both being 'correct' for their respective estimand targets. Without estimand language, clinical debates devolve into vague arguments about whether the authors used the 'right' p-value or the 'correct' covariate adjustment.

The ICH E9(R1) framework requires specifying five attributes to construct a complete estimand: (1) the treatment conditions or exposures being contrasted; (2) the target population; (3) the outcome variable and its time horizon; (4) the population-level summary measure; and crucially, (5) the strategy for handling intercurrent events. Intercurrent events are post-randomization events that preclude observation of the outcome or fundamentally alter its interpretation—such as treatment discontinuation, the initiation of rescue therapy, or death.

- Treatment-policy strategy: Include outcomes regardless of the specified intercurrent event. This strategy is an estimand attribute and should not be treated as synonymous with a particular analysis set or estimator.
- Hypothetical strategy: Target outcomes under a specified scenario in which the intercurrent event would not occur. The scenario and identifying assumptions must be stated; it does not universally mean perfect adherence.
- Composite Strategy: The intercurrent event is absorbed into the outcome. For example, if a patient undergoes decompressive hemicraniectomy after an MCA stroke, this is counted as a failure equivalent to death or severe disability.
- While-on-Treatment Strategy: Evaluates the outcome only during the period the patient is actively exposed. Relevant for transient symptomatic therapies, but dangerous for disease-modifying treatments.
- Principal Stratum Strategy: The effect in the subset of patients who would have exhibited a specific intercurrent event behavior under both treatment conditions (e.g., those who would survive regardless of assignment).

A pragmatic, treatment-policy estimand sentence for acute stroke might read: 'In adults with ICA or M1 occlusion, NIHSS ≥6, ASPECTS ≥6, and last known well 6–16 hours earlier meeting specified perfusion-mismatch criteria, the estimand is the absolute increase in the probability of 90-day mRS 0–2 resulting from assignment to immediate EVT plus standard medical care versus standard medical care alone, regardless of subsequent procedural complications or crossover, among the population randomized.' This sentence is dense because clinical decisions are dense. Short slogans hide methodological disagreements that surface during appraisal.

Estimand mismatch is a primary diagnostic finding in critical appraisal. When an abstract strongly implies a pragmatic, treatment-policy benefit (suggesting you should offer this drug to everyone), but the only statistically significant result in the paper is a per-protocol or hypothetical estimand that excludes non-adherent patients or those who suffered early complications, the authors are selling a product they did not test. You must evaluate the paper based on the estimand they actually estimated, not the one they claim in the discussion.

## Index Time (t0) and the Chronology of Causation

Index time, or time zero, anchors eligibility, assignment to treatment strategies, and the start of follow-up for a target causal contrast. These elements should be defined at a common decision time or handled with a design that explicitly represents treatment timing and grace periods. Misalignment can create immortal-time or selection bias, but the consequence depends on how time-varying assignment and follow-up are analyzed. In a conventional randomized trial, randomization usually supplies the common assignment and follow-up origin.

In observational stroke research, index time is rarely designed; it is passively implied by the dataset. Researchers might use admission time, exact stroke onset, discharge time, the first pharmacy fill, or the date of a clinic visit as their pseudo-t0. Every single choice radically alters the causal meaning of the estimate. If an analysis compares outcomes between patients who received a medication during their hospital stay versus those who did not, but starts the follow-up clock at admission, it has decoupled treatment assignment from eligibility.

- Diagnostic Question 1: When, exactly, could a patient first theoretically be eligible for either of the treatment strategies being compared?
- Diagnostic Question 2: When does the exposure status become permanently knowable in real time for clinical decision-making?
- Diagnostic Question 3: Are clinical events that occur before exposure classification inappropriately counted, excluded, or misattributed to the exposure?
- Diagnostic Question 4: Does the study align eligibility, strategy assignment, and follow-up at a defensible t0, or explicitly handle any grace period and time-varying treatment?

Acute stroke care adds immense prehospital and transfer complexity. Time from last known well, door time, non-contrast CT time, and puncture time are all critical operational clocks, but the causal index time for a specific treatment contrast is the exact moment the clinician faces the choice between strategies. Landmark EVT trials use randomization as t0, which usually occurs immediately after imaging. Retrospective observational comparisons of 'EVT versus no EVT' that start their follow-up clock at hospital admission—without carefully emulating the exact moment of imaging eligibility—create a chaotic mixture of selection bias, immortal time bias, and survival bias.

The concept of 'target-trial emulation' in observational epidemiology is fundamentally an exercise in index-time discipline. It forces the observational researcher to construct a protocol skeleton that artificially enforces the alignment of eligibility, assignment, and follow-up, just as an RCT would. When you review a paper, checking the alignment of t0 is never optional. Finding a failure here protects you from over-interpreting a complex, machine-learning-adjusted hazard ratio that is temporally incoherent.

## Quantitative Reasoning: Formalizing the Causal Contrast

To move beyond linguistic arguments, we must define the causal contrast quantitatively using potential outcomes notation. Let $Y$ represent the outcome of interest, such as achieving functional independence (mRS 0-2) at 90 days. Let $A$ represent the treatment assignment, where $A=1$ for the active intervention (e.g., tenecteplase) and $A=0$ for the comparator (e.g., alteplase). For any individual patient $i$, we theorize two potential outcomes: $Y_i^{a=1}$, the outcome if they received tenecteplase, and $Y_i^{a=0}$, the outcome if they received alteplase.

The individual causal effect is simply $Y_i^{a=1} - Y_i^{a=0}$. However, because a patient cannot simultaneously receive both treatments, we can never observe both potential outcomes for the same individual at the same time. This is the fundamental problem of causal inference. Instead, we must estimate the Average Treatment Effect (ATE) across the target population: $E[Y^{a=1}] - E[Y^{a=0}]$. This contrast requires exchangeability; randomization supports exchangeability in expectation, while observational analyses require additional identification assumptions and appropriate adjustment.

Let $Y=1$ denote a favorable outcome. Then $E[Y^{a=1}] - E[Y^{a=0}]$ is the causal risk difference—here, an absolute increase in the favorable outcome. If $Y=1$ denotes an adverse outcome, ARR is $E[Y^{a=0}] - E[Y^{a=1}]$ when treatment lowers risk. NNT is the reciprocal of the absolute risk difference, with endpoint, direction, and horizon stated. Increasing mRS 0–2 from 0.25 to 0.40 gives a 0.15 absolute increase and a reciprocal of 6.7, conventionally rounded up to an NNT of 7.

- Associational contrast: $E[Y | A=1] - E[Y | A=0]$. This compares observed outcomes among people who received different treatments; without an identifying design and assumptions, it can mix treatment effect with confounding and selection.
- Causal Equation: $E[Y^{a=1}] - E[Y^{a=0}]$. This compares the counterfactual states of the entire population. This is what you actually care about.
- Absolute effects retain the event-probability scale. RR, OR, and HR do not by themselves communicate baseline risk or an absolute risk difference.
- A relative risk reduction of 50% is clinically meaningless if the baseline risk is 1 in 10,000. It is practice-changing if the baseline risk is 30%.

We ruthlessly prefer absolute effects because clinical decisions are weighed in absolute terms. You do not balance a 'relative increase in bleeding' against a 'relative decrease in stroke.' You balance an NNH of 100 for symptomatic intracranial hemorrhage against an NNT of 20 for stroke prevention. Papers that report impressive relative hazard ratios while burying absolute risk differences in supplemental tables are engaging in statistical spin. Always manually calculate the ARR from the raw event rates before interpreting the conclusion.

## Pitfalls and Failure Modes: When Time Zero Breaks

When index time (t0) is misaligned, observational studies fail catastrophically. The most notorious of these failures is immortal time bias. Immortal time bias arises when a period of follow-up is misclassified such that patients in the 'exposed' group must have survived event-free until the exposure actually occurs, yet that waiting time is counted as exposed time. Alternatively, early deaths before exposure are assigned exclusively to the unexposed group. The exposed patients are artificially rendered 'immortal' during the wait.

Consider a deeply flawed cohort study investigating whether outpatient cardiac rehabilitation after mild ischemic stroke improves 1-year mortality. The authors define the exposure as attending at least one cardiac rehab session within 90 days of hospital discharge. They start the follow-up clock (t0) at hospital discharge for everyone. The fatal structural error is obvious: to be in the 'exposed' group, a patient must survive long enough, and remain functionally intact enough, to attend a rehab session on day 45. A patient who suffers a fatal recurrent stroke on day 10 cannot attend rehab and is automatically assigned to the 'unexposed' cohort.

By definition, the cardiac rehab group has guaranteed 100% survival from discharge until their first session. The resulting hazard ratio will massively favor cardiac rehab, but not because rehabilitation prevented death; rather, early survival was a prerequisite for rehabilitation. The exposure was defined by a future event while follow-up started earlier for all. The epidemiological fixes require aligning index time: using a landmarking approach (e.g., starting follow-up at day 90 for those who survived), treating exposure as a time-varying covariate, or using sequential target-trial emulation.

- Prevalent User Bias: Occurs when studies compare chronic users of a drug (e.g., DOACs) to non-users. Prevalent users have already survived the initial high-risk period for adverse events (like early GI bleeds). They are 'depleted of susceptibles,' making the drug look safer than it is.
- Confounding by Indication: The reason the physician prescribed the drug is an independent predictor of the outcome. A statin given at discharge marks a patient who was transitioning to outpatient care, not hospice.
- Time-lag Bias: Comparing a newly approved drug against an older drug, where the cohorts reflect entirely different eras of baseline medical care and stroke severity.

Your primary defense against these failure modes is to ruthlessly map the chronology. If you cannot draw a timeline explicitly demonstrating when a patient becomes exposed and verifying that pre-exposure person-time is handled correctly, you must reject any claim of an observational protective effect. That single chronological standard eliminates a massive volume of misleading health services research from your practice-change queue.

## Fully Worked Example: Secondary Stroke Prevention and Target Trial Emulation

A stroke center leadership committee is debating readmission metrics. A member states: 'We should be far more aggressive about dual antiplatelet therapy (DAPT) for everyone after mild stroke. Our 30-day readmissions look high, and a recent retrospective claims paper showed that DAPT at discharge is associated with significantly fewer readmissions.' The room is rapidly mixing a causal treatment policy, an observational association, a generic process outcome, and a completely undefined population. Your task as a clinical epidemiologist is to dismantle and reconstruct the question.

Step 1: Separate the overlapping decisions. Decision A: For an early high-risk TIA or minor non-cardioembolic ischemic stroke, should a trial-defined aspirin-plus-clopidogrel strategy replace aspirin alone to reduce recurrent ischemic events, and what is the corresponding bleeding risk? Decision B: Does earlier post-discharge neurology follow-up reduce 30-day readmissions? Decision C: What does the claims association actually mean? These are distinct questions requiring different study designs.

Step 2: Formalize the PICO without blending trials. [CHANCE](https://www.nejm.org/doi/full/10.1056/NEJMoa1215340) enrolled high-risk TIA or minor stroke (NIHSS ≤3) within 24 hours and used a 300-mg clopidogrel load, clopidogrel through day 90, and aspirin for the first 21 days. [POINT](https://www.nejm.org/doi/full/10.1056/NEJMoa1800410) enrolled a similar NIHSS ≤3 population within 12 hours and used a 600-mg clopidogrel load with aspirin-clopidogrel through day 90. Readmission is absent from both causal formulations; it is a health-system metric, not the neurologic efficacy endpoint.

Step 3: Draft the estimand for Decision A. 'Among patients meeting a specified trial's eligibility criteria at ED diagnosis (t0), the treatment-policy estimand is the 90-day absolute risk difference for that trial's primary efficacy endpoint comparing assignment to its aspirin-plus-clopidogrel regimen versus aspirin, regardless of subsequent adherence, estimated alongside the absolute difference in major hemorrhage.' This wording points to the randomized evidence while preserving differences in regimen and endpoint.

Step 4: Critique the Claims Paper. You evaluate the paper cited in the meeting. It defines exposure as any pharmacy fill for DAPT within 14 days of discharge, but begins readmission follow-up at discharge. Immortal time bias is flagrant: patients who are readmitted on day 3 for an infection never have the chance to fill DAPT on day 10, dumping early readmissions into the unexposed cohort. Furthermore, the outcome is all-cause readmission, a target heavily confounded by frailty and social determinants of health, not a specific neurologic recurrence.

Step 5: Operational Action. You re-center the committee with trial-specific absolute effects. In CHANCE, 90-day stroke occurred in 8.2% versus 11.7% (ARR 3.5 percentage points; NNT about 29), while moderate or severe hemorrhage was 0.3% in both groups. In POINT, the primary composite occurred in 5.0% versus 6.5% (ARR 1.5 points; NNT about 67), ischemic stroke in 4.6% versus 6.3% (ARR 1.7 points; NNT about 59), and major hemorrhage in 0.9% versus 0.4% (ARI 0.5 points; NNH 200). These are not interchangeable estimates. You spin readmission into a separate quality-improvement question and retain the claims paper as an immortal-time-bias example.

## Clinical and Epidemiologic Notes

Clinical decisions always occur at a strict time zero, even when we fail to articulate it. The stroke neurologist decides about intravenous thrombolysis at a precise door-and-imaging moment; about EVT at an imaging-and-consent moment; about initiating DAPT at a diagnosis-and-risk-stratification moment. Papers that fail to align their analysis with these exact decision moments are estimating something fundamentally detached from the choice you face at the bedside. Demanding index-time clarity is not pedantry; it is a clinical safety practice.

Eligibility criteria can enrich a trial for a treatment-responsive population. [DAWN](https://www.nejm.org/doi/full/10.1056/NEJMoa1706442) enrolled selected anterior-circulation large-vessel occlusions 6–24 hours after last known well using an age-adjusted clinical-core mismatch. Its result directly supports that enrolled population; it does not prove what happens in every excluded phenotype. Large-core stroke is now informed by separate randomized evidence—including [RESCUE-Japan LIMIT](https://www.nejm.org/doi/abs/10.1056/NEJMoa2118191), [SELECT2](https://www.nejm.org/doi/abs/10.1056/NEJMoa2214403), and [ANGEL-ASPECT](https://www.nejm.org/doi/full/10.1056/NEJMoa2213379)—showing benefit in selected large-core populations. Low-NIHSS LVO remains a distinct evidence question. Appraise each population against the trial that actually enrolled it.

Estimand thinking profoundly clarifies shared decision-making with patients. When a family asks, 'If we choose to proceed with the thrombectomy, what are his chances of walking again?' they are asking a pure treatment-policy question. This requires an intention-to-treat estimate that incorporates all downstream failures, including the risk of procedural hemorrhage, access site complications, and futile recanalization. A 'while-on-treatment' estimand that censors patients who suffer complications might answer an interesting mechanistic question about reperfusion physiology, but it completely fails the family meeting. You must match the estimand to the conversation.

For neurology researchers utilizing electronic health records and massive observational datasets, the discipline of writing a target trial protocol—explicitly defining eligibility, index time, treatment strategies, outcomes, and causal contrasts before any SQL code is written—is the single best vaccine against immortal time bias and ill-posed PECO questions. It does not guarantee unbiased estimates, but it prevents the estimation of a chaotic blur. Reviewers can interrogate a clear estimand; they cannot fix a shapeless, machine-learning-derived association post hoc.

## Cross-Links to Other Chapters

The structural principles detailed in this chapter form the absolute prerequisite for Chapter 4 (Bias Taxonomy and Causal Inference). You cannot accurately diagnose a bias (such as selection bias, information bias, or unmeasured confounding) until you have defined the exact causal target the study is attempting to estimate. Without Chapter 3, discussions of bias are merely academic theater; with it, bias identification becomes a precise diagnostic procedure.

The PICO sentences and target-trial frameworks developed here directly populate the rapid appraisal tools introduced in Chapter 2. The concepts of index time and immortal time bias then support the design-specific appraisal of observational studies in Chapter 7 and the causal diagrams and target-trial logic in Chapter 5.


## Chapter summary

PICO and PECO provide an initial question scaffold; a full estimand adds treatment conditions, population, outcome and horizon, intercurrent-event strategy, and summary measure. Distinguish the target population, enrolled sample, and actual analysis set. Anchor eligibility, strategy assignment, and follow-up at a defensible time zero or model treatment timing explicitly. Translate estimates to endpoint- and horizon-specific absolute effects when the target baseline risk and relative effect are supportable. These steps make disagreements about validity and transportability explicit rather than hiding them in a broad clinical slogan.

## Practice and reflection

1. Rewrite the vague query 'Is tenecteplase better than tPA?' into a complete PICO sentence, and then expand it into a formal treatment-policy estimand including index time.
2. Take a recent endovascular therapy paper from a major journal. Explicitly list the demographic and clinical differences between your local target population, the paper's study sample, and the final analytic set.
3. For a retrospective claims study evaluating post-stroke DOAC initiation, define two distinctly different index times (t0) and diagram exactly how each choice alters the interpretation of the hazard ratio.
4. Decompose a composite vascular endpoint from a major secondary-prevention stroke trial. State definitively which component drives the statistical significance and whether that component alone should dictate your clinic counseling.
5. Identify an instance of immortal time bias in a published neurocritical care or stroke services paper, or construct a realistic hypothetical scenario. Sketch the target-trial emulation required to fix it.
6. Write the eligibility criteria for a hypothetical trial of delayed dual antiplatelet therapy initiation in patients referred more than 48 hours after stroke onset. Defend whether each criterion serves safety, efficacy enrichment, or logistics.
7. Locate a published stroke trial whose abstract implies an intention-to-treat (treatment policy) benefit, but whose only statistically significant finding relies on a per-protocol analysis. Document the exact estimand mismatch.
8. Convert a vague quality-improvement aim ('improve stroke clinic follow-up') into a strict PECO format utilizing both a patient-important outcome and a procedural outcome. State which outcome supports which decision.
9. Explain algebraically why the predictive expectation E[Y|A=1] - E[Y|A=0] cannot substitute for the causal contrast E[Y^{a=1}] - E[Y^{a=0}]. Define what happens when confounding is present.
10. Draft the mandatory estimand paragraph you would require in the methods section of your next retrospective EHR analysis before authorizing any data extraction or coding.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
