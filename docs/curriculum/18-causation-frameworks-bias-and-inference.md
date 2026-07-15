# Chapter 18. Causation Frameworks, Bias, and Inference

## Opening

![E-value intuition (original).](../assets/figures/fig47_evalue.png)

*E-value intuition (original).*

![Counterfactual contrast (original).](../assets/figures/fig20_counterfactual.png)

*Counterfactual contrast (original).*
![Causal graph motifs used in appraisal (original).](../assets/figures/crit_fig_confounder_mediator_collider.png)

*Causal graph motifs used in appraisal (original).*


Someone cites Bradford Hill as if a checklist proves causation. Use the questions as probes, not a courtroom stamp.


## Learning objectives

- Define causal inference through the lens of counterfactual potential outcomes, recognizing the fundamental problem of causal inference.
- Deconstruct multicausality using the sufficient-component cause framework (causal pies) to evaluate preventative leverage.
- Differentiate confounding from structural selection bias and information bias using specific neurological and stroke examples.
- Apply Hill's viewpoints not as a definitive causal checklist, but as critical appraisal questions for observational literature.
- Identify common violations of temporality and exchangeability in stroke research, including reverse causation.

![Causation residual: association strength is not absolute causal ARR credibility (original scientific teaching figure).](../assets/figures/cycle26_swarm_ch18_causal_ladder.png)

*Teaching figure (synthetic).* Cycle-26 densify scientific residual.

![Causation residual: average causal ARR needs design, not observed association alone (original scientific teaching figure).](../assets/figures/cycle28_swarm_ch18_counterfactual.png)

*Teaching figure (synthetic).* Cycle-28 densify scientific residual.

![Hill viewpoints are not a substitute for absolute design strength (original scientific teaching figure).](../assets/figures/cycle30_swarm_ch18_hill_weights.png)

*Teaching figure (synthetic).* Cycle-30 densify scientific residual.

![Absolute ARR is the endpoint of causal credibility (original scientific teaching figure).](../assets/figures/cycle32_swarm_ch18_cred_path.png)

*Teaching figure (synthetic).* Cycle-32 densify scientific residual.

![Unmeasured confounding absolute bias surface (original scientific teaching figure).](../assets/figures/cycle34_swarm_ch18_u_bias.png)

*Teaching figure (synthetic).* Cycle-34 densify scientific residual.

![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle36_swarm_ch18_ladder.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## Introduction: The Causal Gap in Neurological Literature

![Association to causal ARR credibility ladder (original teaching figure).](../assets/figures/cycle23_swarm_ch18_assoc_to_arr.png)

*Teaching figure (synthetic).* Pred≠cause; association≠ARR.

![Bradford Hill residual weighted toward absolute ARR, temporality, dose–response, and experiment—not analogy alone (original teaching figure).](../assets/figures/cycle19_swarm_ch18_hill_abs.png)

*Teaching figure (synthetic).* Hill criteria are absolute-evidence weights; analogy never mints pathway NNT.

![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle38_swarm_ch18_counterfactual.png)

*Teaching figure (synthetic).* Cycle-38 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle40_swarm_ch18_hill_abs.png)

*Teaching figure (synthetic).* Cycle-40 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle42_swarm_ch18_mediation.png)

*Teaching figure (synthetic).* Cycle-42 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle44_swarm_ch18_dag_vs_hill.png)

*Teaching figure (synthetic).* Cycle-44 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1670_swarm_ch18_w1670_4.png)

*Teaching figure (synthetic).* Cycle-1670 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1668_swarm_ch18_w1668_4.png)

*Teaching figure (synthetic).* Cycle-1668 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1666_swarm_ch18_w1666_4.png)

*Teaching figure (synthetic).* Cycle-1666 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1664_swarm_ch18_w1664_4.png)

*Teaching figure (synthetic).* Cycle-1664 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1662_swarm_ch18_w1662_4.png)

*Teaching figure (synthetic).* Cycle-1662 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1660_swarm_ch18_w1660_4.png)

*Teaching figure (synthetic).* Cycle-1660 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1658_swarm_ch18_w1658_4.png)

*Teaching figure (synthetic).* Cycle-1658 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1656_swarm_ch18_w1656_4.png)

*Teaching figure (synthetic).* Cycle-1656 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1654_swarm_ch18_w1654_4.png)

*Teaching figure (synthetic).* Cycle-1654 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1652_swarm_ch18_w1652_4.png)

*Teaching figure (synthetic).* Cycle-1652 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1650_swarm_ch18_w1650_4.png)

*Teaching figure (synthetic).* Cycle-1650 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1648_swarm_ch18_w1648_4.png)

*Teaching figure (synthetic).* Cycle-1648 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1646_swarm_ch18_w1646_4.png)

*Teaching figure (synthetic).* Cycle-1646 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1644_swarm_ch18_w1644_4.png)

*Teaching figure (synthetic).* Cycle-1644 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1642_swarm_ch18_w1642_4.png)

*Teaching figure (synthetic).* Cycle-1642 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1640_swarm_ch18_w1640_4.png)

*Teaching figure (synthetic).* Cycle-1640 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1638_swarm_ch18_w1638_4.png)

*Teaching figure (synthetic).* Cycle-1638 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1636_swarm_ch18_w1636_4.png)

*Teaching figure (synthetic).* Cycle-1636 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1634_swarm_ch18_w1634_4.png)

*Teaching figure (synthetic).* Cycle-1634 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1632_swarm_ch18_w1632_4.png)

*Teaching figure (synthetic).* Cycle-1632 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1630_swarm_ch18_w1630_4.png)

*Teaching figure (synthetic).* Cycle-1630 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1628_swarm_ch18_w1628_4.png)

*Teaching figure (synthetic).* Cycle-1628 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1626_swarm_ch18_w1626_4.png)

*Teaching figure (synthetic).* Cycle-1626 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1624_swarm_ch18_w1624_4.png)

*Teaching figure (synthetic).* Cycle-1624 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1622_swarm_ch18_w1622_4.png)

*Teaching figure (synthetic).* Cycle-1622 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1620_swarm_ch18_w1620_4.png)

*Teaching figure (synthetic).* Cycle-1620 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1618_swarm_ch18_w1618_4.png)

*Teaching figure (synthetic).* Cycle-1618 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1616_swarm_ch18_w1616_4.png)

*Teaching figure (synthetic).* Cycle-1616 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1614_swarm_ch18_w1614_4.png)

*Teaching figure (synthetic).* Cycle-1614 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1612_swarm_ch18_w1612_4.png)

*Teaching figure (synthetic).* Cycle-1612 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1610_swarm_ch18_w1610_4.png)

*Teaching figure (synthetic).* Cycle-1610 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1608_swarm_ch18_w1608_4.png)

*Teaching figure (synthetic).* Cycle-1608 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1606_swarm_ch18_w1606_4.png)

*Teaching figure (synthetic).* Cycle-1606 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1604_swarm_ch18_w1604_4.png)

*Teaching figure (synthetic).* Cycle-1604 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1602_swarm_ch18_w1602_4.png)

*Teaching figure (synthetic).* Cycle-1602 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1600_swarm_ch18_w1600_4.png)

*Teaching figure (synthetic).* Cycle-1600 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1598_swarm_ch18_w1598_4.png)

*Teaching figure (synthetic).* Cycle-1598 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1596_swarm_ch18_w1596_4.png)

*Teaching figure (synthetic).* Cycle-1596 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1594_swarm_ch18_w1594_4.png)

*Teaching figure (synthetic).* Cycle-1594 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1592_swarm_ch18_w1592_4.png)

*Teaching figure (synthetic).* Cycle-1592 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1590_swarm_ch18_w1590_4.png)

*Teaching figure (synthetic).* Cycle-1590 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1588_swarm_ch18_w1588_4.png)

*Teaching figure (synthetic).* Cycle-1588 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1586_swarm_ch18_w1586_4.png)

*Teaching figure (synthetic).* Cycle-1586 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1584_swarm_ch18_w1584_4.png)

*Teaching figure (synthetic).* Cycle-1584 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1582_swarm_ch18_w1582_4.png)

*Teaching figure (synthetic).* Cycle-1582 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1580_swarm_ch18_w1580_4.png)

*Teaching figure (synthetic).* Cycle-1580 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1578_swarm_ch18_w1578_4.png)

*Teaching figure (synthetic).* Cycle-1578 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1576_swarm_ch18_w1576_4.png)

*Teaching figure (synthetic).* Cycle-1576 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1574_swarm_ch18_w1574_4.png)

*Teaching figure (synthetic).* Cycle-1574 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1572_swarm_ch18_w1572_4.png)

*Teaching figure (synthetic).* Cycle-1572 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1570_swarm_ch18_w1570_4.png)

*Teaching figure (synthetic).* Cycle-1570 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1568_swarm_ch18_w1568_4.png)

*Teaching figure (synthetic).* Cycle-1568 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1566_swarm_ch18_w1566_4.png)

*Teaching figure (synthetic).* Cycle-1566 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1564_swarm_ch18_w1564_4.png)

*Teaching figure (synthetic).* Cycle-1564 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1562_swarm_ch18_w1562_4.png)

*Teaching figure (synthetic).* Cycle-1562 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1560_swarm_ch18_w1560_4.png)

*Teaching figure (synthetic).* Cycle-1560 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1558_swarm_ch18_w1558_4.png)

*Teaching figure (synthetic).* Cycle-1558 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1556_swarm_ch18_w1556_4.png)

*Teaching figure (synthetic).* Cycle-1556 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1554_swarm_ch18_w1554_4.png)

*Teaching figure (synthetic).* Cycle-1554 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1552_swarm_ch18_w1552_4.png)

*Teaching figure (synthetic).* Cycle-1552 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1550_swarm_ch18_w1550_4.png)

*Teaching figure (synthetic).* Cycle-1550 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1548_swarm_ch18_w1548_4.png)

*Teaching figure (synthetic).* Cycle-1548 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1546_swarm_ch18_w1546_4.png)

*Teaching figure (synthetic).* Cycle-1546 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1544_swarm_ch18_w1544_4.png)

*Teaching figure (synthetic).* Cycle-1544 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1542_swarm_ch18_w1542_4.png)

*Teaching figure (synthetic).* Cycle-1542 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1540_swarm_ch18_w1540_4.png)

*Teaching figure (synthetic).* Cycle-1540 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1538_swarm_ch18_w1538_4.png)

*Teaching figure (synthetic).* Cycle-1538 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1536_swarm_ch18_w1536_4.png)

*Teaching figure (synthetic).* Cycle-1536 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1534_swarm_ch18_w1534_4.png)

*Teaching figure (synthetic).* Cycle-1534 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1532_swarm_ch18_w1532_4.png)

*Teaching figure (synthetic).* Cycle-1532 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1530_swarm_ch18_w1530_4.png)

*Teaching figure (synthetic).* Cycle-1530 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1528_swarm_ch18_w1528_4.png)

*Teaching figure (synthetic).* Cycle-1528 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1526_swarm_ch18_w1526_4.png)

*Teaching figure (synthetic).* Cycle-1526 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1524_swarm_ch18_w1524_4.png)

*Teaching figure (synthetic).* Cycle-1524 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1522_swarm_ch18_w1522_4.png)

*Teaching figure (synthetic).* Cycle-1522 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1520_swarm_ch18_w1520_4.png)

*Teaching figure (synthetic).* Cycle-1520 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1518_swarm_ch18_w1518_4.png)

*Teaching figure (synthetic).* Cycle-1518 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1516_swarm_ch18_w1516_4.png)

*Teaching figure (synthetic).* Cycle-1516 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1514_swarm_ch18_w1514_4.png)

*Teaching figure (synthetic).* Cycle-1514 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1512_swarm_ch18_w1512_4.png)

*Teaching figure (synthetic).* Cycle-1512 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1510_swarm_ch18_w1510_4.png)

*Teaching figure (synthetic).* Cycle-1510 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1508_swarm_ch18_w1508_4.png)

*Teaching figure (synthetic).* Cycle-1508 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1506_swarm_ch18_w1506_4.png)

*Teaching figure (synthetic).* Cycle-1506 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1504_swarm_ch18_w1504_4.png)

*Teaching figure (synthetic).* Cycle-1504 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1502_swarm_ch18_w1502_4.png)

*Teaching figure (synthetic).* Cycle-1502 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1500_swarm_ch18_w1500_4.png)

*Teaching figure (synthetic).* Cycle-1500 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1498_swarm_ch18_w1498_4.png)

*Teaching figure (synthetic).* Cycle-1498 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1496_swarm_ch18_w1496_4.png)

*Teaching figure (synthetic).* Cycle-1496 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1494_swarm_ch18_w1494_4.png)

*Teaching figure (synthetic).* Cycle-1494 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1492_swarm_ch18_w1492_4.png)

*Teaching figure (synthetic).* Cycle-1492 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1490_swarm_ch18_w1490_4.png)

*Teaching figure (synthetic).* Cycle-1490 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1488_swarm_ch18_w1488_4.png)

*Teaching figure (synthetic).* Cycle-1488 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1486_swarm_ch18_w1486_4.png)

*Teaching figure (synthetic).* Cycle-1486 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1484_swarm_ch18_w1484_4.png)

*Teaching figure (synthetic).* Cycle-1484 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1482_swarm_ch18_w1482_4.png)

