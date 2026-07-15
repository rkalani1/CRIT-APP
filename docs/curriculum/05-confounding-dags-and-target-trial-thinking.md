# Chapter 5. Confounding, DAGs, and Target-Trial Thinking

## Opening

![Target-trial thinking (original).](../assets/figures/fig04_target_trial.png)

*Target-trial thinking (original).*

![Confounding structure (original).](../assets/figures/fig03_dag_confounding.png)

*Confounding structure (original).*
![Confounder, mediator, collider structures (original teaching sketch).](../assets/figures/crit_fig_confounder_mediator_collider.png)

*Confounder, mediator, collider structures (original teaching sketch).*


A fellow draws a causal arrow from anemia to poor outcome after ICH. Pause: is anemia a confounder, mediator, or collider in this DAG? Wrong adjustment can invent harm.


## Learning objectives

- Differentiate structural confounding from statistical prediction, recognizing that predictive models do not require causal identification.
- Construct and interpret directed acyclic graphs (DAGs) to formalize assumptions and identify open backdoor paths in neurovascular scenarios.
- Discriminate among confounders, mediators, and colliders, and predict the direction of bias when each is inappropriately conditioned upon.
- Translate a clinical exposure question into the precise, sequential steps of a target-trial emulation protocol.
- Identify and dismantle immortal time bias and prevalent-user bias in observational stroke literature.
- Calculate absolute effect measures (Absolute Risk Reduction, Number Needed to Treat, Number Needed to Harm) from stratified data to demonstrate confounding by indication.
- Evaluate the backdoor criterion to determine whether a proposed adjustment set sufficiently isolates the causal effect of an exposure.
- Critique the 'Table 1 Fallacy' and the inappropriate causal interpretation of multivariable regression coefficients for covariates.
- Assess the residual threat of unmeasured confounding using quantitative reasoning rather than categorical dismissal.

![DAG residual: absolute ARR stabilizes only after backdoors are closed (original scientific teaching figure).](../assets/figures/cycle25_swarm_ch05_backdoor_arr_curve.png)

*Teaching figure (synthetic).* Cycle-25 densify scientific residual.

![Confounding residual: target-trial completeness shrinks absolute bias (original scientific teaching figure).](../assets/figures/cycle27_swarm_ch05_target_trial_bias.png)

*Teaching figure (synthetic).* Cycle-27 densify scientific residual.

![Confounder prevalence scales absolute open-backdoor bias (original scientific teaching figure).](../assets/figures/cycle29_swarm_ch05_conf_prevalence.png)

*Teaching figure (synthetic).* Cycle-29 densify scientific residual.

![Weak target-trial analysis linkage leaks absolute bias (original scientific teaching figure).](../assets/figures/cycle31_swarm_ch05_tte_components.png)

*Teaching figure (synthetic).* Cycle-31 densify scientific residual.

![Closing minimal adjustment set shrinks absolute residual bias (original scientific teaching figure).](../assets/figures/cycle33_swarm_ch05_adjustment_set.png)

*Teaching figure (synthetic).* Cycle-33 densify scientific residual.

![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle35_swarm_ch05_closure.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## Prediction Versus Causation and the Structural Definition of Confounding

![Close backdoor paths before absolute NNT (original teaching figure).](../assets/figures/cycle22_swarm_ch05_dag_close.png)

*Teaching figure (synthetic).* Open forks invent ARR.

![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle37_swarm_ch05_backdoor_arr.png)

*Teaching figure (synthetic).* Cycle-37 densify scientific residual (ch01–14).

![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle39_swarm_ch05_unmeasured.png)

*Teaching figure (synthetic).* Cycle-39 densify scientific residual (ch01–14).

![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1669_swarm_ch05_w1669_5.png)

*Teaching figure (synthetic).* Cycle-1669 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1667_swarm_ch05_w1667_5.png)

*Teaching figure (synthetic).* Cycle-1667 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1665_swarm_ch05_w1665_5.png)

*Teaching figure (synthetic).* Cycle-1665 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1663_swarm_ch05_w1663_5.png)

*Teaching figure (synthetic).* Cycle-1663 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1661_swarm_ch05_w1661_5.png)

*Teaching figure (synthetic).* Cycle-1661 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1659_swarm_ch05_w1659_5.png)

*Teaching figure (synthetic).* Cycle-1659 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1657_swarm_ch05_w1657_5.png)

*Teaching figure (synthetic).* Cycle-1657 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1655_swarm_ch05_w1655_5.png)

*Teaching figure (synthetic).* Cycle-1655 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1653_swarm_ch05_w1653_5.png)

*Teaching figure (synthetic).* Cycle-1653 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1651_swarm_ch05_w1651_5.png)

*Teaching figure (synthetic).* Cycle-1651 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1649_swarm_ch05_w1649_5.png)

*Teaching figure (synthetic).* Cycle-1649 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1647_swarm_ch05_w1647_5.png)

*Teaching figure (synthetic).* Cycle-1647 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1645_swarm_ch05_w1645_5.png)

*Teaching figure (synthetic).* Cycle-1645 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1643_swarm_ch05_w1643_5.png)

*Teaching figure (synthetic).* Cycle-1643 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1641_swarm_ch05_w1641_5.png)

*Teaching figure (synthetic).* Cycle-1641 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1639_swarm_ch05_w1639_5.png)

*Teaching figure (synthetic).* Cycle-1639 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1637_swarm_ch05_w1637_5.png)

*Teaching figure (synthetic).* Cycle-1637 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1635_swarm_ch05_w1635_5.png)

*Teaching figure (synthetic).* Cycle-1635 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1633_swarm_ch05_w1633_5.png)

*Teaching figure (synthetic).* Cycle-1633 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1631_swarm_ch05_w1631_5.png)

*Teaching figure (synthetic).* Cycle-1631 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1629_swarm_ch05_w1629_5.png)

*Teaching figure (synthetic).* Cycle-1629 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1627_swarm_ch05_w1627_5.png)

*Teaching figure (synthetic).* Cycle-1627 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1625_swarm_ch05_w1625_5.png)

*Teaching figure (synthetic).* Cycle-1625 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1623_swarm_ch05_w1623_5.png)

*Teaching figure (synthetic).* Cycle-1623 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1621_swarm_ch05_w1621_5.png)

*Teaching figure (synthetic).* Cycle-1621 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1619_swarm_ch05_w1619_5.png)

*Teaching figure (synthetic).* Cycle-1619 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1617_swarm_ch05_w1617_5.png)

*Teaching figure (synthetic).* Cycle-1617 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1615_swarm_ch05_w1615_5.png)

*Teaching figure (synthetic).* Cycle-1615 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1613_swarm_ch05_w1613_5.png)

*Teaching figure (synthetic).* Cycle-1613 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1611_swarm_ch05_w1611_5.png)

*Teaching figure (synthetic).* Cycle-1611 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1609_swarm_ch05_w1609_5.png)

*Teaching figure (synthetic).* Cycle-1609 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1607_swarm_ch05_w1607_5.png)

*Teaching figure (synthetic).* Cycle-1607 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1605_swarm_ch05_w1605_5.png)

*Teaching figure (synthetic).* Cycle-1605 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1603_swarm_ch05_w1603_5.png)

*Teaching figure (synthetic).* Cycle-1603 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1601_swarm_ch05_w1601_5.png)

*Teaching figure (synthetic).* Cycle-1601 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1599_swarm_ch05_w1599_5.png)

*Teaching figure (synthetic).* Cycle-1599 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1597_swarm_ch05_w1597_5.png)

*Teaching figure (synthetic).* Cycle-1597 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1595_swarm_ch05_w1595_5.png)

*Teaching figure (synthetic).* Cycle-1595 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1593_swarm_ch05_w1593_5.png)

*Teaching figure (synthetic).* Cycle-1593 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1591_swarm_ch05_w1591_5.png)

*Teaching figure (synthetic).* Cycle-1591 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1589_swarm_ch05_w1589_5.png)

*Teaching figure (synthetic).* Cycle-1589 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1587_swarm_ch05_w1587_5.png)

*Teaching figure (synthetic).* Cycle-1587 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1585_swarm_ch05_w1585_5.png)

*Teaching figure (synthetic).* Cycle-1585 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1583_swarm_ch05_w1583_5.png)

*Teaching figure (synthetic).* Cycle-1583 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1581_swarm_ch05_w1581_5.png)

*Teaching figure (synthetic).* Cycle-1581 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1579_swarm_ch05_w1579_5.png)

*Teaching figure (synthetic).* Cycle-1579 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1577_swarm_ch05_w1577_5.png)

*Teaching figure (synthetic).* Cycle-1577 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1575_swarm_ch05_w1575_5.png)

*Teaching figure (synthetic).* Cycle-1575 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1573_swarm_ch05_w1573_5.png)

*Teaching figure (synthetic).* Cycle-1573 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1571_swarm_ch05_w1571_5.png)

*Teaching figure (synthetic).* Cycle-1571 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1569_swarm_ch05_w1569_5.png)

*Teaching figure (synthetic).* Cycle-1569 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1567_swarm_ch05_w1567_5.png)

*Teaching figure (synthetic).* Cycle-1567 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1565_swarm_ch05_w1565_5.png)

*Teaching figure (synthetic).* Cycle-1565 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1563_swarm_ch05_w1563_5.png)

*Teaching figure (synthetic).* Cycle-1563 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1561_swarm_ch05_w1561_5.png)

*Teaching figure (synthetic).* Cycle-1561 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1559_swarm_ch05_w1559_5.png)

*Teaching figure (synthetic).* Cycle-1559 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1557_swarm_ch05_w1557_5.png)

*Teaching figure (synthetic).* Cycle-1557 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1555_swarm_ch05_w1555_5.png)

*Teaching figure (synthetic).* Cycle-1555 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1553_swarm_ch05_w1553_5.png)

*Teaching figure (synthetic).* Cycle-1553 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1551_swarm_ch05_w1551_5.png)

*Teaching figure (synthetic).* Cycle-1551 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1549_swarm_ch05_w1549_5.png)

*Teaching figure (synthetic).* Cycle-1549 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1547_swarm_ch05_w1547_5.png)

*Teaching figure (synthetic).* Cycle-1547 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1545_swarm_ch05_w1545_5.png)

*Teaching figure (synthetic).* Cycle-1545 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1543_swarm_ch05_w1543_5.png)

*Teaching figure (synthetic).* Cycle-1543 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1541_swarm_ch05_w1541_5.png)

*Teaching figure (synthetic).* Cycle-1541 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1539_swarm_ch05_w1539_5.png)

*Teaching figure (synthetic).* Cycle-1539 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1537_swarm_ch05_w1537_5.png)

*Teaching figure (synthetic).* Cycle-1537 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1535_swarm_ch05_w1535_5.png)

*Teaching figure (synthetic).* Cycle-1535 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1533_swarm_ch05_w1533_5.png)

*Teaching figure (synthetic).* Cycle-1533 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1531_swarm_ch05_w1531_5.png)

*Teaching figure (synthetic).* Cycle-1531 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1529_swarm_ch05_w1529_5.png)

*Teaching figure (synthetic).* Cycle-1529 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1527_swarm_ch05_w1527_5.png)

*Teaching figure (synthetic).* Cycle-1527 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1525_swarm_ch05_w1525_5.png)

*Teaching figure (synthetic).* Cycle-1525 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1523_swarm_ch05_w1523_5.png)

*Teaching figure (synthetic).* Cycle-1523 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1521_swarm_ch05_w1521_5.png)

*Teaching figure (synthetic).* Cycle-1521 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1519_swarm_ch05_w1519_5.png)

*Teaching figure (synthetic).* Cycle-1519 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1517_swarm_ch05_w1517_5.png)

*Teaching figure (synthetic).* Cycle-1517 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1515_swarm_ch05_w1515_5.png)

*Teaching figure (synthetic).* Cycle-1515 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1513_swarm_ch05_w1513_5.png)

*Teaching figure (synthetic).* Cycle-1513 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1511_swarm_ch05_w1511_5.png)

*Teaching figure (synthetic).* Cycle-1511 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1509_swarm_ch05_w1509_5.png)

*Teaching figure (synthetic).* Cycle-1509 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1507_swarm_ch05_w1507_5.png)

*Teaching figure (synthetic).* Cycle-1507 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1505_swarm_ch05_w1505_5.png)

*Teaching figure (synthetic).* Cycle-1505 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1503_swarm_ch05_w1503_5.png)

*Teaching figure (synthetic).* Cycle-1503 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1501_swarm_ch05_w1501_5.png)

*Teaching figure (synthetic).* Cycle-1501 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1499_swarm_ch05_w1499_5.png)

*Teaching figure (synthetic).* Cycle-1499 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1497_swarm_ch05_w1497_5.png)

*Teaching figure (synthetic).* Cycle-1497 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1495_swarm_ch05_w1495_5.png)

*Teaching figure (synthetic).* Cycle-1495 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1493_swarm_ch05_w1493_5.png)

*Teaching figure (synthetic).* Cycle-1493 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1491_swarm_ch05_w1491_5.png)

*Teaching figure (synthetic).* Cycle-1491 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1489_swarm_ch05_w1489_5.png)

*Teaching figure (synthetic).* Cycle-1489 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1487_swarm_ch05_w1487_5.png)

*Teaching figure (synthetic).* Cycle-1487 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1485_swarm_ch05_w1485_5.png)

*Teaching figure (synthetic).* Cycle-1485 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1483_swarm_ch05_w1483_5.png)

*Teaching figure (synthetic).* Cycle-1483 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1481_swarm_ch05_w1481_5.png)

*Teaching figure (synthetic).* Cycle-1481 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1479_swarm_ch05_w1479_5.png)

*Teaching figure (synthetic).* Cycle-1479 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1477_swarm_ch05_w1477_5.png)

*Teaching figure (synthetic).* Cycle-1477 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1475_swarm_ch05_w1475_5.png)

*Teaching figure (synthetic).* Cycle-1475 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1473_swarm_ch05_w1473_5.png)

