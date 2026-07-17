# Chapter 16. Paper Autopsies: Integrated Worked Critiques

## Opening
![Name prediction vs causal claims first.](../assets/figures/crit_fig_claim_types.png)

*Name prediction vs causal claims first.*

![Paper autopsy sequence.](../assets/figures/crit_fig_autopsy_sequence.png)

*Paper autopsy sequence.*


![Paper autopsy sequence.](../assets/figures/swarm_ch16_autopsy_flow.png)

*Paper autopsy sequence.*

Five synthetic paper autopsies appear in this chapter. Practice the autopsy sequence: claim → design → absolute effect → transport → decide.


## The Architecture of the Paper Autopsy

Integrated appraisal is slower than abstract skimming and faster than regret after a pathway change based on statistical spin. Autopsies train the slower skill until it becomes a rapid reflex. The educational standard is not cruelty to authors; it is fairness to patients. A paper can be honest, important, and still structurally incapable of justifying the practice change its abstract implies. Autopsy language must be precise, proportionate, and entirely free of ad hominem attack. When we identify a 'fatal flaw,' we mean the architecture of the paper cannot support a particular causal or deployment claim—we are not passing judgment on the authors' careers.

```
PAPER AUTOPSY TEMPLATE
=====================
ID / Citation:
Clinical decision at stake (1 sentence):
Design one-liner:
Estimand (PICO-T):

VALIDITY (rank top 3 threats):
1.
2.
3.

RESULTS:
- Primary endpoint absolute risks / effect (CI):
- Harms absolute:
- Fragility / precision notes:
- Subgroups / secondary claims to quarantine:

SPIN / COI / Data control:
APPLICABILITY to our system (ops + equity):
REPLICATION landscape:

BOTTOM LINE: Act / Conditional / Watch / No change
What would change my mind:
Owner / review date (if operational):
```

*Teaching figure.* Every autopsy must end in one of four operational buckets—not “interesting.” Map claim capacity, absolute effects, and transportability before rewriting a pathway.

## Autopsy A — The EVT-Like RCT (CLEAR-PATH 7–18 Hour Trial)

### A1. Trial Architecture and Clinical Stake

CLEAR-PATH is a fictional, multicenter, open-label, blinded-endpoint randomized trial comparing endovascular thrombectomy (EVT) plus best medical care versus best medical care alone in patients with anterior circulation LVO last known well 7–18 hours earlier. Selection required NCCT ASPECTS >= 6 and CTA-defined occlusion of the ICA or M1. The primary endpoint is functional independence (mRS 0–2) at 90 days. The clinical stake is defining whether comprehensive stroke centers should liberalize late-window EVT when advanced perfusion imaging (CTP) is unavailable, and whether spoke hospitals should initiate patient transfers based on non-contrast CT and CTA alone.

### A2. Internal Validity and Estimand Mapping

The design is PROBE (Prospective Randomized Open, Blinded Endpoint), common for procedural trials where blinding is impossible. Open-label treatment can introduce performance bias if co-interventions differ by assignment. The primary analysis was modified Intention-to-Treat (mITT), excluding 11 patients found post-randomization to lack an LVO upon central imaging review. Post-randomization exclusions can break the randomized comparison if exclusion relates to assignment and outcome risk. Crossover changes the assignment-based estimand and may attenuate or exaggerate an estimate depending on timing, outcomes, and mechanisms; do not infer the per-protocol effect from its direction without appropriate methods.

### A3. Quantitative Reconstruction

Reconstructing the absolute effects: EVT yielded 43.4% independence versus 33.1% for control, an absolute increase of 10.3 percentage points (95% CI +1.9 to +18.7) and reciprocal NNT of about 10. The sICH point estimate is 6.2% versus 3.5%, an absolute increase of 2.7 points with interval −1.0 to +6.4. Its reciprocal is about 37 at the point estimate, but the interval includes no increase and possible harm; report the event counts and interval rather than presenting one NNH as settled.

### A4. Subgroups and Spin

The paper highlights a benefit in tandem lesions based on an unadjusted within-stratum p=0.04 but omits the interaction estimate and interval. Separate subgroup p-values do not test heterogeneity, while an interaction p-value neither proves biological heterogeneity nor does nonsignificance prove homogeneity. Treat this estimate as exploratory until its scale, prespecification, multiplicity, precision, plausibility, and replication are evaluated.

### A5. Bottom-Line Decision