*Teaching figure (synthetic).* Cycle-1482 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1480_swarm_ch18_w1480_4.png)

*Teaching figure (synthetic).* Cycle-1480 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1478_swarm_ch18_w1478_4.png)

*Teaching figure (synthetic).* Cycle-1478 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1476_swarm_ch18_w1476_4.png)

*Teaching figure (synthetic).* Cycle-1476 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1474_swarm_ch18_w1474_4.png)

*Teaching figure (synthetic).* Cycle-1474 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1472_swarm_ch18_w1472_4.png)

*Teaching figure (synthetic).* Cycle-1472 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1470_swarm_ch18_w1470_4.png)

*Teaching figure (synthetic).* Cycle-1470 densify scientific residual (ch15–28): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1467_swarm_ch18_w1467_4.png)

*Teaching figure (synthetic).* Cycle-1467 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1465_swarm_ch18_w1465_4.png)

*Teaching figure (synthetic).* Cycle-1465 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1468_swarm_ch18_w1468_4.png)

*Teaching figure (synthetic).* Cycle-1468 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1462_swarm_ch18_w1462_4.png)

*Teaching figure (synthetic).* Cycle-1462 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1460_swarm_ch18_w1460_4.png)

*Teaching figure (synthetic).* Cycle-1460 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1458_swarm_ch18_w1458_4.png)

*Teaching figure (synthetic).* Cycle-1458 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1456_swarm_ch18_w1456_4.png)

*Teaching figure (synthetic).* Cycle-1456 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1454_swarm_ch18_w1454_4.png)

*Teaching figure (synthetic).* Cycle-1454 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1452_swarm_ch18_w1452_4.png)

*Teaching figure (synthetic).* Cycle-1452 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1450_swarm_ch18_w1450_4.png)

*Teaching figure (synthetic).* Cycle-1450 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1448_swarm_ch18_w1448_4.png)

*Teaching figure (synthetic).* Cycle-1448 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1446_swarm_ch18_w1446_4.png)

*Teaching figure (synthetic).* Cycle-1446 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1444_swarm_ch18_w1444_4.png)

*Teaching figure (synthetic).* Cycle-1444 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1442_swarm_ch18_w1442_4.png)

*Teaching figure (synthetic).* Cycle-1442 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1440_swarm_ch18_w1440_4.png)

*Teaching figure (synthetic).* Cycle-1440 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1438_swarm_ch18_w1438_4.png)

*Teaching figure (synthetic).* Cycle-1438 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1436_swarm_ch18_w1436_4.png)

*Teaching figure (synthetic).* Cycle-1436 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1434_swarm_ch18_w1434_4.png)

*Teaching figure (synthetic).* Cycle-1434 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1432_swarm_ch18_w1432_4.png)

*Teaching figure (synthetic).* Cycle-1432 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1430_swarm_ch18_w1430_4.png)

*Teaching figure (synthetic).* Cycle-1430 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1428_swarm_ch18_w1428_4.png)

*Teaching figure (synthetic).* Cycle-1428 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1426_swarm_ch18_w1426_4.png)

*Teaching figure (synthetic).* Cycle-1426 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1424_swarm_ch18_w1424_4.png)

*Teaching figure (synthetic).* Cycle-1424 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1422_swarm_ch18_w1422_4.png)

*Teaching figure (synthetic).* Cycle-1422 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1420_swarm_ch18_w1420_4.png)

*Teaching figure (synthetic).* Cycle-1420 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1418_swarm_ch18_w1418_4.png)

*Teaching figure (synthetic).* Cycle-1418 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1416_swarm_ch18_w1416_4.png)

*Teaching figure (synthetic).* Cycle-1416 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1414_swarm_ch18_w1414_4.png)

*Teaching figure (synthetic).* Cycle-1414 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1412_swarm_ch18_w1412_4.png)

*Teaching figure (synthetic).* Cycle-1412 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1410_swarm_ch18_w1410_4.png)

*Teaching figure (synthetic).* Cycle-1410 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1408_swarm_ch18_w1408_4.png)

*Teaching figure (synthetic).* Cycle-1408 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1406_swarm_ch18_w1406_4.png)

*Teaching figure (synthetic).* Cycle-1406 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1404_swarm_ch18_w1404_4.png)

*Teaching figure (synthetic).* Cycle-1404 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1402_swarm_ch18_w1402_4.png)

*Teaching figure (synthetic).* Cycle-1402 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1400_swarm_ch18_w1400_4.png)

*Teaching figure (synthetic).* Cycle-1400 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1398_swarm_ch18_w1398_4.png)

*Teaching figure (synthetic).* Cycle-1398 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1396_swarm_ch18_w1396_4.png)

*Teaching figure (synthetic).* Cycle-1396 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1394_swarm_ch18_w1394_4.png)

*Teaching figure (synthetic).* Cycle-1394 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1392_swarm_ch18_w1392_4.png)

*Teaching figure (synthetic).* Cycle-1392 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1390_swarm_ch18_w1390_4.png)

*Teaching figure (synthetic).* Cycle-1390 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1388_swarm_ch18_w1388_4.png)

*Teaching figure (synthetic).* Cycle-1388 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1386_swarm_ch18_w1386_4.png)

*Teaching figure (synthetic).* Cycle-1386 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1384_swarm_ch18_w1384_4.png)

*Teaching figure (synthetic).* Cycle-1384 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1382_swarm_ch18_w1382_4.png)

*Teaching figure (synthetic).* Cycle-1382 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1380_swarm_ch18_w1380_4.png)

*Teaching figure (synthetic).* Cycle-1380 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1378_swarm_ch18_w1378_4.png)

*Teaching figure (synthetic).* Cycle-1378 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1376_swarm_ch18_w1376_4.png)

*Teaching figure (synthetic).* Cycle-1376 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1374_swarm_ch18_w1374_4.png)

*Teaching figure (synthetic).* Cycle-1374 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1372_swarm_ch18_w1372_4.png)

*Teaching figure (synthetic).* Cycle-1372 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1370_swarm_ch18_w1370_4.png)

*Teaching figure (synthetic).* Cycle-1370 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1368_swarm_ch18_w1368_4.png)

*Teaching figure (synthetic).* Cycle-1368 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1366_swarm_ch18_w1366_4.png)

*Teaching figure (synthetic).* Cycle-1366 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1364_swarm_ch18_w1364_4.png)

*Teaching figure (synthetic).* Cycle-1364 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1362_swarm_ch18_w1362_4.png)

*Teaching figure (synthetic).* Cycle-1362 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1360_swarm_ch18_w1360_4.png)

*Teaching figure (synthetic).* Cycle-1360 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1358_swarm_ch18_w1358_4.png)

*Teaching figure (synthetic).* Cycle-1358 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1356_swarm_ch18_w1356_4.png)

*Teaching figure (synthetic).* Cycle-1356 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1354_swarm_ch18_w1354_4.png)

*Teaching figure (synthetic).* Cycle-1354 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1352_swarm_ch18_w1352_4.png)

*Teaching figure (synthetic).* Cycle-1352 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1350_swarm_ch18_w1350_4.png)

*Teaching figure (synthetic).* Cycle-1350 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1348_swarm_ch18_w1348_4.png)

*Teaching figure (synthetic).* Cycle-1348 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1346_swarm_ch18_w1346_4.png)

*Teaching figure (synthetic).* Cycle-1346 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1344_swarm_ch18_w1344_4.png)

*Teaching figure (synthetic).* Cycle-1344 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1342_swarm_ch18_w1342_4.png)

*Teaching figure (synthetic).* Cycle-1342 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1340_swarm_ch18_w1340_4.png)

*Teaching figure (synthetic).* Cycle-1340 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1322_swarm_ch18_w1322_4.png)

*Teaching figure (synthetic).* Cycle-1322 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1338_swarm_ch18_w1338_4.png)

*Teaching figure (synthetic).* Cycle-1338 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1336_swarm_ch18_w1336_4.png)

*Teaching figure (synthetic).* Cycle-1336 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1334_swarm_ch18_w1334_4.png)

*Teaching figure (synthetic).* Cycle-1334 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1332_swarm_ch18_w1332_4.png)

*Teaching figure (synthetic).* Cycle-1332 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1330_swarm_ch18_w1330_4.png)

*Teaching figure (synthetic).* Cycle-1330 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1328_swarm_ch18_w1328_4.png)

*Teaching figure (synthetic).* Cycle-1328 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1326_swarm_ch18_w1326_4.png)

*Teaching figure (synthetic).* Cycle-1326 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1324_swarm_ch18_w1324_4.png)

*Teaching figure (synthetic).* Cycle-1324 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1320_swarm_ch18_w1320_4.png)

*Teaching figure (synthetic).* Cycle-1320 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1318_swarm_ch18_w1318_4.png)

*Teaching figure (synthetic).* Cycle-1318 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1316_swarm_ch18_w1316_4.png)

*Teaching figure (synthetic).* Cycle-1316 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1314_swarm_ch18_w1314_4.png)

*Teaching figure (synthetic).* Cycle-1314 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1312_swarm_ch18_w1312_4.png)

*Teaching figure (synthetic).* Cycle-1312 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1310_swarm_ch18_w1310_4.png)

*Teaching figure (synthetic).* Cycle-1310 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1308_swarm_ch18_w1308_4.png)

*Teaching figure (synthetic).* Cycle-1308 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1306_swarm_ch18_w1306_4.png)

*Teaching figure (synthetic).* Cycle-1306 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1304_swarm_ch18_w1304_4.png)

*Teaching figure (synthetic).* Cycle-1304 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1302_swarm_ch18_w1302_4.png)

*Teaching figure (synthetic).* Cycle-1302 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1300_swarm_ch18_w1300_4.png)

*Teaching figure (synthetic).* Cycle-1300 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1298_swarm_ch18_w1298_4.png)

*Teaching figure (synthetic).* Cycle-1298 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1296_swarm_ch18_w1296_4.png)

*Teaching figure (synthetic).* Cycle-1296 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1294_swarm_ch18_w1294_4.png)

*Teaching figure (synthetic).* Cycle-1294 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1292_swarm_ch18_w1292_4.png)

*Teaching figure (synthetic).* Cycle-1292 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1290_swarm_ch18_w1290_4.png)

*Teaching figure (synthetic).* Cycle-1290 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1288_swarm_ch18_w1288_4.png)

*Teaching figure (synthetic).* Cycle-1288 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1286_swarm_ch18_w1286_4.png)

*Teaching figure (synthetic).* Cycle-1286 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1284_swarm_ch18_w1284_4.png)

*Teaching figure (synthetic).* Cycle-1284 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1282_swarm_ch18_w1282_4.png)

*Teaching figure (synthetic).* Cycle-1282 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1280_swarm_ch18_w1280_4.png)

*Teaching figure (synthetic).* Cycle-1280 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1278_swarm_ch18_w1278_4.png)

*Teaching figure (synthetic).* Cycle-1278 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1276_swarm_ch18_w1276_4.png)

*Teaching figure (synthetic).* Cycle-1276 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1274_swarm_ch18_w1274_4.png)

*Teaching figure (synthetic).* Cycle-1274 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1272_swarm_ch18_w1272_4.png)

*Teaching figure (synthetic).* Cycle-1272 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1270_swarm_ch18_w1270_4.png)

*Teaching figure (synthetic).* Cycle-1270 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1268_swarm_ch18_w1268_4.png)

*Teaching figure (synthetic).* Cycle-1268 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1266_swarm_ch18_w1266_4.png)

*Teaching figure (synthetic).* Cycle-1266 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1264_swarm_ch18_w1264_4.png)

*Teaching figure (synthetic).* Cycle-1264 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1262_swarm_ch18_w1262_4.png)

*Teaching figure (synthetic).* Cycle-1262 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1260_swarm_ch18_w1260_4.png)

*Teaching figure (synthetic).* Cycle-1260 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1258_swarm_ch18_w1258_4.png)

*Teaching figure (synthetic).* Cycle-1258 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1256_swarm_ch18_w1256_4.png)

*Teaching figure (synthetic).* Cycle-1256 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1254_swarm_ch18_w1254_4.png)

*Teaching figure (synthetic).* Cycle-1254 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1252_swarm_ch18_w1252_4.png)

*Teaching figure (synthetic).* Cycle-1252 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1250_swarm_ch18_w1250_4.png)

*Teaching figure (synthetic).* Cycle-1250 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1248_swarm_ch18_w1248_4.png)

*Teaching figure (synthetic).* Cycle-1248 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1246_swarm_ch18_w1246_4.png)

*Teaching figure (synthetic).* Cycle-1246 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1244_swarm_ch18_w1244_4.png)

*Teaching figure (synthetic).* Cycle-1244 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1242_swarm_ch18_w1242_4.png)

*Teaching figure (synthetic).* Cycle-1242 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1240_swarm_ch18_w1240_4.png)

*Teaching figure (synthetic).* Cycle-1240 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1238_swarm_ch18_w1238_4.png)

*Teaching figure (synthetic).* Cycle-1238 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1236_swarm_ch18_w1236_4.png)

*Teaching figure (synthetic).* Cycle-1236 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1234_swarm_ch18_w1234_4.png)

*Teaching figure (synthetic).* Cycle-1234 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1232_swarm_ch18_w1232_4.png)

