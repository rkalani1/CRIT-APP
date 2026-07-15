# Chapter 3. Questions, PICO, Estimands, and Index Time

## Opening

![Validity and transportability (original).](../assets/figures/fig25_validity_transport.png)

*Validity and transportability (original).*
![Two claim templates for paper claims (original).](../assets/figures/crit_fig_prediction_vs_causation.png)

*Two claim templates for paper claims (original).*


A family already saw the press release. Your job is translation: map the paper to a prediction template or a causal template, then decide whether anything at the bedside should change today.


## Learning objectives

- Translate vague clinical curiosity into a structurally sound PICO or PECO question without losing physiologic or pragmatic meaning.
- Delineate the target population, study sample, and analytic set, computing transportability gaps between them.
- Specify the intervention, exposure, and comparator with sufficient operational granularity to reproduce the clinical decision.
- Construct a complete estimand under the ICH E9(R1) framework for an acute stroke trial and an observational cohort study.
- Define index time (t0) rigorously and explain how misaligned clocks destroy causal inference.
- Identify immortal time bias as a failure of index time alignment, using medication dispensing and procedural delays as paradigms.
- Formalize the quantitative causal contrast using potential outcomes notation, differentiating absolute effects (ARR) from relative measures.
- Reconstruct and critique the true estimand of a published paper when the authors conflate prediction with causation.
- Evaluate eligibility criteria not merely as safety guards, but as fundamental parameters defining the causal target.
- Identify neighbor questions that appear relevant but address different clinical decisions or temporal horizons.

![Estimand clock: index time and intercurrent policy required for transportable absolute ARR (original scientific teaching figure).](../assets/figures/cycle25_swarm_ch03_estimand_clock.png)

*Teaching figure (synthetic).* Cycle-25 densify scientific residual.

![Question residual: incomplete PICO or estimand blocks absolute ARR transport (original scientific teaching figure).](../assets/figures/cycle27_swarm_ch03_pico_heatmap.png)

*Teaching figure (synthetic).* Cycle-27 densify scientific residual.

![Index-time choice moves absolute risk curves (original scientific teaching figure).](../assets/figures/cycle29_swarm_ch03_index_time.png)

*Teaching figure (synthetic).* Cycle-29 densify scientific residual.

![Comparator choice rewrites absolute ARR (original scientific teaching figure).](../assets/figures/cycle31_swarm_ch03_comparator_arr.png)

*Teaching figure (synthetic).* Cycle-31 densify scientific residual.

![Intercurrent strategy changes absolute ARR (original scientific teaching figure).](../assets/figures/cycle33_swarm_ch03_intercurrent.png)

*Teaching figure (synthetic).* Cycle-33 densify scientific residual.

![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle35_swarm_ch03_pico_miss.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## Conceptual Core: The Linguistic Chaos of Clinical Medicine

![Estimand completeness residual: intercurrent and absolute summary often missing (original teaching figure).](../assets/figures/cycle22_swarm_ch03_estimand_complete.png)

*Teaching figure (synthetic).* Incomplete estimand kills transportable ARR.

![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle37_swarm_ch03_index_arr.png)

*Teaching figure (synthetic).* Cycle-37 densify scientific residual (ch01–14).

![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle39_swarm_ch03_ice_estimand.png)

*Teaching figure (synthetic).* Cycle-39 densify scientific residual (ch01–14).

![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle727_swarm_ch03_w727_3.png)

*Teaching figure (synthetic).* Cycle-727 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle725_swarm_ch03_w725_3.png)

*Teaching figure (synthetic).* Cycle-725 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle723_swarm_ch03_w723_3.png)

*Teaching figure (synthetic).* Cycle-723 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle721_swarm_ch03_w721_3.png)

*Teaching figure (synthetic).* Cycle-721 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle719_swarm_ch03_w719_3.png)

*Teaching figure (synthetic).* Cycle-719 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle717_swarm_ch03_w717_3.png)

*Teaching figure (synthetic).* Cycle-717 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle715_swarm_ch03_w715_3.png)

*Teaching figure (synthetic).* Cycle-715 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle713_swarm_ch03_w713_3.png)

*Teaching figure (synthetic).* Cycle-713 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle711_swarm_ch03_w711_3.png)

*Teaching figure (synthetic).* Cycle-711 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle709_swarm_ch03_w709_3.png)

*Teaching figure (synthetic).* Cycle-709 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle707_swarm_ch03_w707_3.png)

*Teaching figure (synthetic).* Cycle-707 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle705_swarm_ch03_w705_3.png)

*Teaching figure (synthetic).* Cycle-705 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle703_swarm_ch03_w703_3.png)

*Teaching figure (synthetic).* Cycle-703 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle701_swarm_ch03_w701_3.png)

*Teaching figure (synthetic).* Cycle-701 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle699_swarm_ch03_w699_3.png)

*Teaching figure (synthetic).* Cycle-699 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle697_swarm_ch03_w697_3.png)

*Teaching figure (synthetic).* Cycle-697 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle695_swarm_ch03_w695_3.png)

*Teaching figure (synthetic).* Cycle-695 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle693_swarm_ch03_w693_3.png)

*Teaching figure (synthetic).* Cycle-693 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle691_swarm_ch03_w691_3.png)

*Teaching figure (synthetic).* Cycle-691 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle689_swarm_ch03_w689_3.png)

*Teaching figure (synthetic).* Cycle-689 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle687_swarm_ch03_w687_3.png)

*Teaching figure (synthetic).* Cycle-687 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle685_swarm_ch03_w685_3.png)

*Teaching figure (synthetic).* Cycle-685 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle683_swarm_ch03_w683_3.png)

*Teaching figure (synthetic).* Cycle-683 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle681_swarm_ch03_w681_3.png)

*Teaching figure (synthetic).* Cycle-681 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle679_swarm_ch03_w679_3.png)

*Teaching figure (synthetic).* Cycle-679 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle677_swarm_ch03_w677_3.png)

*Teaching figure (synthetic).* Cycle-677 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle675_swarm_ch03_w675_3.png)

*Teaching figure (synthetic).* Cycle-675 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle673_swarm_ch03_w673_3.png)

*Teaching figure (synthetic).* Cycle-673 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle671_swarm_ch03_w671_3.png)

*Teaching figure (synthetic).* Cycle-671 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle669_swarm_ch03_w669_3.png)

*Teaching figure (synthetic).* Cycle-669 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle667_swarm_ch03_w667_3.png)

*Teaching figure (synthetic).* Cycle-667 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle665_swarm_ch03_w665_3.png)

*Teaching figure (synthetic).* Cycle-665 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle663_swarm_ch03_w663_3.png)

*Teaching figure (synthetic).* Cycle-663 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle661_swarm_ch03_w661_3.png)

*Teaching figure (synthetic).* Cycle-661 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle659_swarm_ch03_w659_3.png)

*Teaching figure (synthetic).* Cycle-659 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle657_swarm_ch03_w657_3.png)

*Teaching figure (synthetic).* Cycle-657 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle655_swarm_ch03_w655_3.png)

*Teaching figure (synthetic).* Cycle-655 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle653_swarm_ch03_w653_3.png)

*Teaching figure (synthetic).* Cycle-653 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle651_swarm_ch03_w651_3.png)

*Teaching figure (synthetic).* Cycle-651 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle649_swarm_ch03_w649_3.png)