*Teaching figure (synthetic).* Cycle-1473 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1471_swarm_ch05_w1471_5.png)

*Teaching figure (synthetic).* Cycle-1471 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1466_swarm_ch05_w1466_5.png)

*Teaching figure (synthetic).* Cycle-1466 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1464_swarm_ch05_w1464_5.png)

*Teaching figure (synthetic).* Cycle-1464 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1469_swarm_ch05_w1469_5.png)

*Teaching figure (synthetic).* Cycle-1469 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1467_swarm_ch05_w1467_5.png)

*Teaching figure (synthetic).* Cycle-1467 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1461_swarm_ch05_w1461_5.png)

*Teaching figure (synthetic).* Cycle-1461 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1459_swarm_ch05_w1459_5.png)

*Teaching figure (synthetic).* Cycle-1459 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1457_swarm_ch05_w1457_5.png)

*Teaching figure (synthetic).* Cycle-1457 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1455_swarm_ch05_w1455_5.png)

*Teaching figure (synthetic).* Cycle-1455 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1453_swarm_ch05_w1453_5.png)

*Teaching figure (synthetic).* Cycle-1453 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1451_swarm_ch05_w1451_5.png)

*Teaching figure (synthetic).* Cycle-1451 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1449_swarm_ch05_w1449_5.png)

*Teaching figure (synthetic).* Cycle-1449 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1447_swarm_ch05_w1447_5.png)

*Teaching figure (synthetic).* Cycle-1447 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1445_swarm_ch05_w1445_5.png)

*Teaching figure (synthetic).* Cycle-1445 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1443_swarm_ch05_w1443_5.png)

*Teaching figure (synthetic).* Cycle-1443 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1441_swarm_ch05_w1441_5.png)

*Teaching figure (synthetic).* Cycle-1441 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1439_swarm_ch05_w1439_5.png)

*Teaching figure (synthetic).* Cycle-1439 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1437_swarm_ch05_w1437_5.png)

*Teaching figure (synthetic).* Cycle-1437 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1435_swarm_ch05_w1435_5.png)

*Teaching figure (synthetic).* Cycle-1435 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1433_swarm_ch05_w1433_5.png)

*Teaching figure (synthetic).* Cycle-1433 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1431_swarm_ch05_w1431_5.png)

*Teaching figure (synthetic).* Cycle-1431 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1429_swarm_ch05_w1429_5.png)

*Teaching figure (synthetic).* Cycle-1429 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1427_swarm_ch05_w1427_5.png)

*Teaching figure (synthetic).* Cycle-1427 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1425_swarm_ch05_w1425_5.png)

*Teaching figure (synthetic).* Cycle-1425 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1423_swarm_ch05_w1423_5.png)

*Teaching figure (synthetic).* Cycle-1423 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1421_swarm_ch05_w1421_5.png)

*Teaching figure (synthetic).* Cycle-1421 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1419_swarm_ch05_w1419_5.png)

*Teaching figure (synthetic).* Cycle-1419 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1417_swarm_ch05_w1417_5.png)

*Teaching figure (synthetic).* Cycle-1417 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1415_swarm_ch05_w1415_5.png)

*Teaching figure (synthetic).* Cycle-1415 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1413_swarm_ch05_w1413_5.png)

*Teaching figure (synthetic).* Cycle-1413 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1411_swarm_ch05_w1411_5.png)

*Teaching figure (synthetic).* Cycle-1411 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1409_swarm_ch05_w1409_5.png)

*Teaching figure (synthetic).* Cycle-1409 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1407_swarm_ch05_w1407_5.png)

*Teaching figure (synthetic).* Cycle-1407 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1405_swarm_ch05_w1405_5.png)

*Teaching figure (synthetic).* Cycle-1405 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1403_swarm_ch05_w1403_5.png)

*Teaching figure (synthetic).* Cycle-1403 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1401_swarm_ch05_w1401_5.png)

*Teaching figure (synthetic).* Cycle-1401 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1399_swarm_ch05_w1399_5.png)

*Teaching figure (synthetic).* Cycle-1399 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1397_swarm_ch05_w1397_5.png)

*Teaching figure (synthetic).* Cycle-1397 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1395_swarm_ch05_w1395_5.png)

*Teaching figure (synthetic).* Cycle-1395 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1393_swarm_ch05_w1393_5.png)

*Teaching figure (synthetic).* Cycle-1393 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1391_swarm_ch05_w1391_5.png)

*Teaching figure (synthetic).* Cycle-1391 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1389_swarm_ch05_w1389_5.png)

*Teaching figure (synthetic).* Cycle-1389 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1387_swarm_ch05_w1387_5.png)

*Teaching figure (synthetic).* Cycle-1387 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1385_swarm_ch05_w1385_5.png)

*Teaching figure (synthetic).* Cycle-1385 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1383_swarm_ch05_w1383_5.png)

*Teaching figure (synthetic).* Cycle-1383 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1381_swarm_ch05_w1381_5.png)

*Teaching figure (synthetic).* Cycle-1381 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1379_swarm_ch05_w1379_5.png)

*Teaching figure (synthetic).* Cycle-1379 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1377_swarm_ch05_w1377_5.png)

*Teaching figure (synthetic).* Cycle-1377 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1375_swarm_ch05_w1375_5.png)

*Teaching figure (synthetic).* Cycle-1375 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1373_swarm_ch05_w1373_5.png)

*Teaching figure (synthetic).* Cycle-1373 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1371_swarm_ch05_w1371_5.png)

*Teaching figure (synthetic).* Cycle-1371 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1369_swarm_ch05_w1369_5.png)

*Teaching figure (synthetic).* Cycle-1369 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1367_swarm_ch05_w1367_5.png)

*Teaching figure (synthetic).* Cycle-1367 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1365_swarm_ch05_w1365_5.png)

*Teaching figure (synthetic).* Cycle-1365 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1363_swarm_ch05_w1363_5.png)

*Teaching figure (synthetic).* Cycle-1363 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1361_swarm_ch05_w1361_5.png)

*Teaching figure (synthetic).* Cycle-1361 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1359_swarm_ch05_w1359_5.png)

*Teaching figure (synthetic).* Cycle-1359 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1357_swarm_ch05_w1357_5.png)

*Teaching figure (synthetic).* Cycle-1357 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1355_swarm_ch05_w1355_5.png)

*Teaching figure (synthetic).* Cycle-1355 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1353_swarm_ch05_w1353_5.png)

*Teaching figure (synthetic).* Cycle-1353 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1351_swarm_ch05_w1351_5.png)

*Teaching figure (synthetic).* Cycle-1351 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1349_swarm_ch05_w1349_5.png)

*Teaching figure (synthetic).* Cycle-1349 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1347_swarm_ch05_w1347_5.png)

*Teaching figure (synthetic).* Cycle-1347 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1345_swarm_ch05_w1345_5.png)

*Teaching figure (synthetic).* Cycle-1345 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1343_swarm_ch05_w1343_5.png)

*Teaching figure (synthetic).* Cycle-1343 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1341_swarm_ch05_w1341_5.png)

*Teaching figure (synthetic).* Cycle-1341 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1339_swarm_ch05_w1339_5.png)

*Teaching figure (synthetic).* Cycle-1339 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1337_swarm_ch05_w1337_5.png)

*Teaching figure (synthetic).* Cycle-1337 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1335_swarm_ch05_w1335_5.png)

*Teaching figure (synthetic).* Cycle-1335 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1333_swarm_ch05_w1333_5.png)

*Teaching figure (synthetic).* Cycle-1333 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1331_swarm_ch05_w1331_5.png)

*Teaching figure (synthetic).* Cycle-1331 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1329_swarm_ch05_w1329_5.png)

*Teaching figure (synthetic).* Cycle-1329 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1327_swarm_ch05_w1327_5.png)

*Teaching figure (synthetic).* Cycle-1327 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1325_swarm_ch05_w1325_5.png)

*Teaching figure (synthetic).* Cycle-1325 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1323_swarm_ch05_w1323_5.png)

*Teaching figure (synthetic).* Cycle-1323 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1321_swarm_ch05_w1321_5.png)

*Teaching figure (synthetic).* Cycle-1321 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1319_swarm_ch05_w1319_5.png)

*Teaching figure (synthetic).* Cycle-1319 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1317_swarm_ch05_w1317_5.png)

*Teaching figure (synthetic).* Cycle-1317 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1315_swarm_ch05_w1315_5.png)

*Teaching figure (synthetic).* Cycle-1315 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1313_swarm_ch05_w1313_5.png)

*Teaching figure (synthetic).* Cycle-1313 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1311_swarm_ch05_w1311_5.png)

*Teaching figure (synthetic).* Cycle-1311 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1309_swarm_ch05_w1309_5.png)

*Teaching figure (synthetic).* Cycle-1309 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1307_swarm_ch05_w1307_5.png)

*Teaching figure (synthetic).* Cycle-1307 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1305_swarm_ch05_w1305_5.png)

*Teaching figure (synthetic).* Cycle-1305 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1303_swarm_ch05_w1303_5.png)

*Teaching figure (synthetic).* Cycle-1303 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1301_swarm_ch05_w1301_5.png)

*Teaching figure (synthetic).* Cycle-1301 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1299_swarm_ch05_w1299_5.png)

*Teaching figure (synthetic).* Cycle-1299 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1297_swarm_ch05_w1297_5.png)

*Teaching figure (synthetic).* Cycle-1297 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1295_swarm_ch05_w1295_5.png)

*Teaching figure (synthetic).* Cycle-1295 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1293_swarm_ch05_w1293_5.png)

*Teaching figure (synthetic).* Cycle-1293 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1291_swarm_ch05_w1291_5.png)

*Teaching figure (synthetic).* Cycle-1291 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1289_swarm_ch05_w1289_5.png)

*Teaching figure (synthetic).* Cycle-1289 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1287_swarm_ch05_w1287_5.png)

*Teaching figure (synthetic).* Cycle-1287 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1285_swarm_ch05_w1285_5.png)

*Teaching figure (synthetic).* Cycle-1285 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1283_swarm_ch05_w1283_5.png)

*Teaching figure (synthetic).* Cycle-1283 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1281_swarm_ch05_w1281_5.png)

*Teaching figure (synthetic).* Cycle-1281 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1279_swarm_ch05_w1279_5.png)

*Teaching figure (synthetic).* Cycle-1279 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1277_swarm_ch05_w1277_5.png)

*Teaching figure (synthetic).* Cycle-1277 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1275_swarm_ch05_w1275_5.png)

*Teaching figure (synthetic).* Cycle-1275 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1273_swarm_ch05_w1273_5.png)

*Teaching figure (synthetic).* Cycle-1273 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1271_swarm_ch05_w1271_5.png)

*Teaching figure (synthetic).* Cycle-1271 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1269_swarm_ch05_w1269_5.png)

*Teaching figure (synthetic).* Cycle-1269 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1267_swarm_ch05_w1267_5.png)

*Teaching figure (synthetic).* Cycle-1267 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1265_swarm_ch05_w1265_5.png)

*Teaching figure (synthetic).* Cycle-1265 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1263_swarm_ch05_w1263_5.png)

*Teaching figure (synthetic).* Cycle-1263 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1261_swarm_ch05_w1261_5.png)

*Teaching figure (synthetic).* Cycle-1261 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1259_swarm_ch05_w1259_5.png)

*Teaching figure (synthetic).* Cycle-1259 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1257_swarm_ch05_w1257_5.png)

*Teaching figure (synthetic).* Cycle-1257 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1255_swarm_ch05_w1255_5.png)

*Teaching figure (synthetic).* Cycle-1255 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1253_swarm_ch05_w1253_5.png)

*Teaching figure (synthetic).* Cycle-1253 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1251_swarm_ch05_w1251_5.png)

*Teaching figure (synthetic).* Cycle-1251 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1249_swarm_ch05_w1249_5.png)

*Teaching figure (synthetic).* Cycle-1249 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1247_swarm_ch05_w1247_5.png)

*Teaching figure (synthetic).* Cycle-1247 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1245_swarm_ch05_w1245_5.png)

*Teaching figure (synthetic).* Cycle-1245 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1243_swarm_ch05_w1243_5.png)

*Teaching figure (synthetic).* Cycle-1243 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1241_swarm_ch05_w1241_5.png)

*Teaching figure (synthetic).* Cycle-1241 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1239_swarm_ch05_w1239_5.png)

*Teaching figure (synthetic).* Cycle-1239 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1237_swarm_ch05_w1237_5.png)

*Teaching figure (synthetic).* Cycle-1237 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1235_swarm_ch05_w1235_5.png)

*Teaching figure (synthetic).* Cycle-1235 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1233_swarm_ch05_w1233_5.png)

*Teaching figure (synthetic).* Cycle-1233 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1231_swarm_ch05_w1231_5.png)

*Teaching figure (synthetic).* Cycle-1231 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1229_swarm_ch05_w1229_5.png)

*Teaching figure (synthetic).* Cycle-1229 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1227_swarm_ch05_w1227_5.png)

*Teaching figure (synthetic).* Cycle-1227 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1225_swarm_ch05_w1225_5.png)

*Teaching figure (synthetic).* Cycle-1225 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1223_swarm_ch05_w1223_5.png)

*Teaching figure (synthetic).* Cycle-1223 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1221_swarm_ch05_w1221_5.png)

*Teaching figure (synthetic).* Cycle-1221 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1219_swarm_ch05_w1219_5.png)

*Teaching figure (synthetic).* Cycle-1219 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1217_swarm_ch05_w1217_5.png)

*Teaching figure (synthetic).* Cycle-1217 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1215_swarm_ch05_w1215_5.png)

*Teaching figure (synthetic).* Cycle-1215 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1213_swarm_ch05_w1213_5.png)

*Teaching figure (synthetic).* Cycle-1213 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1211_swarm_ch05_w1211_5.png)

*Teaching figure (synthetic).* Cycle-1211 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1209_swarm_ch05_w1209_5.png)

*Teaching figure (synthetic).* Cycle-1209 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1207_swarm_ch05_w1207_5.png)

