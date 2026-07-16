#!/usr/bin/env python3
"""
Reproducible verification of worked numerical examples in the CRIT-APP ebook.
Exit 0 only if all checks pass. This is the shipped source of truth for math gates.
"""
from __future__ import annotations

import math
import sys


def near(a: float, b: float, tol: float = 1e-3) -> bool:
    return abs(a - b) <= tol


def fisher_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher p using the probability-at-most-observed convention."""
    row1, row2 = a + b, c + d
    event_total = a + c
    total = row1 + row2
    denominator = math.comb(total, event_total)

    def probability(x: int) -> float:
        return math.comb(row1, x) * math.comb(row2, event_total - x) / denominator

    observed = probability(a)
    lower = max(0, event_total - row2)
    upper = min(row1, event_total)
    return sum(
        probability(x)
        for x in range(lower, upper + 1)
        if probability(x) <= observed + 1e-15
    )


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # Ch03 favorable-outcome causal contrast
    p_control, p_treated = 0.25, 0.40
    favorable_rd = p_treated - p_control
    checks.append(("ch03_favorable_RD", near(favorable_rd, 0.15, 1e-12), f"{favorable_rd:.3f}"))
    checks.append(("ch03_favorable_NNT", near(1 / favorable_rd, 6.6667, 1e-3), f"{1/favorable_rd:.4f}"))

    # Ch05 synthetic confounding-by-indication table
    early_risk = (200 + 250) / (1000 + 5000)
    delayed_risk = (750 + 100) / (3000 + 1000)
    crude_arr = delayed_risk - early_risk
    checks.append(("ch05_early_risk", near(early_risk, 0.075, 1e-12), f"{early_risk:.4f}"))
    checks.append(("ch05_delayed_risk", near(delayed_risk, 0.2125, 1e-12), f"{delayed_risk:.4f}"))
    checks.append(("ch05_crude_ARR", near(crude_arr, 0.1375, 1e-12), f"{crude_arr:.4f}"))
    checks.append(("ch05_crude_NNT", near(1 / crude_arr, 7.2727, 1e-3), f"{1/crude_arr:.4f}"))

    # Ch06 synthetic reperfusion trial
    evt_favorable, evt_total = 528, 1200
    ctl_favorable, ctl_total = 384, 1200
    evt_risk, ctl_risk = evt_favorable / evt_total, ctl_favorable / ctl_total
    evt_rd = evt_risk - ctl_risk
    evt_rr = evt_risk / ctl_risk
    evt_or = (528 / 672) / (384 / 816)
    checks.append(("ch06_EVT_RD", near(evt_rd, 0.12, 1e-12), f"{evt_rd:.4f}"))
    checks.append(("ch06_EVT_NNT", near(1 / evt_rd, 8.3333, 1e-3), f"{1/evt_rd:.4f}"))
    checks.append(("ch06_EVT_RR", near(evt_rr, 1.375, 1e-12), f"{evt_rr:.4f}"))
    checks.append(("ch06_EVT_OR", near(evt_or, 1.669, 1e-3), f"{evt_or:.4f}"))
    checks.append(("ch06_sICH_NNH", near(1 / (0.05 - 0.02), 33.3333, 1e-3), f"{1/(0.05-0.02):.4f}"))

    # Ch08 synthetic LVO-screen 2x2 and 5% deployment update
    tp, fn, fp, tn = 120, 30, 160, 690
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    lr_pos = sensitivity / (1 - specificity)
    lr_neg = (1 - sensitivity) / specificity
    post_pos_odds = (0.05 / 0.95) * lr_pos
    post_neg_odds = (0.05 / 0.95) * lr_neg
    checks.append(("ch08_sensitivity", near(sensitivity, 0.80, 1e-12), f"{sensitivity:.4f}"))
    checks.append(("ch08_specificity", near(specificity, 0.8118, 1e-4), f"{specificity:.4f}"))
    checks.append(("ch08_PPV", near(ppv, 0.4286, 1e-4), f"{ppv:.4f}"))
    checks.append(("ch08_NPV", near(npv, 0.9583, 1e-4), f"{npv:.4f}"))
    checks.append(("ch08_LR_pos", near(lr_pos, 4.25, 1e-12), f"{lr_pos:.4f}"))
    checks.append(("ch08_LR_neg", near(lr_neg, 0.2464, 1e-4), f"{lr_neg:.4f}"))
    checks.append(("ch08_post_pos_5pct", near(post_pos_odds / (1 + post_pos_odds), 0.1828, 2e-4), f"{post_pos_odds/(1+post_pos_odds):.4f}"))
    checks.append(("ch08_post_neg_5pct", near(post_neg_odds / (1 + post_neg_odds), 0.0128, 2e-4), f"{post_neg_odds/(1+post_neg_odds):.4f}"))

    # Ch27 synthetic fragility-index example (two-sided Fisher exact test)
    p_initial = fisher_two_sided(40, 160, 22, 178)
    p_three_flips = fisher_two_sided(40, 160, 25, 175)
    checks.append(("ch27_fisher_initial", near(p_initial, 0.018316, 1e-6), f"{p_initial:.6f}"))
    checks.append(("ch27_fisher_three_flips", near(p_three_flips, 0.057172, 1e-6), f"{p_three_flips:.6f}"))

    # Ch17 synthetic association table
    r1, r0 = 0.10, 0.05
    checks.append(("ch17_RD", near(r1 - r0, 0.05, 1e-12), f"{r1-r0}"))
    checks.append(("ch17_RR", near(r1 / r0, 2.0, 1e-12), f"{r1/r0}"))
    or_ = (40 / 360) / (30 / 570)
    checks.append(("ch17_OR", near(or_, 2.111, 0.01), f"{or_:.4f}"))

    # NNT teaching
    checks.append(("nnt_50", near(1 / 0.02, 50, 1e-12), str(1 / 0.02)))

    # Bayes LR+ = 5, prior 0.2
    prior, lr = 0.2, 5.0
    odds = prior / (1 - prior)
    post = (odds * lr) / (1 + odds * lr)
    checks.append(("bayes_post", near(post, 5 / 9, 1e-9), f"{post:.6f}"))

    # Ch12 OR for p_c=0.40, p_t=0.60 → OR = (0.6/0.4)/(0.4/0.6) = 2.25
    pc, pt = 0.40, 0.60
    or12 = (pt / (1 - pt)) / (pc / (1 - pc))
    checks.append(("ch12_OR", near(or12, 2.25, 1e-9), f"{or12}"))

    # Ch10 DAPT inverse-variance fixed-effect meta (full recompute from counts)
    # Study 1
    a1, n1t, c1, n1c = 200, 2500, 300, 2500
    rr1 = (a1 / n1t) / (c1 / n1c)
    ln1 = math.log(rr1)
    se1_sq = 1 / a1 - 1 / n1t + 1 / c1 - 1 / n1c
    w1 = 1 / se1_sq
    # Study 2
    a2, n2t, c2, n2c = 120, 2000, 160, 2000
    rr2 = (a2 / n2t) / (c2 / n2c)
    ln2 = math.log(rr2)
    se2_sq = 1 / a2 - 1 / n2t + 1 / c2 - 1 / n2c
    w2 = 1 / se2_sq
    wsum = w1 + w2
    ln_pool = (w1 * ln1 + w2 * ln2) / wsum
    se_pool = math.sqrt(1 / wsum)
    rr_pool = math.exp(ln_pool)
    lo = math.exp(ln_pool - 1.96 * se_pool)
    hi = math.exp(ln_pool + 1.96 * se_pool)
    # Published book values after consistent rounding
    checks.append(("ch10_rr1", near(rr1, 0.6667, 1e-3), f"{rr1:.4f}"))
    checks.append(("ch10_rr2", near(rr2, 0.75, 1e-3), f"{rr2:.4f}"))
    checks.append(("ch10_pool_rr", near(rr_pool, 0.695, 0.005), f"{rr_pool:.4f}"))
    checks.append(("ch10_ci_lo", near(lo, 0.607, 0.01), f"{lo:.3f}"))
    checks.append(("ch10_ci_hi", near(hi, 0.796, 0.01), f"{hi:.3f}"))
    # ARR/NNT at CER 10%
    arr = 0.10 * (1 - rr_pool)
    nnt = 1 / arr
    checks.append(("ch10_arr10", near(arr, 0.0305, 0.001), f"{arr:.4f}"))
    checks.append(("ch10_nnt10", near(nnt, 33, 1.0), f"{nnt:.1f}"))

    # Ch09 REPERFUSE-3 grouped calibration example
    expected_events = 300 * 0.05 + 400 * 0.15 + 200 * 0.40 + 100 * 0.85
    observed_events = 15 + 80 + 90 + 85
    oe_ratio = observed_events / expected_events
    checks.append(("ch09_expected_events", near(expected_events, 240, 1e-12), f"{expected_events:.0f}"))
    checks.append(("ch09_observed_events", near(observed_events, 270, 1e-12), f"{observed_events:.0f}"))
    checks.append(("ch09_oe_ratio", near(oe_ratio, 1.125, 1e-12), f"{oe_ratio:.3f}"))

    # Ch11 two-interval competing-risk illustration
    net_risk = 1 - (1 - 40 / 1000) * (1 - 25 / 900)
    cumulative_incidence = 40 / 1000 + (900 / 1000) * (25 / 900)
    checks.append(("ch11_net_risk", near(net_risk, 0.066667, 1e-6), f"{net_risk:.6f}"))
    checks.append(("ch11_cif", near(cumulative_incidence, 0.065, 1e-12), f"{cumulative_incidence:.6f}"))

    failed = 0
    for name, ok, detail in checks:
        status = "PASS" if ok else "FAIL"
        print(f"{status} {name} {detail}")
        if not ok:
            failed += 1
    if failed:
        print(f"FAILED {failed}")
        return 1
    print("ALL_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