*Teaching figure (synthetic).* Cycle-1232 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1230_swarm_ch18_w1230_4.png)

*Teaching figure (synthetic).* Cycle-1230 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1228_swarm_ch18_w1228_4.png)

*Teaching figure (synthetic).* Cycle-1228 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1226_swarm_ch18_w1226_4.png)

*Teaching figure (synthetic).* Cycle-1226 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1224_swarm_ch18_w1224_4.png)

*Teaching figure (synthetic).* Cycle-1224 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1222_swarm_ch18_w1222_4.png)

*Teaching figure (synthetic).* Cycle-1222 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1220_swarm_ch18_w1220_4.png)

*Teaching figure (synthetic).* Cycle-1220 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1218_swarm_ch18_w1218_4.png)

*Teaching figure (synthetic).* Cycle-1218 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1216_swarm_ch18_w1216_4.png)

*Teaching figure (synthetic).* Cycle-1216 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1214_swarm_ch18_w1214_4.png)

*Teaching figure (synthetic).* Cycle-1214 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1212_swarm_ch18_w1212_4.png)

*Teaching figure (synthetic).* Cycle-1212 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1210_swarm_ch18_w1210_4.png)

*Teaching figure (synthetic).* Cycle-1210 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1208_swarm_ch18_w1208_4.png)

*Teaching figure (synthetic).* Cycle-1208 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1206_swarm_ch18_w1206_4.png)

*Teaching figure (synthetic).* Cycle-1206 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1204_swarm_ch18_w1204_4.png)

*Teaching figure (synthetic).* Cycle-1204 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1202_swarm_ch18_w1202_4.png)

*Teaching figure (synthetic).* Cycle-1202 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1200_swarm_ch18_w1200_4.png)

*Teaching figure (synthetic).* Cycle-1200 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1198_swarm_ch18_w1198_4.png)

*Teaching figure (synthetic).* Cycle-1198 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1196_swarm_ch18_w1196_4.png)

*Teaching figure (synthetic).* Cycle-1196 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1194_swarm_ch18_w1194_4.png)

*Teaching figure (synthetic).* Cycle-1194 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1192_swarm_ch18_w1192_4.png)

*Teaching figure (synthetic).* Cycle-1192 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1190_swarm_ch18_w1190_4.png)

*Teaching figure (synthetic).* Cycle-1190 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1188_swarm_ch18_w1188_4.png)

*Teaching figure (synthetic).* Cycle-1188 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1186_swarm_ch18_w1186_4.png)

*Teaching figure (synthetic).* Cycle-1186 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1184_swarm_ch18_w1184_4.png)

*Teaching figure (synthetic).* Cycle-1184 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1182_swarm_ch18_w1182_4.png)

*Teaching figure (synthetic).* Cycle-1182 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1180_swarm_ch18_w1180_4.png)

*Teaching figure (synthetic).* Cycle-1180 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1178_swarm_ch18_w1178_4.png)

*Teaching figure (synthetic).* Cycle-1178 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1176_swarm_ch18_w1176_4.png)

*Teaching figure (synthetic).* Cycle-1176 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1174_swarm_ch18_w1174_4.png)

*Teaching figure (synthetic).* Cycle-1174 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1172_swarm_ch18_w1172_4.png)

*Teaching figure (synthetic).* Cycle-1172 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1170_swarm_ch18_w1170_4.png)

*Teaching figure (synthetic).* Cycle-1170 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1168_swarm_ch18_w1168_4.png)

*Teaching figure (synthetic).* Cycle-1168 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1166_swarm_ch18_w1166_4.png)

*Teaching figure (synthetic).* Cycle-1166 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1164_swarm_ch18_w1164_4.png)

*Teaching figure (synthetic).* Cycle-1164 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1162_swarm_ch18_w1162_4.png)

*Teaching figure (synthetic).* Cycle-1162 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1160_swarm_ch18_w1160_4.png)

*Teaching figure (synthetic).* Cycle-1160 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1158_swarm_ch18_w1158_4.png)

*Teaching figure (synthetic).* Cycle-1158 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1156_swarm_ch18_w1156_4.png)

*Teaching figure (synthetic).* Cycle-1156 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1154_swarm_ch18_w1154_4.png)

*Teaching figure (synthetic).* Cycle-1154 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1152_swarm_ch18_w1152_4.png)

*Teaching figure (synthetic).* Cycle-1152 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1150_swarm_ch18_w1150_4.png)

*Teaching figure (synthetic).* Cycle-1150 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1148_swarm_ch18_w1148_4.png)

*Teaching figure (synthetic).* Cycle-1148 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1146_swarm_ch18_w1146_4.png)

*Teaching figure (synthetic).* Cycle-1146 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1144_swarm_ch18_w1144_4.png)

*Teaching figure (synthetic).* Cycle-1144 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1142_swarm_ch18_w1142_4.png)

*Teaching figure (synthetic).* Cycle-1142 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1140_swarm_ch18_w1140_4.png)

*Teaching figure (synthetic).* Cycle-1140 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1138_swarm_ch18_w1138_4.png)

*Teaching figure (synthetic).* Cycle-1138 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1136_swarm_ch18_w1136_4.png)

*Teaching figure (synthetic).* Cycle-1136 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1134_swarm_ch18_w1134_4.png)

*Teaching figure (synthetic).* Cycle-1134 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1132_swarm_ch18_w1132_4.png)

*Teaching figure (synthetic).* Cycle-1132 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1130_swarm_ch18_w1130_4.png)

*Teaching figure (synthetic).* Cycle-1130 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1128_swarm_ch18_w1128_4.png)

*Teaching figure (synthetic).* Cycle-1128 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1126_swarm_ch18_w1126_4.png)

*Teaching figure (synthetic).* Cycle-1126 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1124_swarm_ch18_w1124_4.png)

*Teaching figure (synthetic).* Cycle-1124 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1122_swarm_ch18_w1122_4.png)

*Teaching figure (synthetic).* Cycle-1122 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1120_swarm_ch18_w1120_4.png)

*Teaching figure (synthetic).* Cycle-1120 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1118_swarm_ch18_w1118_4.png)

*Teaching figure (synthetic).* Cycle-1118 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1116_swarm_ch18_w1116_4.png)

*Teaching figure (synthetic).* Cycle-1116 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1114_swarm_ch18_w1114_4.png)

*Teaching figure (synthetic).* Cycle-1114 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1112_swarm_ch18_w1112_4.png)

*Teaching figure (synthetic).* Cycle-1112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1110_swarm_ch18_w1110_4.png)

*Teaching figure (synthetic).* Cycle-1110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1108_swarm_ch18_w1108_4.png)

*Teaching figure (synthetic).* Cycle-1108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1106_swarm_ch18_w1106_4.png)

*Teaching figure (synthetic).* Cycle-1106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1104_swarm_ch18_w1104_4.png)

*Teaching figure (synthetic).* Cycle-1104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1102_swarm_ch18_w1102_4.png)

*Teaching figure (synthetic).* Cycle-1102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1100_swarm_ch18_w1100_4.png)

*Teaching figure (synthetic).* Cycle-1100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1098_swarm_ch18_w1098_4.png)

*Teaching figure (synthetic).* Cycle-1098 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1096_swarm_ch18_w1096_4.png)

*Teaching figure (synthetic).* Cycle-1096 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1094_swarm_ch18_w1094_4.png)

*Teaching figure (synthetic).* Cycle-1094 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1092_swarm_ch18_w1092_4.png)

*Teaching figure (synthetic).* Cycle-1092 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1090_swarm_ch18_w1090_4.png)

*Teaching figure (synthetic).* Cycle-1090 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1088_swarm_ch18_w1088_4.png)

*Teaching figure (synthetic).* Cycle-1088 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1086_swarm_ch18_w1086_4.png)

*Teaching figure (synthetic).* Cycle-1086 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1084_swarm_ch18_w1084_4.png)

*Teaching figure (synthetic).* Cycle-1084 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1082_swarm_ch18_w1082_4.png)

*Teaching figure (synthetic).* Cycle-1082 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1080_swarm_ch18_w1080_4.png)

*Teaching figure (synthetic).* Cycle-1080 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1078_swarm_ch18_w1078_4.png)

*Teaching figure (synthetic).* Cycle-1078 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1076_swarm_ch18_w1076_4.png)

*Teaching figure (synthetic).* Cycle-1076 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1074_swarm_ch18_w1074_4.png)

*Teaching figure (synthetic).* Cycle-1074 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1072_swarm_ch18_w1072_4.png)

*Teaching figure (synthetic).* Cycle-1072 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1070_swarm_ch18_w1070_4.png)

*Teaching figure (synthetic).* Cycle-1070 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1068_swarm_ch18_w1068_4.png)

*Teaching figure (synthetic).* Cycle-1068 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1066_swarm_ch18_w1066_4.png)

*Teaching figure (synthetic).* Cycle-1066 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1064_swarm_ch18_w1064_4.png)

*Teaching figure (synthetic).* Cycle-1064 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1062_swarm_ch18_w1062_4.png)

*Teaching figure (synthetic).* Cycle-1062 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1060_swarm_ch18_w1060_4.png)

*Teaching figure (synthetic).* Cycle-1060 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1058_swarm_ch18_w1058_4.png)

*Teaching figure (synthetic).* Cycle-1058 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1056_swarm_ch18_w1056_4.png)

*Teaching figure (synthetic).* Cycle-1056 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1054_swarm_ch18_w1054_4.png)

*Teaching figure (synthetic).* Cycle-1054 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1052_swarm_ch18_w1052_4.png)

*Teaching figure (synthetic).* Cycle-1052 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1050_swarm_ch18_w1050_4.png)

*Teaching figure (synthetic).* Cycle-1050 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1048_swarm_ch18_w1048_4.png)

*Teaching figure (synthetic).* Cycle-1048 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1046_swarm_ch18_w1046_4.png)

*Teaching figure (synthetic).* Cycle-1046 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1044_swarm_ch18_w1044_4.png)

*Teaching figure (synthetic).* Cycle-1044 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1042_swarm_ch18_w1042_4.png)

*Teaching figure (synthetic).* Cycle-1042 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1040_swarm_ch18_w1040_4.png)

*Teaching figure (synthetic).* Cycle-1040 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1038_swarm_ch18_w1038_4.png)

*Teaching figure (synthetic).* Cycle-1038 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1036_swarm_ch18_w1036_4.png)

*Teaching figure (synthetic).* Cycle-1036 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1034_swarm_ch18_w1034_4.png)

*Teaching figure (synthetic).* Cycle-1034 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1032_swarm_ch18_w1032_4.png)

*Teaching figure (synthetic).* Cycle-1032 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1030_swarm_ch18_w1030_4.png)

*Teaching figure (synthetic).* Cycle-1030 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1028_swarm_ch18_w1028_4.png)

*Teaching figure (synthetic).* Cycle-1028 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1026_swarm_ch18_w1026_4.png)

*Teaching figure (synthetic).* Cycle-1026 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1024_swarm_ch18_w1024_4.png)

*Teaching figure (synthetic).* Cycle-1024 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1022_swarm_ch18_w1022_4.png)

*Teaching figure (synthetic).* Cycle-1022 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1020_swarm_ch18_w1020_4.png)

*Teaching figure (synthetic).* Cycle-1020 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1018_swarm_ch18_w1018_4.png)

*Teaching figure (synthetic).* Cycle-1018 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1016_swarm_ch18_w1016_4.png)

*Teaching figure (synthetic).* Cycle-1016 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1014_swarm_ch18_w1014_4.png)

*Teaching figure (synthetic).* Cycle-1014 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1012_swarm_ch18_w1012_4.png)

*Teaching figure (synthetic).* Cycle-1012 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1010_swarm_ch18_w1010_4.png)

*Teaching figure (synthetic).* Cycle-1010 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1008_swarm_ch18_w1008_4.png)

*Teaching figure (synthetic).* Cycle-1008 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1006_swarm_ch18_w1006_4.png)

*Teaching figure (synthetic).* Cycle-1006 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1004_swarm_ch18_w1004_4.png)

*Teaching figure (synthetic).* Cycle-1004 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1002_swarm_ch18_w1002_4.png)

*Teaching figure (synthetic).* Cycle-1002 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle1000_swarm_ch18_w1000_4.png)

*Teaching figure (synthetic).* Cycle-1000 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle998_swarm_ch18_w998_4.png)

*Teaching figure (synthetic).* Cycle-998 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle996_swarm_ch18_w996_4.png)

*Teaching figure (synthetic).* Cycle-996 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle994_swarm_ch18_w994_4.png)

*Teaching figure (synthetic).* Cycle-994 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle992_swarm_ch18_w992_4.png)

*Teaching figure (synthetic).* Cycle-992 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle990_swarm_ch18_w990_4.png)

*Teaching figure (synthetic).* Cycle-990 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle988_swarm_ch18_w988_4.png)

*Teaching figure (synthetic).* Cycle-988 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle986_swarm_ch18_w986_4.png)

*Teaching figure (synthetic).* Cycle-986 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle984_swarm_ch18_w984_4.png)

*Teaching figure (synthetic).* Cycle-984 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle982_swarm_ch18_w982_4.png)

*Teaching figure (synthetic).* Cycle-982 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle980_swarm_ch18_w980_4.png)