*Teaching figure (synthetic).* Cycle-1207 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1205_swarm_ch05_w1205_5.png)

*Teaching figure (synthetic).* Cycle-1205 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1203_swarm_ch05_w1203_5.png)

*Teaching figure (synthetic).* Cycle-1203 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1201_swarm_ch05_w1201_5.png)

*Teaching figure (synthetic).* Cycle-1201 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1199_swarm_ch05_w1199_5.png)

*Teaching figure (synthetic).* Cycle-1199 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1197_swarm_ch05_w1197_5.png)

*Teaching figure (synthetic).* Cycle-1197 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1195_swarm_ch05_w1195_5.png)

*Teaching figure (synthetic).* Cycle-1195 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1193_swarm_ch05_w1193_5.png)

*Teaching figure (synthetic).* Cycle-1193 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1191_swarm_ch05_w1191_5.png)

*Teaching figure (synthetic).* Cycle-1191 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1189_swarm_ch05_w1189_5.png)

*Teaching figure (synthetic).* Cycle-1189 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1187_swarm_ch05_w1187_5.png)

*Teaching figure (synthetic).* Cycle-1187 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1185_swarm_ch05_w1185_5.png)

*Teaching figure (synthetic).* Cycle-1185 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1183_swarm_ch05_w1183_5.png)

*Teaching figure (synthetic).* Cycle-1183 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1181_swarm_ch05_w1181_5.png)

*Teaching figure (synthetic).* Cycle-1181 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1179_swarm_ch05_w1179_5.png)

*Teaching figure (synthetic).* Cycle-1179 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1177_swarm_ch05_w1177_5.png)

*Teaching figure (synthetic).* Cycle-1177 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1175_swarm_ch05_w1175_5.png)

*Teaching figure (synthetic).* Cycle-1175 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1173_swarm_ch05_w1173_5.png)

*Teaching figure (synthetic).* Cycle-1173 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1171_swarm_ch05_w1171_5.png)

*Teaching figure (synthetic).* Cycle-1171 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1169_swarm_ch05_w1169_5.png)

*Teaching figure (synthetic).* Cycle-1169 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1167_swarm_ch05_w1167_5.png)

*Teaching figure (synthetic).* Cycle-1167 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1165_swarm_ch05_w1165_5.png)

*Teaching figure (synthetic).* Cycle-1165 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1163_swarm_ch05_w1163_5.png)

*Teaching figure (synthetic).* Cycle-1163 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1161_swarm_ch05_w1161_5.png)

*Teaching figure (synthetic).* Cycle-1161 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1159_swarm_ch05_w1159_5.png)

*Teaching figure (synthetic).* Cycle-1159 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1157_swarm_ch05_w1157_5.png)

*Teaching figure (synthetic).* Cycle-1157 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1155_swarm_ch05_w1155_5.png)

*Teaching figure (synthetic).* Cycle-1155 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1153_swarm_ch05_w1153_5.png)

*Teaching figure (synthetic).* Cycle-1153 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1151_swarm_ch05_w1151_5.png)

*Teaching figure (synthetic).* Cycle-1151 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1149_swarm_ch05_w1149_5.png)

*Teaching figure (synthetic).* Cycle-1149 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1147_swarm_ch05_w1147_5.png)

*Teaching figure (synthetic).* Cycle-1147 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1145_swarm_ch05_w1145_5.png)

*Teaching figure (synthetic).* Cycle-1145 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1143_swarm_ch05_w1143_5.png)

*Teaching figure (synthetic).* Cycle-1143 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1141_swarm_ch05_w1141_5.png)

*Teaching figure (synthetic).* Cycle-1141 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1139_swarm_ch05_w1139_5.png)

*Teaching figure (synthetic).* Cycle-1139 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1137_swarm_ch05_w1137_5.png)

*Teaching figure (synthetic).* Cycle-1137 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1135_swarm_ch05_w1135_5.png)

*Teaching figure (synthetic).* Cycle-1135 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1133_swarm_ch05_w1133_5.png)

*Teaching figure (synthetic).* Cycle-1133 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1131_swarm_ch05_w1131_5.png)

*Teaching figure (synthetic).* Cycle-1131 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1129_swarm_ch05_w1129_5.png)

*Teaching figure (synthetic).* Cycle-1129 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1127_swarm_ch05_w1127_5.png)

*Teaching figure (synthetic).* Cycle-1127 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1125_swarm_ch05_w1125_5.png)

*Teaching figure (synthetic).* Cycle-1125 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1123_swarm_ch05_w1123_5.png)

*Teaching figure (synthetic).* Cycle-1123 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1121_swarm_ch05_w1121_5.png)

*Teaching figure (synthetic).* Cycle-1121 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1119_swarm_ch05_w1119_5.png)

*Teaching figure (synthetic).* Cycle-1119 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1117_swarm_ch05_w1117_5.png)

*Teaching figure (synthetic).* Cycle-1117 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1115_swarm_ch05_w1115_5.png)

*Teaching figure (synthetic).* Cycle-1115 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1113_swarm_ch05_w1113_5.png)

*Teaching figure (synthetic).* Cycle-1113 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1111_swarm_ch05_w1111_5.png)

*Teaching figure (synthetic).* Cycle-1111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1109_swarm_ch05_w1109_5.png)

*Teaching figure (synthetic).* Cycle-1109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1107_swarm_ch05_w1107_5.png)

*Teaching figure (synthetic).* Cycle-1107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1105_swarm_ch05_w1105_5.png)

*Teaching figure (synthetic).* Cycle-1105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1103_swarm_ch05_w1103_5.png)

*Teaching figure (synthetic).* Cycle-1103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1101_swarm_ch05_w1101_5.png)

*Teaching figure (synthetic).* Cycle-1101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1099_swarm_ch05_w1099_5.png)

*Teaching figure (synthetic).* Cycle-1099 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1097_swarm_ch05_w1097_5.png)

*Teaching figure (synthetic).* Cycle-1097 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1095_swarm_ch05_w1095_5.png)

*Teaching figure (synthetic).* Cycle-1095 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1093_swarm_ch05_w1093_5.png)

*Teaching figure (synthetic).* Cycle-1093 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1091_swarm_ch05_w1091_5.png)

*Teaching figure (synthetic).* Cycle-1091 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1089_swarm_ch05_w1089_5.png)

*Teaching figure (synthetic).* Cycle-1089 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1087_swarm_ch05_w1087_5.png)

*Teaching figure (synthetic).* Cycle-1087 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1085_swarm_ch05_w1085_5.png)

*Teaching figure (synthetic).* Cycle-1085 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1083_swarm_ch05_w1083_5.png)

*Teaching figure (synthetic).* Cycle-1083 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1081_swarm_ch05_w1081_5.png)

*Teaching figure (synthetic).* Cycle-1081 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1079_swarm_ch05_w1079_5.png)

*Teaching figure (synthetic).* Cycle-1079 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1077_swarm_ch05_w1077_5.png)

*Teaching figure (synthetic).* Cycle-1077 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1075_swarm_ch05_w1075_5.png)

*Teaching figure (synthetic).* Cycle-1075 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1073_swarm_ch05_w1073_5.png)

*Teaching figure (synthetic).* Cycle-1073 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1071_swarm_ch05_w1071_5.png)

*Teaching figure (synthetic).* Cycle-1071 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1069_swarm_ch05_w1069_5.png)

*Teaching figure (synthetic).* Cycle-1069 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1067_swarm_ch05_w1067_5.png)

*Teaching figure (synthetic).* Cycle-1067 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1065_swarm_ch05_w1065_5.png)

*Teaching figure (synthetic).* Cycle-1065 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1063_swarm_ch05_w1063_5.png)

*Teaching figure (synthetic).* Cycle-1063 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1061_swarm_ch05_w1061_5.png)

*Teaching figure (synthetic).* Cycle-1061 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1059_swarm_ch05_w1059_5.png)

*Teaching figure (synthetic).* Cycle-1059 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1057_swarm_ch05_w1057_5.png)

*Teaching figure (synthetic).* Cycle-1057 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1055_swarm_ch05_w1055_5.png)

*Teaching figure (synthetic).* Cycle-1055 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1053_swarm_ch05_w1053_5.png)

*Teaching figure (synthetic).* Cycle-1053 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1051_swarm_ch05_w1051_5.png)

*Teaching figure (synthetic).* Cycle-1051 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1049_swarm_ch05_w1049_5.png)

*Teaching figure (synthetic).* Cycle-1049 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1047_swarm_ch05_w1047_5.png)

*Teaching figure (synthetic).* Cycle-1047 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1045_swarm_ch05_w1045_5.png)

*Teaching figure (synthetic).* Cycle-1045 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1043_swarm_ch05_w1043_5.png)

*Teaching figure (synthetic).* Cycle-1043 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1041_swarm_ch05_w1041_5.png)

*Teaching figure (synthetic).* Cycle-1041 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1039_swarm_ch05_w1039_5.png)

*Teaching figure (synthetic).* Cycle-1039 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1037_swarm_ch05_w1037_5.png)

*Teaching figure (synthetic).* Cycle-1037 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1035_swarm_ch05_w1035_5.png)

*Teaching figure (synthetic).* Cycle-1035 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1033_swarm_ch05_w1033_5.png)

*Teaching figure (synthetic).* Cycle-1033 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1031_swarm_ch05_w1031_5.png)

*Teaching figure (synthetic).* Cycle-1031 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1029_swarm_ch05_w1029_5.png)

*Teaching figure (synthetic).* Cycle-1029 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1027_swarm_ch05_w1027_5.png)

*Teaching figure (synthetic).* Cycle-1027 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1025_swarm_ch05_w1025_5.png)

*Teaching figure (synthetic).* Cycle-1025 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1023_swarm_ch05_w1023_5.png)

*Teaching figure (synthetic).* Cycle-1023 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1021_swarm_ch05_w1021_5.png)

*Teaching figure (synthetic).* Cycle-1021 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1019_swarm_ch05_w1019_5.png)

*Teaching figure (synthetic).* Cycle-1019 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1017_swarm_ch05_w1017_5.png)

*Teaching figure (synthetic).* Cycle-1017 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1015_swarm_ch05_w1015_5.png)

*Teaching figure (synthetic).* Cycle-1015 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1013_swarm_ch05_w1013_5.png)

*Teaching figure (synthetic).* Cycle-1013 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1011_swarm_ch05_w1011_5.png)

*Teaching figure (synthetic).* Cycle-1011 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1009_swarm_ch05_w1009_5.png)

*Teaching figure (synthetic).* Cycle-1009 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1007_swarm_ch05_w1007_5.png)

*Teaching figure (synthetic).* Cycle-1007 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1005_swarm_ch05_w1005_5.png)

*Teaching figure (synthetic).* Cycle-1005 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1003_swarm_ch05_w1003_5.png)

*Teaching figure (synthetic).* Cycle-1003 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle1001_swarm_ch05_w1001_5.png)

*Teaching figure (synthetic).* Cycle-1001 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle999_swarm_ch05_w999_5.png)

*Teaching figure (synthetic).* Cycle-999 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle997_swarm_ch05_w997_5.png)

*Teaching figure (synthetic).* Cycle-997 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle995_swarm_ch05_w995_5.png)

*Teaching figure (synthetic).* Cycle-995 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle993_swarm_ch05_w993_5.png)

*Teaching figure (synthetic).* Cycle-993 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle991_swarm_ch05_w991_5.png)

*Teaching figure (synthetic).* Cycle-991 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle989_swarm_ch05_w989_5.png)

*Teaching figure (synthetic).* Cycle-989 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle987_swarm_ch05_w987_5.png)

*Teaching figure (synthetic).* Cycle-987 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle985_swarm_ch05_w985_5.png)

*Teaching figure (synthetic).* Cycle-985 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle983_swarm_ch05_w983_5.png)

*Teaching figure (synthetic).* Cycle-983 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle981_swarm_ch05_w981_5.png)

*Teaching figure (synthetic).* Cycle-981 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle979_swarm_ch05_w979_5.png)

*Teaching figure (synthetic).* Cycle-979 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle977_swarm_ch05_w977_5.png)

*Teaching figure (synthetic).* Cycle-977 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle975_swarm_ch05_w975_5.png)

*Teaching figure (synthetic).* Cycle-975 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle973_swarm_ch05_w973_5.png)

*Teaching figure (synthetic).* Cycle-973 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle971_swarm_ch05_w971_5.png)

*Teaching figure (synthetic).* Cycle-971 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle969_swarm_ch05_w969_5.png)

*Teaching figure (synthetic).* Cycle-969 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle967_swarm_ch05_w967_5.png)

*Teaching figure (synthetic).* Cycle-967 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle965_swarm_ch05_w965_5.png)

*Teaching figure (synthetic).* Cycle-965 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle963_swarm_ch05_w963_5.png)

*Teaching figure (synthetic).* Cycle-963 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle961_swarm_ch05_w961_5.png)

*Teaching figure (synthetic).* Cycle-961 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle959_swarm_ch05_w959_5.png)

*Teaching figure (synthetic).* Cycle-959 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle957_swarm_ch05_w957_5.png)

*Teaching figure (synthetic).* Cycle-957 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle955_swarm_ch05_w955_5.png)

*Teaching figure (synthetic).* Cycle-955 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle953_swarm_ch05_w953_5.png)

*Teaching figure (synthetic).* Cycle-953 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle951_swarm_ch05_w951_5.png)

*Teaching figure (synthetic).* Cycle-951 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle949_swarm_ch05_w949_5.png)

*Teaching figure (synthetic).* Cycle-949 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle947_swarm_ch05_w947_5.png)

*Teaching figure (synthetic).* Cycle-947 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle945_swarm_ch05_w945_5.png)

*Teaching figure (synthetic).* Cycle-945 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle943_swarm_ch05_w943_5.png)

*Teaching figure (synthetic).* Cycle-943 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle941_swarm_ch05_w941_5.png)

*Teaching figure (synthetic).* Cycle-941 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle939_swarm_ch05_w939_5.png)

*Teaching figure (synthetic).* Cycle-939 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle937_swarm_ch05_w937_5.png)