*Teaching figure (synthetic).* Cycle-649 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle647_swarm_ch03_w647_3.png)

*Teaching figure (synthetic).* Cycle-647 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle645_swarm_ch03_w645_3.png)

*Teaching figure (synthetic).* Cycle-645 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle643_swarm_ch03_w643_3.png)

*Teaching figure (synthetic).* Cycle-643 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle641_swarm_ch03_w641_3.png)

*Teaching figure (synthetic).* Cycle-641 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle639_swarm_ch03_w639_3.png)

*Teaching figure (synthetic).* Cycle-639 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle637_swarm_ch03_w637_3.png)

*Teaching figure (synthetic).* Cycle-637 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle635_swarm_ch03_w635_3.png)

*Teaching figure (synthetic).* Cycle-635 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle633_swarm_ch03_w633_3.png)

*Teaching figure (synthetic).* Cycle-633 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle631_swarm_ch03_w631_3.png)

*Teaching figure (synthetic).* Cycle-631 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle629_swarm_ch03_w629_3.png)

*Teaching figure (synthetic).* Cycle-629 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle627_swarm_ch03_w627_3.png)

*Teaching figure (synthetic).* Cycle-627 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle625_swarm_ch03_w625_3.png)

*Teaching figure (synthetic).* Cycle-625 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle623_swarm_ch03_w623_3.png)

*Teaching figure (synthetic).* Cycle-623 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle621_swarm_ch03_w621_3.png)

*Teaching figure (synthetic).* Cycle-621 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle619_swarm_ch03_w619_3.png)

*Teaching figure (synthetic).* Cycle-619 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle617_swarm_ch03_w617_3.png)

*Teaching figure (synthetic).* Cycle-617 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle615_swarm_ch03_w615_3.png)

*Teaching figure (synthetic).* Cycle-615 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle613_swarm_ch03_w613_3.png)

*Teaching figure (synthetic).* Cycle-613 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle611_swarm_ch03_w611_3.png)

*Teaching figure (synthetic).* Cycle-611 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle609_swarm_ch03_w609_3.png)

*Teaching figure (synthetic).* Cycle-609 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle607_swarm_ch03_w607_3.png)

*Teaching figure (synthetic).* Cycle-607 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle605_swarm_ch03_w605_3.png)

*Teaching figure (synthetic).* Cycle-605 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle603_swarm_ch03_w603_3.png)

*Teaching figure (synthetic).* Cycle-603 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle601_swarm_ch03_w601_3.png)

*Teaching figure (synthetic).* Cycle-601 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle599_swarm_ch03_w599_3.png)

*Teaching figure (synthetic).* Cycle-599 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle597_swarm_ch03_w597_3.png)

*Teaching figure (synthetic).* Cycle-597 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle595_swarm_ch03_w595_3.png)

*Teaching figure (synthetic).* Cycle-595 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle593_swarm_ch03_w593_3.png)

*Teaching figure (synthetic).* Cycle-593 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle591_swarm_ch03_w591_3.png)

*Teaching figure (synthetic).* Cycle-591 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle589_swarm_ch03_w589_3.png)

*Teaching figure (synthetic).* Cycle-589 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle587_swarm_ch03_w587_3.png)

*Teaching figure (synthetic).* Cycle-587 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle585_swarm_ch03_w585_3.png)

*Teaching figure (synthetic).* Cycle-585 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle583_swarm_ch03_w583_3.png)

*Teaching figure (synthetic).* Cycle-583 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle581_swarm_ch03_w581_3.png)

*Teaching figure (synthetic).* Cycle-581 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle579_swarm_ch03_w579_3.png)

*Teaching figure (synthetic).* Cycle-579 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle577_swarm_ch03_w577_3.png)

*Teaching figure (synthetic).* Cycle-577 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle575_swarm_ch03_w575_3.png)

*Teaching figure (synthetic).* Cycle-575 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle573_swarm_ch03_w573_3.png)

*Teaching figure (synthetic).* Cycle-573 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle571_swarm_ch03_w571_3.png)

*Teaching figure (synthetic).* Cycle-571 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle569_swarm_ch03_w569_3.png)

*Teaching figure (synthetic).* Cycle-569 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle567_swarm_ch03_w567_3.png)

*Teaching figure (synthetic).* Cycle-567 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle565_swarm_ch03_w565_3.png)

*Teaching figure (synthetic).* Cycle-565 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle563_swarm_ch03_w563_3.png)

*Teaching figure (synthetic).* Cycle-563 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle561_swarm_ch03_w561_3.png)

*Teaching figure (synthetic).* Cycle-561 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle559_swarm_ch03_w559_3.png)

*Teaching figure (synthetic).* Cycle-559 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle557_swarm_ch03_w557_3.png)

*Teaching figure (synthetic).* Cycle-557 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle555_swarm_ch03_w555_3.png)

*Teaching figure (synthetic).* Cycle-555 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle553_swarm_ch03_w553_3.png)

*Teaching figure (synthetic).* Cycle-553 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle551_swarm_ch03_w551_3.png)

*Teaching figure (synthetic).* Cycle-551 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle549_swarm_ch03_w549_3.png)

*Teaching figure (synthetic).* Cycle-549 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle547_swarm_ch03_w547_3.png)

*Teaching figure (synthetic).* Cycle-547 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle545_swarm_ch03_w545_3.png)

*Teaching figure (synthetic).* Cycle-545 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle543_swarm_ch03_w543_3.png)

*Teaching figure (synthetic).* Cycle-543 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle541_swarm_ch03_w541_3.png)

*Teaching figure (synthetic).* Cycle-541 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle539_swarm_ch03_w539_3.png)

*Teaching figure (synthetic).* Cycle-539 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle537_swarm_ch03_w537_3.png)

*Teaching figure (synthetic).* Cycle-537 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle535_swarm_ch03_w535_3.png)

*Teaching figure (synthetic).* Cycle-535 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle533_swarm_ch03_w533_3.png)

*Teaching figure (synthetic).* Cycle-533 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle531_swarm_ch03_w531_3.png)

*Teaching figure (synthetic).* Cycle-531 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle529_swarm_ch03_w529_3.png)

*Teaching figure (synthetic).* Cycle-529 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle527_swarm_ch03_w527_3.png)

*Teaching figure (synthetic).* Cycle-527 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle525_swarm_ch03_w525_3.png)

*Teaching figure (synthetic).* Cycle-525 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle523_swarm_ch03_w523_3.png)

*Teaching figure (synthetic).* Cycle-523 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle521_swarm_ch03_w521_3.png)

*Teaching figure (synthetic).* Cycle-521 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle519_swarm_ch03_w519_3.png)

*Teaching figure (synthetic).* Cycle-519 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle517_swarm_ch03_w517_3.png)

*Teaching figure (synthetic).* Cycle-517 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle515_swarm_ch03_w515_3.png)

*Teaching figure (synthetic).* Cycle-515 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle513_swarm_ch03_w513_3.png)

*Teaching figure (synthetic).* Cycle-513 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle511_swarm_ch03_w511_3.png)

*Teaching figure (synthetic).* Cycle-511 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle509_swarm_ch03_w509_3.png)

*Teaching figure (synthetic).* Cycle-509 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle507_swarm_ch03_w507_3.png)

*Teaching figure (synthetic).* Cycle-507 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle505_swarm_ch03_w505_3.png)