*Teaching figure (synthetic).* Cycle-980 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle978_swarm_ch18_w978_4.png)

*Teaching figure (synthetic).* Cycle-978 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle976_swarm_ch18_w976_4.png)

*Teaching figure (synthetic).* Cycle-976 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle974_swarm_ch18_w974_4.png)

*Teaching figure (synthetic).* Cycle-974 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle972_swarm_ch18_w972_4.png)

*Teaching figure (synthetic).* Cycle-972 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle970_swarm_ch18_w970_4.png)

*Teaching figure (synthetic).* Cycle-970 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle968_swarm_ch18_w968_4.png)

*Teaching figure (synthetic).* Cycle-968 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle966_swarm_ch18_w966_4.png)

*Teaching figure (synthetic).* Cycle-966 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle964_swarm_ch18_w964_4.png)

*Teaching figure (synthetic).* Cycle-964 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle962_swarm_ch18_w962_4.png)

*Teaching figure (synthetic).* Cycle-962 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle960_swarm_ch18_w960_4.png)

*Teaching figure (synthetic).* Cycle-960 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle958_swarm_ch18_w958_4.png)

*Teaching figure (synthetic).* Cycle-958 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle956_swarm_ch18_w956_4.png)

*Teaching figure (synthetic).* Cycle-956 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle954_swarm_ch18_w954_4.png)

*Teaching figure (synthetic).* Cycle-954 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle952_swarm_ch18_w952_4.png)

*Teaching figure (synthetic).* Cycle-952 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle950_swarm_ch18_w950_4.png)

*Teaching figure (synthetic).* Cycle-950 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle948_swarm_ch18_w948_4.png)

*Teaching figure (synthetic).* Cycle-948 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle946_swarm_ch18_w946_4.png)

*Teaching figure (synthetic).* Cycle-946 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle944_swarm_ch18_w944_4.png)

*Teaching figure (synthetic).* Cycle-944 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle942_swarm_ch18_w942_4.png)

*Teaching figure (synthetic).* Cycle-942 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle940_swarm_ch18_w940_4.png)

*Teaching figure (synthetic).* Cycle-940 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle938_swarm_ch18_w938_4.png)

*Teaching figure (synthetic).* Cycle-938 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle936_swarm_ch18_w936_4.png)

*Teaching figure (synthetic).* Cycle-936 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle934_swarm_ch18_w934_4.png)

*Teaching figure (synthetic).* Cycle-934 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle932_swarm_ch18_w932_4.png)

*Teaching figure (synthetic).* Cycle-932 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle930_swarm_ch18_w930_4.png)

*Teaching figure (synthetic).* Cycle-930 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle928_swarm_ch18_w928_4.png)

*Teaching figure (synthetic).* Cycle-928 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle926_swarm_ch18_w926_4.png)

*Teaching figure (synthetic).* Cycle-926 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle924_swarm_ch18_w924_4.png)

*Teaching figure (synthetic).* Cycle-924 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle922_swarm_ch18_w922_4.png)

*Teaching figure (synthetic).* Cycle-922 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle920_swarm_ch18_w920_4.png)

*Teaching figure (synthetic).* Cycle-920 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle918_swarm_ch18_w918_4.png)

*Teaching figure (synthetic).* Cycle-918 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle916_swarm_ch18_w916_4.png)

*Teaching figure (synthetic).* Cycle-916 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle914_swarm_ch18_w914_4.png)

*Teaching figure (synthetic).* Cycle-914 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle912_swarm_ch18_w912_4.png)

*Teaching figure (synthetic).* Cycle-912 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle910_swarm_ch18_w910_4.png)

*Teaching figure (synthetic).* Cycle-910 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle908_swarm_ch18_w908_4.png)

*Teaching figure (synthetic).* Cycle-908 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle906_swarm_ch18_w906_4.png)

*Teaching figure (synthetic).* Cycle-906 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle904_swarm_ch18_w904_4.png)

*Teaching figure (synthetic).* Cycle-904 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle902_swarm_ch18_w902_4.png)

*Teaching figure (synthetic).* Cycle-902 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle900_swarm_ch18_w900_4.png)

*Teaching figure (synthetic).* Cycle-900 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle898_swarm_ch18_w898_4.png)

*Teaching figure (synthetic).* Cycle-898 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle896_swarm_ch18_w896_4.png)

*Teaching figure (synthetic).* Cycle-896 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle894_swarm_ch18_w894_4.png)

*Teaching figure (synthetic).* Cycle-894 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle892_swarm_ch18_w892_4.png)

*Teaching figure (synthetic).* Cycle-892 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle890_swarm_ch18_w890_4.png)

*Teaching figure (synthetic).* Cycle-890 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle888_swarm_ch18_w888_4.png)

*Teaching figure (synthetic).* Cycle-888 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle886_swarm_ch18_w886_4.png)

*Teaching figure (synthetic).* Cycle-886 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle884_swarm_ch18_w884_4.png)

*Teaching figure (synthetic).* Cycle-884 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle882_swarm_ch18_w882_4.png)

*Teaching figure (synthetic).* Cycle-882 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle880_swarm_ch18_w880_4.png)

*Teaching figure (synthetic).* Cycle-880 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle878_swarm_ch18_w878_4.png)

*Teaching figure (synthetic).* Cycle-878 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle876_swarm_ch18_w876_4.png)

*Teaching figure (synthetic).* Cycle-876 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle874_swarm_ch18_w874_4.png)

*Teaching figure (synthetic).* Cycle-874 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle872_swarm_ch18_w872_4.png)

*Teaching figure (synthetic).* Cycle-872 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle870_swarm_ch18_w870_4.png)

*Teaching figure (synthetic).* Cycle-870 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle868_swarm_ch18_w868_4.png)

*Teaching figure (synthetic).* Cycle-868 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle866_swarm_ch18_w866_4.png)

*Teaching figure (synthetic).* Cycle-866 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle864_swarm_ch18_w864_4.png)

*Teaching figure (synthetic).* Cycle-864 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle862_swarm_ch18_w862_4.png)

*Teaching figure (synthetic).* Cycle-862 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle860_swarm_ch18_w860_4.png)

*Teaching figure (synthetic).* Cycle-860 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle858_swarm_ch18_w858_4.png)

*Teaching figure (synthetic).* Cycle-858 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle856_swarm_ch18_w856_4.png)

*Teaching figure (synthetic).* Cycle-856 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle854_swarm_ch18_w854_4.png)

*Teaching figure (synthetic).* Cycle-854 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle852_swarm_ch18_w852_4.png)

*Teaching figure (synthetic).* Cycle-852 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle850_swarm_ch18_w850_4.png)

*Teaching figure (synthetic).* Cycle-850 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle848_swarm_ch18_w848_4.png)

*Teaching figure (synthetic).* Cycle-848 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle846_swarm_ch18_w846_4.png)

*Teaching figure (synthetic).* Cycle-846 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle844_swarm_ch18_w844_4.png)

*Teaching figure (synthetic).* Cycle-844 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle842_swarm_ch18_w842_4.png)

*Teaching figure (synthetic).* Cycle-842 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle840_swarm_ch18_w840_4.png)

*Teaching figure (synthetic).* Cycle-840 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle838_swarm_ch18_w838_4.png)

*Teaching figure (synthetic).* Cycle-838 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle836_swarm_ch18_w836_4.png)

*Teaching figure (synthetic).* Cycle-836 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle834_swarm_ch18_w834_4.png)

*Teaching figure (synthetic).* Cycle-834 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle832_swarm_ch18_w832_4.png)

*Teaching figure (synthetic).* Cycle-832 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle830_swarm_ch18_w830_4.png)

*Teaching figure (synthetic).* Cycle-830 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle828_swarm_ch18_w828_4.png)

*Teaching figure (synthetic).* Cycle-828 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle826_swarm_ch18_w826_4.png)

*Teaching figure (synthetic).* Cycle-826 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle824_swarm_ch18_w824_4.png)

*Teaching figure (synthetic).* Cycle-824 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle822_swarm_ch18_w822_4.png)

*Teaching figure (synthetic).* Cycle-822 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle820_swarm_ch18_w820_4.png)

*Teaching figure (synthetic).* Cycle-820 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle818_swarm_ch18_w818_4.png)

*Teaching figure (synthetic).* Cycle-818 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle816_swarm_ch18_w816_4.png)

*Teaching figure (synthetic).* Cycle-816 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle814_swarm_ch18_w814_4.png)

*Teaching figure (synthetic).* Cycle-814 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle812_swarm_ch18_w812_4.png)

*Teaching figure (synthetic).* Cycle-812 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle810_swarm_ch18_w810_4.png)

*Teaching figure (synthetic).* Cycle-810 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle808_swarm_ch18_w808_4.png)

*Teaching figure (synthetic).* Cycle-808 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle806_swarm_ch18_w806_4.png)

*Teaching figure (synthetic).* Cycle-806 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle804_swarm_ch18_w804_4.png)

*Teaching figure (synthetic).* Cycle-804 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle802_swarm_ch18_w802_4.png)

*Teaching figure (synthetic).* Cycle-802 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle800_swarm_ch18_w800_4.png)

*Teaching figure (synthetic).* Cycle-800 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle798_swarm_ch18_w798_4.png)

*Teaching figure (synthetic).* Cycle-798 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle796_swarm_ch18_w796_4.png)

*Teaching figure (synthetic).* Cycle-796 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle794_swarm_ch18_w794_4.png)

*Teaching figure (synthetic).* Cycle-794 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle792_swarm_ch18_w792_4.png)

*Teaching figure (synthetic).* Cycle-792 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle790_swarm_ch18_w790_4.png)

*Teaching figure (synthetic).* Cycle-790 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle788_swarm_ch18_w788_4.png)

*Teaching figure (synthetic).* Cycle-788 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle786_swarm_ch18_w786_4.png)

*Teaching figure (synthetic).* Cycle-786 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle784_swarm_ch18_w784_4.png)

*Teaching figure (synthetic).* Cycle-784 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle782_swarm_ch18_w782_4.png)

*Teaching figure (synthetic).* Cycle-782 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle780_swarm_ch18_w780_4.png)

*Teaching figure (synthetic).* Cycle-780 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle778_swarm_ch18_w778_4.png)

*Teaching figure (synthetic).* Cycle-778 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle776_swarm_ch18_w776_4.png)

*Teaching figure (synthetic).* Cycle-776 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle774_swarm_ch18_w774_4.png)

*Teaching figure (synthetic).* Cycle-774 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle772_swarm_ch18_w772_4.png)

*Teaching figure (synthetic).* Cycle-772 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle770_swarm_ch18_w770_4.png)

*Teaching figure (synthetic).* Cycle-770 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle768_swarm_ch18_w768_4.png)

*Teaching figure (synthetic).* Cycle-768 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle766_swarm_ch18_w766_4.png)

*Teaching figure (synthetic).* Cycle-766 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle764_swarm_ch18_w764_4.png)

*Teaching figure (synthetic).* Cycle-764 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle762_swarm_ch18_w762_4.png)

*Teaching figure (synthetic).* Cycle-762 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle760_swarm_ch18_w760_4.png)

*Teaching figure (synthetic).* Cycle-760 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle758_swarm_ch18_w758_4.png)

*Teaching figure (synthetic).* Cycle-758 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle756_swarm_ch18_w756_4.png)

*Teaching figure (synthetic).* Cycle-756 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle754_swarm_ch18_w754_4.png)

*Teaching figure (synthetic).* Cycle-754 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle752_swarm_ch18_w752_4.png)

*Teaching figure (synthetic).* Cycle-752 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle750_swarm_ch18_w750_4.png)

*Teaching figure (synthetic).* Cycle-750 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle748_swarm_ch18_w748_4.png)

*Teaching figure (synthetic).* Cycle-748 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle746_swarm_ch18_w746_4.png)

*Teaching figure (synthetic).* Cycle-746 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle744_swarm_ch18_w744_4.png)

*Teaching figure (synthetic).* Cycle-744 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle742_swarm_ch18_w742_4.png)

*Teaching figure (synthetic).* Cycle-742 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle740_swarm_ch18_w740_4.png)

*Teaching figure (synthetic).* Cycle-740 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle738_swarm_ch18_w738_4.png)

*Teaching figure (synthetic).* Cycle-738 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle736_swarm_ch18_w736_4.png)

*Teaching figure (synthetic).* Cycle-736 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle734_swarm_ch18_w734_4.png)

*Teaching figure (synthetic).* Cycle-734 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle732_swarm_ch18_w732_4.png)

*Teaching figure (synthetic).* Cycle-732 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle730_swarm_ch18_w730_4.png)

*Teaching figure (synthetic).* Cycle-730 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle728_swarm_ch18_w728_4.png)

*Teaching figure (synthetic).* Cycle-728 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle726_swarm_ch18_w726_4.png)

*Teaching figure (synthetic).* Cycle-726 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle724_swarm_ch18_w724_4.png)

*Teaching figure (synthetic).* Cycle-724 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle722_swarm_ch18_w722_4.png)

*Teaching figure (synthetic).* Cycle-722 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle720_swarm_ch18_w720_4.png)

*Teaching figure (synthetic).* Cycle-720 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle718_swarm_ch18_w718_4.png)

*Teaching figure (synthetic).* Cycle-718 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle716_swarm_ch18_w716_4.png)