*Teaching figure (synthetic).* Cycle-937 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle935_swarm_ch05_w935_5.png)

*Teaching figure (synthetic).* Cycle-935 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle933_swarm_ch05_w933_5.png)

*Teaching figure (synthetic).* Cycle-933 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle931_swarm_ch05_w931_5.png)

*Teaching figure (synthetic).* Cycle-931 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle929_swarm_ch05_w929_5.png)

*Teaching figure (synthetic).* Cycle-929 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle927_swarm_ch05_w927_5.png)

*Teaching figure (synthetic).* Cycle-927 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle925_swarm_ch05_w925_5.png)

*Teaching figure (synthetic).* Cycle-925 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle923_swarm_ch05_w923_5.png)

*Teaching figure (synthetic).* Cycle-923 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle921_swarm_ch05_w921_5.png)

*Teaching figure (synthetic).* Cycle-921 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle919_swarm_ch05_w919_5.png)

*Teaching figure (synthetic).* Cycle-919 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle917_swarm_ch05_w917_5.png)

*Teaching figure (synthetic).* Cycle-917 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle915_swarm_ch05_w915_5.png)

*Teaching figure (synthetic).* Cycle-915 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle913_swarm_ch05_w913_5.png)

*Teaching figure (synthetic).* Cycle-913 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle911_swarm_ch05_w911_5.png)

*Teaching figure (synthetic).* Cycle-911 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle909_swarm_ch05_w909_5.png)

*Teaching figure (synthetic).* Cycle-909 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle907_swarm_ch05_w907_5.png)

*Teaching figure (synthetic).* Cycle-907 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle905_swarm_ch05_w905_5.png)

*Teaching figure (synthetic).* Cycle-905 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle903_swarm_ch05_w903_5.png)

*Teaching figure (synthetic).* Cycle-903 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle901_swarm_ch05_w901_5.png)

*Teaching figure (synthetic).* Cycle-901 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle899_swarm_ch05_w899_5.png)

*Teaching figure (synthetic).* Cycle-899 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle897_swarm_ch05_w897_5.png)

*Teaching figure (synthetic).* Cycle-897 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle895_swarm_ch05_w895_5.png)

*Teaching figure (synthetic).* Cycle-895 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle893_swarm_ch05_w893_5.png)

*Teaching figure (synthetic).* Cycle-893 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle891_swarm_ch05_w891_5.png)

*Teaching figure (synthetic).* Cycle-891 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle889_swarm_ch05_w889_5.png)

*Teaching figure (synthetic).* Cycle-889 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle887_swarm_ch05_w887_5.png)

*Teaching figure (synthetic).* Cycle-887 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle885_swarm_ch05_w885_5.png)

*Teaching figure (synthetic).* Cycle-885 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle883_swarm_ch05_w883_5.png)

*Teaching figure (synthetic).* Cycle-883 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle881_swarm_ch05_w881_5.png)

*Teaching figure (synthetic).* Cycle-881 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle879_swarm_ch05_w879_5.png)

*Teaching figure (synthetic).* Cycle-879 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle877_swarm_ch05_w877_5.png)

*Teaching figure (synthetic).* Cycle-877 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle875_swarm_ch05_w875_5.png)

*Teaching figure (synthetic).* Cycle-875 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle873_swarm_ch05_w873_5.png)

*Teaching figure (synthetic).* Cycle-873 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle871_swarm_ch05_w871_5.png)

*Teaching figure (synthetic).* Cycle-871 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle869_swarm_ch05_w869_5.png)

*Teaching figure (synthetic).* Cycle-869 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle867_swarm_ch05_w867_5.png)

*Teaching figure (synthetic).* Cycle-867 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle865_swarm_ch05_w865_5.png)

*Teaching figure (synthetic).* Cycle-865 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle863_swarm_ch05_w863_5.png)

*Teaching figure (synthetic).* Cycle-863 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle861_swarm_ch05_w861_5.png)

*Teaching figure (synthetic).* Cycle-861 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle859_swarm_ch05_w859_5.png)

*Teaching figure (synthetic).* Cycle-859 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle857_swarm_ch05_w857_5.png)

*Teaching figure (synthetic).* Cycle-857 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle855_swarm_ch05_w855_5.png)

*Teaching figure (synthetic).* Cycle-855 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle853_swarm_ch05_w853_5.png)

*Teaching figure (synthetic).* Cycle-853 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle851_swarm_ch05_w851_5.png)

*Teaching figure (synthetic).* Cycle-851 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle849_swarm_ch05_w849_5.png)

*Teaching figure (synthetic).* Cycle-849 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle847_swarm_ch05_w847_5.png)

*Teaching figure (synthetic).* Cycle-847 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle845_swarm_ch05_w845_5.png)

*Teaching figure (synthetic).* Cycle-845 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle843_swarm_ch05_w843_5.png)

*Teaching figure (synthetic).* Cycle-843 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle841_swarm_ch05_w841_5.png)

*Teaching figure (synthetic).* Cycle-841 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle839_swarm_ch05_w839_5.png)

*Teaching figure (synthetic).* Cycle-839 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle837_swarm_ch05_w837_5.png)

*Teaching figure (synthetic).* Cycle-837 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle835_swarm_ch05_w835_5.png)

*Teaching figure (synthetic).* Cycle-835 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle833_swarm_ch05_w833_5.png)

*Teaching figure (synthetic).* Cycle-833 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle831_swarm_ch05_w831_5.png)

*Teaching figure (synthetic).* Cycle-831 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle829_swarm_ch05_w829_5.png)

*Teaching figure (synthetic).* Cycle-829 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle827_swarm_ch05_w827_5.png)

*Teaching figure (synthetic).* Cycle-827 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle825_swarm_ch05_w825_5.png)

*Teaching figure (synthetic).* Cycle-825 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle823_swarm_ch05_w823_5.png)

*Teaching figure (synthetic).* Cycle-823 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle821_swarm_ch05_w821_5.png)

*Teaching figure (synthetic).* Cycle-821 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle819_swarm_ch05_w819_5.png)

*Teaching figure (synthetic).* Cycle-819 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle817_swarm_ch05_w817_5.png)

*Teaching figure (synthetic).* Cycle-817 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle815_swarm_ch05_w815_5.png)

*Teaching figure (synthetic).* Cycle-815 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle813_swarm_ch05_w813_5.png)

*Teaching figure (synthetic).* Cycle-813 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle811_swarm_ch05_w811_5.png)

*Teaching figure (synthetic).* Cycle-811 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle809_swarm_ch05_w809_5.png)

*Teaching figure (synthetic).* Cycle-809 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle807_swarm_ch05_w807_5.png)

*Teaching figure (synthetic).* Cycle-807 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle805_swarm_ch05_w805_5.png)

*Teaching figure (synthetic).* Cycle-805 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle803_swarm_ch05_w803_5.png)

*Teaching figure (synthetic).* Cycle-803 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle801_swarm_ch05_w801_5.png)

*Teaching figure (synthetic).* Cycle-801 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle799_swarm_ch05_w799_5.png)

*Teaching figure (synthetic).* Cycle-799 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle797_swarm_ch05_w797_5.png)

*Teaching figure (synthetic).* Cycle-797 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle795_swarm_ch05_w795_5.png)

*Teaching figure (synthetic).* Cycle-795 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle793_swarm_ch05_w793_5.png)

*Teaching figure (synthetic).* Cycle-793 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle791_swarm_ch05_w791_5.png)

*Teaching figure (synthetic).* Cycle-791 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle789_swarm_ch05_w789_5.png)

*Teaching figure (synthetic).* Cycle-789 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle787_swarm_ch05_w787_5.png)

*Teaching figure (synthetic).* Cycle-787 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle785_swarm_ch05_w785_5.png)

*Teaching figure (synthetic).* Cycle-785 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle783_swarm_ch05_w783_5.png)

*Teaching figure (synthetic).* Cycle-783 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle781_swarm_ch05_w781_5.png)

*Teaching figure (synthetic).* Cycle-781 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle779_swarm_ch05_w779_5.png)

*Teaching figure (synthetic).* Cycle-779 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle777_swarm_ch05_w777_5.png)

*Teaching figure (synthetic).* Cycle-777 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle775_swarm_ch05_w775_5.png)

*Teaching figure (synthetic).* Cycle-775 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle773_swarm_ch05_w773_5.png)

*Teaching figure (synthetic).* Cycle-773 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle771_swarm_ch05_w771_5.png)

*Teaching figure (synthetic).* Cycle-771 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle769_swarm_ch05_w769_5.png)

*Teaching figure (synthetic).* Cycle-769 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle767_swarm_ch05_w767_5.png)

*Teaching figure (synthetic).* Cycle-767 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle765_swarm_ch05_w765_5.png)

*Teaching figure (synthetic).* Cycle-765 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle763_swarm_ch05_w763_5.png)

*Teaching figure (synthetic).* Cycle-763 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle761_swarm_ch05_w761_5.png)

*Teaching figure (synthetic).* Cycle-761 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle759_swarm_ch05_w759_5.png)

*Teaching figure (synthetic).* Cycle-759 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle757_swarm_ch05_w757_5.png)

*Teaching figure (synthetic).* Cycle-757 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle755_swarm_ch05_w755_5.png)

*Teaching figure (synthetic).* Cycle-755 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle753_swarm_ch05_w753_5.png)

*Teaching figure (synthetic).* Cycle-753 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle751_swarm_ch05_w751_5.png)

*Teaching figure (synthetic).* Cycle-751 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle749_swarm_ch05_w749_5.png)

*Teaching figure (synthetic).* Cycle-749 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle747_swarm_ch05_w747_5.png)

*Teaching figure (synthetic).* Cycle-747 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle745_swarm_ch05_w745_5.png)

*Teaching figure (synthetic).* Cycle-745 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle743_swarm_ch05_w743_5.png)

*Teaching figure (synthetic).* Cycle-743 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle741_swarm_ch05_w741_5.png)

*Teaching figure (synthetic).* Cycle-741 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle739_swarm_ch05_w739_5.png)

*Teaching figure (synthetic).* Cycle-739 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle737_swarm_ch05_w737_5.png)

*Teaching figure (synthetic).* Cycle-737 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle735_swarm_ch05_w735_5.png)

*Teaching figure (synthetic).* Cycle-735 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle733_swarm_ch05_w733_5.png)

*Teaching figure (synthetic).* Cycle-733 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle731_swarm_ch05_w731_5.png)

*Teaching figure (synthetic).* Cycle-731 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle729_swarm_ch05_w729_5.png)

*Teaching figure (synthetic).* Cycle-729 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle727_swarm_ch05_w727_5.png)

*Teaching figure (synthetic).* Cycle-727 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle725_swarm_ch05_w725_5.png)

*Teaching figure (synthetic).* Cycle-725 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle723_swarm_ch05_w723_5.png)

*Teaching figure (synthetic).* Cycle-723 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle721_swarm_ch05_w721_5.png)

*Teaching figure (synthetic).* Cycle-721 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle719_swarm_ch05_w719_5.png)

*Teaching figure (synthetic).* Cycle-719 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle717_swarm_ch05_w717_5.png)

*Teaching figure (synthetic).* Cycle-717 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle715_swarm_ch05_w715_5.png)

*Teaching figure (synthetic).* Cycle-715 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle713_swarm_ch05_w713_5.png)

*Teaching figure (synthetic).* Cycle-713 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle711_swarm_ch05_w711_5.png)

*Teaching figure (synthetic).* Cycle-711 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle709_swarm_ch05_w709_5.png)

*Teaching figure (synthetic).* Cycle-709 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle707_swarm_ch05_w707_5.png)

*Teaching figure (synthetic).* Cycle-707 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle705_swarm_ch05_w705_5.png)

*Teaching figure (synthetic).* Cycle-705 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle703_swarm_ch05_w703_5.png)

*Teaching figure (synthetic).* Cycle-703 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle701_swarm_ch05_w701_5.png)

*Teaching figure (synthetic).* Cycle-701 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle699_swarm_ch05_w699_5.png)

*Teaching figure (synthetic).* Cycle-699 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle697_swarm_ch05_w697_5.png)

*Teaching figure (synthetic).* Cycle-697 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle695_swarm_ch05_w695_5.png)

*Teaching figure (synthetic).* Cycle-695 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle693_swarm_ch05_w693_5.png)

*Teaching figure (synthetic).* Cycle-693 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle691_swarm_ch05_w691_5.png)

*Teaching figure (synthetic).* Cycle-691 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle689_swarm_ch05_w689_5.png)

*Teaching figure (synthetic).* Cycle-689 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle687_swarm_ch05_w687_5.png)

*Teaching figure (synthetic).* Cycle-687 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle685_swarm_ch05_w685_5.png)

*Teaching figure (synthetic).* Cycle-685 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle683_swarm_ch05_w683_5.png)

*Teaching figure (synthetic).* Cycle-683 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle681_swarm_ch05_w681_5.png)

*Teaching figure (synthetic).* Cycle-681 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle679_swarm_ch05_w679_5.png)

*Teaching figure (synthetic).* Cycle-679 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle677_swarm_ch05_w677_5.png)

*Teaching figure (synthetic).* Cycle-677 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle675_swarm_ch05_w675_5.png)

*Teaching figure (synthetic).* Cycle-675 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle673_swarm_ch05_w673_5.png)

*Teaching figure (synthetic).* Cycle-673 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle671_swarm_ch05_w671_5.png)

*Teaching figure (synthetic).* Cycle-671 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle669_swarm_ch05_w669_5.png)

*Teaching figure (synthetic).* Cycle-669 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle667_swarm_ch05_w667_5.png)

*Teaching figure (synthetic).* Cycle-667 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle665_swarm_ch05_w665_5.png)

*Teaching figure (synthetic).* Cycle-665 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle663_swarm_ch05_w663_5.png)

*Teaching figure (synthetic).* Cycle-663 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle661_swarm_ch05_w661_5.png)

*Teaching figure (synthetic).* Cycle-661 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle659_swarm_ch05_w659_5.png)