- Decision: Conditional Act. Support late-window EVT strategy based on ASPECTS >= 6.
- Methodological caveat: The NNT of 10 justifies pathway integration, provided the local health system can replicate the rigid ASPECTS selection without inducing excessive false-positive transfers.
- What would change mind: Discovery of severe unblinding of the central mRS adjudicators, or a subsequent trial showing severe harm in the age > 80 subgroup.

## Autopsy B — The Observational Association (REHAB-FIRST)

### B1. Study Architecture and Clinical Stake

REHAB-FIRST is a fictional retrospective observational study utilizing a regional claims registry to assess stroke outcomes. The exposure is defined as admission to an inpatient rehabilitation facility (IRF) within 7 days of acute hospital discharge. The comparator is no IRF admission within 7 days. The primary outcome is 1-year all-cause mortality. The authors report an adjusted Hazard Ratio (HR) of 0.72 and conclude in the abstract that early intensive rehabilitation is 'life-saving.' The clinical stake is substantial: hospital administrators may use this metric to punish safety-net hospitals with longer IRF placement times or limited bed access.

### B2. Immortal Time Bias and Time-Zero Misalignment

This analysis is mathematically crippled by immortal time bias. Time-zero (cohort entry) is defined as acute hospital admission. However, to be classified as 'exposed,' a patient must survive the acute hospitalization, be discharged alive, and then survive up to 7 subsequent days to successfully enter an IRF. Patients who die on hospital day 4, or post-discharge day 2, are systematically allocated to the 'unexposed' cohort because they physically did not live long enough to receive the exposure. The exposed cohort is mathematically immortal during this prerequisite survival window. The Cox proportional hazards model, unaware of this time-dependent classification, improperly credits the exposure with preventing early deaths.

### B3. Target Trial Emulation

To emulate the target trial, define eligibility, assignment, and follow-up at a common time zero such as discharge. A 7-day treatment grace period requires a method that assigns comparable strategies without crediting survival time to future treatment; options include cloning, censoring, and weighting under explicit assumptions. A day-7 landmark answers a different survivor-population question. The reported HR of 0.72 mixes any treatment effect with immortal-time selection and confounding by functional reserve, illness severity, access, and socioeconomic factors, so it cannot support the stated causal estimate.

### B4. Bottom-Line Decision

- Decision: No Change. Reject the causal claim entirely. Do not use HR 0.72 in operational dashboards.
- Methodological veto: Fatal immortal time bias due to time-zero misalignment; uncontrolled confounding by indication and frailty.
- What would change mind: A rigorously designed target trial emulation utilizing a clone-censor-weight approach, or a cluster-randomized trial of early IRF pathways.

## Autopsy C — The Imaging AI Model (RapidLVO-Net)

### C1. Model Architecture and Clinical Stake

RapidLVO-Net describes a convolutional neural network designed for automated large vessel occlusion (LVO) detection on computed tomography angiography (CTA). The abstract broadcasts a test set AUROC of 0.96 and claims 'external validation' demonstrates outperformance over radiologists, implying readiness for autonomous triage and queue preemption. The clinical stake is whether to hardwire this algorithm into the acute stroke pathway, bypassing human radiology reads for immediate EVT team activation.

### C2. Prevalence, Bayes' Theorem, and PPV Collapse

The reported AUROC of 0.96 does not establish operational value because predictive values depend on prevalence. The synthetic test set is enriched to 18% LVO prevalence; with sensitivity 94% and specificity 91%, PPV is about 69%. Assume the intended local deployment population instead has 4% LVO prevalence; under that explicit synthetic assumption, PPV is about 30%, or roughly seven false alerts for every ten positive alerts. The workflow consequence must be evaluated prospectively rather than asserted from discrimination alone.

### C3. External Validation Gaps and Data Leakage

The purported external validation was conducted at a sister hospital sharing the same PACS vendor, CT scanner models, and trainee pool. It provides limited evidence for that closely related setting but does not establish stability across manufacturers, contrast protocols, or different patient spectra. Optimizing the threshold on the test set creates selection-induced optimism. NLP-derived report labels may also reproduce reporting errors and institutional terminology.

### C4. Bottom-Line Decision

- Decision: Watch. Autonomous triage is strictly contraindicated. Do not procure without prospective local validation.
- Methodological veto: PPV collapse at true clinical prevalence; pseudo-external validation; optimistic threshold tuning.
- Service action: Any pilot must run in silent-mode for 3 months to audit true PPV, with strict vascular neurology oversight.
- What would change mind: True external, multi-vendor prospective validation with a locked threshold, demonstrating workflow speedup without excessive false-positive alert burden.

## Autopsy D — The Non-Inferiority RCT (DUAL-SAFE)