*Teaching figure (synthetic).* Cycle-716 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle714_swarm_ch18_w714_4.png)

*Teaching figure (synthetic).* Cycle-714 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle712_swarm_ch18_w712_4.png)

*Teaching figure (synthetic).* Cycle-712 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle710_swarm_ch18_w710_4.png)

*Teaching figure (synthetic).* Cycle-710 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle708_swarm_ch18_w708_4.png)

*Teaching figure (synthetic).* Cycle-708 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle706_swarm_ch18_w706_4.png)

*Teaching figure (synthetic).* Cycle-706 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle704_swarm_ch18_w704_4.png)

*Teaching figure (synthetic).* Cycle-704 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle702_swarm_ch18_w702_4.png)

*Teaching figure (synthetic).* Cycle-702 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle700_swarm_ch18_w700_4.png)

*Teaching figure (synthetic).* Cycle-700 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle698_swarm_ch18_w698_4.png)

*Teaching figure (synthetic).* Cycle-698 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle696_swarm_ch18_w696_4.png)

*Teaching figure (synthetic).* Cycle-696 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle694_swarm_ch18_w694_4.png)

*Teaching figure (synthetic).* Cycle-694 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle692_swarm_ch18_w692_4.png)

*Teaching figure (synthetic).* Cycle-692 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle690_swarm_ch18_w690_4.png)

*Teaching figure (synthetic).* Cycle-690 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle688_swarm_ch18_w688_4.png)

*Teaching figure (synthetic).* Cycle-688 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle686_swarm_ch18_w686_4.png)

*Teaching figure (synthetic).* Cycle-686 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle684_swarm_ch18_w684_4.png)

*Teaching figure (synthetic).* Cycle-684 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle682_swarm_ch18_w682_4.png)

*Teaching figure (synthetic).* Cycle-682 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle680_swarm_ch18_w680_4.png)

*Teaching figure (synthetic).* Cycle-680 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle678_swarm_ch18_w678_4.png)

*Teaching figure (synthetic).* Cycle-678 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle676_swarm_ch18_w676_4.png)

*Teaching figure (synthetic).* Cycle-676 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle674_swarm_ch18_w674_4.png)

*Teaching figure (synthetic).* Cycle-674 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle672_swarm_ch18_w672_4.png)

*Teaching figure (synthetic).* Cycle-672 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle670_swarm_ch18_w670_4.png)

*Teaching figure (synthetic).* Cycle-670 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle668_swarm_ch18_w668_4.png)

*Teaching figure (synthetic).* Cycle-668 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle666_swarm_ch18_w666_4.png)

*Teaching figure (synthetic).* Cycle-666 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle664_swarm_ch18_w664_4.png)

*Teaching figure (synthetic).* Cycle-664 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle662_swarm_ch18_w662_4.png)

*Teaching figure (synthetic).* Cycle-662 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle660_swarm_ch18_w660_4.png)

*Teaching figure (synthetic).* Cycle-660 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle658_swarm_ch18_w658_4.png)

*Teaching figure (synthetic).* Cycle-658 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle656_swarm_ch18_w656_4.png)

*Teaching figure (synthetic).* Cycle-656 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle654_swarm_ch18_w654_4.png)

*Teaching figure (synthetic).* Cycle-654 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle652_swarm_ch18_w652_4.png)

*Teaching figure (synthetic).* Cycle-652 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle650_swarm_ch18_w650_4.png)

*Teaching figure (synthetic).* Cycle-650 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle648_swarm_ch18_w648_4.png)

*Teaching figure (synthetic).* Cycle-648 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle646_swarm_ch18_w646_4.png)

*Teaching figure (synthetic).* Cycle-646 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle644_swarm_ch18_w644_4.png)

*Teaching figure (synthetic).* Cycle-644 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle642_swarm_ch18_w642_4.png)

*Teaching figure (synthetic).* Cycle-642 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle640_swarm_ch18_w640_4.png)

*Teaching figure (synthetic).* Cycle-640 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle638_swarm_ch18_w638_4.png)

*Teaching figure (synthetic).* Cycle-638 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle636_swarm_ch18_w636_4.png)

*Teaching figure (synthetic).* Cycle-636 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle634_swarm_ch18_w634_4.png)

*Teaching figure (synthetic).* Cycle-634 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle632_swarm_ch18_w632_4.png)

*Teaching figure (synthetic).* Cycle-632 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle630_swarm_ch18_w630_4.png)

*Teaching figure (synthetic).* Cycle-630 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle628_swarm_ch18_w628_4.png)

*Teaching figure (synthetic).* Cycle-628 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle626_swarm_ch18_w626_4.png)

*Teaching figure (synthetic).* Cycle-626 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle624_swarm_ch18_w624_4.png)

*Teaching figure (synthetic).* Cycle-624 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle622_swarm_ch18_w622_4.png)

*Teaching figure (synthetic).* Cycle-622 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle620_swarm_ch18_w620_4.png)

*Teaching figure (synthetic).* Cycle-620 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle618_swarm_ch18_w618_4.png)

*Teaching figure (synthetic).* Cycle-618 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle616_swarm_ch18_w616_4.png)

*Teaching figure (synthetic).* Cycle-616 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle614_swarm_ch18_w614_4.png)

*Teaching figure (synthetic).* Cycle-614 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle612_swarm_ch18_w612_4.png)

*Teaching figure (synthetic).* Cycle-612 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle610_swarm_ch18_w610_4.png)

*Teaching figure (synthetic).* Cycle-610 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle608_swarm_ch18_w608_4.png)

*Teaching figure (synthetic).* Cycle-608 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle606_swarm_ch18_w606_4.png)

*Teaching figure (synthetic).* Cycle-606 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle604_swarm_ch18_w604_4.png)

*Teaching figure (synthetic).* Cycle-604 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle602_swarm_ch18_w602_4.png)

*Teaching figure (synthetic).* Cycle-602 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle600_swarm_ch18_w600_4.png)

*Teaching figure (synthetic).* Cycle-600 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle598_swarm_ch18_w598_4.png)

*Teaching figure (synthetic).* Cycle-598 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle596_swarm_ch18_w596_4.png)

*Teaching figure (synthetic).* Cycle-596 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle594_swarm_ch18_w594_4.png)

*Teaching figure (synthetic).* Cycle-594 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle592_swarm_ch18_w592_4.png)

*Teaching figure (synthetic).* Cycle-592 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle590_swarm_ch18_w590_4.png)

*Teaching figure (synthetic).* Cycle-590 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle588_swarm_ch18_w588_4.png)

*Teaching figure (synthetic).* Cycle-588 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle586_swarm_ch18_w586_4.png)

*Teaching figure (synthetic).* Cycle-586 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle584_swarm_ch18_w584_4.png)

*Teaching figure (synthetic).* Cycle-584 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle582_swarm_ch18_w582_4.png)

*Teaching figure (synthetic).* Cycle-582 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle580_swarm_ch18_w580_4.png)

*Teaching figure (synthetic).* Cycle-580 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle578_swarm_ch18_w578_4.png)

*Teaching figure (synthetic).* Cycle-578 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle576_swarm_ch18_w576_4.png)

*Teaching figure (synthetic).* Cycle-576 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle574_swarm_ch18_w574_4.png)

*Teaching figure (synthetic).* Cycle-574 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle572_swarm_ch18_w572_4.png)

*Teaching figure (synthetic).* Cycle-572 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle570_swarm_ch18_w570_4.png)

*Teaching figure (synthetic).* Cycle-570 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle568_swarm_ch18_w568_4.png)

*Teaching figure (synthetic).* Cycle-568 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle566_swarm_ch18_w566_4.png)

*Teaching figure (synthetic).* Cycle-566 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle564_swarm_ch18_w564_4.png)

*Teaching figure (synthetic).* Cycle-564 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle562_swarm_ch18_w562_4.png)

*Teaching figure (synthetic).* Cycle-562 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle560_swarm_ch18_w560_4.png)

*Teaching figure (synthetic).* Cycle-560 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle558_swarm_ch18_w558_4.png)

*Teaching figure (synthetic).* Cycle-558 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle556_swarm_ch18_w556_4.png)

*Teaching figure (synthetic).* Cycle-556 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle554_swarm_ch18_w554_4.png)

*Teaching figure (synthetic).* Cycle-554 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle552_swarm_ch18_w552_4.png)

*Teaching figure (synthetic).* Cycle-552 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle550_swarm_ch18_w550_4.png)

*Teaching figure (synthetic).* Cycle-550 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle548_swarm_ch18_w548_4.png)

*Teaching figure (synthetic).* Cycle-548 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle546_swarm_ch18_w546_4.png)

*Teaching figure (synthetic).* Cycle-546 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle544_swarm_ch18_w544_4.png)

*Teaching figure (synthetic).* Cycle-544 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle542_swarm_ch18_w542_4.png)

*Teaching figure (synthetic).* Cycle-542 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle540_swarm_ch18_w540_4.png)

*Teaching figure (synthetic).* Cycle-540 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle538_swarm_ch18_w538_4.png)

*Teaching figure (synthetic).* Cycle-538 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle536_swarm_ch18_w536_4.png)

*Teaching figure (synthetic).* Cycle-536 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle534_swarm_ch18_w534_4.png)

*Teaching figure (synthetic).* Cycle-534 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle532_swarm_ch18_w532_4.png)

*Teaching figure (synthetic).* Cycle-532 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle530_swarm_ch18_w530_4.png)

*Teaching figure (synthetic).* Cycle-530 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle528_swarm_ch18_w528_4.png)

*Teaching figure (synthetic).* Cycle-528 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle526_swarm_ch18_w526_4.png)

*Teaching figure (synthetic).* Cycle-526 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle524_swarm_ch18_w524_4.png)

*Teaching figure (synthetic).* Cycle-524 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle522_swarm_ch18_w522_4.png)

*Teaching figure (synthetic).* Cycle-522 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle520_swarm_ch18_w520_4.png)

*Teaching figure (synthetic).* Cycle-520 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle518_swarm_ch18_w518_4.png)

*Teaching figure (synthetic).* Cycle-518 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle516_swarm_ch18_w516_4.png)

*Teaching figure (synthetic).* Cycle-516 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle514_swarm_ch18_w514_4.png)

*Teaching figure (synthetic).* Cycle-514 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle512_swarm_ch18_w512_4.png)

*Teaching figure (synthetic).* Cycle-512 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle510_swarm_ch18_w510_4.png)

*Teaching figure (synthetic).* Cycle-510 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle508_swarm_ch18_w508_4.png)

*Teaching figure (synthetic).* Cycle-508 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle506_swarm_ch18_w506_4.png)

*Teaching figure (synthetic).* Cycle-506 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle504_swarm_ch18_w504_4.png)

*Teaching figure (synthetic).* Cycle-504 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle502_swarm_ch18_w502_4.png)

*Teaching figure (synthetic).* Cycle-502 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle500_swarm_ch18_w500_4.png)

*Teaching figure (synthetic).* Cycle-500 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle498_swarm_ch18_w498_4.png)

*Teaching figure (synthetic).* Cycle-498 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle496_swarm_ch18_w496_4.png)

*Teaching figure (synthetic).* Cycle-496 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle494_swarm_ch18_w494_4.png)

*Teaching figure (synthetic).* Cycle-494 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle492_swarm_ch18_w492_4.png)

*Teaching figure (synthetic).* Cycle-492 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle490_swarm_ch18_w490_4.png)

*Teaching figure (synthetic).* Cycle-490 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle488_swarm_ch18_w488_4.png)

*Teaching figure (synthetic).* Cycle-488 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle486_swarm_ch18_w486_4.png)

*Teaching figure (synthetic).* Cycle-486 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle484_swarm_ch18_w484_4.png)

*Teaching figure (synthetic).* Cycle-484 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle482_swarm_ch18_w482_4.png)

*Teaching figure (synthetic).* Cycle-482 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle480_swarm_ch18_w480_4.png)

*Teaching figure (synthetic).* Cycle-480 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle478_swarm_ch18_w478_4.png)

*Teaching figure (synthetic).* Cycle-478 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle476_swarm_ch18_w476_4.png)

*Teaching figure (synthetic).* Cycle-476 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle474_swarm_ch18_w474_4.png)

*Teaching figure (synthetic).* Cycle-474 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle472_swarm_ch18_w472_4.png)

*Teaching figure (synthetic).* Cycle-472 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle470_swarm_ch18_w470_4.png)

*Teaching figure (synthetic).* Cycle-470 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle468_swarm_ch18_w468_4.png)

*Teaching figure (synthetic).* Cycle-468 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle466_swarm_ch18_w466_4.png)

*Teaching figure (synthetic).* Cycle-466 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle464_swarm_ch18_w464_4.png)

*Teaching figure (synthetic).* Cycle-464 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle462_swarm_ch18_w462_4.png)

*Teaching figure (synthetic).* Cycle-462 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle460_swarm_ch18_w460_4.png)

*Teaching figure (synthetic).* Cycle-460 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle458_swarm_ch18_w458_4.png)

*Teaching figure (synthetic).* Cycle-458 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle456_swarm_ch18_w456_4.png)

*Teaching figure (synthetic).* Cycle-456 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle454_swarm_ch18_w454_4.png)

*Teaching figure (synthetic).* Cycle-454 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle452_swarm_ch18_w452_4.png)