*Teaching figure (synthetic).* Cycle-505 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle503_swarm_ch03_w503_3.png)

*Teaching figure (synthetic).* Cycle-503 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle501_swarm_ch03_w501_3.png)

*Teaching figure (synthetic).* Cycle-501 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle499_swarm_ch03_w499_3.png)

*Teaching figure (synthetic).* Cycle-499 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle497_swarm_ch03_w497_3.png)

*Teaching figure (synthetic).* Cycle-497 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle495_swarm_ch03_w495_3.png)

*Teaching figure (synthetic).* Cycle-495 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle493_swarm_ch03_w493_3.png)

*Teaching figure (synthetic).* Cycle-493 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle491_swarm_ch03_w491_3.png)

*Teaching figure (synthetic).* Cycle-491 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle489_swarm_ch03_w489_3.png)

*Teaching figure (synthetic).* Cycle-489 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle487_swarm_ch03_w487_3.png)

*Teaching figure (synthetic).* Cycle-487 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle485_swarm_ch03_w485_3.png)

*Teaching figure (synthetic).* Cycle-485 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle483_swarm_ch03_w483_3.png)

*Teaching figure (synthetic).* Cycle-483 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle481_swarm_ch03_w481_3.png)

*Teaching figure (synthetic).* Cycle-481 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle479_swarm_ch03_w479_3.png)

*Teaching figure (synthetic).* Cycle-479 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle477_swarm_ch03_w477_3.png)

*Teaching figure (synthetic).* Cycle-477 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle475_swarm_ch03_w475_3.png)

*Teaching figure (synthetic).* Cycle-475 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle473_swarm_ch03_w473_3.png)

*Teaching figure (synthetic).* Cycle-473 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle471_swarm_ch03_w471_3.png)

*Teaching figure (synthetic).* Cycle-471 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle469_swarm_ch03_w469_3.png)

*Teaching figure (synthetic).* Cycle-469 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle467_swarm_ch03_w467_3.png)

*Teaching figure (synthetic).* Cycle-467 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle465_swarm_ch03_w465_3.png)

*Teaching figure (synthetic).* Cycle-465 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle463_swarm_ch03_w463_3.png)

*Teaching figure (synthetic).* Cycle-463 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle461_swarm_ch03_w461_3.png)

*Teaching figure (synthetic).* Cycle-461 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle459_swarm_ch03_w459_3.png)

*Teaching figure (synthetic).* Cycle-459 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle457_swarm_ch03_w457_3.png)

*Teaching figure (synthetic).* Cycle-457 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle455_swarm_ch03_w455_3.png)

*Teaching figure (synthetic).* Cycle-455 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle453_swarm_ch03_w453_3.png)

*Teaching figure (synthetic).* Cycle-453 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle451_swarm_ch03_w451_3.png)

*Teaching figure (synthetic).* Cycle-451 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle449_swarm_ch03_w449_3.png)

*Teaching figure (synthetic).* Cycle-449 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle447_swarm_ch03_w447_3.png)

*Teaching figure (synthetic).* Cycle-447 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle445_swarm_ch03_w445_3.png)

*Teaching figure (synthetic).* Cycle-445 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle443_swarm_ch03_w443_3.png)

*Teaching figure (synthetic).* Cycle-443 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle441_swarm_ch03_w441_3.png)

*Teaching figure (synthetic).* Cycle-441 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle439_swarm_ch03_w439_3.png)

*Teaching figure (synthetic).* Cycle-439 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle437_swarm_ch03_w437_3.png)

*Teaching figure (synthetic).* Cycle-437 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle435_swarm_ch03_w435_3.png)

*Teaching figure (synthetic).* Cycle-435 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle433_swarm_ch03_w433_3.png)

*Teaching figure (synthetic).* Cycle-433 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle431_swarm_ch03_w431_3.png)

*Teaching figure (synthetic).* Cycle-431 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle429_swarm_ch03_w429_3.png)

*Teaching figure (synthetic).* Cycle-429 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle427_swarm_ch03_w427_3.png)

*Teaching figure (synthetic).* Cycle-427 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle425_swarm_ch03_w425_3.png)

*Teaching figure (synthetic).* Cycle-425 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle423_swarm_ch03_w423_3.png)

*Teaching figure (synthetic).* Cycle-423 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle421_swarm_ch03_w421_3.png)

*Teaching figure (synthetic).* Cycle-421 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle419_swarm_ch03_w419_3.png)

*Teaching figure (synthetic).* Cycle-419 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle417_swarm_ch03_w417_3.png)

*Teaching figure (synthetic).* Cycle-417 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle415_swarm_ch03_w415_3.png)

*Teaching figure (synthetic).* Cycle-415 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle413_swarm_ch03_w413_3.png)

*Teaching figure (synthetic).* Cycle-413 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle411_swarm_ch03_w411_3.png)

*Teaching figure (synthetic).* Cycle-411 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle409_swarm_ch03_w409_3.png)

*Teaching figure (synthetic).* Cycle-409 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle407_swarm_ch03_w407_3.png)

*Teaching figure (synthetic).* Cycle-407 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle405_swarm_ch03_w405_3.png)

*Teaching figure (synthetic).* Cycle-405 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle403_swarm_ch03_w403_3.png)

*Teaching figure (synthetic).* Cycle-403 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle401_swarm_ch03_w401_3.png)

*Teaching figure (synthetic).* Cycle-401 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle399_swarm_ch03_w399_3.png)

*Teaching figure (synthetic).* Cycle-399 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle397_swarm_ch03_w397_3.png)

*Teaching figure (synthetic).* Cycle-397 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle395_swarm_ch03_w395_3.png)

*Teaching figure (synthetic).* Cycle-395 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle393_swarm_ch03_w393_3.png)

*Teaching figure (synthetic).* Cycle-393 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle391_swarm_ch03_w391_3.png)

*Teaching figure (synthetic).* Cycle-391 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle389_swarm_ch03_w389_3.png)

*Teaching figure (synthetic).* Cycle-389 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle387_swarm_ch03_w387_3.png)

*Teaching figure (synthetic).* Cycle-387 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle385_swarm_ch03_w385_3.png)

*Teaching figure (synthetic).* Cycle-385 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle383_swarm_ch03_w383_3.png)

*Teaching figure (synthetic).* Cycle-383 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle381_swarm_ch03_w381_3.png)

*Teaching figure (synthetic).* Cycle-381 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle379_swarm_ch03_w379_3.png)

*Teaching figure (synthetic).* Cycle-379 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle377_swarm_ch03_w377_3.png)

*Teaching figure (synthetic).* Cycle-377 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle375_swarm_ch03_w375_3.png)

*Teaching figure (synthetic).* Cycle-375 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle373_swarm_ch03_w373_3.png)

*Teaching figure (synthetic).* Cycle-373 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle371_swarm_ch03_w371_3.png)

*Teaching figure (synthetic).* Cycle-371 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle369_swarm_ch03_w369_3.png)

*Teaching figure (synthetic).* Cycle-369 densify scientific residual.


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle367_swarm_ch03_w367_3.png)

*Teaching figure (synthetic).* Cycle-367 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle365_swarm_ch03_w365_3.png)

*Teaching figure (synthetic).* Cycle-365 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle363_swarm_ch03_w363_3.png)