### D1. Trial Architecture and Clinical Stake

DUAL-SAFE is a fictional, multicenter, randomized, double-blind trial evaluating whether a novel P2Y12 inhibitor is non-inferior to clopidogrel, each combined with aspirin, for 21 days following high-risk TIA or minor ischemic stroke. The primary efficacy endpoint is recurrent ischemic stroke at 90 days. The primary safety endpoint is major hemorrhage. The non-inferiority margin ($\Delta$) is pre-specified as a relative Hazard Ratio (HR) of 1.30. The clinical stake is massive: pharmaceutical adoption of a costly novel agent over generic clopidogrel hinges entirely on proving equivalent efficacy coupled with superior safety.

### D2. Assay Sensitivity and The Dilution Effect

Non-inferiority requires a clinically justified margin and credible assay sensitivity. DUAL-SAFE reports HR 1.08 (95% CI 0.89–1.28), whose upper bound lies below the prespecified 1.30 margin in this analysis. The lower-than-planned event rate reduces information and may widen uncertainty; it does not mechanically make non-inferiority easier. It should trigger an audit of population risk, adherence, endpoint ascertainment, constancy of the active comparator, power, and whether the margin remains clinically acceptable. If assay sensitivity is absent, two ineffective strategies can appear similar, so the confidence interval alone is not sufficient.

### D3. Intention-to-Treat vs. Per-Protocol Conflict

Assignment-based and per-protocol analyses target different estimands, and nonadherence, crossover, missingness, or exclusions can bias either comparison. Non-inferiority trials commonly present both prespecified assignment-based and appropriately defined per-protocol analyses, plus sensitivity analyses; a naive per-protocol analysis is neither universally mandatory nor automatically unbiased. Here the per-protocol CI (HR 1.18, 95% CI 0.94–1.36) crosses the 1.30 margin, so the non-inferiority conclusion is not robust across analysis sets and should be qualified.

### D4. Asymmetric Spin and Safety Superiority

The authors report fewer major hemorrhages (0.5% vs 1.2%, risk difference −0.7 percentage points; reciprocal ≈143). That absolute estimate and its uncertainty should be weighed against cost and the unresolved efficacy conclusion. The value of avoiding one major hemorrhage depends on bleed severity, treatment burden, ischemic uncertainty, and patient preferences; it cannot be reduced to a universal operational verdict.

### D5. Bottom-Line Decision

- Decision: No Change. Do not replace generic clopidogrel with the novel agent for routine secondary prevention.
- Methodological caveat: Non-inferiority is not robust across prespecified analyses; assay sensitivity and constancy remain unverified.
- What would change mind: A superiority trial in a high-risk, biomarker-confirmed atherosclerotic cohort demonstrating actual ischemic benefit.

## Autopsy E — The Prognostic Prediction Model (EPI-PREDICT)

### E1. Model Architecture and Clinical Stake

EPI-PREDICT is a fictional model of two-year unprovoked-seizure risk after MCA infarction. The teaching scenario assumes—rather than asserts as guideline fact—a 15% action threshold derived from explicit local estimates of seizure harm, treatment benefit, adverse effects, and patient preferences. Antiseizure-medication adverse effects vary by drug and patient; neither toxicity nor net benefit is certain.

### E2. Discrimination vs. Calibration

The paper reports AUROC 0.81, a ranking measure. For a random event/non-event pair, AUROC is the probability that the event case receives a higher score when there are no ties; conventional calculation gives half credit to ties. It does not measure absolute-risk accuracy. In the synthetic top decile, mean predicted risk is 40% and observed frequency 20%, showing substantial overprediction in that region; an interval and a flexible calibration curve are still needed.

### E3. Operationalizing Harm Without Decision Curve Analysis

Under the scenario’s synthetic 15% threshold, miscalibration could push patients across the modeled action boundary even when their observed risk is lower. Because the paper omits decision-curve or other utility analysis, net benefit remains unknown. A high C-statistic cannot repair miscalibrated absolute risks; deployment would require recalibration, explicit benefit-harm assumptions, local validation, and prospective impact evaluation.

### E4. Bottom-Line Decision

- Decision: Do not deploy. Reject clinical integration of the algorithm.
- Methodological veto: Severe calibration failure crossing the clinical decision threshold; absence of Net Benefit quantification.
- Service action: Educate house staff that AUROC is insufficient for prognostic model adoption.
- What would change mind: Model recalibration (e.g., using Platt scaling or isotonic regression) followed by prospective temporal validation demonstrating positive Net Benefit at the 15% threshold via DCA.

## Clinical and Epidemiologic Notes