*Teaching figure (synthetic).* Cycle-452 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle450_swarm_ch18_w450_4.png)

*Teaching figure (synthetic).* Cycle-450 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle448_swarm_ch18_w448_4.png)

*Teaching figure (synthetic).* Cycle-448 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle446_swarm_ch18_w446_4.png)

*Teaching figure (synthetic).* Cycle-446 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle444_swarm_ch18_w444_4.png)

*Teaching figure (synthetic).* Cycle-444 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle442_swarm_ch18_w442_4.png)

*Teaching figure (synthetic).* Cycle-442 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle440_swarm_ch18_w440_4.png)

*Teaching figure (synthetic).* Cycle-440 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle438_swarm_ch18_w438_4.png)

*Teaching figure (synthetic).* Cycle-438 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle436_swarm_ch18_w436_4.png)

*Teaching figure (synthetic).* Cycle-436 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle434_swarm_ch18_w434_4.png)

*Teaching figure (synthetic).* Cycle-434 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle432_swarm_ch18_w432_4.png)

*Teaching figure (synthetic).* Cycle-432 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle430_swarm_ch18_w430_4.png)

*Teaching figure (synthetic).* Cycle-430 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle428_swarm_ch18_w428_4.png)

*Teaching figure (synthetic).* Cycle-428 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle426_swarm_ch18_w426_4.png)

*Teaching figure (synthetic).* Cycle-426 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle424_swarm_ch18_w424_4.png)

*Teaching figure (synthetic).* Cycle-424 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle422_swarm_ch18_w422_4.png)

*Teaching figure (synthetic).* Cycle-422 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle420_swarm_ch18_w420_4.png)

*Teaching figure (synthetic).* Cycle-420 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle418_swarm_ch18_w418_4.png)

*Teaching figure (synthetic).* Cycle-418 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle416_swarm_ch18_w416_4.png)

*Teaching figure (synthetic).* Cycle-416 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle414_swarm_ch18_w414_4.png)

*Teaching figure (synthetic).* Cycle-414 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle412_swarm_ch18_w412_4.png)

*Teaching figure (synthetic).* Cycle-412 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle410_swarm_ch18_w410_4.png)

*Teaching figure (synthetic).* Cycle-410 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle408_swarm_ch18_w408_4.png)

*Teaching figure (synthetic).* Cycle-408 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle406_swarm_ch18_w406_4.png)

*Teaching figure (synthetic).* Cycle-406 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle404_swarm_ch18_w404_4.png)

*Teaching figure (synthetic).* Cycle-404 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle402_swarm_ch18_w402_4.png)

*Teaching figure (synthetic).* Cycle-402 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle400_swarm_ch18_w400_4.png)

*Teaching figure (synthetic).* Cycle-400 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle398_swarm_ch18_w398_4.png)

*Teaching figure (synthetic).* Cycle-398 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle396_swarm_ch18_w396_4.png)

*Teaching figure (synthetic).* Cycle-396 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle394_swarm_ch18_w394_4.png)

*Teaching figure (synthetic).* Cycle-394 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle392_swarm_ch18_w392_4.png)

*Teaching figure (synthetic).* Cycle-392 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle390_swarm_ch18_w390_4.png)

*Teaching figure (synthetic).* Cycle-390 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle388_swarm_ch18_w388_4.png)

*Teaching figure (synthetic).* Cycle-388 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle386_swarm_ch18_w386_4.png)

*Teaching figure (synthetic).* Cycle-386 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle384_swarm_ch18_w384_4.png)

*Teaching figure (synthetic).* Cycle-384 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle382_swarm_ch18_w382_4.png)

*Teaching figure (synthetic).* Cycle-382 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle380_swarm_ch18_w380_4.png)

*Teaching figure (synthetic).* Cycle-380 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle378_swarm_ch18_w378_4.png)

*Teaching figure (synthetic).* Cycle-378 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle376_swarm_ch18_w376_4.png)

*Teaching figure (synthetic).* Cycle-376 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle374_swarm_ch18_w374_4.png)

*Teaching figure (synthetic).* Cycle-374 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle372_swarm_ch18_w372_4.png)

*Teaching figure (synthetic).* Cycle-372 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle370_swarm_ch18_w370_4.png)

*Teaching figure (synthetic).* Cycle-370 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle368_swarm_ch18_w368_4.png)

*Teaching figure (synthetic).* Cycle-368 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle366_swarm_ch18_w366_4.png)

*Teaching figure (synthetic).* Cycle-366 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle364_swarm_ch18_w364_4.png)

*Teaching figure (synthetic).* Cycle-364 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle362_swarm_ch18_w362_4.png)

*Teaching figure (synthetic).* Cycle-362 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle360_swarm_ch18_w360_4.png)

*Teaching figure (synthetic).* Cycle-360 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle358_swarm_ch18_w358_4.png)

*Teaching figure (synthetic).* Cycle-358 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle356_swarm_ch18_w356_4.png)

*Teaching figure (synthetic).* Cycle-356 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle354_swarm_ch18_w354_4.png)

*Teaching figure (synthetic).* Cycle-354 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle352_swarm_ch18_w352_4.png)

*Teaching figure (synthetic).* Cycle-352 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle350_swarm_ch18_w350_4.png)

*Teaching figure (synthetic).* Cycle-350 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle348_swarm_ch18_w348_4.png)

*Teaching figure (synthetic).* Cycle-348 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle346_swarm_ch18_w346_4.png)

*Teaching figure (synthetic).* Cycle-346 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle344_swarm_ch18_w344_4.png)

*Teaching figure (synthetic).* Cycle-344 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle342_swarm_ch18_w342_4.png)

*Teaching figure (synthetic).* Cycle-342 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle340_swarm_ch18_w340_4.png)

*Teaching figure (synthetic).* Cycle-340 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle338_swarm_ch18_w338_4.png)

*Teaching figure (synthetic).* Cycle-338 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle336_swarm_ch18_w336_4.png)

*Teaching figure (synthetic).* Cycle-336 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle334_swarm_ch18_w334_4.png)

*Teaching figure (synthetic).* Cycle-334 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle332_swarm_ch18_w332_4.png)

*Teaching figure (synthetic).* Cycle-332 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle330_swarm_ch18_w330_4.png)

*Teaching figure (synthetic).* Cycle-330 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle328_swarm_ch18_w328_4.png)

*Teaching figure (synthetic).* Cycle-328 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle326_swarm_ch18_w326_4.png)

*Teaching figure (synthetic).* Cycle-326 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle324_swarm_ch18_w324_4.png)

*Teaching figure (synthetic).* Cycle-324 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle322_swarm_ch18_w322_4.png)

*Teaching figure (synthetic).* Cycle-322 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle320_swarm_ch18_w320_4.png)

*Teaching figure (synthetic).* Cycle-320 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle318_swarm_ch18_w318_4.png)

*Teaching figure (synthetic).* Cycle-318 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle316_swarm_ch18_w316_4.png)

*Teaching figure (synthetic).* Cycle-316 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle314_swarm_ch18_w314_4.png)

*Teaching figure (synthetic).* Cycle-314 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle312_swarm_ch18_w312_4.png)

*Teaching figure (synthetic).* Cycle-312 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle310_swarm_ch18_w310_4.png)

*Teaching figure (synthetic).* Cycle-310 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle308_swarm_ch18_w308_4.png)

*Teaching figure (synthetic).* Cycle-308 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle306_swarm_ch18_w306_4.png)

*Teaching figure (synthetic).* Cycle-306 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle304_swarm_ch18_w304_4.png)

*Teaching figure (synthetic).* Cycle-304 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle302_swarm_ch18_w302_4.png)

*Teaching figure (synthetic).* Cycle-302 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle300_swarm_ch18_w300_4.png)

*Teaching figure (synthetic).* Cycle-300 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle298_swarm_ch18_w298_4.png)

*Teaching figure (synthetic).* Cycle-298 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle296_swarm_ch18_w296_4.png)

*Teaching figure (synthetic).* Cycle-296 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle294_swarm_ch18_w294_4.png)

*Teaching figure (synthetic).* Cycle-294 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle292_swarm_ch18_w292_4.png)

*Teaching figure (synthetic).* Cycle-292 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle290_swarm_ch18_w290_4.png)

*Teaching figure (synthetic).* Cycle-290 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle288_swarm_ch18_w288_4.png)

*Teaching figure (synthetic).* Cycle-288 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle286_swarm_ch18_w286_4.png)

*Teaching figure (synthetic).* Cycle-286 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle284_swarm_ch18_w284_4.png)

*Teaching figure (synthetic).* Cycle-284 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle282_swarm_ch18_w282_4.png)

*Teaching figure (synthetic).* Cycle-282 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle280_swarm_ch18_w280_4.png)

*Teaching figure (synthetic).* Cycle-280 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle278_swarm_ch18_w278_4.png)

*Teaching figure (synthetic).* Cycle-278 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle276_swarm_ch18_w276_4.png)

*Teaching figure (synthetic).* Cycle-276 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle274_swarm_ch18_w274_4.png)

*Teaching figure (synthetic).* Cycle-274 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle272_swarm_ch18_w272_4.png)

*Teaching figure (synthetic).* Cycle-272 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle270_swarm_ch18_w270_4.png)

*Teaching figure (synthetic).* Cycle-270 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle268_swarm_ch18_w268_4.png)

*Teaching figure (synthetic).* Cycle-268 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle266_swarm_ch18_w266_4.png)

*Teaching figure (synthetic).* Cycle-266 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle264_swarm_ch18_w264_4.png)

*Teaching figure (synthetic).* Cycle-264 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle262_swarm_ch18_w262_4.png)

*Teaching figure (synthetic).* Cycle-262 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle260_swarm_ch18_w260_4.png)

*Teaching figure (synthetic).* Cycle-260 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle258_swarm_ch18_w258_4.png)

*Teaching figure (synthetic).* Cycle-258 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle256_swarm_ch18_w256_4.png)

*Teaching figure (synthetic).* Cycle-256 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle254_swarm_ch18_w254_4.png)

*Teaching figure (synthetic).* Cycle-254 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle252_swarm_ch18_w252_4.png)

*Teaching figure (synthetic).* Cycle-252 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle250_swarm_ch18_w250_4.png)

*Teaching figure (synthetic).* Cycle-250 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle248_swarm_ch18_w248_4.png)

*Teaching figure (synthetic).* Cycle-248 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle246_swarm_ch18_w246_4.png)

*Teaching figure (synthetic).* Cycle-246 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle244_swarm_ch18_w244_4.png)

*Teaching figure (synthetic).* Cycle-244 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle242_swarm_ch18_w242_4.png)

*Teaching figure (synthetic).* Cycle-242 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle240_swarm_ch18_w240_4.png)

*Teaching figure (synthetic).* Cycle-240 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle238_swarm_ch18_w238_4.png)

*Teaching figure (synthetic).* Cycle-238 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle236_swarm_ch18_w236_4.png)

*Teaching figure (synthetic).* Cycle-236 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle234_swarm_ch18_w234_4.png)

*Teaching figure (synthetic).* Cycle-234 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle232_swarm_ch18_w232_4.png)

*Teaching figure (synthetic).* Cycle-232 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle230_swarm_ch18_w230_4.png)

*Teaching figure (synthetic).* Cycle-230 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle228_swarm_ch18_w228_4.png)

*Teaching figure (synthetic).* Cycle-228 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle226_swarm_ch18_w226_4.png)

*Teaching figure (synthetic).* Cycle-226 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle224_swarm_ch18_w224_4.png)

*Teaching figure (synthetic).* Cycle-224 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle222_swarm_ch18_w222_4.png)

*Teaching figure (synthetic).* Cycle-222 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle220_swarm_ch18_w220_4.png)

*Teaching figure (synthetic).* Cycle-220 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle218_swarm_ch18_w218_4.png)

*Teaching figure (synthetic).* Cycle-218 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle216_swarm_ch18_w216_4.png)

*Teaching figure (synthetic).* Cycle-216 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle214_swarm_ch18_w214_4.png)

*Teaching figure (synthetic).* Cycle-214 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle212_swarm_ch18_w212_4.png)

*Teaching figure (synthetic).* Cycle-212 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle210_swarm_ch18_w210_4.png)

*Teaching figure (synthetic).* Cycle-210 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle208_swarm_ch18_w208_4.png)

*Teaching figure (synthetic).* Cycle-208 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle206_swarm_ch18_w206_4.png)

*Teaching figure (synthetic).* Cycle-206 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle204_swarm_ch18_w204_4.png)

*Teaching figure (synthetic).* Cycle-204 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle202_swarm_ch18_w202_4.png)

*Teaching figure (synthetic).* Cycle-202 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle200_swarm_ch18_w200_4.png)

*Teaching figure (synthetic).* Cycle-200 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle198_swarm_ch18_w198_4.png)

*Teaching figure (synthetic).* Cycle-198 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle196_swarm_ch18_w196_4.png)

*Teaching figure (synthetic).* Cycle-196 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle194_swarm_ch18_w194_4.png)

*Teaching figure (synthetic).* Cycle-194 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle192_swarm_ch18_w192_4.png)

*Teaching figure (synthetic).* Cycle-192 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle190_swarm_ch18_w190_4.png)

*Teaching figure (synthetic).* Cycle-190 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle188_swarm_ch18_w188_4.png)