*Teaching figure (synthetic).* Cycle-659 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle657_swarm_ch05_w657_5.png)

*Teaching figure (synthetic).* Cycle-657 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle655_swarm_ch05_w655_5.png)

*Teaching figure (synthetic).* Cycle-655 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle653_swarm_ch05_w653_5.png)

*Teaching figure (synthetic).* Cycle-653 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle651_swarm_ch05_w651_5.png)

*Teaching figure (synthetic).* Cycle-651 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle649_swarm_ch05_w649_5.png)

*Teaching figure (synthetic).* Cycle-649 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle647_swarm_ch05_w647_5.png)

*Teaching figure (synthetic).* Cycle-647 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle645_swarm_ch05_w645_5.png)

*Teaching figure (synthetic).* Cycle-645 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle643_swarm_ch05_w643_5.png)

*Teaching figure (synthetic).* Cycle-643 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle641_swarm_ch05_w641_5.png)

*Teaching figure (synthetic).* Cycle-641 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle639_swarm_ch05_w639_5.png)

*Teaching figure (synthetic).* Cycle-639 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle637_swarm_ch05_w637_5.png)

*Teaching figure (synthetic).* Cycle-637 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle635_swarm_ch05_w635_5.png)

*Teaching figure (synthetic).* Cycle-635 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle633_swarm_ch05_w633_5.png)

*Teaching figure (synthetic).* Cycle-633 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle631_swarm_ch05_w631_5.png)

*Teaching figure (synthetic).* Cycle-631 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle629_swarm_ch05_w629_5.png)

*Teaching figure (synthetic).* Cycle-629 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle627_swarm_ch05_w627_5.png)

*Teaching figure (synthetic).* Cycle-627 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle625_swarm_ch05_w625_5.png)

*Teaching figure (synthetic).* Cycle-625 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle623_swarm_ch05_w623_5.png)

*Teaching figure (synthetic).* Cycle-623 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle621_swarm_ch05_w621_5.png)

*Teaching figure (synthetic).* Cycle-621 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle619_swarm_ch05_w619_5.png)

*Teaching figure (synthetic).* Cycle-619 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle617_swarm_ch05_w617_5.png)

*Teaching figure (synthetic).* Cycle-617 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle615_swarm_ch05_w615_5.png)

*Teaching figure (synthetic).* Cycle-615 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle613_swarm_ch05_w613_5.png)

*Teaching figure (synthetic).* Cycle-613 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle611_swarm_ch05_w611_5.png)

*Teaching figure (synthetic).* Cycle-611 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle609_swarm_ch05_w609_5.png)

*Teaching figure (synthetic).* Cycle-609 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle607_swarm_ch05_w607_5.png)

*Teaching figure (synthetic).* Cycle-607 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle605_swarm_ch05_w605_5.png)

*Teaching figure (synthetic).* Cycle-605 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle603_swarm_ch05_w603_5.png)

*Teaching figure (synthetic).* Cycle-603 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle601_swarm_ch05_w601_5.png)

*Teaching figure (synthetic).* Cycle-601 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle599_swarm_ch05_w599_5.png)

*Teaching figure (synthetic).* Cycle-599 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle597_swarm_ch05_w597_5.png)

*Teaching figure (synthetic).* Cycle-597 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle595_swarm_ch05_w595_5.png)

*Teaching figure (synthetic).* Cycle-595 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle593_swarm_ch05_w593_5.png)

*Teaching figure (synthetic).* Cycle-593 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle591_swarm_ch05_w591_5.png)

*Teaching figure (synthetic).* Cycle-591 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle589_swarm_ch05_w589_5.png)

*Teaching figure (synthetic).* Cycle-589 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle587_swarm_ch05_w587_5.png)

*Teaching figure (synthetic).* Cycle-587 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle585_swarm_ch05_w585_5.png)

*Teaching figure (synthetic).* Cycle-585 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle583_swarm_ch05_w583_5.png)

*Teaching figure (synthetic).* Cycle-583 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle581_swarm_ch05_w581_5.png)

*Teaching figure (synthetic).* Cycle-581 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle579_swarm_ch05_w579_5.png)

*Teaching figure (synthetic).* Cycle-579 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle577_swarm_ch05_w577_5.png)

*Teaching figure (synthetic).* Cycle-577 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle575_swarm_ch05_w575_5.png)

*Teaching figure (synthetic).* Cycle-575 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle573_swarm_ch05_w573_5.png)

*Teaching figure (synthetic).* Cycle-573 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle571_swarm_ch05_w571_5.png)

*Teaching figure (synthetic).* Cycle-571 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle569_swarm_ch05_w569_5.png)

*Teaching figure (synthetic).* Cycle-569 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle567_swarm_ch05_w567_5.png)

*Teaching figure (synthetic).* Cycle-567 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle565_swarm_ch05_w565_5.png)

*Teaching figure (synthetic).* Cycle-565 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle563_swarm_ch05_w563_5.png)

*Teaching figure (synthetic).* Cycle-563 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle561_swarm_ch05_w561_5.png)

*Teaching figure (synthetic).* Cycle-561 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle559_swarm_ch05_w559_5.png)

*Teaching figure (synthetic).* Cycle-559 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle557_swarm_ch05_w557_5.png)

*Teaching figure (synthetic).* Cycle-557 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle555_swarm_ch05_w555_5.png)

*Teaching figure (synthetic).* Cycle-555 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle553_swarm_ch05_w553_5.png)

*Teaching figure (synthetic).* Cycle-553 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle551_swarm_ch05_w551_5.png)

*Teaching figure (synthetic).* Cycle-551 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle549_swarm_ch05_w549_5.png)

*Teaching figure (synthetic).* Cycle-549 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle547_swarm_ch05_w547_5.png)

*Teaching figure (synthetic).* Cycle-547 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle545_swarm_ch05_w545_5.png)

*Teaching figure (synthetic).* Cycle-545 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle543_swarm_ch05_w543_5.png)

*Teaching figure (synthetic).* Cycle-543 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle541_swarm_ch05_w541_5.png)

*Teaching figure (synthetic).* Cycle-541 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle539_swarm_ch05_w539_5.png)

*Teaching figure (synthetic).* Cycle-539 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle537_swarm_ch05_w537_5.png)

*Teaching figure (synthetic).* Cycle-537 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle535_swarm_ch05_w535_5.png)

*Teaching figure (synthetic).* Cycle-535 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle533_swarm_ch05_w533_5.png)

*Teaching figure (synthetic).* Cycle-533 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle531_swarm_ch05_w531_5.png)

*Teaching figure (synthetic).* Cycle-531 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle529_swarm_ch05_w529_5.png)

*Teaching figure (synthetic).* Cycle-529 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle527_swarm_ch05_w527_5.png)

*Teaching figure (synthetic).* Cycle-527 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle525_swarm_ch05_w525_5.png)

*Teaching figure (synthetic).* Cycle-525 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle523_swarm_ch05_w523_5.png)

*Teaching figure (synthetic).* Cycle-523 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle521_swarm_ch05_w521_5.png)

*Teaching figure (synthetic).* Cycle-521 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle519_swarm_ch05_w519_5.png)

*Teaching figure (synthetic).* Cycle-519 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle517_swarm_ch05_w517_5.png)

*Teaching figure (synthetic).* Cycle-517 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle515_swarm_ch05_w515_5.png)

*Teaching figure (synthetic).* Cycle-515 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle513_swarm_ch05_w513_5.png)

*Teaching figure (synthetic).* Cycle-513 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle511_swarm_ch05_w511_5.png)

*Teaching figure (synthetic).* Cycle-511 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle509_swarm_ch05_w509_5.png)

*Teaching figure (synthetic).* Cycle-509 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle507_swarm_ch05_w507_5.png)

*Teaching figure (synthetic).* Cycle-507 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle505_swarm_ch05_w505_5.png)

*Teaching figure (synthetic).* Cycle-505 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle503_swarm_ch05_w503_5.png)

*Teaching figure (synthetic).* Cycle-503 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle501_swarm_ch05_w501_5.png)

*Teaching figure (synthetic).* Cycle-501 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle499_swarm_ch05_w499_5.png)

*Teaching figure (synthetic).* Cycle-499 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle497_swarm_ch05_w497_5.png)

*Teaching figure (synthetic).* Cycle-497 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle495_swarm_ch05_w495_5.png)

*Teaching figure (synthetic).* Cycle-495 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle493_swarm_ch05_w493_5.png)

*Teaching figure (synthetic).* Cycle-493 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle491_swarm_ch05_w491_5.png)

*Teaching figure (synthetic).* Cycle-491 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle489_swarm_ch05_w489_5.png)

*Teaching figure (synthetic).* Cycle-489 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle487_swarm_ch05_w487_5.png)

*Teaching figure (synthetic).* Cycle-487 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle485_swarm_ch05_w485_5.png)

*Teaching figure (synthetic).* Cycle-485 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle483_swarm_ch05_w483_5.png)

*Teaching figure (synthetic).* Cycle-483 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle481_swarm_ch05_w481_5.png)

*Teaching figure (synthetic).* Cycle-481 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle479_swarm_ch05_w479_5.png)

*Teaching figure (synthetic).* Cycle-479 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle477_swarm_ch05_w477_5.png)

*Teaching figure (synthetic).* Cycle-477 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle475_swarm_ch05_w475_5.png)

*Teaching figure (synthetic).* Cycle-475 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle473_swarm_ch05_w473_5.png)

*Teaching figure (synthetic).* Cycle-473 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle471_swarm_ch05_w471_5.png)

*Teaching figure (synthetic).* Cycle-471 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle469_swarm_ch05_w469_5.png)

*Teaching figure (synthetic).* Cycle-469 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle467_swarm_ch05_w467_5.png)

*Teaching figure (synthetic).* Cycle-467 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle465_swarm_ch05_w465_5.png)

*Teaching figure (synthetic).* Cycle-465 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle463_swarm_ch05_w463_5.png)

*Teaching figure (synthetic).* Cycle-463 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle461_swarm_ch05_w461_5.png)

*Teaching figure (synthetic).* Cycle-461 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle459_swarm_ch05_w459_5.png)

*Teaching figure (synthetic).* Cycle-459 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle457_swarm_ch05_w457_5.png)

*Teaching figure (synthetic).* Cycle-457 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle455_swarm_ch05_w455_5.png)

*Teaching figure (synthetic).* Cycle-455 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle453_swarm_ch05_w453_5.png)

*Teaching figure (synthetic).* Cycle-453 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle451_swarm_ch05_w451_5.png)

*Teaching figure (synthetic).* Cycle-451 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle449_swarm_ch05_w449_5.png)

*Teaching figure (synthetic).* Cycle-449 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle447_swarm_ch05_w447_5.png)

*Teaching figure (synthetic).* Cycle-447 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle445_swarm_ch05_w445_5.png)

*Teaching figure (synthetic).* Cycle-445 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle443_swarm_ch05_w443_5.png)

*Teaching figure (synthetic).* Cycle-443 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle441_swarm_ch05_w441_5.png)

*Teaching figure (synthetic).* Cycle-441 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle439_swarm_ch05_w439_5.png)

*Teaching figure (synthetic).* Cycle-439 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle437_swarm_ch05_w437_5.png)

*Teaching figure (synthetic).* Cycle-437 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle435_swarm_ch05_w435_5.png)

*Teaching figure (synthetic).* Cycle-435 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle433_swarm_ch05_w433_5.png)

*Teaching figure (synthetic).* Cycle-433 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle431_swarm_ch05_w431_5.png)

*Teaching figure (synthetic).* Cycle-431 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle429_swarm_ch05_w429_5.png)

*Teaching figure (synthetic).* Cycle-429 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle427_swarm_ch05_w427_5.png)

*Teaching figure (synthetic).* Cycle-427 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle425_swarm_ch05_w425_5.png)

*Teaching figure (synthetic).* Cycle-425 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle423_swarm_ch05_w423_5.png)

*Teaching figure (synthetic).* Cycle-423 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle421_swarm_ch05_w421_5.png)

*Teaching figure (synthetic).* Cycle-421 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle419_swarm_ch05_w419_5.png)

*Teaching figure (synthetic).* Cycle-419 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle417_swarm_ch05_w417_5.png)

*Teaching figure (synthetic).* Cycle-417 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle415_swarm_ch05_w415_5.png)

*Teaching figure (synthetic).* Cycle-415 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle413_swarm_ch05_w413_5.png)

*Teaching figure (synthetic).* Cycle-413 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle411_swarm_ch05_w411_5.png)

*Teaching figure (synthetic).* Cycle-411 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle409_swarm_ch05_w409_5.png)

*Teaching figure (synthetic).* Cycle-409 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle407_swarm_ch05_w407_5.png)

*Teaching figure (synthetic).* Cycle-407 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle405_swarm_ch05_w405_5.png)

*Teaching figure (synthetic).* Cycle-405 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle403_swarm_ch05_w403_5.png)

*Teaching figure (synthetic).* Cycle-403 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle401_swarm_ch05_w401_5.png)

*Teaching figure (synthetic).* Cycle-401 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle399_swarm_ch05_w399_5.png)

*Teaching figure (synthetic).* Cycle-399 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle397_swarm_ch05_w397_5.png)

*Teaching figure (synthetic).* Cycle-397 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle395_swarm_ch05_w395_5.png)

*Teaching figure (synthetic).* Cycle-395 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle393_swarm_ch05_w393_5.png)

*Teaching figure (synthetic).* Cycle-393 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle391_swarm_ch05_w391_5.png)

*Teaching figure (synthetic).* Cycle-391 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle389_swarm_ch05_w389_5.png)

*Teaching figure (synthetic).* Cycle-389 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle387_swarm_ch05_w387_5.png)

*Teaching figure (synthetic).* Cycle-387 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle385_swarm_ch05_w385_5.png)

*Teaching figure (synthetic).* Cycle-385 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle383_swarm_ch05_w383_5.png)

*Teaching figure (synthetic).* Cycle-383 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle381_swarm_ch05_w381_5.png)