*Teaching figure (synthetic).* Cycle-363 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle361_swarm_ch03_w361_3.png)

*Teaching figure (synthetic).* Cycle-361 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle359_swarm_ch03_w359_3.png)

*Teaching figure (synthetic).* Cycle-359 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle357_swarm_ch03_w357_3.png)

*Teaching figure (synthetic).* Cycle-357 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle355_swarm_ch03_w355_3.png)

*Teaching figure (synthetic).* Cycle-355 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle353_swarm_ch03_w353_3.png)

*Teaching figure (synthetic).* Cycle-353 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle351_swarm_ch03_w351_3.png)

*Teaching figure (synthetic).* Cycle-351 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle349_swarm_ch03_w349_3.png)

*Teaching figure (synthetic).* Cycle-349 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle347_swarm_ch03_w347_3.png)

*Teaching figure (synthetic).* Cycle-347 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle345_swarm_ch03_w345_3.png)

*Teaching figure (synthetic).* Cycle-345 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle343_swarm_ch03_w343_3.png)

*Teaching figure (synthetic).* Cycle-343 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle341_swarm_ch03_w341_3.png)

*Teaching figure (synthetic).* Cycle-341 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle339_swarm_ch03_w339_3.png)

*Teaching figure (synthetic).* Cycle-339 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle337_swarm_ch03_w337_3.png)

*Teaching figure (synthetic).* Cycle-337 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle335_swarm_ch03_w335_3.png)

*Teaching figure (synthetic).* Cycle-335 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle333_swarm_ch03_w333_3.png)

*Teaching figure (synthetic).* Cycle-333 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle331_swarm_ch03_w331_3.png)

*Teaching figure (synthetic).* Cycle-331 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle329_swarm_ch03_w329_3.png)

*Teaching figure (synthetic).* Cycle-329 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle327_swarm_ch03_w327_3.png)

*Teaching figure (synthetic).* Cycle-327 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle325_swarm_ch03_w325_3.png)

*Teaching figure (synthetic).* Cycle-325 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle323_swarm_ch03_w323_3.png)

*Teaching figure (synthetic).* Cycle-323 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle321_swarm_ch03_w321_3.png)

*Teaching figure (synthetic).* Cycle-321 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle319_swarm_ch03_w319_3.png)

*Teaching figure (synthetic).* Cycle-319 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle317_swarm_ch03_w317_3.png)

*Teaching figure (synthetic).* Cycle-317 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle315_swarm_ch03_w315_3.png)

*Teaching figure (synthetic).* Cycle-315 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle313_swarm_ch03_w313_3.png)

*Teaching figure (synthetic).* Cycle-313 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle311_swarm_ch03_w311_3.png)

*Teaching figure (synthetic).* Cycle-311 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle309_swarm_ch03_w309_3.png)

*Teaching figure (synthetic).* Cycle-309 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle307_swarm_ch03_w307_3.png)

*Teaching figure (synthetic).* Cycle-307 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle305_swarm_ch03_w305_3.png)

*Teaching figure (synthetic).* Cycle-305 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle303_swarm_ch03_w303_3.png)

*Teaching figure (synthetic).* Cycle-303 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle301_swarm_ch03_w301_3.png)

*Teaching figure (synthetic).* Cycle-301 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle299_swarm_ch03_w299_3.png)

*Teaching figure (synthetic).* Cycle-299 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle297_swarm_ch03_w297_3.png)

*Teaching figure (synthetic).* Cycle-297 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle295_swarm_ch03_w295_3.png)

*Teaching figure (synthetic).* Cycle-295 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle293_swarm_ch03_w293_3.png)

*Teaching figure (synthetic).* Cycle-293 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle291_swarm_ch03_w291_3.png)

*Teaching figure (synthetic).* Cycle-291 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle289_swarm_ch03_w289_3.png)

*Teaching figure (synthetic).* Cycle-289 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle287_swarm_ch03_w287_3.png)

*Teaching figure (synthetic).* Cycle-287 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle285_swarm_ch03_w285_3.png)

*Teaching figure (synthetic).* Cycle-285 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle283_swarm_ch03_w283_3.png)

*Teaching figure (synthetic).* Cycle-283 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle281_swarm_ch03_w281_3.png)

*Teaching figure (synthetic).* Cycle-281 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle279_swarm_ch03_w279_3.png)

*Teaching figure (synthetic).* Cycle-279 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle277_swarm_ch03_w277_3.png)

*Teaching figure (synthetic).* Cycle-277 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle275_swarm_ch03_w275_3.png)

*Teaching figure (synthetic).* Cycle-275 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle273_swarm_ch03_w273_3.png)

*Teaching figure (synthetic).* Cycle-273 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle271_swarm_ch03_w271_3.png)

*Teaching figure (synthetic).* Cycle-271 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle269_swarm_ch03_w269_3.png)

*Teaching figure (synthetic).* Cycle-269 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle267_swarm_ch03_w267_3.png)

*Teaching figure (synthetic).* Cycle-267 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle265_swarm_ch03_w265_3.png)

*Teaching figure (synthetic).* Cycle-265 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle263_swarm_ch03_w263_3.png)

*Teaching figure (synthetic).* Cycle-263 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle261_swarm_ch03_w261_3.png)

*Teaching figure (synthetic).* Cycle-261 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle259_swarm_ch03_w259_3.png)

*Teaching figure (synthetic).* Cycle-259 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle257_swarm_ch03_w257_3.png)

*Teaching figure (synthetic).* Cycle-257 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle255_swarm_ch03_w255_3.png)

*Teaching figure (synthetic).* Cycle-255 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle253_swarm_ch03_w253_3.png)

*Teaching figure (synthetic).* Cycle-253 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle251_swarm_ch03_w251_3.png)

*Teaching figure (synthetic).* Cycle-251 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle249_swarm_ch03_w249_3.png)

*Teaching figure (synthetic).* Cycle-249 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle247_swarm_ch03_w247_3.png)

*Teaching figure (synthetic).* Cycle-247 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle245_swarm_ch03_w245_3.png)

*Teaching figure (synthetic).* Cycle-245 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle243_swarm_ch03_w243_3.png)

*Teaching figure (synthetic).* Cycle-243 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle241_swarm_ch03_w241_3.png)

*Teaching figure (synthetic).* Cycle-241 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle239_swarm_ch03_w239_3.png)

*Teaching figure (synthetic).* Cycle-239 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle237_swarm_ch03_w237_3.png)

*Teaching figure (synthetic).* Cycle-237 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle235_swarm_ch03_w235_3.png)

*Teaching figure (synthetic).* Cycle-235 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle233_swarm_ch03_w233_3.png)

*Teaching figure (synthetic).* Cycle-233 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle231_swarm_ch03_w231_3.png)

*Teaching figure (synthetic).* Cycle-231 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle229_swarm_ch03_w229_3.png)

*Teaching figure (synthetic).* Cycle-229 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle227_swarm_ch03_w227_3.png)

*Teaching figure (synthetic).* Cycle-227 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle225_swarm_ch03_w225_3.png)

*Teaching figure (synthetic).* Cycle-225 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle223_swarm_ch03_w223_3.png)

*Teaching figure (synthetic).* Cycle-223 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle221_swarm_ch03_w221_3.png)

*Teaching figure (synthetic).* Cycle-221 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle219_swarm_ch03_w219_3.png)

