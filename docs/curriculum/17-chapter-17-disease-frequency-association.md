# Chapter 17. Disease Frequency and Association

## Opening

![Occurrence measures.](../assets/figures/fig18_occurrence_measures.png)

*Occurrence measures.*

Epidemiology rounds put crude incidence next to a relative risk. Stop the category error: frequency grammar first, then association, then cause.

![Incidence versus prevalence teaching diagram.](../assets/figures/crit_fig_incidence_prevalence.png)

*Incidence focuses on new events in a time window; prevalence counts who lives with the condition now.*

## Learning objectives

- Define incidence, prevalence, and cumulative risk with explicit time windows.
- Distinguish absolute frequency from relative association measures.
- Compute and interpret risk difference, risk ratio, and odds ratio on synthetic tables.
- Explain why prevalence is a poor stand-in for incidence in dynamic stroke pathways.
- Identify selection and measurement structures that distort frequency estimates.
- Translate association language into prediction vs causation templates before acting.

## Conceptual core: frequency first

**Incidence** answers: how often do *new* events occur in a defined population
at risk over a defined time? Stroke services live on incidence thinking—codes
per week, EVT candidates per month, ICH admissions per year—because operations
and prevention programs care about *new* events.

**Prevalence** answers: how many people *currently* live with a condition or
history? Prevalence mixes incidence with duration and survival. A rise in
prevalence of “prior stroke” in a clinic panel can reflect better survival,
aging, or coding practices—not necessarily a surge in new strokes.

**Cumulative risk** (incidence proportion) over a fixed window (30 days, 90 days,
1 year) is often what trial arms and quality dashboards actually report.

## Association measures (synthetic teaching table)

Imagine a simplified 90-day cohort of **1,000** high-risk TIA/minor stroke patients:

| Group | n | Recurrent ischemic stroke | Risk |
|-------|---:|--------------------------:|-----:|
| Exposed (example risk factor present) | 400 | 40 | 0.10 |
| Unexposed | 600 | 30 | 0.05 |

- **Risk difference (RD)** = \(0.10 - 0.05 = 0.05\) (5 percentage points).  
- **Risk ratio (RR)** = \(0.10 / 0.05 = 2.0\).  
- **Odds ratio (OR)** = \((40/360) / (30/570) \approx 2.11\).

Same table, three stories: absolute burden (RD), multiplicative association (RR),
and a slightly larger OR typical when outcomes are not rare. Bedside counseling
needs the **absolute** story; meta-analysis math often travels in RR/OR space.

*Teaching figure (synthetic).* Hold the risk ratio fixed at 2.0 while unexposed risk climbs: the odds ratio inflates as the outcome becomes common. The right panel restates the chapter 2×2 (RD 5 pp, RR 2.0, OR ≈ 2.11). Use RD for counseling; treat OR ≈ RR only when events are rare.

## Pitfalls specific to neurology and stroke data

1. **Wrong denominator** — counting only admitted patients when the research
   question is population incidence.
2. **Index-time chaos** — starting follow-up at hospital discharge instead of
   symptom onset can manufacture immortal time or miss early recurrence.
3. **Coding ≠ phenotype** — ICD-based “stroke” bundles ischemic stroke, TIA
   miscodes, and sequelae visits.
4. **Competing risks** — death prevents observation of later recurrent stroke;
   crude cumulative incidence can mislead if mortality is high (ICH, elderly EVT).
5. **Standardization ignored** — crude rates compared across young vs older
   regions look like quality differences when they are demography.

## Clinical and epidemiologic notes

- When a paper says “associated with,” force the sentence into either a
  **prediction** template (“among patients like these, factor X forecasts Y”)
  or a **causal** template (“intervening on X would change Y”). Frequency and
  association alone do not license pathway changes.
- Quality dashboards that show only relative changes (“−20%”) without baseline
  rates invite false urgency or false reassurance.
- Transportability: a risk ratio from a trial-eligible LVO population does not
  automatically transfer to an unselected ED census.

## Worked micro-example (absolute vs relative)

Baseline 90-day risk 8% → 6% under a hypothetical strategy:

- Relative risk reduction = \((0.08-0.06)/0.08 = 25\%\).  
- Absolute risk reduction = \(2\%\).  
- NNT ≈ \(1/0.02 = 50\).

![Icon array for NNT 50.](../assets/figures/crit_fig_nnt_icon_array.png)

*One highlighted person among fifty: absolute benefit intuition for NNT 50.*

Press releases love 25%. Shared decisions need 2% and NNT 50—plus harm metrics
on the same absolute scale.

## Rate vs risk (precision language)

A **risk** (incidence proportion) needs a closed cohort and a fixed window: “8% had
recurrent stroke by day 90.” A **rate** (incidence rate) needs person-time: “12 events
per 100 person-years.” Mixing them produces nonsense comparisons—for example, quoting
an annualized rate next to a 90-day trial risk without conversion.

In hyperacute stroke care, short-window risks dominate (door-to-needle, 24-hour sICH,
90-day mRS). In secondary prevention, person-time rates reappear. Appraisal asks which
clock the authors actually used and whether the comparator used the same clock.

*Teaching figure (synthetic).* Each horizontal line is a patient contributing person-time until an incident event (X) or administrative/censor end (square). Incidence density = events ÷ person-years (here ≈ 0.67 per person-year). Do not quote this rate next to a closed-cohort 90-day risk without conversion. Frequency grammar is not causation: association tables still need a prediction-vs-cause sentence before pathway change.

*Teaching figure (synthetic).* A constant incidence rate of 0.20 per person-year maps to very different cumulative risks at 30, 90, 180, and 365 days. The naive “rate × time” shortcut overstates risk at longer horizons. When a secondary-prevention abstract quotes events per 100 person-years next to a 90-day trial risk, demand conversion onto one clock before comparing.

## From association table to decision sentence

After computing RD/RR/OR, force one sentence:

- **Descriptive / predictive:** “Among patients like these, factor X marks higher
  90-day recurrence risk (RD = 5 percentage points).”
- **Causal (only if design supports):** “Assigning treatment A versus C changes
  90-day recurrence by RD = … under assumptions S.”

If the paper’s methods cannot carry the causal sentence, do not let the discussion
section smuggle it in.


![Forest plot of study-specific estimates and confidence intervals around a heterogeneous pooled effect.](../assets/figures/fig63_heterogeneity_forest.png)

*Teaching graphic (fig63_heterogeneity_forest.png).*

## Chapter summary

Disease frequency is the grammar of epidemiology; association measures are the
verbs. Read every claim with a clock (time window), a denominator (who is at
risk), and an absolute scale (how many events per hundred). Only then ask
whether the design supports prediction, description, or cause.

## Practice and reflection

1. Rewrite a relative-risk abstract sentence into RD and NNT using made-up but
   explicit baselines.
2. List two reasons prevalence of atrial fibrillation in a stroke clinic can
   rise without incidence rising.
3. Draw a 2×2 table for a synthetic ICH expansion study and compute RR and RD.
4. Identify a competing risk that would break a naive Kaplan–Meier for
   “time to recurrent stroke.”
5. For tomorrow’s journal club paper, write one prediction-template sentence
   and one causal-template sentence; mark which the paper actually supports.

---

*Figures and tables in this chapter are original teaching materials for CRIT-APP
unless a caption explicitly states otherwise. Methods standards are cited by name only.*