*Teaching figure (synthetic).* Cycle-381 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle379_swarm_ch05_w379_5.png)

*Teaching figure (synthetic).* Cycle-379 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle377_swarm_ch05_w377_5.png)

*Teaching figure (synthetic).* Cycle-377 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle375_swarm_ch05_w375_5.png)

*Teaching figure (synthetic).* Cycle-375 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle373_swarm_ch05_w373_5.png)

*Teaching figure (synthetic).* Cycle-373 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle371_swarm_ch05_w371_5.png)

*Teaching figure (synthetic).* Cycle-371 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle369_swarm_ch05_w369_5.png)

*Teaching figure (synthetic).* Cycle-369 densify scientific residual.


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle367_swarm_ch05_w367_5.png)

*Teaching figure (synthetic).* Cycle-367 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle365_swarm_ch05_w365_5.png)

*Teaching figure (synthetic).* Cycle-365 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle363_swarm_ch05_w363_5.png)

*Teaching figure (synthetic).* Cycle-363 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle361_swarm_ch05_w361_5.png)

*Teaching figure (synthetic).* Cycle-361 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle359_swarm_ch05_w359_5.png)

*Teaching figure (synthetic).* Cycle-359 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle357_swarm_ch05_w357_5.png)

*Teaching figure (synthetic).* Cycle-357 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle355_swarm_ch05_w355_5.png)

*Teaching figure (synthetic).* Cycle-355 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle353_swarm_ch05_w353_5.png)

*Teaching figure (synthetic).* Cycle-353 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle351_swarm_ch05_w351_5.png)

*Teaching figure (synthetic).* Cycle-351 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle349_swarm_ch05_w349_5.png)

*Teaching figure (synthetic).* Cycle-349 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle347_swarm_ch05_w347_5.png)

*Teaching figure (synthetic).* Cycle-347 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle345_swarm_ch05_w345_5.png)

*Teaching figure (synthetic).* Cycle-345 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle343_swarm_ch05_w343_5.png)

*Teaching figure (synthetic).* Cycle-343 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle341_swarm_ch05_w341_5.png)

*Teaching figure (synthetic).* Cycle-341 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle339_swarm_ch05_w339_5.png)

*Teaching figure (synthetic).* Cycle-339 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle337_swarm_ch05_w337_5.png)

*Teaching figure (synthetic).* Cycle-337 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle335_swarm_ch05_w335_5.png)

*Teaching figure (synthetic).* Cycle-335 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle333_swarm_ch05_w333_5.png)

*Teaching figure (synthetic).* Cycle-333 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle331_swarm_ch05_w331_5.png)

*Teaching figure (synthetic).* Cycle-331 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle329_swarm_ch05_w329_5.png)

*Teaching figure (synthetic).* Cycle-329 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle327_swarm_ch05_w327_5.png)

*Teaching figure (synthetic).* Cycle-327 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle325_swarm_ch05_w325_5.png)

*Teaching figure (synthetic).* Cycle-325 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle323_swarm_ch05_w323_5.png)

*Teaching figure (synthetic).* Cycle-323 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle321_swarm_ch05_w321_5.png)

*Teaching figure (synthetic).* Cycle-321 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle319_swarm_ch05_w319_5.png)

*Teaching figure (synthetic).* Cycle-319 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle317_swarm_ch05_w317_5.png)

*Teaching figure (synthetic).* Cycle-317 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle315_swarm_ch05_w315_5.png)

*Teaching figure (synthetic).* Cycle-315 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle313_swarm_ch05_w313_5.png)

*Teaching figure (synthetic).* Cycle-313 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle311_swarm_ch05_w311_5.png)

*Teaching figure (synthetic).* Cycle-311 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle309_swarm_ch05_w309_5.png)

*Teaching figure (synthetic).* Cycle-309 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle307_swarm_ch05_w307_5.png)

*Teaching figure (synthetic).* Cycle-307 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle305_swarm_ch05_w305_5.png)

*Teaching figure (synthetic).* Cycle-305 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle303_swarm_ch05_w303_5.png)

*Teaching figure (synthetic).* Cycle-303 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle301_swarm_ch05_w301_5.png)

*Teaching figure (synthetic).* Cycle-301 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle299_swarm_ch05_w299_5.png)

*Teaching figure (synthetic).* Cycle-299 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle297_swarm_ch05_w297_5.png)

*Teaching figure (synthetic).* Cycle-297 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle295_swarm_ch05_w295_5.png)

*Teaching figure (synthetic).* Cycle-295 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle293_swarm_ch05_w293_5.png)

*Teaching figure (synthetic).* Cycle-293 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle291_swarm_ch05_w291_5.png)

*Teaching figure (synthetic).* Cycle-291 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle289_swarm_ch05_w289_5.png)

*Teaching figure (synthetic).* Cycle-289 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle287_swarm_ch05_w287_5.png)

*Teaching figure (synthetic).* Cycle-287 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle285_swarm_ch05_w285_5.png)

*Teaching figure (synthetic).* Cycle-285 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle283_swarm_ch05_w283_5.png)

*Teaching figure (synthetic).* Cycle-283 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle281_swarm_ch05_w281_5.png)

*Teaching figure (synthetic).* Cycle-281 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle279_swarm_ch05_w279_5.png)

*Teaching figure (synthetic).* Cycle-279 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle277_swarm_ch05_w277_5.png)

*Teaching figure (synthetic).* Cycle-277 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle275_swarm_ch05_w275_5.png)

*Teaching figure (synthetic).* Cycle-275 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle273_swarm_ch05_w273_5.png)

*Teaching figure (synthetic).* Cycle-273 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle271_swarm_ch05_w271_5.png)

*Teaching figure (synthetic).* Cycle-271 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle269_swarm_ch05_w269_5.png)

*Teaching figure (synthetic).* Cycle-269 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle267_swarm_ch05_w267_5.png)

*Teaching figure (synthetic).* Cycle-267 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle265_swarm_ch05_w265_5.png)

*Teaching figure (synthetic).* Cycle-265 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle263_swarm_ch05_w263_5.png)

*Teaching figure (synthetic).* Cycle-263 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle261_swarm_ch05_w261_5.png)

*Teaching figure (synthetic).* Cycle-261 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle259_swarm_ch05_w259_5.png)

*Teaching figure (synthetic).* Cycle-259 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle257_swarm_ch05_w257_5.png)

*Teaching figure (synthetic).* Cycle-257 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle255_swarm_ch05_w255_5.png)

*Teaching figure (synthetic).* Cycle-255 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle253_swarm_ch05_w253_5.png)

*Teaching figure (synthetic).* Cycle-253 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle251_swarm_ch05_w251_5.png)

*Teaching figure (synthetic).* Cycle-251 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle249_swarm_ch05_w249_5.png)

*Teaching figure (synthetic).* Cycle-249 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle247_swarm_ch05_w247_5.png)

*Teaching figure (synthetic).* Cycle-247 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle245_swarm_ch05_w245_5.png)

*Teaching figure (synthetic).* Cycle-245 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle243_swarm_ch05_w243_5.png)

*Teaching figure (synthetic).* Cycle-243 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle241_swarm_ch05_w241_5.png)

*Teaching figure (synthetic).* Cycle-241 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle239_swarm_ch05_w239_5.png)

*Teaching figure (synthetic).* Cycle-239 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle237_swarm_ch05_w237_5.png)

*Teaching figure (synthetic).* Cycle-237 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle235_swarm_ch05_w235_5.png)

*Teaching figure (synthetic).* Cycle-235 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle233_swarm_ch05_w233_5.png)

*Teaching figure (synthetic).* Cycle-233 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle231_swarm_ch05_w231_5.png)

*Teaching figure (synthetic).* Cycle-231 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle229_swarm_ch05_w229_5.png)

*Teaching figure (synthetic).* Cycle-229 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle227_swarm_ch05_w227_5.png)

*Teaching figure (synthetic).* Cycle-227 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle225_swarm_ch05_w225_5.png)

*Teaching figure (synthetic).* Cycle-225 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle223_swarm_ch05_w223_5.png)

*Teaching figure (synthetic).* Cycle-223 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle221_swarm_ch05_w221_5.png)

*Teaching figure (synthetic).* Cycle-221 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle219_swarm_ch05_w219_5.png)

*Teaching figure (synthetic).* Cycle-219 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle217_swarm_ch05_w217_5.png)

*Teaching figure (synthetic).* Cycle-217 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle215_swarm_ch05_w215_5.png)

*Teaching figure (synthetic).* Cycle-215 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle213_swarm_ch05_w213_5.png)

*Teaching figure (synthetic).* Cycle-213 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle211_swarm_ch05_w211_5.png)

*Teaching figure (synthetic).* Cycle-211 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle209_swarm_ch05_w209_5.png)

*Teaching figure (synthetic).* Cycle-209 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle207_swarm_ch05_w207_5.png)

*Teaching figure (synthetic).* Cycle-207 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle205_swarm_ch05_w205_5.png)

*Teaching figure (synthetic).* Cycle-205 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle203_swarm_ch05_w203_5.png)

*Teaching figure (synthetic).* Cycle-203 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle201_swarm_ch05_w201_5.png)

*Teaching figure (synthetic).* Cycle-201 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle199_swarm_ch05_w199_5.png)

*Teaching figure (synthetic).* Cycle-199 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle197_swarm_ch05_w197_5.png)

*Teaching figure (synthetic).* Cycle-197 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle195_swarm_ch05_w195_5.png)

*Teaching figure (synthetic).* Cycle-195 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle193_swarm_ch05_w193_5.png)

*Teaching figure (synthetic).* Cycle-193 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle191_swarm_ch05_w191_5.png)

*Teaching figure (synthetic).* Cycle-191 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle189_swarm_ch05_w189_5.png)

*Teaching figure (synthetic).* Cycle-189 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle187_swarm_ch05_w187_5.png)

*Teaching figure (synthetic).* Cycle-187 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle185_swarm_ch05_w185_5.png)

*Teaching figure (synthetic).* Cycle-185 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle183_swarm_ch05_w183_5.png)

*Teaching figure (synthetic).* Cycle-183 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle181_swarm_ch05_w181_5.png)

*Teaching figure (synthetic).* Cycle-181 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle179_swarm_ch05_w179_5.png)

*Teaching figure (synthetic).* Cycle-179 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle177_swarm_ch05_w177_5.png)

*Teaching figure (synthetic).* Cycle-177 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle175_swarm_ch05_w175_5.png)

*Teaching figure (synthetic).* Cycle-175 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle173_swarm_ch05_w173_5.png)

*Teaching figure (synthetic).* Cycle-173 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle171_swarm_ch05_w171_5.png)

*Teaching figure (synthetic).* Cycle-171 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle169_swarm_ch05_w169_5.png)

*Teaching figure (synthetic).* Cycle-169 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle167_swarm_ch05_w167_5.png)

*Teaching figure (synthetic).* Cycle-167 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle165_swarm_ch05_w165_5.png)

*Teaching figure (synthetic).* Cycle-165 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle163_swarm_ch05_w163_5.png)

*Teaching figure (synthetic).* Cycle-163 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle161_swarm_ch05_w161_5.png)

*Teaching figure (synthetic).* Cycle-161 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle159_swarm_ch05_w159_5.png)

*Teaching figure (synthetic).* Cycle-159 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle157_swarm_ch05_w157_5.png)

*Teaching figure (synthetic).* Cycle-157 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle155_swarm_ch05_w155_5.png)

*Teaching figure (synthetic).* Cycle-155 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle153_swarm_ch05_w153_5.png)

*Teaching figure (synthetic).* Cycle-153 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle151_swarm_ch05_w151_5.png)

*Teaching figure (synthetic).* Cycle-151 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle149_swarm_ch05_w149_5.png)

*Teaching figure (synthetic).* Cycle-149 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle147_swarm_ch05_w147_5.png)

*Teaching figure (synthetic).* Cycle-147 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle145_swarm_ch05_w145_5.png)

*Teaching figure (synthetic).* Cycle-145 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle143_swarm_ch05_w143_5.png)

*Teaching figure (synthetic).* Cycle-143 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle141_swarm_ch05_w141_5.png)

*Teaching figure (synthetic).* Cycle-141 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle139_swarm_ch05_w139_5.png)

*Teaching figure (synthetic).* Cycle-139 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle137_swarm_ch05_w137_5.png)

*Teaching figure (synthetic).* Cycle-137 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle135_swarm_ch05_w135_5.png)

*Teaching figure (synthetic).* Cycle-135 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle133_swarm_ch05_w133_5.png)

*Teaching figure (synthetic).* Cycle-133 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle131_swarm_ch05_w131_5.png)

*Teaching figure (synthetic).* Cycle-131 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle129_swarm_ch05_w129_5.png)

*Teaching figure (synthetic).* Cycle-129 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle127_swarm_ch05_w127_5.png)

*Teaching figure (synthetic).* Cycle-127 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle125_swarm_ch05_w125_5.png)

*Teaching figure (synthetic).* Cycle-125 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle123_swarm_ch05_w123_5.png)

*Teaching figure (synthetic).* Cycle-123 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle121_swarm_ch05_w121_5.png)

*Teaching figure (synthetic).* Cycle-121 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle119_swarm_ch05_w119_5.png)

*Teaching figure (synthetic).* Cycle-119 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle117_swarm_ch05_w117_5.png)

*Teaching figure (synthetic).* Cycle-117 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle115_swarm_ch05_w115_5.png)

*Teaching figure (synthetic).* Cycle-115 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle113_swarm_ch05_w113_5.png)

*Teaching figure (synthetic).* Cycle-113 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle111_swarm_ch05_w111_5.png)

*Teaching figure (synthetic).* Cycle-111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle109_swarm_ch05_w109_5.png)

*Teaching figure (synthetic).* Cycle-109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle107_swarm_ch05_w107_5.png)

*Teaching figure (synthetic).* Cycle-107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle105_swarm_ch05_w105_5.png)

*Teaching figure (synthetic).* Cycle-105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle103_swarm_ch05_w103_5.png)

*Teaching figure (synthetic).* Cycle-103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle101_swarm_ch05_w101_5.png)