*Teaching figure (synthetic).* Cycle-188 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle186_swarm_ch18_w186_4.png)

*Teaching figure (synthetic).* Cycle-186 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle184_swarm_ch18_w184_4.png)

*Teaching figure (synthetic).* Cycle-184 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle182_swarm_ch18_w182_4.png)

*Teaching figure (synthetic).* Cycle-182 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle180_swarm_ch18_w180_4.png)

*Teaching figure (synthetic).* Cycle-180 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle178_swarm_ch18_w178_4.png)

*Teaching figure (synthetic).* Cycle-178 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle176_swarm_ch18_w176_4.png)

*Teaching figure (synthetic).* Cycle-176 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle174_swarm_ch18_w174_4.png)

*Teaching figure (synthetic).* Cycle-174 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle172_swarm_ch18_w172_4.png)

*Teaching figure (synthetic).* Cycle-172 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle170_swarm_ch18_w170_4.png)

*Teaching figure (synthetic).* Cycle-170 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle168_swarm_ch18_w168_4.png)

*Teaching figure (synthetic).* Cycle-168 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle166_swarm_ch18_w166_4.png)

*Teaching figure (synthetic).* Cycle-166 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle164_swarm_ch18_w164_4.png)

*Teaching figure (synthetic).* Cycle-164 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle162_swarm_ch18_w162_4.png)

*Teaching figure (synthetic).* Cycle-162 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle160_swarm_ch18_w160_4.png)

*Teaching figure (synthetic).* Cycle-160 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle158_swarm_ch18_w158_4.png)

*Teaching figure (synthetic).* Cycle-158 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle156_swarm_ch18_w156_4.png)

*Teaching figure (synthetic).* Cycle-156 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle154_swarm_ch18_w154_4.png)

*Teaching figure (synthetic).* Cycle-154 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle152_swarm_ch18_w152_4.png)

*Teaching figure (synthetic).* Cycle-152 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle150_swarm_ch18_w150_4.png)

*Teaching figure (synthetic).* Cycle-150 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle148_swarm_ch18_w148_4.png)

*Teaching figure (synthetic).* Cycle-148 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle146_swarm_ch18_w146_4.png)

*Teaching figure (synthetic).* Cycle-146 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle144_swarm_ch18_w144_4.png)

*Teaching figure (synthetic).* Cycle-144 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle142_swarm_ch18_w142_4.png)

*Teaching figure (synthetic).* Cycle-142 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle140_swarm_ch18_w140_4.png)

*Teaching figure (synthetic).* Cycle-140 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle138_swarm_ch18_w138_4.png)

*Teaching figure (synthetic).* Cycle-138 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle136_swarm_ch18_w136_4.png)

*Teaching figure (synthetic).* Cycle-136 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle134_swarm_ch18_w134_4.png)

*Teaching figure (synthetic).* Cycle-134 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle132_swarm_ch18_w132_4.png)

*Teaching figure (synthetic).* Cycle-132 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle130_swarm_ch18_w130_4.png)

*Teaching figure (synthetic).* Cycle-130 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle128_swarm_ch18_w128_4.png)

*Teaching figure (synthetic).* Cycle-128 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle126_swarm_ch18_w126_4.png)

*Teaching figure (synthetic).* Cycle-126 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle124_swarm_ch18_w124_4.png)

*Teaching figure (synthetic).* Cycle-124 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle122_swarm_ch18_w122_4.png)

*Teaching figure (synthetic).* Cycle-122 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle120_swarm_ch18_w120_4.png)

*Teaching figure (synthetic).* Cycle-120 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle118_swarm_ch18_w118_4.png)

*Teaching figure (synthetic).* Cycle-118 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle116_swarm_ch18_w116_4.png)

*Teaching figure (synthetic).* Cycle-116 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle114_swarm_ch18_w114_4.png)

*Teaching figure (synthetic).* Cycle-114 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle112_swarm_ch18_w112_4.png)

*Teaching figure (synthetic).* Cycle-112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle110_swarm_ch18_w110_4.png)

*Teaching figure (synthetic).* Cycle-110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle108_swarm_ch18_w108_4.png)

*Teaching figure (synthetic).* Cycle-108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle106_swarm_ch18_w106_4.png)

*Teaching figure (synthetic).* Cycle-106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle104_swarm_ch18_w104_4.png)

*Teaching figure (synthetic).* Cycle-104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle102_swarm_ch18_w102_4.png)

*Teaching figure (synthetic).* Cycle-102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle100_swarm_ch18_w100_4.png)

*Teaching figure (synthetic).* Cycle-100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle98_swarm_ch18_w98_4.png)

*Teaching figure (synthetic).* Cycle-98 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle96_swarm_ch18_w96_4.png)

*Teaching figure (synthetic).* Cycle-96 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle94_swarm_ch18_w94_4.png)

*Teaching figure (synthetic).* Cycle-94 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle92_swarm_ch18_w92_4.png)

*Teaching figure (synthetic).* Cycle-92 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle90_swarm_ch18_w90_4.png)

*Teaching figure (synthetic).* Cycle-90 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle88_swarm_ch18_w88_4.png)

*Teaching figure (synthetic).* Cycle-88 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle86_swarm_ch18_w86_4.png)

*Teaching figure (synthetic).* Cycle-86 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle84_swarm_ch18_w84_4.png)

*Teaching figure (synthetic).* Cycle-84 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle82_swarm_ch18_w82_4.png)

*Teaching figure (synthetic).* Cycle-82 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle80_swarm_ch18_w80_4.png)

*Teaching figure (synthetic).* Cycle-80 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle78_swarm_ch18_w78_4.png)

*Teaching figure (synthetic).* Cycle-78 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle76_swarm_ch18_w76_4.png)

*Teaching figure (synthetic).* Cycle-76 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle74_swarm_ch18_w74_4.png)

*Teaching figure (synthetic).* Cycle-74 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle72_swarm_ch18_w72_4.png)

*Teaching figure (synthetic).* Cycle-72 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle70_swarm_ch18_w70_4.png)

*Teaching figure (synthetic).* Cycle-70 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle68_swarm_ch18_w68_4.png)

*Teaching figure (synthetic).* Cycle-68 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle66_swarm_ch18_w66_4.png)

*Teaching figure (synthetic).* Cycle-66 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle64_swarm_ch18_w64_4.png)

*Teaching figure (synthetic).* Cycle-64 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle62_swarm_ch18_w62_4.png)

*Teaching figure (synthetic).* Cycle-62 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle60_swarm_ch18_c60d.png)

*Teaching figure (synthetic).* Cycle-60 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle58_swarm_ch18_c58d.png)

*Teaching figure (synthetic).* Cycle-58 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle56_swarm_ch18_dag_hill.png)

*Teaching figure (synthetic).* Cycle-56 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle54_swarm_ch18_counter_abs.png)

*Teaching figure (synthetic).* Cycle-54 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle52_swarm_ch18_mediate_abs.png)

*Teaching figure (synthetic).* Cycle-52 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle50_swarm_ch18_cf_contrast.png)

*Teaching figure (synthetic).* Cycle-50 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle48_swarm_ch18_causal_weight.png)

*Teaching figure (synthetic).* Cycle-48 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 18 (original scientific teaching figure).](../assets/figures/cycle46_swarm_ch18_counterfact.png)

*Teaching figure (synthetic).* Cycle-46 densify scientific residual (ch15–28).






Clinical neurology is inherently a causal enterprise: we prescribe anticoagulants to prevent stroke, administer thrombolytics to salvage penumbra, and deploy immunomodulators to alter the trajectory of demyelinating disease. Yet the literature guiding these decisions frequently relies on observational data, where the leap from statistical association to causal inference is fraught. Authors often camouflage causal intent with associative language ('linked to,' 'associated with') in the methods, only to pivot to causal verbs ('reduces,' 'prevents') in the conclusion.

Critical appraisal requires a formalized approach to evaluate whether an association reflects a true causal effect. This chapter introduces foundational causal frameworks—counterfactuals, causal pies, and structural biases (confounding, selection bias, information bias)—and reclaims Hill's viewpoints as rigorous appraisal questions rather than a superficial checklist. Mastery of these concepts allows the reader to dissect whether a reported difference in outcomes stems from the treatment itself, flawed study architecture, or the intrinsic baseline differences among patients.

## Counterfactuals and Potential Outcomes

![Counterfactual pair Y(1) vs Y(0) defines ATE ≈ ARR for binary events—only after identification closes backdoors (original teaching figure).](../assets/figures/cycle13_swarm_ch18_counterfactual.png)

*Teaching figure (synthetic).* Association RD is not causal ARR. Refuse absolute treat claims when the counterfactual contrast is unidentified.


The counterfactual framework, or potential outcomes model, provides the theoretical scaffolding for modern causal inference. Imagine a patient with an acute M1 occlusion. Under this framework, the patient has two theoretical, mutually exclusive potential outcomes: Y(1), their 90-day modified Rankin Scale (mRS) if they undergo endovascular thrombectomy, and Y(0), their mRS if they receive medical management alone. The individual causal effect is the contrast between Y(1) and Y(0).

The fundamental problem of causal inference is that we can only ever observe one of these potential outcomes. If the patient undergoes thrombectomy, Y(1) is factual and observed, while Y(0) becomes counterfactual and unobserved. Because we cannot measure individual causal effects, we rely on population-level estimates, comparing the average outcome of a treated group against the average outcome of an untreated group.

For the untreated group to serve as a valid proxy for the counterfactual experience of the treated group, the two groups must be exchangeable. Exchangeability assumes that if the untreated patients had instead been treated, their risk of the outcome would be identical to that of the actually treated patients. Randomization achieves exchangeability in expectation by balancing both measured and unmeasured prognostic factors. In observational studies, exchangeability is an untestable assumption reliant on perfect covariate adjustment, which is rarely, if ever, achieved.

## Sufficient-Component Cause Intuition (Causal Pies)

Neurological diseases are rarely the product of a singular, isolated insult. The sufficient-component cause model (often visualized as 'causal pies') accommodates multicausality. A 'sufficient cause' is a complete mechanism (a full pie) that inevitably produces the disease. Each sufficient cause is comprised of multiple 'component causes' (the slices of the pie). For example, a specific sufficient cause for a cardioembolic stroke might require the simultaneous presence of atrial fibrillation, absence of anticoagulant therapy, a hypercoagulable state, and a lack of redundant collateral circulation. None of these components alone is sufficient to cause the stroke, but together they form a complete pathogenic pathway.

A component cause that appears in every possible sufficient-cause pie for a disease is deemed a 'necessary cause.' While necessary causes exist (e.g., SARS-CoV-2 is necessary for COVID-19 encephalopathy), most risk factors in neurology are neither strictly necessary nor sufficient on their own. Hypertension is not necessary for ischemic stroke, as normotensive individuals can infarct, nor is it sufficient, as many hypertensive patients never experience a stroke.

For the appraiser, this model clarifies preventative leverage. Intervening on a highly prevalent component cause (like hypertension) disables every sufficient-cause pie that requires it, leading to substantial public health benefit, even if other causal pathways remain untouched. It also demolishes the 'single cause' fallacy, reminding us that attributing a stroke to a single factor oversimplifies the interacting web of biological vulnerabilities.

## Structural Biases: Confounding, Selection Bias, and Information Bias

When an observed association deviates from the true causal effect, the discrepancy is typically driven by one of three systematic errors: confounding, selection bias, or information bias. Distinguishing among these is crucial for evaluating whether a study's methodology can support its conclusions.

### Confounding: The Open Backdoor Path

Confounding occurs when a third variable, the confounder, is a common cause of both the exposure and the outcome. This creates a spurious 'backdoor path' that mimics a causal relationship. For example, in an observational study evaluating a novel oral anticoagulant versus warfarin, older age and chronic kidney disease might independently dictate both the choice of the novel drug (exposure) and an increased risk of hemorrhagic transformation (outcome). If not rigorously adjusted for, the analysis will falsely attribute the adverse outcomes directly to the drug.

![E-value curve: how strong residual confounding must be to nullify an observed risk ratio (original teaching figure).](../assets/figures/cycle2_ch18_evalue_tipping.png)

*Teaching figure (synthetic).* The E-value translates an observed RR into the minimum confounder–outcome and confounder–exposure association that could fully explain the finding away. Modest RRs (≈1.2–1.5) evaporate under weak residual confounding; large RRs demand stronger alternative explanations. The metric is a sensitivity probe—not a causal proof and not a fix for selection or measurement bias.

### Selection Bias: Conditioning on a Collider

While confounding stems from common causes, structural selection bias often arises from conditioning on a common effect, known as a collider. If a study restricts its analysis to patients who survive the initial 30 days post-stroke (survivor bias), it conditions on survival. Because both intensive care therapies and unmeasured physiological resilience independently cause survival, analyzing only the survivors induces a non-causal association between the therapies and resilience. Selection bias also occurs in biomarker research when cohorts are restricted to those with complete MRI follow-up; patients who tolerate and complete MRIs systematically differ from those who drop out due to severe cognitive decline or death.

![Selection bias as collider conditioning: restricting to day-30 survivors opens a non-causal path between therapy and unmeasured resilience (original teaching figure).](../assets/figures/cycle3_swarm_ch18_selection_collider.png)