*Teaching figure (synthetic).* Cycle-219 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle217_swarm_ch03_w217_3.png)

*Teaching figure (synthetic).* Cycle-217 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle215_swarm_ch03_w215_3.png)

*Teaching figure (synthetic).* Cycle-215 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle213_swarm_ch03_w213_3.png)

*Teaching figure (synthetic).* Cycle-213 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle211_swarm_ch03_w211_3.png)

*Teaching figure (synthetic).* Cycle-211 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle209_swarm_ch03_w209_3.png)

*Teaching figure (synthetic).* Cycle-209 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle207_swarm_ch03_w207_3.png)

*Teaching figure (synthetic).* Cycle-207 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle205_swarm_ch03_w205_3.png)

*Teaching figure (synthetic).* Cycle-205 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle203_swarm_ch03_w203_3.png)

*Teaching figure (synthetic).* Cycle-203 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle201_swarm_ch03_w201_3.png)

*Teaching figure (synthetic).* Cycle-201 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle199_swarm_ch03_w199_3.png)

*Teaching figure (synthetic).* Cycle-199 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle197_swarm_ch03_w197_3.png)

*Teaching figure (synthetic).* Cycle-197 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle195_swarm_ch03_w195_3.png)

*Teaching figure (synthetic).* Cycle-195 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle193_swarm_ch03_w193_3.png)

*Teaching figure (synthetic).* Cycle-193 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle191_swarm_ch03_w191_3.png)

*Teaching figure (synthetic).* Cycle-191 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle189_swarm_ch03_w189_3.png)

*Teaching figure (synthetic).* Cycle-189 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle187_swarm_ch03_w187_3.png)

*Teaching figure (synthetic).* Cycle-187 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle185_swarm_ch03_w185_3.png)

*Teaching figure (synthetic).* Cycle-185 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle183_swarm_ch03_w183_3.png)

*Teaching figure (synthetic).* Cycle-183 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle181_swarm_ch03_w181_3.png)

*Teaching figure (synthetic).* Cycle-181 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle179_swarm_ch03_w179_3.png)

*Teaching figure (synthetic).* Cycle-179 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle177_swarm_ch03_w177_3.png)

*Teaching figure (synthetic).* Cycle-177 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle175_swarm_ch03_w175_3.png)

*Teaching figure (synthetic).* Cycle-175 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle173_swarm_ch03_w173_3.png)

*Teaching figure (synthetic).* Cycle-173 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle171_swarm_ch03_w171_3.png)

*Teaching figure (synthetic).* Cycle-171 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle169_swarm_ch03_w169_3.png)

*Teaching figure (synthetic).* Cycle-169 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle167_swarm_ch03_w167_3.png)

*Teaching figure (synthetic).* Cycle-167 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle165_swarm_ch03_w165_3.png)

*Teaching figure (synthetic).* Cycle-165 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle163_swarm_ch03_w163_3.png)

*Teaching figure (synthetic).* Cycle-163 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle161_swarm_ch03_w161_3.png)

*Teaching figure (synthetic).* Cycle-161 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle159_swarm_ch03_w159_3.png)

*Teaching figure (synthetic).* Cycle-159 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle157_swarm_ch03_w157_3.png)

*Teaching figure (synthetic).* Cycle-157 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle155_swarm_ch03_w155_3.png)

*Teaching figure (synthetic).* Cycle-155 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle153_swarm_ch03_w153_3.png)

*Teaching figure (synthetic).* Cycle-153 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle151_swarm_ch03_w151_3.png)

*Teaching figure (synthetic).* Cycle-151 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle149_swarm_ch03_w149_3.png)

*Teaching figure (synthetic).* Cycle-149 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle147_swarm_ch03_w147_3.png)

*Teaching figure (synthetic).* Cycle-147 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle145_swarm_ch03_w145_3.png)

*Teaching figure (synthetic).* Cycle-145 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle143_swarm_ch03_w143_3.png)

*Teaching figure (synthetic).* Cycle-143 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle141_swarm_ch03_w141_3.png)

*Teaching figure (synthetic).* Cycle-141 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle139_swarm_ch03_w139_3.png)

*Teaching figure (synthetic).* Cycle-139 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle137_swarm_ch03_w137_3.png)

*Teaching figure (synthetic).* Cycle-137 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle135_swarm_ch03_w135_3.png)

*Teaching figure (synthetic).* Cycle-135 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle133_swarm_ch03_w133_3.png)

*Teaching figure (synthetic).* Cycle-133 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle131_swarm_ch03_w131_3.png)

*Teaching figure (synthetic).* Cycle-131 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle129_swarm_ch03_w129_3.png)

*Teaching figure (synthetic).* Cycle-129 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle127_swarm_ch03_w127_3.png)

*Teaching figure (synthetic).* Cycle-127 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle125_swarm_ch03_w125_3.png)

*Teaching figure (synthetic).* Cycle-125 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle123_swarm_ch03_w123_3.png)

*Teaching figure (synthetic).* Cycle-123 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle121_swarm_ch03_w121_3.png)

*Teaching figure (synthetic).* Cycle-121 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle119_swarm_ch03_w119_3.png)

*Teaching figure (synthetic).* Cycle-119 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle117_swarm_ch03_w117_3.png)

*Teaching figure (synthetic).* Cycle-117 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle115_swarm_ch03_w115_3.png)

*Teaching figure (synthetic).* Cycle-115 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle113_swarm_ch03_w113_3.png)

*Teaching figure (synthetic).* Cycle-113 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle111_swarm_ch03_w111_3.png)

*Teaching figure (synthetic).* Cycle-111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle109_swarm_ch03_w109_3.png)

*Teaching figure (synthetic).* Cycle-109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle107_swarm_ch03_w107_3.png)

*Teaching figure (synthetic).* Cycle-107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle105_swarm_ch03_w105_3.png)

*Teaching figure (synthetic).* Cycle-105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle103_swarm_ch03_w103_3.png)

*Teaching figure (synthetic).* Cycle-103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle101_swarm_ch03_w101_3.png)

*Teaching figure (synthetic).* Cycle-101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle99_swarm_ch03_w99_3.png)

*Teaching figure (synthetic).* Cycle-99 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle97_swarm_ch03_w97_3.png)

*Teaching figure (synthetic).* Cycle-97 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle95_swarm_ch03_w95_3.png)

*Teaching figure (synthetic).* Cycle-95 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle93_swarm_ch03_w93_3.png)

*Teaching figure (synthetic).* Cycle-93 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle91_swarm_ch03_w91_3.png)

*Teaching figure (synthetic).* Cycle-91 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle89_swarm_ch03_w89_3.png)

*Teaching figure (synthetic).* Cycle-89 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle87_swarm_ch03_w87_3.png)

*Teaching figure (synthetic).* Cycle-87 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle85_swarm_ch03_w85_3.png)

*Teaching figure (synthetic).* Cycle-85 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle83_swarm_ch03_w83_3.png)

*Teaching figure (synthetic).* Cycle-83 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle81_swarm_ch03_w81_3.png)

*Teaching figure (synthetic).* Cycle-81 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle79_swarm_ch03_w79_3.png)

*Teaching figure (synthetic).* Cycle-79 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle77_swarm_ch03_w77_3.png)

*Teaching figure (synthetic).* Cycle-77 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle75_swarm_ch03_w75_3.png)