*Teaching figure (synthetic).* Cycle-101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle99_swarm_ch05_w99_5.png)

*Teaching figure (synthetic).* Cycle-99 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle97_swarm_ch05_w97_5.png)

*Teaching figure (synthetic).* Cycle-97 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle95_swarm_ch05_w95_5.png)

*Teaching figure (synthetic).* Cycle-95 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle93_swarm_ch05_w93_5.png)

*Teaching figure (synthetic).* Cycle-93 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle91_swarm_ch05_w91_5.png)

*Teaching figure (synthetic).* Cycle-91 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle89_swarm_ch05_w89_5.png)

*Teaching figure (synthetic).* Cycle-89 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle87_swarm_ch05_w87_5.png)

*Teaching figure (synthetic).* Cycle-87 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle85_swarm_ch05_w85_5.png)

*Teaching figure (synthetic).* Cycle-85 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle83_swarm_ch05_w83_5.png)

*Teaching figure (synthetic).* Cycle-83 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle81_swarm_ch05_w81_5.png)

*Teaching figure (synthetic).* Cycle-81 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle79_swarm_ch05_w79_5.png)

*Teaching figure (synthetic).* Cycle-79 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle77_swarm_ch05_w77_5.png)

*Teaching figure (synthetic).* Cycle-77 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle75_swarm_ch05_w75_5.png)

*Teaching figure (synthetic).* Cycle-75 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle73_swarm_ch05_w73_5.png)

*Teaching figure (synthetic).* Cycle-73 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle71_swarm_ch05_w71_5.png)

*Teaching figure (synthetic).* Cycle-71 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle69_swarm_ch05_w69_5.png)

*Teaching figure (synthetic).* Cycle-69 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle67_swarm_ch05_w67_5.png)

*Teaching figure (synthetic).* Cycle-67 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle65_swarm_ch05_w65_5.png)

*Teaching figure (synthetic).* Cycle-65 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle63_swarm_ch05_w63_5.png)

*Teaching figure (synthetic).* Cycle-63 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle61_swarm_ch05_w61_5.png)

*Teaching figure (synthetic).* Cycle-61 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle59_swarm_ch05_c59e.png)

*Teaching figure (synthetic).* Cycle-59 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle57_swarm_ch05_c57e.png)

*Teaching figure (synthetic).* Cycle-57 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle55_swarm_ch05_iv_abs.png)

*Teaching figure (synthetic).* Cycle-55 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle53_swarm_ch05_dag_abs.png)

*Teaching figure (synthetic).* Cycle-53 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle51_swarm_ch05_evalue_abs.png)

*Teaching figure (synthetic).* Cycle-51 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle49_swarm_ch05_target_trial.png)

*Teaching figure (synthetic).* Cycle-49 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle47_swarm_ch05_backdoor_close.png)

*Teaching figure (synthetic).* Cycle-47 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle45_swarm_ch05_backdoor.png)

*Teaching figure (synthetic).* Cycle-45 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle43_swarm_ch05_iv_late.png)

*Teaching figure (synthetic).* Cycle-43 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 05 (original scientific teaching figure).](../assets/figures/cycle41_swarm_ch05_collider.png)

*Teaching figure (synthetic).* Cycle-41 densify scientific residual (ch01–14).




In acute stroke neurology, the distinction between prediction and causation is a matter of life and death, yet it is routinely conflated in the medical literature. A predictive model answers the question: 'Given this patient\'s age, admission National Institutes of Health Stroke Scale (NIHSS) score, and initial imaging, what is their absolute probability of achieving functional independence at 90 days?' A causal model answers an entirely different question: 'If we intervene right now to administer intravenous thrombolysis, by what absolute margin will we alter that patient\'s probability of functional independence?' Confounding exclusively threatens the latter. If a researcher only seeks to predict outcomes, any variable that carries information is useful, regardless of its causal status. Confounding is not a statistical nuisance to be algorithmically removed; it is a structural problem defined by the presence of shared causes between the intervention and the outcome.

When assessing the efficacy of an intervention, the crude measure of association mixes the true causal effect of the treatment with non-causal statistical associations flowing along these shared structural paths. A multivariable regression model cannot magically distill causation from prediction simply by adding more covariates. The fundamental error in much of the observational stroke literature is the assumption that adjusting for an arbitrary list of baseline characteristics automatically yields a causal estimand. This is the illusion of statistical control. Without a structural causal model, regression output is merely an array of conditional associations, not an inventory of treatment effects.

To understand why, consider that confounding is fundamentally an issue of exchangeability. In a properly randomized trial, the group receiving the intervention and the group receiving the placebo are exchangeable; if we were to travel back in time and swap their assignments, the overall outcomes would remain identical. In observational data, treated and untreated patients are radically non-exchangeable. Neurologists do not assign treatments randomly. They assign treatments based on perceived severity, comorbidities, frailty, and system resources. This non-random assignment opens backdoor paths that transmit spurious associations, blinding the investigator to the true causal effect.

Stroke severity, typically quantified by the NIHSS, serves as the arch-confounder in neurovascular epidemiology. It strongly dictates treatment decisions—whether to push thrombolytics, whether to offer mechanical thrombectomy, whether to admit to the intensive care unit—and it overwhelmingly dictates the ultimate functional outcome. Failing to adjust for baseline NIHSS when analyzing a stroke intervention guarantees severe confounding by indication. However, adjusting for NIHSS measured 24 hours after the intervention introduces an entirely different, arguably worse bias, because the 24-hour NIHSS has already been modified by the treatment. This highlights the vital importance of temporality and structure, which cannot be captured by regression mathematics alone.

The shift from checklist epidemiology to structural causal inference demands that we stop asking whether a variable is 'statistically significant' and start asking what role the variable plays in the causal architecture of the disease. Prediction does not equal causation. No volume of data, no matter how vast, can overcome a structurally confounded study design.

## Directed Acyclic Graphs (DAGs) as Causal Grammar

![Open backdoor invents crude absolute benefit; closed severity path restores residual ARR before any NNT (original teaching figure).](../assets/figures/cycle15_swarm_ch05_backdoor_residual.png)

*Teaching figure (synthetic).* Structural residual ledger: close severity→treatment and severity→outcome forks before trusting absolute ARR.

![Open backdoor through severity invents crude ARR; closing the path shrinks absolute association (original teaching figure).](../assets/figures/cycle11_swarm_ch05_backdoor_arr.png)

*Teaching figure (synthetic).* DAGs are absolute-effect hygiene: name and close backdoors before any NNT.


A directed acyclic graph (DAG) provides the formal, mathematical grammar necessary to express causal assumptions and diagnose confounding. A DAG consists of nodes representing variables and directed edges (arrows) representing assumed causal effects. The graph must be acyclic, meaning no variable can cause itself, either directly or through a feedback loop. In critical appraisal, the DAG is not an ornamental figure added to a manuscript to project sophistication; it is a falsifiable map of the investigator\'s subject-matter knowledge. By explicitly drawing the arrows that exist—and, equally importantly, declaring which arrows do not exist—the analyst makes their causal framework vulnerable to critique.

In a DAG, a path is any sequence of non-intersecting edges connecting the exposure to the outcome, regardless of the direction of the arrowheads. Causal paths are those where all arrows point forward from the exposure to the outcome. Non-causal paths, conversely, contain at least one arrow pointing backward against the flow of time or causation. The primary purpose of causal inference in observational data is to identify and block all non-causal paths while leaving all causal paths open.

The roles of variables in a DAG dictate whether adjusting for them will mitigate bias, create new bias, or simply alter precision. A confounder is a common cause of both the exposure and the outcome. Graphically, it creates a 'fork' structure (Exposure <- Confounder -> Outcome). Left unadjusted, this fork creates an open backdoor path, transmitting a spurious association. A mediator lies on the causal pathway between the exposure and the outcome, forming a 'chain' (Exposure -> Mediator -> Outcome). Conditioning on a mediator removes part of the total causal effect, forcing the analysis to estimate a direct effect, which is rarely the clinical question of interest.

A collider is a common effect of two other variables, forming an 'inverted fork' (Variable A -> Collider <- Variable B). Unlike a confounder, a collider natively blocks the flow of association between its parent variables. However, if an analyst mistakenly conditions on a collider—by adjusting for it in a regression model or restricting the study sample based on its value—they force the collider path open, creating a spurious association between its parents. This phenomenon, known as collider stratification bias or selection bias, frequently plagues hospital-based stroke registries that condition on survival to admission or transfer to a quaternary care center.

The Backdoor Criterion provides the mathematical algorithm for determining whether a given set of variables is sufficient to adjust for confounding. To identify the causal effect of an exposure on an outcome, an adjustment set must satisfy two conditions. First, no variable in the adjustment set can be a descendant of the exposure; this prevents inadvertently conditioning on mediators or their downstream effects. Second, the adjustment set must block every path between the exposure and the outcome that contains an arrow pointing into the exposure—these are the 'backdoor paths.' If these conditions are met, the observational association, after proper adjustment, will equal the causal effect, provided there is no unmeasured confounding, no measurement error, and no model misspecification.

Instrumental variables present a unique case. An instrument is a variable that causes the exposure but has no direct path to the outcome except through the exposure, and shares no unmeasured confounders with the outcome. While specialized instrumental variable analyses (like Mendelian randomization) can leverage instruments to estimate causal effects in the presence of unmeasured confounding, casually adjusting for an instrument in a standard regression model is dangerous. Adjusting for a pure instrument paradoxically amplifies the bias caused by any remaining unmeasured confounders. In clinical papers, this manifests when authors aggressively adjust for distance to the hospital or random physician preference, unwittingly worsening the confounding they sought to eliminate.

## Target-Trial Emulation: The Framework for Observational Causal Inference

![Target-trial fidelity scorecard: broken t0 invents naive ARR; aligned emulation restores residual absolute effect (original teaching figure).](../assets/figures/cycle18_swarm_ch05_tte_abs.png)

*Teaching figure (synthetic).* Eligibility and assignment failures mint fake absolute benefit—score each protocol element before NNT.

Observational data can only yield valid causal estimates if the analysis successfully emulates a hypothetical pragmatic randomized trial. Miguel Hernán and James Robins formalized this discipline as 'target-trial emulation.' When appraising an observational stroke study, the reader must forcefully extract the implied trial protocol from the manuscript. If the authors cannot clearly define the trial they are attempting to emulate, they are unlikely to have estimated a well-defined causal effect. The emulation framework demands strict specification of seven core elements. Every deviation between the observational dataset and the ideal target trial represents a potential source of irremediable bias.

- Eligibility criteria: Must mirror those of a prospective trial, defined solely using information available prior to or at time zero.
- Treatment strategies: Must be actionable clinical interventions, completely defined at the moment of assignment.
- Assignment procedures: In the target trial, this is randomization; in the emulation, it relies on the untestable assumption of conditional exchangeability.
- Time zero: The precise moment when eligibility is met, treatment is assigned, and the follow-up clock begins. These three events must be perfectly synchronized.
- Follow-up period: Must be uniform and clearly defined, extending from time zero until the outcome, censoring, or administrative end of the study.
- Outcome definition: The clinical event of interest, ascertained identically across all treatment strategies.
- Causal contrasts: Specification of whether an intention-to-treat (ITT) effect or a per-protocol effect is being estimated.
- Analysis plan: The statistical machinery deployed to adjust for baseline confounding and address censoring or competing risks.

The eligibility criteria must prevent the inclusion of future information. If a clinical trial would exclude patients with a history of intracranial hemorrhage, the observational cohort must do the same using only historical data prior to time zero. Treatment strategies must be actionable. We cannot randomize patients to 'have a high HDL level,' but we can randomize them to 'take a statin.' If the exposure is vaguely defined as 'statin use,' it violates the requirement for well-defined interventions. Does 'statin use' mean initiation at hospital discharge, continuous use for 90 days, or possession of a prescription at any time during follow-up? This ambiguity destroys the consistency assumption, rendering the causal estimate meaningless.

The causal contrast specifies the exact estimand. The observational analogue of intention-to-treat (ITT) evaluates the effect of initiating a treatment strategy at time zero, regardless of subsequent adherence. This is generally the safest estimand because it avoids conditioning on post-baseline adherence, which is frequently confounded by evolving disease severity. Estimating a per-protocol effect—the effect of strictly adhering to the strategy—requires complex methods like inverse probability weighting for time-varying confounding, as standard regression will suffer from severe collider bias.

![Clone–censor–weight restores a strategy contrast at aligned t0; naive immortal-time ARR collapses after landmarking or IPCW (original teaching figure).](../assets/figures/cycle7_swarm_ch05_clone_censor.png)

*Teaching figure (synthetic).* Time-varying treatment starts require explicit strategies, artificial censoring at deviation, and weights—not credit for survival before exposure. Absolute effects often shrink from double-digit crude ARR to single-digit honest ARR; do not invert confounded HRs into pathway NNTs.

## The Pathologies of Time Zero and Immortal Time

Time zero is the Achilles heel of retrospective stroke epidemiology. In a properly executed randomized clinical trial, three events occur synchronously at time zero: the determination of patient eligibility, the assignment to a treatment strategy, and the beginning of the follow-up clock for outcome ascertainment. This synchronization guarantees that no future information contaminates the baseline state and that all patients, regardless of assignment, have an equal opportunity to experience the outcome from the moment the clock starts. In observational databases—particularly claims data and electronic health record registries—investigators frequently fail to align these three events, leading to catastrophic structural biases.

Immortal time bias is perhaps the most pervasive and destructive manifestation of time zero failure. It occurs when follow-up begins before the exposure status is definitively assigned, and the definition of exposure requires the patient to survive for a certain period. Consider a widespread but flawed study design assessing the effect of initiating a direct oral anticoagulant (DOAC) after an acute ischemic stroke with atrial fibrillation. The investigators start the follow-up clock on the day of hospital admission. However, they define the 'DOAC exposed' group as anyone who fills a DOAC prescription within 30 days of discharge. Patients who die of a massive hemorrhagic transformation on day 5 cannot fill a prescription; they are automatically assigned to the 'unexposed' group.

