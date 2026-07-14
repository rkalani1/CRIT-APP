#!/usr/bin/env python3
"""Wire unused original fig*.png assets into matching CRIT chapters."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURR = ROOT / "docs" / "curriculum"
FIG = ROOT / "docs" / "assets" / "figures"

# chapter file prefix -> list of (figure filename, caption)
MAP: dict[str, list[tuple[str, str]]] = {
    "01-": [
        ("fig01_reading_flow.png", "Decision-focused reading flow (original)."),
        ("fig10_appraisal_loop.png", "Appraisal loop for practice change (original)."),
    ],
    "02-": [("fig01_reading_flow.png", "Timed paper-reading pathway (original).")],
    "03-": [
        ("fig24_pico_estimand.png", "From PICO to target estimand (original)."),
        ("fig25_validity_transport.png", "Validity and transportability (original)."),
    ],
    "04-": [
        ("fig02_bias_taxonomy.png", "Bias taxonomy map (original)."),
        ("fig27_three_bias_families.png", "Three bias families (original)."),
    ],
    "05-": [
        ("fig03_dag_confounding.png", "Confounding structure (original)."),
        ("fig04_target_trial.png", "Target-trial thinking (original)."),
        ("fig11_collider.png", "Collider structure (original)."),
        ("fig61_confounder_mediator_collider.png", "Confounder–mediator–collider (original)."),
    ],
    "06-": [
        ("fig05_trial_pathway.png", "Trial pathway overview (original)."),
        ("fig26_consort_minded.png", "CONSORT-minded flow (teaching sketch; original)."),
        ("fig42_itt_vs_pp.png", "ITT versus per-protocol (original)."),
        ("fig81_consort_flow.png", "Flow sketch for trial reading (original)."),
    ],
    "07-": [
        ("fig12_immortal_time.png", "Immortal time structure (original)."),
        ("fig48_active_comparator.png", "Active-comparator new-user design (original)."),
        ("fig74_ps_overlap.png", "Propensity overlap intuition (original)."),
    ],
    "08-": [
        ("fig06_ppv_prevalence.png", "PPV depends on prevalence (original)."),
        ("fig28_lr_bayes_curves.png", "Likelihood-ratio / Bayes curves (original)."),
        ("fig49_diagnostic_2x2.png", "Diagnostic 2×2 (original)."),
        ("fig60_fagan_nomogram.png", "Fagan-style update sketch (original)."),
        ("fig53_spectrum_bias.png", "Spectrum bias (original)."),
        ("fig65_verification_bias.png", "Verification bias (original)."),
    ],
    "09-": [
        ("fig07_calibration.png", "Calibration plot concept (original)."),
        ("fig29_roc_vs_calibration.png", "ROC versus calibration (original)."),
        ("fig64_calibration_deciles.png", "Calibration by decile (original)."),
        ("fig52_decision_curve.png", "Decision-curve intuition (original)."),
    ],
    "10-": [
        ("fig23_forest_meta.png", "Forest plot teaching sketch (original)."),
        ("fig56_funnel.png", "Funnel plot concept (original)."),
        ("fig36_grade_certainty.png", "GRADE certainty ladder (original teaching)."),
        ("fig63_heterogeneity_forest.png", "Heterogeneity on a forest (original)."),
    ],
    "11-": [
        ("fig30_mrs_shift.png", "mRS shift concept (original)."),
        ("fig31_competing_risks.png", "Competing risks (original)."),
        ("fig22_survival_censoring.png", "Survival and censoring (original)."),
        ("fig59_cuminc_curve.png", "Cumulative incidence (original)."),
        ("fig89_km_atrisk.png", "Kaplan–Meier with at-risk table idea (original)."),
    ],
    "12-": [
        ("fig08_arr_nnt.png", "ARR and NNT (original)."),
        ("fig32_nnt_vs_baseline.png", "NNT versus baseline risk (original)."),
        ("fig70_absrel_baseline.png", "Absolute vs relative by baseline (original)."),
        ("fig80_icon_array.png", "Icon array for absolute effects (original)."),
    ],
    "13-": [
        ("fig33_hte_credibility.png", "HTE credibility (original)."),
        ("fig37_spin_detector.png", "Spin detector checklist graphic (original)."),
        ("fig66_subgroup_forest.png", "Subgroup forest caution (original)."),
    ],
    "14-": [
        ("fig34_ai_leakage.png", "AI leakage pathways (original)."),
        ("fig35_ai_site_shift.png", "Site shift for AI models (original)."),
    ],
    "15-": [
        ("fig09_journal_club.png", "Journal club roles (original)."),
        ("fig51_jc_roles.png", "Journal-club architecture (original)."),
    ],
    "16-": [("fig10_appraisal_loop.png", "Integrated autopsy loop (original).")],
    "17-": [
        ("fig18_occurrence_measures.png", "Occurrence measures (original)."),
    ],
    "18-": [
        ("fig20_counterfactual.png", "Counterfactual contrast (original)."),
        ("fig50_bradford_hill_questions.png", "Hill questions as probes (original)."),
        ("fig47_evalue.png", "E-value intuition (original)."),
    ],
    "19-": [
        ("fig21_estimation_ci.png", "Estimation and confidence intervals (original)."),
        ("fig43_ci_width_n.png", "CI width versus n (original)."),
        ("fig82_mid_vs_ci.png", "Point estimate versus interval (original)."),
    ],
    "20-": [
        ("fig55_table2_fallacy.png", "Table 2 fallacy (original)."),
        ("fig67_noncollapsibility.png", "Noncollapsibility sketch (original)."),
    ],
    "21-": [
        ("fig13_interaction_scales.png", "Interaction on different scales (original)."),
        ("fig19_standardization.png", "Standardization (original)."),
    ],
    "22-": [
        ("fig14_screening_biases.png", "Screening biases (original)."),
        ("fig57_nns_cascade.png", "Numbers needed to screen cascade (original)."),
        ("fig83_prevalence_reservoir.png", "Prevalence reservoir (original)."),
    ],
    "23-": [("fig15_dual_process.png", "Dual-process clinical reasoning (original).")],
    "24-": [
        ("fig16_therapy_harm_card.png", "Therapy and harm card (original)."),
        ("fig39_action_thresholds.png", "Action thresholds (original)."),
        ("fig71_action_thresholds2.png", "Thresholds for action (original)."),
    ],
    "25-": [
        ("fig46_cpr_lifecycle.png", "CPR lifecycle (original)."),
        ("fig73_roc_operating.png", "ROC operating point (original)."),
    ],
    "26-": [
        ("fig46_cpr_lifecycle.png", "Prediction-rule lifecycle (original)."),
        ("fig23_forest_meta.png", "Synthesis forest sketch (original)."),
    ],
    "27-": [
        ("fig17_fragility_missing.png", "Fragility and missingness (original)."),
        ("fig44_missingness_mechs.png", "Missingness mechanisms (original)."),
        ("fig45_multiplicity_tree.png", "Multiplicity tree (original)."),
    ],
    "28-": [
        ("fig41_pathway_decisions.png", "Pathway decisions (original)."),
        ("fig72_transportability.png", "Transportability (original)."),
        ("fig40_natural_frequencies.png", "Natural frequencies for communication (original)."),
    ],
}


def main() -> None:
    text_all = ""
    for p in CURR.glob("*.md"):
        text_all += p.read_text(encoding="utf-8")

    wired = 0
    for p in sorted(CURR.glob("*.md")):
        if p.name == "index.md":
            continue
        pref = p.name[:3]
        if pref not in MAP and not any(p.name.startswith(k.rstrip("-")) for k in MAP):
            # match by startswith key
            pass
        key = None
        for k in MAP:
            if p.name.startswith(k):
                key = k
                break
        if not key:
            continue
        t = p.read_text(encoding="utf-8")
        added = []
        for fname, cap in MAP[key]:
            if not (FIG / fname).exists():
                continue
            if fname in t:
                continue
            # add up to 2 new per chapter this pass to avoid bloat
            if len(added) >= 2:
                break
            block = f"\n![{cap}](../assets/figures/{fname})\n\n*{cap}*\n"
            if "## Opening" in t:
                # insert after first opening block end - append after first paragraph following Opening
                t = t.replace("## Opening\n", f"## Opening\n{block}", 1)
            else:
                t = block + t
            added.append(fname)
            wired += 1
        if added:
            p.write_text(t, encoding="utf-8")
            print(p.name, "added", added)
    print("WIRED", wired)


if __name__ == "__main__":
    main()