*Teaching figure (synthetic).* Cycle-75 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle73_swarm_ch03_w73_3.png)

*Teaching figure (synthetic).* Cycle-73 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle71_swarm_ch03_w71_3.png)

*Teaching figure (synthetic).* Cycle-71 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle69_swarm_ch03_w69_3.png)

*Teaching figure (synthetic).* Cycle-69 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle67_swarm_ch03_w67_3.png)

*Teaching figure (synthetic).* Cycle-67 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle65_swarm_ch03_w65_3.png)

*Teaching figure (synthetic).* Cycle-65 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle63_swarm_ch03_w63_3.png)

*Teaching figure (synthetic).* Cycle-63 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle61_swarm_ch03_w61_3.png)

*Teaching figure (synthetic).* Cycle-61 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle59_swarm_ch03_c59c.png)

*Teaching figure (synthetic).* Cycle-59 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle57_swarm_ch03_c57c.png)

*Teaching figure (synthetic).* Cycle-57 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle55_swarm_ch03_index_risk.png)

*Teaching figure (synthetic).* Cycle-55 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle53_swarm_ch03_pop_match.png)

*Teaching figure (synthetic).* Cycle-53 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle51_swarm_ch03_ice_arr.png)

*Teaching figure (synthetic).* Cycle-51 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle49_swarm_ch03_estimand_map.png)

*Teaching figure (synthetic).* Cycle-49 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle47_swarm_ch03_pico_match.png)

*Teaching figure (synthetic).* Cycle-47 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle45_swarm_ch03_index_time.png)

*Teaching figure (synthetic).* Cycle-45 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle43_swarm_ch03_principal.png)

*Teaching figure (synthetic).* Cycle-43 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 03 (original scientific teaching figure).](../assets/figures/cycle41_swarm_ch03_estimand_gap.png)

*Teaching figure (synthetic).* Cycle-41 densify scientific residual (ch01–14).




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
- Analytic set: Defined by post-hoc analysis choices (Intention-to-Treat, modified ITT, complete cases, per-protocol).
- Transportability gap: The absolute difference in anticipated treatment effect when moving from the analytic set back to your target population.

This distinction is exceptionally critical in observational claims research, where the layers blur dangerously. The claimed 'population' might be 'all hospitalizations with an ICD-10 code for ischemic stroke.' This is a data-available population, not a biologic one. Further exclusions for continuous fee-for-service Medicare enrollment create an analytic set with a fundamentally different socioeconomic and comorbidity profile than a safety-net hospital's target population. If your center serves primarily underinsured, younger stroke patients, an enrollment-continuous Medicare analysis may mislead you entirely, regardless of how sophisticated the confounding adjustment appears.

When designing your own research, reverse the standard error: define the target population and the estimand first, and only then select a data source capable of approximating them. A vast graveyard of failed observational neurology projects begins with a convenient, massive dataset, followed by retrofitting a question that the dataset fundamentally cannot support. The appraisal of others' work and the design of your own share this exact discipline.

## Named Frameworks: PICO, PECO, and the Architecture of Clinical Contrasts

![PECO absolute exposure contrast board: population @ t0, strategies, outcome horizon → ARR (original teaching figure).](../assets/figures/cycle18_swarm_ch03_peco_abs.png)

*Teaching figure (synthetic).* Write PECO before any relative effect claim; absolute summary closes the board.

PICO is the classical scaffolding for interventional clinical questions: Population, Intervention, Comparator, Outcome. PECO adapts this framework for exposure-based questions that dominate observational epidemiology: Population, Exposure, Comparator, Outcome. While both are technically incomplete as full causal estimands, they serve as exceptional first-pass compression tools. They force the user to articulate the absolute minimum components required to assess a clinical contrast. If you cannot write a complete PICO sentence, you do not have a question.

- Population: Must be anatomically and temporally specific. 'Adults with anterior-circulation LVO presenting 6-24 hours after last known well with target mismatch.'
- Intervention/Exposure: Requires operational granularity. 'EVT plus standard medical care' or 'High-dose atorvastatin loaded prior to discharge.'
- Comparator: Must reflect a realistic alternative state. 'Medical care without EVT' or 'No statin initiation prior to discharge.'
- Outcome: Patient-important, temporally bound. '90-day mRS ordinal shift' or 'Recurrent ischemic stroke within 30 days.'

Write PICO and PECO frameworks as complete sentences, not as telegraphic fragments. Writing 'Population: stroke' is intellectually lazy and clinically useless. Writing 'Population: adults with non-cardioembolic minor ischemic stroke (NIHSS <= 5) or high-risk TIA randomized within 24 hours of onset, without an existing indication for systemic anticoagulation' provides a falsifiable perimeter. The sentence structure forces you to recognize missing pieces. This exact sentence becomes the first line of your formal appraisal checklist.

The PICO structure is not restricted to randomized drug trials. You must write a PICO for a health systems intervention (e.g., bundled door-to-puncture process improvements versus standard operations) or for a diagnostic strategy (e.g., CTA-first versus MRI-first screening for late-window EVT candidates), provided the paper evaluates these strategies against patient outcomes. For pure prediction questions, a modified scaffold applies: Population, Index predictors, Comparator model or default clinical heuristic, and Outcome. This still forces clarity regarding the exact moment of prediction and the time horizon.

Common PICO failures in neurology involve unspecified comparators and composite outcomes. Asking 'Is EVT beneficial?' is meaningless without specifying 'beneficial compared to what specific era of medical therapy?' Composite outcomes, such as a combined endpoint of 'stroke, myocardial infarction, or vascular death,' frequently hide the specific component that patients actually care about. If a trial claims success based on a composite, but the entire effect is driven by a reduction in asymptomatic troponin leaks while stroke rates remain static, the PICO architecture reveals the deception. When you identify these structural failures in an abstract, your critical appraisal is largely complete.

## The Estimand Framework: ICH E9(R1) in Neurologic Practice

![Estimand board: population vs enrolled vs analytic set can rewrite absolute ARR for the same intervention (original teaching figure).](../assets/figures/cycle15_swarm_ch03_estimand_abs_board.png)

*Teaching figure (synthetic).* Write population, strategies, endpoint horizon, and absolute summary before minting any NNT.

![Intercurrent-event strategy (treatment-policy vs hypothetical vs composite) rewrites the absolute ARR (original teaching figure).](../assets/figures/cycle12_swarm_ch03_intercurrent_arr.png)

*Teaching figure (synthetic).* The estimand sentence must name the intercurrent strategy; abstract–methods mismatch is spin on the absolute scale.


![PICO mapped to estimand components (ICH E9(R1) spirit; original teaching figure).](../assets/figures/fig24_pico_estimand.png)

*PICO anatomy flows into the five estimand components (population, treatment conditions, variable, intercurrent-event strategy, population-level summary). Original teaching figure.*


An estimand is the precise mathematical and clinical target of estimation. Introduced formally to the clinical trial community via the ICH E9(R1) addendum, the estimand framework demands that researchers explicitly define what they are trying to measure before they measure it. Modern trial methodology relies heavily on estimands because two completely different statistical analyses can yield different numbers while both being 'correct' for their respective estimand targets. Without estimand language, clinical debates devolve into vague arguments about whether the authors used the 'right' p-value or the 'correct' covariate adjustment.