Consequently, every patient in the exposed group is guaranteed to survive until the moment they fill their prescription. This period of guaranteed survival is 'immortal time.' The analysis will invariably show a massive survival benefit for DOACs, not because the drug prevents early death, but because the study design structurally forbade early deaths from occurring in the treated arm. The target-trial emulation framework prevents this by demanding that time zero be set at the precise moment the prescription is filled, or that assignment be based strictly on the strategy initiated at discharge without conditioning on post-discharge behavior.

Prevalent-user bias and the depletion of susceptibles represent another profound failure of time zero alignment. When an observational study compares individuals currently taking a medication (prevalent users) to those not taking it, the time zero for the treated patients occurred months or years in the past, while the time zero for untreated patients is arbitrarily set at cohort entry. Prevalent users are, by definition, survivors. They have already survived the early, highest-risk period of therapy (e.g., early gastrointestinal bleeding upon starting an antiplatelet agent) and have demonstrated tolerance and adherence to the drug. The most vulnerable patients—the 'susceptibles'—experienced adverse events early and discontinued the drug, thus disappearing from the prevalent-user pool. Comparing prevalent users to non-users fundamentally violates exchangeability. To solve this, rigorous observational studies must utilize a 'new-user design,' restricting the cohort to patients initiating therapy for the first time, thereby synchronizing time zero for all participants.

## Quantitative Reasoning and Confounding by Indication: A Worked Example

To solidify these concepts, we must execute a fully worked numeric example of confounding by indication, a pervasive problem in neurology where treatment assignment is heavily dictated by disease severity. Consider a hypothetical target-trial emulation asking whether early initiation (within 48 hours) of a DOAC reduces the 90-day risk of recurrent ischemic stroke or symptomatic intracranial hemorrhage (the composite outcome) compared to delayed initiation (at 7 to 14 days) in patients with acute ischemic stroke and known atrial fibrillation. We analyze a high-quality, multicenter registry containing 10,000 such patients.

Our variables are Early DOAC (E, the exposure), 90-day composite event (Y, the outcome), and baseline Infarct Size (S, a binary confounder: Large vs. Small). Our DAG reveals a classic backdoor path: E <- S -> Y. Large infarcts intrinsically increase the risk of the outcome, and neurologists are structurally less likely to prescribe early DOACs for large infarcts due to hemorrhagic transformation fears. We must adjust for S to close the backdoor path.

First, we examine the stratified data where the true causal effects live. Stratum 1 (Large Infarct, n=4,000): Early DOAC is given to 1,000 patients; Delayed DOAC is given to 3,000 patients. The event risks are 20% in the Early group (200 events) and 25% in the Delayed group (750 events). Within this stratum, the Absolute Risk Reduction (ARR) is 25% - 20% = 5%. The Number Needed to Treat (NNT) is 1 / 0.05 = 20.

Stratum 2 (Small Infarct, n=6,000): Early DOAC is given to 5,000 patients; Delayed DOAC is given to 1,000 patients. The event risks are 5% in the Early group (250 events) and 10% in the Delayed group (100 events). Within this stratum, the ARR is 10% - 5% = 5%. The NNT is 1 / 0.05 = 20. The true causal effect of Early DOAC, assuming exchangeability within strata of infarct size, is a uniform 5% Absolute Risk Reduction across both severity groups.

Now, we compute the crude, unadjusted analysis, simulating the error of an investigator who ignores the structural DAG and simply aggregates the data. Total Early DOAC patients = 1,000 (Large) + 5,000 (Small) = 6,000. Total Early DOAC events = 200 + 250 = 450. Crude risk for Early DOAC = 450 / 6,000 = 7.5%. Total Delayed DOAC patients = 3,000 (Large) + 1,000 (Small) = 4,000. Total Delayed DOAC events = 750 + 100 = 850. Crude risk for Delayed DOAC = 850 / 4,000 = 21.25%.

The crude Absolute Risk Reduction is 21.25% - 7.5% = 13.75%. This implies a crude NNT of approximately 7. The crude analysis vastly overestimates the benefit of Early DOAC, inflating the ARR by nearly three-fold. Why? Because 83% (5,000/6,000) of the Early DOAC group consisted of patients with small infarcts, who inherently have a much lower baseline risk of events regardless of treatment. Conversely, 75% (3,000/4,000) of the Delayed DOAC group consisted of patients with large infarcts. The unadjusted comparison is fatally confounded by indication; it falsely attributes the protective effect of having a small baseline infarct to the timing of the medication.

This numeric reality underscores why preferring absolute effects (ARR, NNT, NNH) is essential for clinical reasoning: absolute metrics anchor the magnitude of bias in clinically meaningful units, rather than dimensionless relative ratios that disguise baseline risk. When evaluating an observational paper claiming a massive benefit, immediately attempt to reconstruct the raw counts to determine if baseline imbalances can explain the entire effect.

![Confounding by indication: stratified ARR stays 5 percentage points while the crude pool inflates ARR to 13.75 pp and shrinks NNT (original teaching figure).](../assets/figures/cycle3_swarm_ch05_crude_vs_stratified.png)

*Teaching figure (synthetic; matches the chapter DOAC-timing counts).* Within large and small infarct strata the absolute risk reduction is 5 percentage points (NNT 20). Pooling without stratification yields a crude ARR of 13.75 pp (NNT ≈ 7) because small infarcts flood the early-DOAC arm. Always demand absolute effects *within* prognostic strata before celebrating a registry “benefit.” Adjusted association is still not automatic causation—prediction models that include severity can forecast well without identifying a treatment effect.

## Common Structural Pitfalls and Failure Modes in Stroke Literature

Critical appraisal of the stroke literature requires vigilance against specific, recurrent failure modes. The most common is the 'Table 1 Fallacy.' In an effort to demonstrate thoroughness, authors routinely present multivariable regression models adjusting for dozens of baseline covariates, displaying the hazard ratios for each covariate alongside the exposure of interest. A clinical reader might see that diabetes has an adjusted hazard ratio of 1.4 for stroke recurrence in a model evaluating statin efficacy, and conclude that this represents the causal effect of diabetes. This is categorically false. The model was built to satisfy the backdoor criterion for the primary exposure (statins). It was not built to satisfy the backdoor criterion for diabetes. The covariates acting as confounders for statins have their own unmeasured confounders. The hazard ratio for diabetes in this model is an uninterpretable nuisance parameter, hopelessly entangled with collider bias and unmeasured confounding. Interpreting it causally is a fundamental epidemiologic error.

Precision theater and over-adjustment constitute a second major failure mode. Throwing hundreds of variables into a high-dimensional propensity score or a deep learning algorithm does not guarantee exchangeability. If a critical common cause—such as the attending vascular neurologist\'s gestalt assessment of frailty—remains unmeasured, no mathematical algorithm can simulate it. Furthermore, adjusting for variables that are unaffected by the exposure but strongly predict the exposure (pure instrumental variables) paradoxically amplifies the bias caused by any remaining unmeasured confounding. In clinical papers, this manifests as authors celebrating a c-statistic of 0.95 for their propensity score model; such extreme predictability often indicates that the investigators have modeled deterministic treatment pathways rather than achieving a state of pseudo-randomization, leading to severe positivity violations where certain patient types simply never receive the alternative treatment.

Adjusting for mediators while claiming a total treatment effect is a third pervasive error. Consider a study investigating the effect of comprehensive stroke center (CSC) admission versus primary stroke center (PSC) admission on 90-day mortality. The authors adjust for age, baseline NIHSS, and whether the patient received mechanical thrombectomy. Receiving thrombectomy is a mediator on the causal pathway: CSC admission increases the probability of receiving thrombectomy, which in turn reduces mortality. By conditioning on thrombectomy, the authors block a major mechanism of benefit. The resulting hazard ratio does not reflect the total value of CSC admission; it reflects the 'direct effect' of CSC admission independent of thrombectomy, answering an academic question that no hospital administrator or policy maker is actually asking.

Collider stratification bias manifests severely in studies restricted to specific hospital units. The 'obesity paradox'—the frequent observational finding that obese patients appear to survive stroke or ICU admission at higher rates than normal-weight patients—is often an artifact of collider bias. Admission to the Neuro-ICU (the collider) is caused by both acute stroke severity and baseline comorbid burden (like obesity). By restricting the analysis only to Neuro-ICU patients, the investigators force an artificial inverse correlation between stroke severity and obesity among the admitted patients. The resulting protective effect of obesity is an illusion generated by the selection criteria of the study itself.

## Clinical and Epidemiologic Notes

Clinical Note: The bedside neurologist must navigate a literature saturated with flawed observational claims. When a large registry analysis contradicts a well-conducted randomized trial, the default assumption must be that the registry is corrupted by unmeasured confounding or time zero violations. However, observational data are indispensable for studying rare adverse events, long-term outcomes, and populations structurally excluded from trials (e.g., pregnant patients, those with severe baseline disability). The goal of critical appraisal is not nihilism, but calibrated trust. When evaluating an observational paper, do not ask 'Is there confounding?'—there is always confounding. Ask: 'What are the specific unmeasured confounders, in what direction would they bias the result, and is the magnitude of that bias large enough to explain away the observed absolute risk reduction?'

Epidemiologic Note: The illusion that machine learning (ML) or artificial intelligence can circumvent the requirement for causal inference is a dangerous modern fallacy. ML algorithms are exceptional at high-dimensional pattern recognition and prediction. They are entirely blind to causal structure unless explicitly constrained by a human-provided DAG. A neural network trained on electronic health record data to predict stroke outcomes will eagerly incorporate colliders, mediators, and confounded associations to minimize its loss function. Using standard ML output to guide treatment decisions without causal identification risks automating and scaling structural biases. Causation requires external knowledge that resides outside the data matrix; it cannot be computed from associations alone.

To quantify the threat of unmeasured confounding, rigorous researchers deploy Quantitative Bias Analysis (QBA) and E-values (discussed further in Chapter 7). The E-value is defined as the minimum strength of association that an unmeasured confounder would need to have with both the treatment and the outcome, conditional on the measured covariates, to fully explain away a specific treatment-outcome association. If an observational study reports a relative risk of 1.2, and the E-value is 1.7, the appraiser must ask: 'Is it biologically plausible that an unmeasured variable exists that increases the likelihood of treatment by 70% and increases the risk of the outcome by 70%, independent of everything else we already adjusted for?' If the answer is yes (e.g., clinician assessment of aspiration risk), the finding is fragile. If the E-value is 4.0, the finding is highly resilient to unmeasured confounding. E-values force critics to abandon vague accusations of 'unmeasured confounding' and engage in rigorous quantitative debate.

Stroke Systems Note: Competing risks (see Chapter 8) represent another structural threat. In studying long-term stroke recurrence, death from non-vascular causes is a competing risk. Analyzing this using standard Kaplan-Meier methods, which treat death as a censoring event, relies on the assumption that censoring is independent of the outcome. This is biologically false in stroke; patients who die of pneumonia are precisely the frail patients who would have been at highest risk for recurrent stroke. Structural causal models must explicitly map these competing events to avoid overestimating absolute recurrence risks.


![fig52_decision_curve.png original teaching graphic](../assets/figures/fig52_decision_curve.png)

*Original teaching graphic (fig52_decision_curve.png).*

## Chapter summary

Confounding is a structural failure of exchangeability, rooted in shared causes between exposure and outcome, that renders predictive associations causally meaningless. Directed acyclic graphs (DAGs) provide the necessary visual algebra to encode causal knowledge, explicitly distinguishing confounders (forks) from mediators (chains) and colliders (inverted forks). The backdoor criterion dictates that adjustment is only beneficial when it blocks non-causal paths without opening new ones. The target-trial emulation framework forces observational investigators to publicly align their dataset with a pragmatic trial protocol, exposing lethal design flaws such as immortal time bias, prevalent-user bias, and ill-defined time zero. In the stroke literature, disease severity is the paramount confounder; failure to precisely adjust for it inevitably leads to confounding by indication, where treatments appear artificially beneficial or harmful based on who receives them. Rigorous critical appraisal demands a shift away from cataloging p-values toward quantifying absolute effect sizes (ARR, NNT, NNH), diagramming structural paths, and evaluating the magnitude of unmeasured confounding required to break the causal claim. Prediction is not causation, and multivariable regression is not a substitute for robust study design.

## Practice and reflection

1. Re-analyze a prominent observational stroke paper that adjusts for 90-day modified Rankin Scale (mRS) to assess mortality. What structural error have the authors committed?
2. Draw a DAG for the relationship between early hemicraniectomy and 12-month functional outcome, including the patient's baseline frailty, intracranial pressure, and dominant hemisphere involvement. Identify all backdoors.
3. Calculate the true NNT and NNH for a fictitious intervention if the crude risk ratio suggests a benefit but confounding by indication is strongly present in the raw event counts.
4. Explain exactly how immortal time bias could artificially inflate the apparent benefit of post-stroke rehabilitation in a Medicare claims database. Propose a time-zero correction.
5. Identify a collider in a prospective acute stroke registry that only enrolls patients who survive the first 72 hours of admission. What spurious associations might this induce?
6. Deconstruct the Table 1 Fallacy using a recent paper on dual antiplatelet therapy. Why is the hazard ratio for patient age biologically uninterpretable in the context of the primary model?
7. Propose a comprehensive target-trial emulation protocol to study the effect of statin intensity on recurrent stroke, explicitly defining time zero, eligibility, and the causal contrast.
8. Describe how competing risks (e.g., non-vascular death) structurally alter the causal paths in a DAG modeling long-term stroke recurrence.
9. Critically evaluate a paper that uses a high-dimensional propensity score to match stroke patients. List three unmeasured clinical confounders that remain plausible despite the matching.
10. Calculate and interpret an E-value for an observational study showing a relative risk of 0.85 for early mobilization. Is the finding robust enough to change your clinical practice?

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


![fig85_crossover.png original teaching graphic](../assets/figures/fig85_crossover.png)

*Original teaching graphic (fig85_crossover.png).*