Clinical note — Living Pathways. Use autopsy bottom lines to drive explicit operational ownership and expiration dates. Evidence is not static. CLEAR-PATH-style evidence should map directly to regional transfer agreements and night imaging capabilities. RapidLVO-Net-style papers should mandate local procurement governance, replacing fear-of-missing-out purchasing with rigid mathematical audits of positive predictive value.

Clinical note — Communicating Uncertainty to Patients. Patients, families, and hospital administrators deeply desire binary certainty. The physician's duty is to offer calibrated probabilistic language. State: 'This trial indicates offering EVT to patients in this state yields a 1 in 10 chance of additional independence, carrying a small but real risk of procedural hemorrhage.' Contrast this precision with the vague assertions of observational HRs: 'This rehab study is structurally incapable of proving mortality reduction; we will recommend rehab based on functional necessity, not this metric.'

Epidemiologic note — The Architecture of Estimands. An estimand defines the exact causal target of a trial. CLEAR-PATH targets the effect of assignment to an EVT strategy (Intention-to-Treat). REHAB-FIRST entirely fails to articulate a clear intervention estimand anchored to a specific time-zero. RapidLVO-Net targets a diagnostic classification parameter, not a causal treatment effect, yet its authors borrow the rhetoric of practice change appropriate only for randomized trials. Rigorous adherence to estimand definitions prevents severe category errors.

Epidemiologic note — Vectoring Bias Direction. State bias direction only when the causal structure and measurement process support it; otherwise label direction and magnitude uncertain. Immortal-time misclassification in REHAB-FIRST and test-set leakage in RapidLVO-Net plausibly favor the headline result, whereas the direction of crossover bias in CLEAR-PATH cannot be signed from crossover frequency alone.

Epidemiologic note — Transportability and Transport Causal Models. Source and target populations need not have identical effect-modifier distributions. Transport may be possible through standardization or weighting when the relevant modifiers are measured, treatment versions and outcomes are consistent, conditional effects are exchangeable across settings, and positivity holds. Assess those assumptions rather than demanding an exact distributional match.

## Pitfalls and Failure Modes

1. Confusing a Flawed Paper with a Disproven Hypothesis. Rejecting the REHAB-FIRST paper due to immortal time bias does not mean that early intensive rehabilitation is ineffective. It strictly means this specific evidentiary artifact cannot be used to prove it. Physicians frequently over-correct, adopting nihilism when confronted with poor methods. The hypothesis survives; the paper does not.

2. Letting P-Values Override Clinical Magnitude. A massive trial may produce a p-value of 0.001 for a 0.2% absolute risk reduction. Statistical significance alone must not dictate a pathway. Absolute effects and uncertainty are essential inputs, alongside harms, outcome importance, applicability, feasibility, cost, and patient values.

3. Ad Hominem Critique. The educational standard of the autopsy is absolute fairness to patients, which demands ruthless exactitude regarding methodology. It does not permit cruelty toward authors. A paper can be honest, well-intentioned, and still structurally incapable of justifying the practice change its abstract implies. Keep the critique restricted to the mathematics, the design geometry, and the causal map.

4. Acceptance of Asymmetric Spin. Authors frequently emphasize relative risk reductions for efficacy (which appear large) while switching to absolute risk increases for safety (which appear small). Standardize all metrics to absolute space prior to rendering judgment.

5. Blindness to Prevalence in Diagnostic AI. Recompute predictive values at the intended prevalence and evaluate the operational consequences of false alerts; AUROC or sensitivity alone cannot establish workflow value.


## Chapter summary

Paper autopsies synthesize isolated methodological concepts into comprehensive, defensible clinical judgments. Through the rigorous deconstruction of five distinct archetypes—the EVT RCT, the observational rehabilitation study, the AI imaging algorithm, the non-inferiority secondary prevention trial, and the prognostic prediction model—this chapter establishes a repeatable architecture for evidence appraisal. We demonstrated that absolute risk metrics routinely deflate relative hype, that immortal time bias manufactures spurious survival benefits, and that the Positive Predictive Value of AI models collapses under the weight of true clinical prevalence. Furthermore, we exposed how assay sensitivity failures dilute non-inferiority trials and how miscalibrated prediction models mechanize iatrogenic harm. The ultimate purpose of the autopsy is not mere critique, but the protection of the patient through the enforcement of epistemological discipline. By operationalizing evidence strictly through absolute effects and structural causal mapping, stroke neurologists can insulate their clinical pathways from both academic nihilism and commercial hype.

---

*Figures and tables in this chapter are Teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*