The ICH E9(R1) framework requires specifying five attributes to construct a complete estimand: (1) the treatment conditions or exposures being contrasted; (2) the target population; (3) the outcome variable and its time horizon; (4) the population-level summary measure; and crucially, (5) the strategy for handling intercurrent events. Intercurrent events are post-randomization events that preclude observation of the outcome or fundamentally alter its interpretation—such as treatment discontinuation, the initiation of rescue therapy, or death.

- Treatment Policy Strategy (Intention-to-Treat): The effect of assignment to the intervention, regardless of whether the patient actually received it or took rescue therapy. This matches the clinical decision to offer a drug.
- Hypothetical Strategy: The effect of the intervention under the imagined scenario that all patients adhered perfectly and no rescue therapies were available. Often requires heavy, untestable causal assumptions.
- Composite Strategy: The intercurrent event is absorbed into the outcome. For example, if a patient undergoes decompressive hemicraniectomy after an MCA stroke, this is counted as a failure equivalent to death or severe disability.
- While-on-Treatment Strategy: Evaluates the outcome only during the period the patient is actively exposed. Relevant for transient symptomatic therapies, but dangerous for disease-modifying treatments.
- Principal Stratum Strategy: The effect in the subset of patients who would have exhibited a specific intercurrent event behavior under both treatment conditions (e.g., those who would survive regardless of assignment).

A pragmatic, treatment-policy estimand sentence for acute stroke might read: 'In adults with ICA or M1 occlusion, NIHSS >= 6, ASPECTS >= 6, and last known well 6-16 hours earlier meeting specific perfusion mismatch criteria, the estimand is the absolute risk reduction of achieving a 90-day mRS of 0-2 resulting from assignment to immediate EVT plus standard medical care versus standard medical care alone, regardless of subsequent procedural complications or crossover, among the population randomized.' This sentence is dense because clinical decisions are dense. Short slogans hide methodological disagreements that inevitably explode during journal club.

Estimand mismatch is a primary diagnostic finding in critical appraisal. When an abstract strongly implies a pragmatic, treatment-policy benefit (suggesting you should offer this drug to everyone), but the only statistically significant result in the paper is a per-protocol or hypothetical estimand that excludes non-adherent patients or those who suffered early complications, the authors are selling a product they did not test. You must evaluate the paper based on the estimand they actually estimated, not the one they claim in the discussion.

![Composite headline ARR can be driven by urgent revascularization while disabling stroke barely moves—disaggregate absolute components on the estimand board (original teaching figure).](../assets/figures/cycle8_swarm_ch03_composite_component.png)

*Teaching figure (synthetic).* Specify population, strategies, outcome hierarchy, and summary measure before debating p-values. Prefer component ARRs with a named horizon; composite spin is an estimand failure, not a rounding issue.

## Index Time (t0) and the Chronology of Causation

Index time, or time zero (t0), is the exact moment when the clock starts on a causal analysis. For a causal contrast to be valid, three distinct chronologies must perfectly align at t0: the moment the patient meets all eligibility criteria, the moment the treatment or exposure is assigned, and the moment follow-up for the outcome begins. If these three clocks are desynchronized by even a few hours, structural bias instantly infects the analysis. In randomized controlled trials, t0 is enforced rigorously by the act of randomization. This forced alignment is precisely why RCTs feel 'clean' and resilient to certain biases.

In observational stroke research, index time is rarely designed; it is passively implied by the dataset. Researchers might use admission time, exact stroke onset, discharge time, the first pharmacy fill, or the date of a clinic visit as their pseudo-t0. Every single choice radically alters the causal meaning of the estimate. If an analysis compares outcomes between patients who received a medication during their hospital stay versus those who did not, but starts the follow-up clock at admission, it has decoupled treatment assignment from eligibility.

- Diagnostic Question 1: When, exactly, could a patient first theoretically be eligible for either of the treatment strategies being compared?
- Diagnostic Question 2: When does the exposure status become permanently knowable in real time for clinical decision-making?
- Diagnostic Question 3: Are clinical events that occur before exposure classification inappropriately counted, excluded, or misattributed to the exposure?
- Diagnostic Question 4: Does the study perfectly align eligibility, exposure assignment, and outcome follow-up clocks at a single t0?

Acute stroke care adds immense prehospital and transfer complexity. Time from last known well, door time, non-contrast CT time, and puncture time are all critical operational clocks, but the causal index time for a specific treatment contrast is the exact moment the clinician faces the choice between strategies. Landmark EVT trials use randomization as t0, which usually occurs immediately after imaging. Retrospective observational comparisons of 'EVT versus no EVT' that start their follow-up clock at hospital admission—without carefully emulating the exact moment of imaging eligibility—create a chaotic mixture of selection bias, immortal time bias, and survival bias.

The concept of 'target-trial emulation' in observational epidemiology is fundamentally an exercise in index-time discipline. It forces the observational researcher to construct a protocol skeleton that artificially enforces the alignment of eligibility, assignment, and follow-up, just as an RCT would. When you review a paper, checking the alignment of t0 is never optional. Finding a failure here protects you from over-interpreting a complex, machine-learning-adjusted hazard ratio that is temporally incoherent.

![Index-time alignment versus immortal-time misclassification: eligibility, assignment, and outcome clocks must share one t0 (original teaching figure).](../assets/figures/cycle5_swarm_ch03_index_time.png)

*Teaching figure (synthetic).* When discharge starts the clock but rehab attendance weeks later defines exposure, early deaths are forced into the unexposed arm and survival becomes a prerequisite for “treatment.” Landmarking, time-varying exposure, or sequential target-trial emulation restores temporal honesty—never invent NNTs from mis-timed associations.

## Quantitative Reasoning: Formalizing the Causal Contrast

To move beyond linguistic arguments, we must define the causal contrast quantitatively using potential outcomes notation. Let $Y$ represent the outcome of interest, such as achieving functional independence (mRS 0-2) at 90 days. Let $A$ represent the treatment assignment, where $A=1$ for the active intervention (e.g., tenecteplase) and $A=0$ for the comparator (e.g., alteplase). For any individual patient $i$, we theorize two potential outcomes: $Y_i^{a=1}$, the outcome if they received tenecteplase, and $Y_i^{a=0}$, the outcome if they received alteplase.

The individual causal effect is simply $Y_i^{a=1} - Y_i^{a=0}$. However, because a patient cannot simultaneously receive both treatments, we can never observe both potential outcomes for the same individual at the same time. This is the fundamental problem of causal inference. Instead, we must estimate the Average Treatment Effect (ATE) across the target population: $E[Y^{a=1}] - E[Y^{a=0}]$. This contrast relies on the assumption of exchangeability—that the treated and untreated groups are entirely comparable, which randomization achieves by design and observational methods attempt to achieve through adjustment.

The difference $E[Y^{a=1}] - E[Y^{a=0}]$ is the Absolute Risk Reduction (ARR). The ARR is the supreme metric of clinical utility. It tells you exactly how much the probability of a favorable outcome changes in absolute terms when shifting from the control state to the active state. The Number Needed to Treat (NNT) is strictly the inverse of the ARR ($1 / \text{ARR}$), and the Number Needed to Harm (NNH) is the inverse of the Absolute Risk Increase (ARI) for adverse events. If endovascular therapy increases the probability of mRS 0-2 from 0.25 under medical management to 0.40, the ARR is 0.15, meaning the NNT is 6.7.