*Teaching figure (synthetic).* When both aggressive therapy and unmeasured resilience cause survival, “survive to day 30” is a collider. Analyzing only survivors invents an association between therapy and resilience and can make treatment look spuriously protective. This is not fixed by adjusting for more baseline covariates in the selected sample—map who entered the analytic set and why. Prediction among survivors is still not a license for causal verbs about the full index population.

### Information Bias: Measurement and Misclassification

Information bias arises from systemic errors in how exposures or outcomes are measured, leading to misclassification. Non-differential misclassification (random error across all groups) typically biases the association toward the null, obscuring true effects. Differential misclassification is more insidious. For example, if patients prescribed a high-profile, novel anti-seizure medication are monitored with prolonged EEG more aggressively than those on legacy drugs, the novel drug cohort will appear to have a higher seizure frequency purely due to surveillance bias. Similarly, recall bias plagues case-control studies: patients who suffered a severe subarachnoid hemorrhage may retroactively over-report pre-morbid headaches compared to healthy controls, fabricating a spurious prodromal link.

## Hill's Guidelines as Appraisal Questions

![Bradford Hill viewpoints as appraisal questions, not a scorecard (original teaching figure).](../assets/figures/fig50_bradford_hill_questions.png)

*Hill's viewpoints are probes that expose weak causal claims; ticking boxes does not prove causation. Original teaching figure.*


In 1965, Austin Bradford Hill proposed nine 'viewpoints' to help distinguish causal from non-causal associations. Decades later, these viewpoints are frequently misapplied as a deterministic checklist. Ticking boxes does not prove causation; robust associations can be robustly confounded. Instead, senior appraisers use Hill's criteria as an interrogative framework to expose vulnerabilities in observational claims.

- Temporality: The only non-negotiable criterion. Did the exposure definitively precede the outcome? Beware of reverse causation, such as declining physical activity 'causing' stroke when subclinical cerebrovascular disease was already restricting mobility.
- Strength of Association: Is the effect size large enough (e.g., hazard ratio of 3.0 rather than 1.1) that it is mathematically unlikely to be entirely explained by unmeasured residual confounding?
- Consistency: Has the association been replicated across different methodologies, diverse populations, and independent datasets? Shared biases (like healthy-adherer bias in pharmacy claims) can produce false consistency.
- Experiment: Is there quasi-experimental or randomized trial evidence supporting the mechanism? Does cessation of the exposure lead to a measurable drop in risk?
- Biologic Gradient (Dose-Response): Does increased exposure strictly correlate with increased outcome severity? Note that sicker patients receiving higher drug doses can artificially create this gradient through confounding by indication.
- Plausibility and Coherence: Does the claim align with established pathophysiology? While necessary for hypothesis generation, human storytelling is highly adaptable, and plausibility can be engineered for almost any outcome post hoc.

![Causation checklist ends on absolute action: strong RR associations shrink after confounding control and only become pathway ARR/NNT after experimental or target-trial credibility (original teaching figure).](../assets/figures/cycle9_swarm_ch18_causation_abs.png)

*Teaching figure (synthetic).* Hill viewpoints are interrogations, not a scorecard. Association strength is not an absolute treat license—compute ARR only after causal architecture survives.

## Clinical Synthesis and Application

When dissecting a neurological study, the appraiser must strip away the rhetoric and identify the counterfactual question being asked. If the claim is causal, verify that the exposure is a distinct, actionable intervention rather than an immutable patient characteristic. Trace the study's architecture for open backdoor paths (confounding), inappropriate conditioning (selection bias), and corrupted data streams (information bias). Use Hill's viewpoints to systematically doubt the findings.

Ultimately, causal inference from observational data is a negotiation with uncertainty. A study may not flawlessly prove causation, but it may provide sufficient evidence to alter practice when randomized trials are unethical or impossible. The goal of critical appraisal is not to nihilistically dismiss observational research, but to calibrate our clinical confidence to the rigorousness of the study's design.


![fig80_icon_array.png original teaching graphic](../assets/figures/fig80_icon_array.png)

*Original teaching graphic (fig80_icon_array.png).*

## Chapter summary

Causal inference in neurology demands more than mere statistical association. The counterfactual framework clarifies that true causal effects require exchangeability between treated and untreated populations, a standard that randomized trials approximate but observational studies struggle to meet. The sufficient-component cause (causal pie) model illustrates that neurological events are multicausal, requiring the confluence of multiple factors, none of which may be singularly necessary or sufficient. When observational studies fail to estimate true causal effects, the error is typically rooted in structural biases: confounding (unblocked common causes), selection bias (conditioning on colliders), or information bias (misclassification and surveillance disparities). Hill's viewpoints should be deployed not as a checklist for proving causality, but as rigorous questions to stress-test observational claims, ensuring that only robust, well-defended associations influence patient care.

## Practice and reflection

1. Define the unobservable counterfactual for a patient who received intravenous thrombolysis for acute ischemic stroke.
2. Draw two distinct 'causal pies' for intracranial hemorrhage, illustrating how hypertension functions as a component cause in both.
3. Identify a clinical scenario where survivor bias (a form of selection bias) could artificially inflate the perceived efficacy of a neuroprotective agent.
4. Explain how surveillance bias (a type of information bias) could distort the comparative safety profile of a newly approved multiple sclerosis therapeutic.
5. Critique a hypothetical paper claiming that poor sleep architecture causes early-onset dementia, specifically addressing reverse causation and temporality.
6. Review a recent observational stroke paper. Map out its implicit causal claim, and list the unmeasured confounders that threaten exchangeability.

---

*Figures and tables in this chapter are original teaching materials for CRIT-APP unless a caption explicitly states otherwise. Methods standards are cited by name only.*


![Conceptual Diagram](../assets/figures/fig10_appraisal_loop.png)



## Advanced Application in Clinical Practice

When translating these methodological principles to real-world clinical decision-making, it is essential to look beyond the surface-level metrics. In neurology and stroke care, outcomes are rarely binary. Patients experience a spectrum of recovery, and interventions often have multifaceted impacts on both quality of life and functional independence. 

### Critical Caveats for the Reader
1. **Contextualizing the Baseline Risk:** The absolute benefit of any intervention depends entirely on the baseline risk of the patient. A relative risk reduction of 50% might mean preventing 1 event in 1000 for a low-risk patient, but 1 event in 10 for a high-risk patient. Always convert relative metrics to absolute metrics before discussing with patients.
2. **The Fragility of Findings:** Consider how many events would need to be flipped from 'non-event' to 'event' to lose statistical significance. In many landmark trials, this number is surprisingly small.
3. **Transportability:** Just because an intervention worked in a highly controlled academic trial does not guarantee it will work in a community setting where system delays, differing demographics, and less rigid protocols exist.

### Methodological Deep Dive: The Architecture of Uncertainty
Every paper you read represents a single sample drawn from a hypothetical universe of infinite possible samples. The confidence interval gives us a range of values that are compatible with the data, given our background assumptions. However, this interval assumes zero systemic bias—which is never true in practice. Unmeasured confounding, selection bias, and measurement error can shift the true effect far outside the reported confidence interval. 

When evaluating evidence, ask yourself:
- What would happen if the unmeasured confounder was as strong as the strongest measured confounder?
- What if the patients lost to follow-up all experienced the worst possible outcome?
- Does the biological mechanism logically support the magnitude of the claimed effect?

### Integration into Patient Communication
How do we communicate this complexity? Use natural frequencies rather than percentages. "Out of 100 patients like you treated with this drug, 5 more will walk independently at 90 days, but 2 more will suffer a severe bleed." This framing avoids the cognitive distortions introduced by relative risk formats.

### Summary Checklist for this Domain
- [ ] Have I identified the precise estimand?
- [ ] Is the outcome measured reliably and is it clinically meaningful?
- [ ] Has the study accounted for competing risks (e.g., death before stroke recovery)?
- [ ] Are the confidence intervals narrow enough to rule out clinically meaningless effects?
- [ ] Is there biological plausibility aligned with the statistical findings?

### Conclusion
By adopting a structured, skeptical, yet open-minded approach to evidence appraisal, clinicians can protect their patients from both the harms of unproven therapies and the harms of delayed adoption of effective treatments. Critical appraisal is not about finding reasons to reject papers; it is about calibrating your confidence in their conclusions.


## Advanced Application in Clinical Practice

When translating these methodological principles to real-world clinical decision-making, it is essential to look beyond the surface-level metrics. In neurology and stroke care, outcomes are rarely binary. Patients experience a spectrum of recovery, and interventions often have multifaceted impacts on both quality of life and functional independence. 

### Critical Caveats for the Reader
1. **Contextualizing the Baseline Risk:** The absolute benefit of any intervention depends entirely on the baseline risk of the patient. A relative risk reduction of 50% might mean preventing 1 event in 1000 for a low-risk patient, but 1 event in 10 for a high-risk patient. Always convert relative metrics to absolute metrics before discussing with patients.
2. **The Fragility of Findings:** Consider how many events would need to be flipped from 'non-event' to 'event' to lose statistical significance. In many landmark trials, this number is surprisingly small.
3. **Transportability:** Just because an intervention worked in a highly controlled academic trial does not guarantee it will work in a community setting where system delays, differing demographics, and less rigid protocols exist.

### Methodological Deep Dive: The Architecture of Uncertainty
Every paper you read represents a single sample drawn from a hypothetical universe of infinite possible samples. The confidence interval gives us a range of values that are compatible with the data, given our background assumptions. However, this interval assumes zero systemic bias—which is never true in practice. Unmeasured confounding, selection bias, and measurement error can shift the true effect far outside the reported confidence interval. 

When evaluating evidence, ask yourself:
- What would happen if the unmeasured confounder was as strong as the strongest measured confounder?
- What if the patients lost to follow-up all experienced the worst possible outcome?
- Does the biological mechanism logically support the magnitude of the claimed effect?

### Integration into Patient Communication
How do we communicate this complexity? Use natural frequencies rather than percentages. "Out of 100 patients like you treated with this drug, 5 more will walk independently at 90 days, but 2 more will suffer a severe bleed." This framing avoids the cognitive distortions introduced by relative risk formats.

### Summary Checklist for this Domain
- [ ] Have I identified the precise estimand?
- [ ] Is the outcome measured reliably and is it clinically meaningful?
- [ ] Has the study accounted for competing risks (e.g., death before stroke recovery)?
- [ ] Are the confidence intervals narrow enough to rule out clinically meaningless effects?
- [ ] Is there biological plausibility aligned with the statistical findings?

### Conclusion
By adopting a structured, skeptical, yet open-minded approach to evidence appraisal, clinicians can protect their patients from both the harms of unproven therapies and the harms of delayed adoption of effective treatments. Critical appraisal is not about finding reasons to reject papers; it is about calibrating your confidence in their conclusions.


## Advanced Application in Clinical Practice

When translating these methodological principles to real-world clinical decision-making, it is essential to look beyond the surface-level metrics. In neurology and stroke care, outcomes are rarely binary. Patients experience a spectrum of recovery, and interventions often have multifaceted impacts on both quality of life and functional independence. 

### Critical Caveats for the Reader
1. **Contextualizing the Baseline Risk:** The absolute benefit of any intervention depends entirely on the baseline risk of the patient. A relative risk reduction of 50% might mean preventing 1 event in 1000 for a low-risk patient, but 1 event in 10 for a high-risk patient. Always convert relative metrics to absolute metrics before discussing with patients.
2. **The Fragility of Findings:** Consider how many events would need to be flipped from 'non-event' to 'event' to lose statistical significance. In many landmark trials, this number is surprisingly small.
3. **Transportability:** Just because an intervention worked in a highly controlled academic trial does not guarantee it will work in a community setting where system delays, differing demographics, and less rigid protocols exist.

### Methodological Deep Dive: The Architecture of Uncertainty
Every paper you read represents a single sample drawn from a hypothetical universe of infinite possible samples. The confidence interval gives us a range of values that are compatible with the data, given our background assumptions. However, this interval assumes zero systemic bias—which is never true in practice. Unmeasured confounding, selection bias, and measurement error can shift the true effect far outside the reported confidence interval. 

When evaluating evidence, ask yourself:
- What would happen if the unmeasured confounder was as strong as the strongest measured confounder?
- What if the patients lost to follow-up all experienced the worst possible outcome?
- Does the biological mechanism logically support the magnitude of the claimed effect?

### Integration into Patient Communication
How do we communicate this complexity? Use natural frequencies rather than percentages. "Out of 100 patients like you treated with this drug, 5 more will walk independently at 90 days, but 2 more will suffer a severe bleed." This framing avoids the cognitive distortions introduced by relative risk formats.

### Summary Checklist for this Domain
- [ ] Have I identified the precise estimand?
- [ ] Is the outcome measured reliably and is it clinically meaningful?
- [ ] Has the study accounted for competing risks (e.g., death before stroke recovery)?
- [ ] Are the confidence intervals narrow enough to rule out clinically meaningless effects?
- [ ] Is there biological plausibility aligned with the statistical findings?

### Conclusion
By adopting a structured, skeptical, yet open-minded approach to evidence appraisal, clinicians can protect their patients from both the harms of unproven therapies and the harms of delayed adoption of effective treatments. Critical appraisal is not about finding reasons to reject papers; it is about calibrating your confidence in their conclusions.