- Prediction Equation: $E[Y | A=1] - E[Y | A=0]$. This simply compares the observed outcomes of those who happened to get treated versus those who did not. It is hopelessly contaminated by confounding bias.
- Causal Equation: $E[Y^{a=1}] - E[Y^{a=0}]$. This compares the counterfactual states of the entire population. This is what you actually care about.
- Absolute effects (ARR) preserve baseline risk. Relative Risk (RR), Odds Ratios (OR), and Hazard Ratios (HR) mathematically erase baseline risk.
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

Step 1: Separate the overlapping decisions. Decision A: For early high-risk TIA or minor ischemic stroke without a cardioembolic source, should we mandate short-course DAPT versus aspirin alone to reduce recurrent ischemic stroke at 90 days, accepting the obligatory increase in major bleeding? Decision B: Does earlier post-discharge neurology clinic follow-up reduce 30-day readmissions? Decision C: What does the claims association actually mean? These are distinct questions requiring entirely different study designs.

Step 2: Formalize the PICO for Decision A. Population: Adults with high-risk TIA or minor non-cardioembolic ischemic stroke (NIHSS <= 5) presenting early enough to initiate therapy within 24 hours. Intervention: Aspirin plus clopidogrel (with a 300-600mg load) for exactly 21 days. Comparator: Aspirin alone. Outcomes: Recurrent ischemic stroke at 90 days (primary efficacy); major hemorrhage (co-primary safety). Notice that readmission is entirely absent from this causal formulation—it is a health systems metric, not the primary neurologic endpoint.

Step 3: Draft the Estimand for Decision A. 'Among patients meeting the population attributes at the time of clinical diagnosis in the ED (t0), the treatment-policy estimand is the absolute risk difference for recurrent ischemic stroke by day 90 comparing assignment to short-course DAPT versus aspirin alone, regardless of subsequent medication nonadherence, estimated alongside the absolute risk increase for major hemorrhage.' This precise estimand points you immediately to randomized evidence like the POINT and CHANCE trials, not to observational claims data.

Step 4: Critique the Claims Paper. You evaluate the paper cited in the meeting. It defines exposure as any pharmacy fill for DAPT within 14 days of discharge, but begins readmission follow-up at discharge. Immortal time bias is flagrant: patients who are readmitted on day 3 for an infection never have the chance to fill DAPT on day 10, dumping early readmissions into the unexposed cohort. Furthermore, the outcome is all-cause readmission, a target heavily confounded by frailty and social determinants of health, not a specific neurologic recurrence.

Step 5: Operational Action. You re-center the committee. You calculate the ARR from the randomized trials for Decision A (ARR for stroke reduction ~1.5%, NNT ~67; ARI for major bleed ~0.5%, NNH ~200). You spin out Decision B (readmission reductions) into a separate quality improvement protocol focused on social work and early clinic access. You formally demote the claims paper to teaching material for immortal time bias. By forcing PICO and estimand discipline, the clinical pathway remains anchored to absolute causal effects, not confounded associations.

## Clinical and Epidemiologic Notes

Clinical decisions always occur at a strict time zero, even when we fail to articulate it. The stroke neurologist decides about intravenous thrombolysis at a precise door-and-imaging moment; about EVT at an imaging-and-consent moment; about initiating DAPT at a diagnosis-and-risk-stratification moment. Papers that fail to align their analysis with these exact decision moments are estimating something fundamentally detached from the choice you face at the bedside. Demanding index-time clarity is not pedantry; it is a clinical safety practice.

Epidemiologically, eligibility criteria serve to enrich trials for efficacy. By restricting the DAWN trial to patients with small core infarcts and massive clinical deficits, the trialists successfully enriched the cohort for maximal EVT benefit. This improves statistical power and average effect sizes, but brutally narrows transportability. The clinical corollary is that unenriched populations (e.g., large core strokes, low NIHSS presentations) will exhibit much smaller absolute benefits and different harm profiles. When health systems blindly generalize enriched trial results to all 'code stroke' patients, they bypass the exact selection mechanics that made the trial successful.

Estimand thinking profoundly clarifies shared decision-making with patients. When a family asks, 'If we choose to proceed with the thrombectomy, what are his chances of walking again?' they are asking a pure treatment-policy question. This requires an intention-to-treat estimate that incorporates all downstream failures, including the risk of procedural hemorrhage, access site complications, and futile recanalization. A 'while-on-treatment' estimand that censors patients who suffer complications might answer an interesting mechanistic question about reperfusion physiology, but it completely fails the family meeting. You must match the estimand to the conversation.

For neurology researchers utilizing electronic health records and massive observational datasets, the discipline of writing a target trial protocol—explicitly defining eligibility, index time, treatment strategies, outcomes, and causal contrasts before any SQL code is written—is the single best vaccine against immortal time bias and ill-posed PECO questions. It does not guarantee unbiased estimates, but it prevents the estimation of a chaotic blur. Reviewers can interrogate a clear estimand; they cannot fix a shapeless, machine-learning-derived association post hoc.

## Cross-Links to Other Chapters

The structural principles detailed in this chapter form the absolute prerequisite for Chapter 4 (Bias Taxonomy and Causal Inference). You cannot accurately diagnose a bias (such as selection bias, information bias, or unmeasured confounding) until you have defined the exact causal target the study is attempting to estimate. Without Chapter 3, discussions of bias are merely academic theater; with it, bias identification becomes a precise diagnostic procedure.

The PICO sentences and target-trial frameworks developed here directly populate the appraisal tools introduced in Chapter 2 (The Senior Appraisal Checklist). Furthermore, the concepts of index time and immortal time bias serve as the foundation for the advanced observational epidemiology chapters, particularly Chapter 8 (Propensity Scores, Emulated Trials, and Instrumental Variables).


![fig40_natural_frequencies.png original teaching graphic](../assets/figures/fig40_natural_frequencies.png)

*Original teaching graphic (fig40_natural_frequencies.png).*

## Chapter summary

Vague clinical curiosities must be ruthlessly repaired into precise, answerable causal questions before critical appraisal or study design can succeed. PICO and PECO frameworks provide the initial structural anatomy for interventions and exposures, demanding sentence-level specificity. The target population, study sample, and analytic set represent distinct demographic layers that frequently diverge, requiring an assessment of transportability gaps. Interventions and comparators demand operational definitions that reflect realistic clinical delivery, while outcomes must be patient-important and temporally bound. The ICH E9(R1) estimand framework formalizes the causal target by specifying population attributes, treatment contrasts, outcomes, summary measures, and explicit strategies for handling intercurrent events. Mismatches between the claimed estimand and the analyzed estimand are high-yield diagnostic findings. Index time (t0) must perfectly align eligibility, exposure assignment, and follow-up; any temporal misalignment invites devastating structural errors, most notably immortal time bias. Absolute effects (ARR, NNT) are vastly superior to relative measures, preserving baseline risk context for bedside decision-making. Eligibility criteria are not mere safety guards; they are fundamental scientific parameters that dictate the transportability of the causal effect. By mastering question craft, the clinical epidemiologist neutralizes linguistic chaos and makes true bias diagnosis possible.

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


![fig83_prevalence_reservoir.png original teaching graphic](../assets/figures/fig83_prevalence_reservoir.png)

*Original teaching graphic (fig83_prevalence_reservoir.png).*
