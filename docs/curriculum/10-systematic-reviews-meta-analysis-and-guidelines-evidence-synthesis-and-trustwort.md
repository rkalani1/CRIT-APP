# Chapter 10. Systematic Reviews, Meta-Analysis, and Guidelines: Evidence Synthesis and Trustworthiness

## Opening

![Funnel plot concept (original).](../assets/figures/fig56_funnel.png)

*Funnel plot concept (original).*

![Forest plot teaching sketch (original).](../assets/figures/fig23_forest_meta.png)

*Forest plot teaching sketch (original).*

![Forest plot intuition for meta-analysis (original synthetic).](../assets/figures/swarm_ch10_forest.png)

*Forest plot intuition for meta-analysis (original synthetic).*

A living systematic review drops at 06:00 with a favorable pooled OR. Check inclusion criteria, double-counting, and absolute baselines before updating the pathway binder.


## Learning objectives

- Formulate and recognize a rigorously structured systematic review question using PICO/PECO frameworks, distinguishing exploratory summaries from confirmatory pooling.
- Identify and quantify search, selection, and publication biases that distort the foundational evidence base before statistical synthesis occurs.
- Critically apply named frameworks (RoB 2, ROBINS-I) to assess risk of bias, separating the mechanistic spirit of bias from administrative checkbox compliance.
- Deconstruct forest plots to evaluate direction, magnitude, precision, and between-study patterns, consciously resisting the urge to jump straight to the pooled diamond.
- Derive and contrast the mathematical and conceptual differences between fixed-effect and random-effects models, explicitly defining symbols such as tau-squared, I-squared, and inverse-variance weights.
- Execute a manual calculation of a fixed-effect meta-analysis for binary stroke outcomes, converting pooled relative effects into absolute risk reductions (ARR) and number needed to treat (NNT).
- Diagnose clinical and statistical heterogeneity, explaining why statistical heterogeneity parameters do not license the pooling of clinically incompatible studies.
- Appraise clinical practice guidelines using the GRADE framework, distinguishing certainty of evidence from strength of recommendations.
- Recognize common failure modes in evidence synthesis, including the ecological fallacy in meta-regression and the danger of up-weighting small, biased trials in random-effects models.
- Translate meta-analytic findings and guideline recommendations into patient-centered clinical discussions without conflating prediction with causal mechanisms.

![Meta residual: pooled RR incomplete without local absolute ARR/NNT transport (original scientific teaching figure).](../assets/figures/cycle25_swarm_ch10_forest_local_arr.png)

*Teaching figure (synthetic).* Cycle-25 densify scientific residual.

![Meta residual: high I-squared widens absolute prediction intervals (original scientific teaching figure).](../assets/figures/cycle27_swarm_ch10_i2_pi_width.png)

*Teaching figure (synthetic).* Cycle-27 densify scientific residual.

![Funnel of absolute ARR flags small-study bias (original scientific teaching figure).](../assets/figures/cycle29_swarm_ch10_funnel_arr.png)

*Teaching figure (synthetic).* Cycle-29 densify scientific residual.

![Early cumulative absolute ARR often drifts before stability (original scientific teaching figure).](../assets/figures/cycle31_swarm_ch10_cum_meta.png)

*Teaching figure (synthetic).* Cycle-31 densify scientific residual.

![Prediction interval for next absolute effect (original scientific teaching figure).](../assets/figures/cycle33_swarm_ch10_pi_forest.png)

*Teaching figure (synthetic).* Cycle-33 densify scientific residual.

![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle35_swarm_ch10_cumarr.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## Conceptual Core: The Architecture of Evidence Synthesis

![Convert pooled RR through local CER to absolute NNT (original teaching figure).](../assets/figures/cycle22_swarm_ch10_local_nnt.png)

*Teaching figure (synthetic).* Guidelines need local absolute transport.

![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1549_swarm_ch10_w1549_10.png)

*Teaching figure (synthetic).* Cycle-1549 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1547_swarm_ch10_w1547_10.png)

*Teaching figure (synthetic).* Cycle-1547 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1545_swarm_ch10_w1545_10.png)

*Teaching figure (synthetic).* Cycle-1545 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1543_swarm_ch10_w1543_10.png)

*Teaching figure (synthetic).* Cycle-1543 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1541_swarm_ch10_w1541_10.png)

*Teaching figure (synthetic).* Cycle-1541 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1539_swarm_ch10_w1539_10.png)

*Teaching figure (synthetic).* Cycle-1539 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1537_swarm_ch10_w1537_10.png)

*Teaching figure (synthetic).* Cycle-1537 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1535_swarm_ch10_w1535_10.png)

*Teaching figure (synthetic).* Cycle-1535 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1533_swarm_ch10_w1533_10.png)

*Teaching figure (synthetic).* Cycle-1533 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1531_swarm_ch10_w1531_10.png)

*Teaching figure (synthetic).* Cycle-1531 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1529_swarm_ch10_w1529_10.png)

*Teaching figure (synthetic).* Cycle-1529 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1527_swarm_ch10_w1527_10.png)

*Teaching figure (synthetic).* Cycle-1527 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1525_swarm_ch10_w1525_10.png)

*Teaching figure (synthetic).* Cycle-1525 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1523_swarm_ch10_w1523_10.png)

*Teaching figure (synthetic).* Cycle-1523 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1521_swarm_ch10_w1521_10.png)

*Teaching figure (synthetic).* Cycle-1521 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1519_swarm_ch10_w1519_10.png)

*Teaching figure (synthetic).* Cycle-1519 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1517_swarm_ch10_w1517_10.png)

*Teaching figure (synthetic).* Cycle-1517 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1515_swarm_ch10_w1515_10.png)

*Teaching figure (synthetic).* Cycle-1515 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1513_swarm_ch10_w1513_10.png)

*Teaching figure (synthetic).* Cycle-1513 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1511_swarm_ch10_w1511_10.png)

*Teaching figure (synthetic).* Cycle-1511 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1509_swarm_ch10_w1509_10.png)

*Teaching figure (synthetic).* Cycle-1509 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1507_swarm_ch10_w1507_10.png)

*Teaching figure (synthetic).* Cycle-1507 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1505_swarm_ch10_w1505_10.png)

*Teaching figure (synthetic).* Cycle-1505 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1503_swarm_ch10_w1503_10.png)

*Teaching figure (synthetic).* Cycle-1503 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1501_swarm_ch10_w1501_10.png)

*Teaching figure (synthetic).* Cycle-1501 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1499_swarm_ch10_w1499_10.png)

*Teaching figure (synthetic).* Cycle-1499 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1497_swarm_ch10_w1497_10.png)

*Teaching figure (synthetic).* Cycle-1497 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1495_swarm_ch10_w1495_10.png)

*Teaching figure (synthetic).* Cycle-1495 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1493_swarm_ch10_w1493_10.png)

*Teaching figure (synthetic).* Cycle-1493 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1491_swarm_ch10_w1491_10.png)

*Teaching figure (synthetic).* Cycle-1491 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1489_swarm_ch10_w1489_10.png)

*Teaching figure (synthetic).* Cycle-1489 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1487_swarm_ch10_w1487_10.png)

*Teaching figure (synthetic).* Cycle-1487 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1485_swarm_ch10_w1485_10.png)

*Teaching figure (synthetic).* Cycle-1485 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1483_swarm_ch10_w1483_10.png)

*Teaching figure (synthetic).* Cycle-1483 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1481_swarm_ch10_w1481_10.png)

*Teaching figure (synthetic).* Cycle-1481 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1479_swarm_ch10_w1479_10.png)

*Teaching figure (synthetic).* Cycle-1479 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1477_swarm_ch10_w1477_10.png)

*Teaching figure (synthetic).* Cycle-1477 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1475_swarm_ch10_w1475_10.png)

*Teaching figure (synthetic).* Cycle-1475 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1473_swarm_ch10_w1473_10.png)

*Teaching figure (synthetic).* Cycle-1473 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10: ARR/NNT absolute framing; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle1471_swarm_ch10_w1471_10.png)

*Teaching figure (synthetic).* Cycle-1471 densify scientific residual (ch01–14): absolute risk, ARR, NNT; pred≠cause. Prefer ARR and NNT over relative-only claims; prediction ≠ causation.


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1466_swarm_ch10_w1466_10.png)

*Teaching figure (synthetic).* Cycle-1466 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1464_swarm_ch10_w1464_10.png)

*Teaching figure (synthetic).* Cycle-1464 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1469_swarm_ch10_w1469_10.png)

*Teaching figure (synthetic).* Cycle-1469 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1467_swarm_ch10_w1467_10.png)

*Teaching figure (synthetic).* Cycle-1467 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1461_swarm_ch10_w1461_10.png)

*Teaching figure (synthetic).* Cycle-1461 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1459_swarm_ch10_w1459_10.png)

*Teaching figure (synthetic).* Cycle-1459 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1457_swarm_ch10_w1457_10.png)

*Teaching figure (synthetic).* Cycle-1457 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1455_swarm_ch10_w1455_10.png)

*Teaching figure (synthetic).* Cycle-1455 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1453_swarm_ch10_w1453_10.png)

*Teaching figure (synthetic).* Cycle-1453 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1451_swarm_ch10_w1451_10.png)

*Teaching figure (synthetic).* Cycle-1451 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1449_swarm_ch10_w1449_10.png)

*Teaching figure (synthetic).* Cycle-1449 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1447_swarm_ch10_w1447_10.png)

*Teaching figure (synthetic).* Cycle-1447 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1445_swarm_ch10_w1445_10.png)

*Teaching figure (synthetic).* Cycle-1445 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1443_swarm_ch10_w1443_10.png)

*Teaching figure (synthetic).* Cycle-1443 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1441_swarm_ch10_w1441_10.png)

*Teaching figure (synthetic).* Cycle-1441 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1439_swarm_ch10_w1439_10.png)

*Teaching figure (synthetic).* Cycle-1439 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1437_swarm_ch10_w1437_10.png)

*Teaching figure (synthetic).* Cycle-1437 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1435_swarm_ch10_w1435_10.png)

*Teaching figure (synthetic).* Cycle-1435 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1433_swarm_ch10_w1433_10.png)

*Teaching figure (synthetic).* Cycle-1433 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1431_swarm_ch10_w1431_10.png)

*Teaching figure (synthetic).* Cycle-1431 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1429_swarm_ch10_w1429_10.png)

*Teaching figure (synthetic).* Cycle-1429 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1427_swarm_ch10_w1427_10.png)

*Teaching figure (synthetic).* Cycle-1427 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1425_swarm_ch10_w1425_10.png)

*Teaching figure (synthetic).* Cycle-1425 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1423_swarm_ch10_w1423_10.png)

*Teaching figure (synthetic).* Cycle-1423 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1421_swarm_ch10_w1421_10.png)

*Teaching figure (synthetic).* Cycle-1421 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1419_swarm_ch10_w1419_10.png)

*Teaching figure (synthetic).* Cycle-1419 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1417_swarm_ch10_w1417_10.png)

*Teaching figure (synthetic).* Cycle-1417 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1415_swarm_ch10_w1415_10.png)

*Teaching figure (synthetic).* Cycle-1415 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1413_swarm_ch10_w1413_10.png)

*Teaching figure (synthetic).* Cycle-1413 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1411_swarm_ch10_w1411_10.png)

*Teaching figure (synthetic).* Cycle-1411 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1409_swarm_ch10_w1409_10.png)

*Teaching figure (synthetic).* Cycle-1409 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1407_swarm_ch10_w1407_10.png)

*Teaching figure (synthetic).* Cycle-1407 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1405_swarm_ch10_w1405_10.png)

*Teaching figure (synthetic).* Cycle-1405 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1403_swarm_ch10_w1403_10.png)

*Teaching figure (synthetic).* Cycle-1403 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1401_swarm_ch10_w1401_10.png)

*Teaching figure (synthetic).* Cycle-1401 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1399_swarm_ch10_w1399_10.png)

*Teaching figure (synthetic).* Cycle-1399 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1397_swarm_ch10_w1397_10.png)

*Teaching figure (synthetic).* Cycle-1397 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1395_swarm_ch10_w1395_10.png)

*Teaching figure (synthetic).* Cycle-1395 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1393_swarm_ch10_w1393_10.png)

*Teaching figure (synthetic).* Cycle-1393 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1391_swarm_ch10_w1391_10.png)

*Teaching figure (synthetic).* Cycle-1391 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1389_swarm_ch10_w1389_10.png)

*Teaching figure (synthetic).* Cycle-1389 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1387_swarm_ch10_w1387_10.png)

*Teaching figure (synthetic).* Cycle-1387 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1385_swarm_ch10_w1385_10.png)

*Teaching figure (synthetic).* Cycle-1385 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1383_swarm_ch10_w1383_10.png)

*Teaching figure (synthetic).* Cycle-1383 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1381_swarm_ch10_w1381_10.png)

*Teaching figure (synthetic).* Cycle-1381 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1379_swarm_ch10_w1379_10.png)

*Teaching figure (synthetic).* Cycle-1379 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1377_swarm_ch10_w1377_10.png)

*Teaching figure (synthetic).* Cycle-1377 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1375_swarm_ch10_w1375_10.png)

*Teaching figure (synthetic).* Cycle-1375 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1373_swarm_ch10_w1373_10.png)

*Teaching figure (synthetic).* Cycle-1373 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1371_swarm_ch10_w1371_10.png)

*Teaching figure (synthetic).* Cycle-1371 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1369_swarm_ch10_w1369_10.png)

*Teaching figure (synthetic).* Cycle-1369 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1367_swarm_ch10_w1367_10.png)

*Teaching figure (synthetic).* Cycle-1367 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1365_swarm_ch10_w1365_10.png)

*Teaching figure (synthetic).* Cycle-1365 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1363_swarm_ch10_w1363_10.png)

*Teaching figure (synthetic).* Cycle-1363 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1361_swarm_ch10_w1361_10.png)

*Teaching figure (synthetic).* Cycle-1361 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1359_swarm_ch10_w1359_10.png)

*Teaching figure (synthetic).* Cycle-1359 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1357_swarm_ch10_w1357_10.png)

*Teaching figure (synthetic).* Cycle-1357 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1355_swarm_ch10_w1355_10.png)

*Teaching figure (synthetic).* Cycle-1355 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1353_swarm_ch10_w1353_10.png)

*Teaching figure (synthetic).* Cycle-1353 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1351_swarm_ch10_w1351_10.png)

*Teaching figure (synthetic).* Cycle-1351 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1349_swarm_ch10_w1349_10.png)

*Teaching figure (synthetic).* Cycle-1349 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1347_swarm_ch10_w1347_10.png)

*Teaching figure (synthetic).* Cycle-1347 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1345_swarm_ch10_w1345_10.png)

*Teaching figure (synthetic).* Cycle-1345 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1343_swarm_ch10_w1343_10.png)

*Teaching figure (synthetic).* Cycle-1343 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1341_swarm_ch10_w1341_10.png)

*Teaching figure (synthetic).* Cycle-1341 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1339_swarm_ch10_w1339_10.png)

*Teaching figure (synthetic).* Cycle-1339 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1337_swarm_ch10_w1337_10.png)

*Teaching figure (synthetic).* Cycle-1337 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1335_swarm_ch10_w1335_10.png)

*Teaching figure (synthetic).* Cycle-1335 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1333_swarm_ch10_w1333_10.png)

*Teaching figure (synthetic).* Cycle-1333 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1331_swarm_ch10_w1331_10.png)

*Teaching figure (synthetic).* Cycle-1331 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1329_swarm_ch10_w1329_10.png)

*Teaching figure (synthetic).* Cycle-1329 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1327_swarm_ch10_w1327_10.png)

*Teaching figure (synthetic).* Cycle-1327 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1325_swarm_ch10_w1325_10.png)

*Teaching figure (synthetic).* Cycle-1325 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1323_swarm_ch10_w1323_10.png)

*Teaching figure (synthetic).* Cycle-1323 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1321_swarm_ch10_w1321_10.png)

*Teaching figure (synthetic).* Cycle-1321 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1319_swarm_ch10_w1319_10.png)

*Teaching figure (synthetic).* Cycle-1319 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1317_swarm_ch10_w1317_10.png)

*Teaching figure (synthetic).* Cycle-1317 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1315_swarm_ch10_w1315_10.png)

*Teaching figure (synthetic).* Cycle-1315 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1313_swarm_ch10_w1313_10.png)

*Teaching figure (synthetic).* Cycle-1313 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1311_swarm_ch10_w1311_10.png)

*Teaching figure (synthetic).* Cycle-1311 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1309_swarm_ch10_w1309_10.png)

*Teaching figure (synthetic).* Cycle-1309 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1307_swarm_ch10_w1307_10.png)

*Teaching figure (synthetic).* Cycle-1307 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1305_swarm_ch10_w1305_10.png)

*Teaching figure (synthetic).* Cycle-1305 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1303_swarm_ch10_w1303_10.png)

*Teaching figure (synthetic).* Cycle-1303 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1301_swarm_ch10_w1301_10.png)

*Teaching figure (synthetic).* Cycle-1301 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1299_swarm_ch10_w1299_10.png)

*Teaching figure (synthetic).* Cycle-1299 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1297_swarm_ch10_w1297_10.png)

*Teaching figure (synthetic).* Cycle-1297 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1295_swarm_ch10_w1295_10.png)

*Teaching figure (synthetic).* Cycle-1295 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1293_swarm_ch10_w1293_10.png)

*Teaching figure (synthetic).* Cycle-1293 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1291_swarm_ch10_w1291_10.png)

*Teaching figure (synthetic).* Cycle-1291 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1289_swarm_ch10_w1289_10.png)

*Teaching figure (synthetic).* Cycle-1289 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1287_swarm_ch10_w1287_10.png)

*Teaching figure (synthetic).* Cycle-1287 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1285_swarm_ch10_w1285_10.png)

*Teaching figure (synthetic).* Cycle-1285 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1283_swarm_ch10_w1283_10.png)

*Teaching figure (synthetic).* Cycle-1283 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1281_swarm_ch10_w1281_10.png)

*Teaching figure (synthetic).* Cycle-1281 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1279_swarm_ch10_w1279_10.png)

*Teaching figure (synthetic).* Cycle-1279 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1277_swarm_ch10_w1277_10.png)

*Teaching figure (synthetic).* Cycle-1277 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1275_swarm_ch10_w1275_10.png)

*Teaching figure (synthetic).* Cycle-1275 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1273_swarm_ch10_w1273_10.png)

*Teaching figure (synthetic).* Cycle-1273 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1271_swarm_ch10_w1271_10.png)

*Teaching figure (synthetic).* Cycle-1271 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1269_swarm_ch10_w1269_10.png)

*Teaching figure (synthetic).* Cycle-1269 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1267_swarm_ch10_w1267_10.png)

*Teaching figure (synthetic).* Cycle-1267 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1265_swarm_ch10_w1265_10.png)

*Teaching figure (synthetic).* Cycle-1265 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1263_swarm_ch10_w1263_10.png)

*Teaching figure (synthetic).* Cycle-1263 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1261_swarm_ch10_w1261_10.png)

*Teaching figure (synthetic).* Cycle-1261 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1259_swarm_ch10_w1259_10.png)

*Teaching figure (synthetic).* Cycle-1259 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1257_swarm_ch10_w1257_10.png)

*Teaching figure (synthetic).* Cycle-1257 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1255_swarm_ch10_w1255_10.png)

*Teaching figure (synthetic).* Cycle-1255 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1253_swarm_ch10_w1253_10.png)

*Teaching figure (synthetic).* Cycle-1253 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1251_swarm_ch10_w1251_10.png)

*Teaching figure (synthetic).* Cycle-1251 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1249_swarm_ch10_w1249_10.png)

*Teaching figure (synthetic).* Cycle-1249 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1247_swarm_ch10_w1247_10.png)

*Teaching figure (synthetic).* Cycle-1247 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1245_swarm_ch10_w1245_10.png)

*Teaching figure (synthetic).* Cycle-1245 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1243_swarm_ch10_w1243_10.png)

*Teaching figure (synthetic).* Cycle-1243 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1241_swarm_ch10_w1241_10.png)

*Teaching figure (synthetic).* Cycle-1241 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1239_swarm_ch10_w1239_10.png)

*Teaching figure (synthetic).* Cycle-1239 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1237_swarm_ch10_w1237_10.png)

*Teaching figure (synthetic).* Cycle-1237 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1235_swarm_ch10_w1235_10.png)

*Teaching figure (synthetic).* Cycle-1235 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1233_swarm_ch10_w1233_10.png)

*Teaching figure (synthetic).* Cycle-1233 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1231_swarm_ch10_w1231_10.png)

*Teaching figure (synthetic).* Cycle-1231 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1229_swarm_ch10_w1229_10.png)

*Teaching figure (synthetic).* Cycle-1229 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1227_swarm_ch10_w1227_10.png)

*Teaching figure (synthetic).* Cycle-1227 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1225_swarm_ch10_w1225_10.png)

*Teaching figure (synthetic).* Cycle-1225 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1223_swarm_ch10_w1223_10.png)

*Teaching figure (synthetic).* Cycle-1223 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1221_swarm_ch10_w1221_10.png)

*Teaching figure (synthetic).* Cycle-1221 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1219_swarm_ch10_w1219_10.png)

*Teaching figure (synthetic).* Cycle-1219 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1217_swarm_ch10_w1217_10.png)

*Teaching figure (synthetic).* Cycle-1217 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1215_swarm_ch10_w1215_10.png)

*Teaching figure (synthetic).* Cycle-1215 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1213_swarm_ch10_w1213_10.png)

*Teaching figure (synthetic).* Cycle-1213 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1211_swarm_ch10_w1211_10.png)

*Teaching figure (synthetic).* Cycle-1211 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1209_swarm_ch10_w1209_10.png)

*Teaching figure (synthetic).* Cycle-1209 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1207_swarm_ch10_w1207_10.png)

*Teaching figure (synthetic).* Cycle-1207 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1205_swarm_ch10_w1205_10.png)

*Teaching figure (synthetic).* Cycle-1205 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1203_swarm_ch10_w1203_10.png)

*Teaching figure (synthetic).* Cycle-1203 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1201_swarm_ch10_w1201_10.png)

*Teaching figure (synthetic).* Cycle-1201 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1199_swarm_ch10_w1199_10.png)

*Teaching figure (synthetic).* Cycle-1199 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1197_swarm_ch10_w1197_10.png)

*Teaching figure (synthetic).* Cycle-1197 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1195_swarm_ch10_w1195_10.png)

*Teaching figure (synthetic).* Cycle-1195 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1193_swarm_ch10_w1193_10.png)

*Teaching figure (synthetic).* Cycle-1193 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1191_swarm_ch10_w1191_10.png)

*Teaching figure (synthetic).* Cycle-1191 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1189_swarm_ch10_w1189_10.png)

*Teaching figure (synthetic).* Cycle-1189 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1187_swarm_ch10_w1187_10.png)

*Teaching figure (synthetic).* Cycle-1187 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1185_swarm_ch10_w1185_10.png)

*Teaching figure (synthetic).* Cycle-1185 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1183_swarm_ch10_w1183_10.png)

*Teaching figure (synthetic).* Cycle-1183 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1181_swarm_ch10_w1181_10.png)

*Teaching figure (synthetic).* Cycle-1181 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1179_swarm_ch10_w1179_10.png)

*Teaching figure (synthetic).* Cycle-1179 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1177_swarm_ch10_w1177_10.png)

*Teaching figure (synthetic).* Cycle-1177 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1175_swarm_ch10_w1175_10.png)

*Teaching figure (synthetic).* Cycle-1175 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1173_swarm_ch10_w1173_10.png)

*Teaching figure (synthetic).* Cycle-1173 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1171_swarm_ch10_w1171_10.png)

*Teaching figure (synthetic).* Cycle-1171 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1169_swarm_ch10_w1169_10.png)

*Teaching figure (synthetic).* Cycle-1169 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1167_swarm_ch10_w1167_10.png)

*Teaching figure (synthetic).* Cycle-1167 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1165_swarm_ch10_w1165_10.png)

*Teaching figure (synthetic).* Cycle-1165 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1163_swarm_ch10_w1163_10.png)

*Teaching figure (synthetic).* Cycle-1163 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1161_swarm_ch10_w1161_10.png)

*Teaching figure (synthetic).* Cycle-1161 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1159_swarm_ch10_w1159_10.png)

*Teaching figure (synthetic).* Cycle-1159 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1157_swarm_ch10_w1157_10.png)

*Teaching figure (synthetic).* Cycle-1157 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1155_swarm_ch10_w1155_10.png)

*Teaching figure (synthetic).* Cycle-1155 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1153_swarm_ch10_w1153_10.png)

*Teaching figure (synthetic).* Cycle-1153 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1151_swarm_ch10_w1151_10.png)

*Teaching figure (synthetic).* Cycle-1151 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1149_swarm_ch10_w1149_10.png)

*Teaching figure (synthetic).* Cycle-1149 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1147_swarm_ch10_w1147_10.png)

*Teaching figure (synthetic).* Cycle-1147 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1145_swarm_ch10_w1145_10.png)

*Teaching figure (synthetic).* Cycle-1145 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1143_swarm_ch10_w1143_10.png)

*Teaching figure (synthetic).* Cycle-1143 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1141_swarm_ch10_w1141_10.png)

*Teaching figure (synthetic).* Cycle-1141 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1139_swarm_ch10_w1139_10.png)

*Teaching figure (synthetic).* Cycle-1139 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1137_swarm_ch10_w1137_10.png)

*Teaching figure (synthetic).* Cycle-1137 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1135_swarm_ch10_w1135_10.png)

*Teaching figure (synthetic).* Cycle-1135 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1133_swarm_ch10_w1133_10.png)

*Teaching figure (synthetic).* Cycle-1133 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1131_swarm_ch10_w1131_10.png)

*Teaching figure (synthetic).* Cycle-1131 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1129_swarm_ch10_w1129_10.png)

*Teaching figure (synthetic).* Cycle-1129 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1127_swarm_ch10_w1127_10.png)

*Teaching figure (synthetic).* Cycle-1127 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1125_swarm_ch10_w1125_10.png)

*Teaching figure (synthetic).* Cycle-1125 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1123_swarm_ch10_w1123_10.png)

*Teaching figure (synthetic).* Cycle-1123 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1121_swarm_ch10_w1121_10.png)

*Teaching figure (synthetic).* Cycle-1121 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1119_swarm_ch10_w1119_10.png)

*Teaching figure (synthetic).* Cycle-1119 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1117_swarm_ch10_w1117_10.png)

*Teaching figure (synthetic).* Cycle-1117 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1115_swarm_ch10_w1115_10.png)

*Teaching figure (synthetic).* Cycle-1115 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1113_swarm_ch10_w1113_10.png)

*Teaching figure (synthetic).* Cycle-1113 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1111_swarm_ch10_w1111_10.png)

*Teaching figure (synthetic).* Cycle-1111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1109_swarm_ch10_w1109_10.png)

*Teaching figure (synthetic).* Cycle-1109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1107_swarm_ch10_w1107_10.png)

*Teaching figure (synthetic).* Cycle-1107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1105_swarm_ch10_w1105_10.png)

*Teaching figure (synthetic).* Cycle-1105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1103_swarm_ch10_w1103_10.png)

*Teaching figure (synthetic).* Cycle-1103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1101_swarm_ch10_w1101_10.png)

*Teaching figure (synthetic).* Cycle-1101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1099_swarm_ch10_w1099_10.png)

*Teaching figure (synthetic).* Cycle-1099 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1097_swarm_ch10_w1097_10.png)

*Teaching figure (synthetic).* Cycle-1097 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1095_swarm_ch10_w1095_10.png)

*Teaching figure (synthetic).* Cycle-1095 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1093_swarm_ch10_w1093_10.png)

*Teaching figure (synthetic).* Cycle-1093 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1091_swarm_ch10_w1091_10.png)

*Teaching figure (synthetic).* Cycle-1091 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1089_swarm_ch10_w1089_10.png)

*Teaching figure (synthetic).* Cycle-1089 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1087_swarm_ch10_w1087_10.png)

*Teaching figure (synthetic).* Cycle-1087 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1085_swarm_ch10_w1085_10.png)

*Teaching figure (synthetic).* Cycle-1085 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1083_swarm_ch10_w1083_10.png)

*Teaching figure (synthetic).* Cycle-1083 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1081_swarm_ch10_w1081_10.png)

*Teaching figure (synthetic).* Cycle-1081 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1079_swarm_ch10_w1079_10.png)

*Teaching figure (synthetic).* Cycle-1079 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1077_swarm_ch10_w1077_10.png)

*Teaching figure (synthetic).* Cycle-1077 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1075_swarm_ch10_w1075_10.png)

*Teaching figure (synthetic).* Cycle-1075 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1073_swarm_ch10_w1073_10.png)

*Teaching figure (synthetic).* Cycle-1073 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1071_swarm_ch10_w1071_10.png)

*Teaching figure (synthetic).* Cycle-1071 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1069_swarm_ch10_w1069_10.png)

*Teaching figure (synthetic).* Cycle-1069 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1067_swarm_ch10_w1067_10.png)

*Teaching figure (synthetic).* Cycle-1067 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1065_swarm_ch10_w1065_10.png)

*Teaching figure (synthetic).* Cycle-1065 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1063_swarm_ch10_w1063_10.png)

*Teaching figure (synthetic).* Cycle-1063 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1061_swarm_ch10_w1061_10.png)

*Teaching figure (synthetic).* Cycle-1061 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1059_swarm_ch10_w1059_10.png)

*Teaching figure (synthetic).* Cycle-1059 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1057_swarm_ch10_w1057_10.png)

*Teaching figure (synthetic).* Cycle-1057 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1055_swarm_ch10_w1055_10.png)

*Teaching figure (synthetic).* Cycle-1055 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1053_swarm_ch10_w1053_10.png)

*Teaching figure (synthetic).* Cycle-1053 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1051_swarm_ch10_w1051_10.png)

*Teaching figure (synthetic).* Cycle-1051 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1049_swarm_ch10_w1049_10.png)

*Teaching figure (synthetic).* Cycle-1049 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1047_swarm_ch10_w1047_10.png)

*Teaching figure (synthetic).* Cycle-1047 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1045_swarm_ch10_w1045_10.png)

*Teaching figure (synthetic).* Cycle-1045 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1043_swarm_ch10_w1043_10.png)

*Teaching figure (synthetic).* Cycle-1043 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1041_swarm_ch10_w1041_10.png)

*Teaching figure (synthetic).* Cycle-1041 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1039_swarm_ch10_w1039_10.png)

*Teaching figure (synthetic).* Cycle-1039 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1037_swarm_ch10_w1037_10.png)

*Teaching figure (synthetic).* Cycle-1037 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1035_swarm_ch10_w1035_10.png)

*Teaching figure (synthetic).* Cycle-1035 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1033_swarm_ch10_w1033_10.png)

*Teaching figure (synthetic).* Cycle-1033 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1031_swarm_ch10_w1031_10.png)

*Teaching figure (synthetic).* Cycle-1031 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1029_swarm_ch10_w1029_10.png)

*Teaching figure (synthetic).* Cycle-1029 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1027_swarm_ch10_w1027_10.png)

*Teaching figure (synthetic).* Cycle-1027 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1025_swarm_ch10_w1025_10.png)

*Teaching figure (synthetic).* Cycle-1025 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1023_swarm_ch10_w1023_10.png)

*Teaching figure (synthetic).* Cycle-1023 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1021_swarm_ch10_w1021_10.png)

*Teaching figure (synthetic).* Cycle-1021 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1019_swarm_ch10_w1019_10.png)

*Teaching figure (synthetic).* Cycle-1019 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1017_swarm_ch10_w1017_10.png)

*Teaching figure (synthetic).* Cycle-1017 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1015_swarm_ch10_w1015_10.png)

*Teaching figure (synthetic).* Cycle-1015 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1013_swarm_ch10_w1013_10.png)

*Teaching figure (synthetic).* Cycle-1013 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1011_swarm_ch10_w1011_10.png)

*Teaching figure (synthetic).* Cycle-1011 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1009_swarm_ch10_w1009_10.png)

*Teaching figure (synthetic).* Cycle-1009 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1007_swarm_ch10_w1007_10.png)

*Teaching figure (synthetic).* Cycle-1007 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1005_swarm_ch10_w1005_10.png)

*Teaching figure (synthetic).* Cycle-1005 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1003_swarm_ch10_w1003_10.png)

*Teaching figure (synthetic).* Cycle-1003 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle1001_swarm_ch10_w1001_10.png)

*Teaching figure (synthetic).* Cycle-1001 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle999_swarm_ch10_w999_10.png)

*Teaching figure (synthetic).* Cycle-999 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle997_swarm_ch10_w997_10.png)

*Teaching figure (synthetic).* Cycle-997 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle995_swarm_ch10_w995_10.png)

*Teaching figure (synthetic).* Cycle-995 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle993_swarm_ch10_w993_10.png)

*Teaching figure (synthetic).* Cycle-993 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle991_swarm_ch10_w991_10.png)

*Teaching figure (synthetic).* Cycle-991 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle989_swarm_ch10_w989_10.png)

*Teaching figure (synthetic).* Cycle-989 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle987_swarm_ch10_w987_10.png)

*Teaching figure (synthetic).* Cycle-987 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle985_swarm_ch10_w985_10.png)

*Teaching figure (synthetic).* Cycle-985 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle983_swarm_ch10_w983_10.png)

*Teaching figure (synthetic).* Cycle-983 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle981_swarm_ch10_w981_10.png)

*Teaching figure (synthetic).* Cycle-981 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle979_swarm_ch10_w979_10.png)

*Teaching figure (synthetic).* Cycle-979 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle977_swarm_ch10_w977_10.png)

*Teaching figure (synthetic).* Cycle-977 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle975_swarm_ch10_w975_10.png)

*Teaching figure (synthetic).* Cycle-975 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle973_swarm_ch10_w973_10.png)

*Teaching figure (synthetic).* Cycle-973 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle971_swarm_ch10_w971_10.png)

*Teaching figure (synthetic).* Cycle-971 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle969_swarm_ch10_w969_10.png)

*Teaching figure (synthetic).* Cycle-969 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle967_swarm_ch10_w967_10.png)

*Teaching figure (synthetic).* Cycle-967 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle965_swarm_ch10_w965_10.png)

*Teaching figure (synthetic).* Cycle-965 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle963_swarm_ch10_w963_10.png)

*Teaching figure (synthetic).* Cycle-963 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle961_swarm_ch10_w961_10.png)

*Teaching figure (synthetic).* Cycle-961 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle959_swarm_ch10_w959_10.png)

*Teaching figure (synthetic).* Cycle-959 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle957_swarm_ch10_w957_10.png)

*Teaching figure (synthetic).* Cycle-957 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle955_swarm_ch10_w955_10.png)

*Teaching figure (synthetic).* Cycle-955 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle953_swarm_ch10_w953_10.png)

*Teaching figure (synthetic).* Cycle-953 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle951_swarm_ch10_w951_10.png)

*Teaching figure (synthetic).* Cycle-951 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle949_swarm_ch10_w949_10.png)

*Teaching figure (synthetic).* Cycle-949 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle947_swarm_ch10_w947_10.png)

*Teaching figure (synthetic).* Cycle-947 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle945_swarm_ch10_w945_10.png)

*Teaching figure (synthetic).* Cycle-945 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle943_swarm_ch10_w943_10.png)

*Teaching figure (synthetic).* Cycle-943 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle941_swarm_ch10_w941_10.png)

*Teaching figure (synthetic).* Cycle-941 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle939_swarm_ch10_w939_10.png)

*Teaching figure (synthetic).* Cycle-939 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle937_swarm_ch10_w937_10.png)

*Teaching figure (synthetic).* Cycle-937 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle935_swarm_ch10_w935_10.png)

*Teaching figure (synthetic).* Cycle-935 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle933_swarm_ch10_w933_10.png)

*Teaching figure (synthetic).* Cycle-933 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle931_swarm_ch10_w931_10.png)

*Teaching figure (synthetic).* Cycle-931 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle929_swarm_ch10_w929_10.png)

*Teaching figure (synthetic).* Cycle-929 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle927_swarm_ch10_w927_10.png)

*Teaching figure (synthetic).* Cycle-927 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle925_swarm_ch10_w925_10.png)

*Teaching figure (synthetic).* Cycle-925 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle923_swarm_ch10_w923_10.png)

*Teaching figure (synthetic).* Cycle-923 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle921_swarm_ch10_w921_10.png)

*Teaching figure (synthetic).* Cycle-921 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle919_swarm_ch10_w919_10.png)

*Teaching figure (synthetic).* Cycle-919 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle917_swarm_ch10_w917_10.png)

*Teaching figure (synthetic).* Cycle-917 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle915_swarm_ch10_w915_10.png)

*Teaching figure (synthetic).* Cycle-915 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle913_swarm_ch10_w913_10.png)

*Teaching figure (synthetic).* Cycle-913 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle911_swarm_ch10_w911_10.png)

*Teaching figure (synthetic).* Cycle-911 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle909_swarm_ch10_w909_10.png)

*Teaching figure (synthetic).* Cycle-909 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle907_swarm_ch10_w907_10.png)

*Teaching figure (synthetic).* Cycle-907 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle905_swarm_ch10_w905_10.png)

*Teaching figure (synthetic).* Cycle-905 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle903_swarm_ch10_w903_10.png)

*Teaching figure (synthetic).* Cycle-903 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle901_swarm_ch10_w901_10.png)

*Teaching figure (synthetic).* Cycle-901 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle899_swarm_ch10_w899_10.png)

*Teaching figure (synthetic).* Cycle-899 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle897_swarm_ch10_w897_10.png)

*Teaching figure (synthetic).* Cycle-897 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle895_swarm_ch10_w895_10.png)

*Teaching figure (synthetic).* Cycle-895 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle893_swarm_ch10_w893_10.png)

*Teaching figure (synthetic).* Cycle-893 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle891_swarm_ch10_w891_10.png)

*Teaching figure (synthetic).* Cycle-891 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle889_swarm_ch10_w889_10.png)

*Teaching figure (synthetic).* Cycle-889 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle887_swarm_ch10_w887_10.png)

*Teaching figure (synthetic).* Cycle-887 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle885_swarm_ch10_w885_10.png)

*Teaching figure (synthetic).* Cycle-885 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle883_swarm_ch10_w883_10.png)

*Teaching figure (synthetic).* Cycle-883 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle881_swarm_ch10_w881_10.png)

*Teaching figure (synthetic).* Cycle-881 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle879_swarm_ch10_w879_10.png)

*Teaching figure (synthetic).* Cycle-879 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle877_swarm_ch10_w877_10.png)

*Teaching figure (synthetic).* Cycle-877 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle875_swarm_ch10_w875_10.png)

*Teaching figure (synthetic).* Cycle-875 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle873_swarm_ch10_w873_10.png)

*Teaching figure (synthetic).* Cycle-873 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle871_swarm_ch10_w871_10.png)

*Teaching figure (synthetic).* Cycle-871 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle869_swarm_ch10_w869_10.png)

*Teaching figure (synthetic).* Cycle-869 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle867_swarm_ch10_w867_10.png)

*Teaching figure (synthetic).* Cycle-867 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle865_swarm_ch10_w865_10.png)

*Teaching figure (synthetic).* Cycle-865 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle863_swarm_ch10_w863_10.png)

*Teaching figure (synthetic).* Cycle-863 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle861_swarm_ch10_w861_10.png)

*Teaching figure (synthetic).* Cycle-861 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle859_swarm_ch10_w859_10.png)

*Teaching figure (synthetic).* Cycle-859 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle857_swarm_ch10_w857_10.png)

*Teaching figure (synthetic).* Cycle-857 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle855_swarm_ch10_w855_10.png)

*Teaching figure (synthetic).* Cycle-855 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle853_swarm_ch10_w853_10.png)

*Teaching figure (synthetic).* Cycle-853 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle851_swarm_ch10_w851_10.png)

*Teaching figure (synthetic).* Cycle-851 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle849_swarm_ch10_w849_10.png)

*Teaching figure (synthetic).* Cycle-849 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle847_swarm_ch10_w847_10.png)

*Teaching figure (synthetic).* Cycle-847 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle845_swarm_ch10_w845_10.png)

*Teaching figure (synthetic).* Cycle-845 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle843_swarm_ch10_w843_10.png)

*Teaching figure (synthetic).* Cycle-843 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle841_swarm_ch10_w841_10.png)

*Teaching figure (synthetic).* Cycle-841 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle839_swarm_ch10_w839_10.png)

*Teaching figure (synthetic).* Cycle-839 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle837_swarm_ch10_w837_10.png)

*Teaching figure (synthetic).* Cycle-837 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle835_swarm_ch10_w835_10.png)

*Teaching figure (synthetic).* Cycle-835 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle833_swarm_ch10_w833_10.png)

*Teaching figure (synthetic).* Cycle-833 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle831_swarm_ch10_w831_10.png)

*Teaching figure (synthetic).* Cycle-831 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle829_swarm_ch10_w829_10.png)

*Teaching figure (synthetic).* Cycle-829 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle827_swarm_ch10_w827_10.png)

*Teaching figure (synthetic).* Cycle-827 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle825_swarm_ch10_w825_10.png)

*Teaching figure (synthetic).* Cycle-825 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle823_swarm_ch10_w823_10.png)

*Teaching figure (synthetic).* Cycle-823 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle821_swarm_ch10_w821_10.png)

*Teaching figure (synthetic).* Cycle-821 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle819_swarm_ch10_w819_10.png)

*Teaching figure (synthetic).* Cycle-819 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle817_swarm_ch10_w817_10.png)

*Teaching figure (synthetic).* Cycle-817 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle815_swarm_ch10_w815_10.png)

*Teaching figure (synthetic).* Cycle-815 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle813_swarm_ch10_w813_10.png)

*Teaching figure (synthetic).* Cycle-813 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle811_swarm_ch10_w811_10.png)

*Teaching figure (synthetic).* Cycle-811 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle809_swarm_ch10_w809_10.png)

*Teaching figure (synthetic).* Cycle-809 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle807_swarm_ch10_w807_10.png)

*Teaching figure (synthetic).* Cycle-807 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle805_swarm_ch10_w805_10.png)

*Teaching figure (synthetic).* Cycle-805 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle803_swarm_ch10_w803_10.png)

*Teaching figure (synthetic).* Cycle-803 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle801_swarm_ch10_w801_10.png)

*Teaching figure (synthetic).* Cycle-801 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle799_swarm_ch10_w799_10.png)

*Teaching figure (synthetic).* Cycle-799 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle797_swarm_ch10_w797_10.png)

*Teaching figure (synthetic).* Cycle-797 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle795_swarm_ch10_w795_10.png)

*Teaching figure (synthetic).* Cycle-795 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle793_swarm_ch10_w793_10.png)

*Teaching figure (synthetic).* Cycle-793 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle791_swarm_ch10_w791_10.png)

*Teaching figure (synthetic).* Cycle-791 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle789_swarm_ch10_w789_10.png)

*Teaching figure (synthetic).* Cycle-789 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle787_swarm_ch10_w787_10.png)

*Teaching figure (synthetic).* Cycle-787 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle785_swarm_ch10_w785_10.png)

*Teaching figure (synthetic).* Cycle-785 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle783_swarm_ch10_w783_10.png)

*Teaching figure (synthetic).* Cycle-783 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle781_swarm_ch10_w781_10.png)

*Teaching figure (synthetic).* Cycle-781 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle779_swarm_ch10_w779_10.png)

*Teaching figure (synthetic).* Cycle-779 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle777_swarm_ch10_w777_10.png)

*Teaching figure (synthetic).* Cycle-777 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle775_swarm_ch10_w775_10.png)

*Teaching figure (synthetic).* Cycle-775 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle773_swarm_ch10_w773_10.png)

*Teaching figure (synthetic).* Cycle-773 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle771_swarm_ch10_w771_10.png)

*Teaching figure (synthetic).* Cycle-771 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle769_swarm_ch10_w769_10.png)

*Teaching figure (synthetic).* Cycle-769 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle767_swarm_ch10_w767_10.png)

*Teaching figure (synthetic).* Cycle-767 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle765_swarm_ch10_w765_10.png)

*Teaching figure (synthetic).* Cycle-765 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle763_swarm_ch10_w763_10.png)

*Teaching figure (synthetic).* Cycle-763 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle761_swarm_ch10_w761_10.png)

*Teaching figure (synthetic).* Cycle-761 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle759_swarm_ch10_w759_10.png)

*Teaching figure (synthetic).* Cycle-759 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle757_swarm_ch10_w757_10.png)

*Teaching figure (synthetic).* Cycle-757 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle755_swarm_ch10_w755_10.png)

*Teaching figure (synthetic).* Cycle-755 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle753_swarm_ch10_w753_10.png)

*Teaching figure (synthetic).* Cycle-753 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle751_swarm_ch10_w751_10.png)

*Teaching figure (synthetic).* Cycle-751 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle749_swarm_ch10_w749_10.png)

*Teaching figure (synthetic).* Cycle-749 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle747_swarm_ch10_w747_10.png)

*Teaching figure (synthetic).* Cycle-747 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle745_swarm_ch10_w745_10.png)

*Teaching figure (synthetic).* Cycle-745 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle743_swarm_ch10_w743_10.png)

*Teaching figure (synthetic).* Cycle-743 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle741_swarm_ch10_w741_10.png)

*Teaching figure (synthetic).* Cycle-741 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle739_swarm_ch10_w739_10.png)

*Teaching figure (synthetic).* Cycle-739 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle737_swarm_ch10_w737_10.png)

*Teaching figure (synthetic).* Cycle-737 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle735_swarm_ch10_w735_10.png)

*Teaching figure (synthetic).* Cycle-735 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle733_swarm_ch10_w733_10.png)

*Teaching figure (synthetic).* Cycle-733 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle731_swarm_ch10_w731_10.png)

*Teaching figure (synthetic).* Cycle-731 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle729_swarm_ch10_w729_10.png)

*Teaching figure (synthetic).* Cycle-729 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle727_swarm_ch10_w727_10.png)

*Teaching figure (synthetic).* Cycle-727 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle725_swarm_ch10_w725_10.png)

*Teaching figure (synthetic).* Cycle-725 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle723_swarm_ch10_w723_10.png)

*Teaching figure (synthetic).* Cycle-723 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle721_swarm_ch10_w721_10.png)

*Teaching figure (synthetic).* Cycle-721 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle719_swarm_ch10_w719_10.png)

*Teaching figure (synthetic).* Cycle-719 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle717_swarm_ch10_w717_10.png)

*Teaching figure (synthetic).* Cycle-717 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle715_swarm_ch10_w715_10.png)

*Teaching figure (synthetic).* Cycle-715 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle713_swarm_ch10_w713_10.png)

*Teaching figure (synthetic).* Cycle-713 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle711_swarm_ch10_w711_10.png)

*Teaching figure (synthetic).* Cycle-711 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle709_swarm_ch10_w709_10.png)

*Teaching figure (synthetic).* Cycle-709 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle707_swarm_ch10_w707_10.png)

*Teaching figure (synthetic).* Cycle-707 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle705_swarm_ch10_w705_10.png)

*Teaching figure (synthetic).* Cycle-705 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle703_swarm_ch10_w703_10.png)

*Teaching figure (synthetic).* Cycle-703 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle701_swarm_ch10_w701_10.png)

*Teaching figure (synthetic).* Cycle-701 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle699_swarm_ch10_w699_10.png)

*Teaching figure (synthetic).* Cycle-699 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle697_swarm_ch10_w697_10.png)

*Teaching figure (synthetic).* Cycle-697 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle695_swarm_ch10_w695_10.png)

*Teaching figure (synthetic).* Cycle-695 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle693_swarm_ch10_w693_10.png)

*Teaching figure (synthetic).* Cycle-693 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle691_swarm_ch10_w691_10.png)

*Teaching figure (synthetic).* Cycle-691 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle689_swarm_ch10_w689_10.png)

*Teaching figure (synthetic).* Cycle-689 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle687_swarm_ch10_w687_10.png)

*Teaching figure (synthetic).* Cycle-687 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle685_swarm_ch10_w685_10.png)

*Teaching figure (synthetic).* Cycle-685 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle683_swarm_ch10_w683_10.png)

*Teaching figure (synthetic).* Cycle-683 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle681_swarm_ch10_w681_10.png)

*Teaching figure (synthetic).* Cycle-681 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle679_swarm_ch10_w679_10.png)

*Teaching figure (synthetic).* Cycle-679 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle677_swarm_ch10_w677_10.png)

*Teaching figure (synthetic).* Cycle-677 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle675_swarm_ch10_w675_10.png)

*Teaching figure (synthetic).* Cycle-675 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle673_swarm_ch10_w673_10.png)

*Teaching figure (synthetic).* Cycle-673 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle671_swarm_ch10_w671_10.png)

*Teaching figure (synthetic).* Cycle-671 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle669_swarm_ch10_w669_10.png)

*Teaching figure (synthetic).* Cycle-669 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle667_swarm_ch10_w667_10.png)

*Teaching figure (synthetic).* Cycle-667 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle665_swarm_ch10_w665_10.png)

*Teaching figure (synthetic).* Cycle-665 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle663_swarm_ch10_w663_10.png)

*Teaching figure (synthetic).* Cycle-663 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle661_swarm_ch10_w661_10.png)

*Teaching figure (synthetic).* Cycle-661 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle659_swarm_ch10_w659_10.png)

*Teaching figure (synthetic).* Cycle-659 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle657_swarm_ch10_w657_10.png)

*Teaching figure (synthetic).* Cycle-657 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle655_swarm_ch10_w655_10.png)

*Teaching figure (synthetic).* Cycle-655 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle653_swarm_ch10_w653_10.png)

*Teaching figure (synthetic).* Cycle-653 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle651_swarm_ch10_w651_10.png)

*Teaching figure (synthetic).* Cycle-651 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle649_swarm_ch10_w649_10.png)

*Teaching figure (synthetic).* Cycle-649 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle647_swarm_ch10_w647_10.png)

*Teaching figure (synthetic).* Cycle-647 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle645_swarm_ch10_w645_10.png)

*Teaching figure (synthetic).* Cycle-645 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle643_swarm_ch10_w643_10.png)

*Teaching figure (synthetic).* Cycle-643 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle641_swarm_ch10_w641_10.png)

*Teaching figure (synthetic).* Cycle-641 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle639_swarm_ch10_w639_10.png)

*Teaching figure (synthetic).* Cycle-639 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle637_swarm_ch10_w637_10.png)

*Teaching figure (synthetic).* Cycle-637 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle635_swarm_ch10_w635_10.png)

*Teaching figure (synthetic).* Cycle-635 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle633_swarm_ch10_w633_10.png)

*Teaching figure (synthetic).* Cycle-633 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle631_swarm_ch10_w631_10.png)

*Teaching figure (synthetic).* Cycle-631 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle629_swarm_ch10_w629_10.png)

*Teaching figure (synthetic).* Cycle-629 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle627_swarm_ch10_w627_10.png)

*Teaching figure (synthetic).* Cycle-627 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle625_swarm_ch10_w625_10.png)

*Teaching figure (synthetic).* Cycle-625 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle623_swarm_ch10_w623_10.png)

*Teaching figure (synthetic).* Cycle-623 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle621_swarm_ch10_w621_10.png)

*Teaching figure (synthetic).* Cycle-621 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle619_swarm_ch10_w619_10.png)

*Teaching figure (synthetic).* Cycle-619 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle617_swarm_ch10_w617_10.png)

*Teaching figure (synthetic).* Cycle-617 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle615_swarm_ch10_w615_10.png)

*Teaching figure (synthetic).* Cycle-615 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle613_swarm_ch10_w613_10.png)

*Teaching figure (synthetic).* Cycle-613 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle611_swarm_ch10_w611_10.png)

*Teaching figure (synthetic).* Cycle-611 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle609_swarm_ch10_w609_10.png)

*Teaching figure (synthetic).* Cycle-609 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle607_swarm_ch10_w607_10.png)

*Teaching figure (synthetic).* Cycle-607 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle605_swarm_ch10_w605_10.png)

*Teaching figure (synthetic).* Cycle-605 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle603_swarm_ch10_w603_10.png)

*Teaching figure (synthetic).* Cycle-603 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle601_swarm_ch10_w601_10.png)

*Teaching figure (synthetic).* Cycle-601 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle599_swarm_ch10_w599_10.png)

*Teaching figure (synthetic).* Cycle-599 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle597_swarm_ch10_w597_10.png)

*Teaching figure (synthetic).* Cycle-597 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle595_swarm_ch10_w595_10.png)

*Teaching figure (synthetic).* Cycle-595 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle593_swarm_ch10_w593_10.png)

*Teaching figure (synthetic).* Cycle-593 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle591_swarm_ch10_w591_10.png)

*Teaching figure (synthetic).* Cycle-591 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle589_swarm_ch10_w589_10.png)

*Teaching figure (synthetic).* Cycle-589 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle587_swarm_ch10_w587_10.png)

*Teaching figure (synthetic).* Cycle-587 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle585_swarm_ch10_w585_10.png)

*Teaching figure (synthetic).* Cycle-585 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle583_swarm_ch10_w583_10.png)

*Teaching figure (synthetic).* Cycle-583 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle581_swarm_ch10_w581_10.png)

*Teaching figure (synthetic).* Cycle-581 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle579_swarm_ch10_w579_10.png)

*Teaching figure (synthetic).* Cycle-579 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle577_swarm_ch10_w577_10.png)

*Teaching figure (synthetic).* Cycle-577 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle575_swarm_ch10_w575_10.png)

*Teaching figure (synthetic).* Cycle-575 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle573_swarm_ch10_w573_10.png)

*Teaching figure (synthetic).* Cycle-573 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle571_swarm_ch10_w571_10.png)

*Teaching figure (synthetic).* Cycle-571 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle569_swarm_ch10_w569_10.png)

*Teaching figure (synthetic).* Cycle-569 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle567_swarm_ch10_w567_10.png)

*Teaching figure (synthetic).* Cycle-567 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle565_swarm_ch10_w565_10.png)

*Teaching figure (synthetic).* Cycle-565 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle563_swarm_ch10_w563_10.png)

*Teaching figure (synthetic).* Cycle-563 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle561_swarm_ch10_w561_10.png)

*Teaching figure (synthetic).* Cycle-561 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle559_swarm_ch10_w559_10.png)

*Teaching figure (synthetic).* Cycle-559 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle557_swarm_ch10_w557_10.png)

*Teaching figure (synthetic).* Cycle-557 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle555_swarm_ch10_w555_10.png)

*Teaching figure (synthetic).* Cycle-555 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle553_swarm_ch10_w553_10.png)

*Teaching figure (synthetic).* Cycle-553 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle551_swarm_ch10_w551_10.png)

*Teaching figure (synthetic).* Cycle-551 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle549_swarm_ch10_w549_10.png)

*Teaching figure (synthetic).* Cycle-549 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle547_swarm_ch10_w547_10.png)

*Teaching figure (synthetic).* Cycle-547 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle545_swarm_ch10_w545_10.png)

*Teaching figure (synthetic).* Cycle-545 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle543_swarm_ch10_w543_10.png)

*Teaching figure (synthetic).* Cycle-543 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle541_swarm_ch10_w541_10.png)

*Teaching figure (synthetic).* Cycle-541 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle539_swarm_ch10_w539_10.png)

*Teaching figure (synthetic).* Cycle-539 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle537_swarm_ch10_w537_10.png)

*Teaching figure (synthetic).* Cycle-537 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle535_swarm_ch10_w535_10.png)

*Teaching figure (synthetic).* Cycle-535 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle533_swarm_ch10_w533_10.png)

*Teaching figure (synthetic).* Cycle-533 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle531_swarm_ch10_w531_10.png)

*Teaching figure (synthetic).* Cycle-531 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle529_swarm_ch10_w529_10.png)

*Teaching figure (synthetic).* Cycle-529 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle527_swarm_ch10_w527_10.png)

*Teaching figure (synthetic).* Cycle-527 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle525_swarm_ch10_w525_10.png)

*Teaching figure (synthetic).* Cycle-525 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle523_swarm_ch10_w523_10.png)

*Teaching figure (synthetic).* Cycle-523 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle521_swarm_ch10_w521_10.png)

*Teaching figure (synthetic).* Cycle-521 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle519_swarm_ch10_w519_10.png)

*Teaching figure (synthetic).* Cycle-519 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle517_swarm_ch10_w517_10.png)

*Teaching figure (synthetic).* Cycle-517 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle515_swarm_ch10_w515_10.png)

*Teaching figure (synthetic).* Cycle-515 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle513_swarm_ch10_w513_10.png)

*Teaching figure (synthetic).* Cycle-513 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle511_swarm_ch10_w511_10.png)

*Teaching figure (synthetic).* Cycle-511 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle509_swarm_ch10_w509_10.png)

*Teaching figure (synthetic).* Cycle-509 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle507_swarm_ch10_w507_10.png)

*Teaching figure (synthetic).* Cycle-507 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle505_swarm_ch10_w505_10.png)

*Teaching figure (synthetic).* Cycle-505 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle503_swarm_ch10_w503_10.png)

*Teaching figure (synthetic).* Cycle-503 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle501_swarm_ch10_w501_10.png)

*Teaching figure (synthetic).* Cycle-501 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle499_swarm_ch10_w499_10.png)

*Teaching figure (synthetic).* Cycle-499 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle497_swarm_ch10_w497_10.png)

*Teaching figure (synthetic).* Cycle-497 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle495_swarm_ch10_w495_10.png)

*Teaching figure (synthetic).* Cycle-495 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle493_swarm_ch10_w493_10.png)

*Teaching figure (synthetic).* Cycle-493 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle491_swarm_ch10_w491_10.png)

*Teaching figure (synthetic).* Cycle-491 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle489_swarm_ch10_w489_10.png)

*Teaching figure (synthetic).* Cycle-489 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle487_swarm_ch10_w487_10.png)

*Teaching figure (synthetic).* Cycle-487 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle485_swarm_ch10_w485_10.png)

*Teaching figure (synthetic).* Cycle-485 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle483_swarm_ch10_w483_10.png)

*Teaching figure (synthetic).* Cycle-483 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle481_swarm_ch10_w481_10.png)

*Teaching figure (synthetic).* Cycle-481 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle479_swarm_ch10_w479_10.png)

*Teaching figure (synthetic).* Cycle-479 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle477_swarm_ch10_w477_10.png)

*Teaching figure (synthetic).* Cycle-477 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle475_swarm_ch10_w475_10.png)

*Teaching figure (synthetic).* Cycle-475 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle473_swarm_ch10_w473_10.png)

*Teaching figure (synthetic).* Cycle-473 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle471_swarm_ch10_w471_10.png)

*Teaching figure (synthetic).* Cycle-471 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle469_swarm_ch10_w469_10.png)

*Teaching figure (synthetic).* Cycle-469 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle467_swarm_ch10_w467_10.png)

*Teaching figure (synthetic).* Cycle-467 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle465_swarm_ch10_w465_10.png)

*Teaching figure (synthetic).* Cycle-465 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle463_swarm_ch10_w463_10.png)

*Teaching figure (synthetic).* Cycle-463 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle461_swarm_ch10_w461_10.png)

*Teaching figure (synthetic).* Cycle-461 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle459_swarm_ch10_w459_10.png)

*Teaching figure (synthetic).* Cycle-459 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle457_swarm_ch10_w457_10.png)

*Teaching figure (synthetic).* Cycle-457 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle455_swarm_ch10_w455_10.png)

*Teaching figure (synthetic).* Cycle-455 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle453_swarm_ch10_w453_10.png)

*Teaching figure (synthetic).* Cycle-453 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle451_swarm_ch10_w451_10.png)

*Teaching figure (synthetic).* Cycle-451 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle449_swarm_ch10_w449_10.png)

*Teaching figure (synthetic).* Cycle-449 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle447_swarm_ch10_w447_10.png)

*Teaching figure (synthetic).* Cycle-447 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle445_swarm_ch10_w445_10.png)

*Teaching figure (synthetic).* Cycle-445 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle443_swarm_ch10_w443_10.png)

*Teaching figure (synthetic).* Cycle-443 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle441_swarm_ch10_w441_10.png)

*Teaching figure (synthetic).* Cycle-441 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle439_swarm_ch10_w439_10.png)

*Teaching figure (synthetic).* Cycle-439 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle437_swarm_ch10_w437_10.png)

*Teaching figure (synthetic).* Cycle-437 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle435_swarm_ch10_w435_10.png)

*Teaching figure (synthetic).* Cycle-435 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle433_swarm_ch10_w433_10.png)

*Teaching figure (synthetic).* Cycle-433 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle431_swarm_ch10_w431_10.png)

*Teaching figure (synthetic).* Cycle-431 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle429_swarm_ch10_w429_10.png)

*Teaching figure (synthetic).* Cycle-429 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle427_swarm_ch10_w427_10.png)

*Teaching figure (synthetic).* Cycle-427 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle425_swarm_ch10_w425_10.png)

*Teaching figure (synthetic).* Cycle-425 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle423_swarm_ch10_w423_10.png)

*Teaching figure (synthetic).* Cycle-423 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle421_swarm_ch10_w421_10.png)

*Teaching figure (synthetic).* Cycle-421 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle419_swarm_ch10_w419_10.png)

*Teaching figure (synthetic).* Cycle-419 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle417_swarm_ch10_w417_10.png)

*Teaching figure (synthetic).* Cycle-417 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle415_swarm_ch10_w415_10.png)

*Teaching figure (synthetic).* Cycle-415 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle413_swarm_ch10_w413_10.png)

*Teaching figure (synthetic).* Cycle-413 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle411_swarm_ch10_w411_10.png)

*Teaching figure (synthetic).* Cycle-411 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle409_swarm_ch10_w409_10.png)

*Teaching figure (synthetic).* Cycle-409 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle407_swarm_ch10_w407_10.png)

*Teaching figure (synthetic).* Cycle-407 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle405_swarm_ch10_w405_10.png)

*Teaching figure (synthetic).* Cycle-405 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle403_swarm_ch10_w403_10.png)

*Teaching figure (synthetic).* Cycle-403 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle401_swarm_ch10_w401_10.png)

*Teaching figure (synthetic).* Cycle-401 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle399_swarm_ch10_w399_10.png)

*Teaching figure (synthetic).* Cycle-399 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle397_swarm_ch10_w397_10.png)

*Teaching figure (synthetic).* Cycle-397 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle395_swarm_ch10_w395_10.png)

*Teaching figure (synthetic).* Cycle-395 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle393_swarm_ch10_w393_10.png)

*Teaching figure (synthetic).* Cycle-393 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle391_swarm_ch10_w391_10.png)

*Teaching figure (synthetic).* Cycle-391 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle389_swarm_ch10_w389_10.png)

*Teaching figure (synthetic).* Cycle-389 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle387_swarm_ch10_w387_10.png)

*Teaching figure (synthetic).* Cycle-387 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle385_swarm_ch10_w385_10.png)

*Teaching figure (synthetic).* Cycle-385 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle383_swarm_ch10_w383_10.png)

*Teaching figure (synthetic).* Cycle-383 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle381_swarm_ch10_w381_10.png)

*Teaching figure (synthetic).* Cycle-381 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle379_swarm_ch10_w379_10.png)

*Teaching figure (synthetic).* Cycle-379 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle377_swarm_ch10_w377_10.png)

*Teaching figure (synthetic).* Cycle-377 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle375_swarm_ch10_w375_10.png)

*Teaching figure (synthetic).* Cycle-375 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle373_swarm_ch10_w373_10.png)

*Teaching figure (synthetic).* Cycle-373 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle371_swarm_ch10_w371_10.png)

*Teaching figure (synthetic).* Cycle-371 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle369_swarm_ch10_w369_10.png)

*Teaching figure (synthetic).* Cycle-369 densify scientific residual.


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle367_swarm_ch10_w367_10.png)

*Teaching figure (synthetic).* Cycle-367 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle365_swarm_ch10_w365_10.png)

*Teaching figure (synthetic).* Cycle-365 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle363_swarm_ch10_w363_10.png)

*Teaching figure (synthetic).* Cycle-363 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle361_swarm_ch10_w361_10.png)

*Teaching figure (synthetic).* Cycle-361 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle359_swarm_ch10_w359_10.png)

*Teaching figure (synthetic).* Cycle-359 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle357_swarm_ch10_w357_10.png)

*Teaching figure (synthetic).* Cycle-357 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle355_swarm_ch10_w355_10.png)

*Teaching figure (synthetic).* Cycle-355 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle353_swarm_ch10_w353_10.png)

*Teaching figure (synthetic).* Cycle-353 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle351_swarm_ch10_w351_10.png)

*Teaching figure (synthetic).* Cycle-351 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle349_swarm_ch10_w349_10.png)

*Teaching figure (synthetic).* Cycle-349 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle347_swarm_ch10_w347_10.png)

*Teaching figure (synthetic).* Cycle-347 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle345_swarm_ch10_w345_10.png)

*Teaching figure (synthetic).* Cycle-345 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle343_swarm_ch10_w343_10.png)

*Teaching figure (synthetic).* Cycle-343 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle341_swarm_ch10_w341_10.png)

*Teaching figure (synthetic).* Cycle-341 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle339_swarm_ch10_w339_10.png)

*Teaching figure (synthetic).* Cycle-339 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle337_swarm_ch10_w337_10.png)

*Teaching figure (synthetic).* Cycle-337 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle335_swarm_ch10_w335_10.png)

*Teaching figure (synthetic).* Cycle-335 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle333_swarm_ch10_w333_10.png)

*Teaching figure (synthetic).* Cycle-333 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle331_swarm_ch10_w331_10.png)

*Teaching figure (synthetic).* Cycle-331 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle329_swarm_ch10_w329_10.png)

*Teaching figure (synthetic).* Cycle-329 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle327_swarm_ch10_w327_10.png)

*Teaching figure (synthetic).* Cycle-327 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle325_swarm_ch10_w325_10.png)

*Teaching figure (synthetic).* Cycle-325 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle323_swarm_ch10_w323_10.png)

*Teaching figure (synthetic).* Cycle-323 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle321_swarm_ch10_w321_10.png)

*Teaching figure (synthetic).* Cycle-321 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle319_swarm_ch10_w319_10.png)

*Teaching figure (synthetic).* Cycle-319 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle317_swarm_ch10_w317_10.png)

*Teaching figure (synthetic).* Cycle-317 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle315_swarm_ch10_w315_10.png)

*Teaching figure (synthetic).* Cycle-315 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle313_swarm_ch10_w313_10.png)

*Teaching figure (synthetic).* Cycle-313 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle311_swarm_ch10_w311_10.png)

*Teaching figure (synthetic).* Cycle-311 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle309_swarm_ch10_w309_10.png)

*Teaching figure (synthetic).* Cycle-309 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle307_swarm_ch10_w307_10.png)

*Teaching figure (synthetic).* Cycle-307 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle305_swarm_ch10_w305_10.png)

*Teaching figure (synthetic).* Cycle-305 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle303_swarm_ch10_w303_10.png)

*Teaching figure (synthetic).* Cycle-303 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle301_swarm_ch10_w301_10.png)

*Teaching figure (synthetic).* Cycle-301 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle299_swarm_ch10_w299_10.png)

*Teaching figure (synthetic).* Cycle-299 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle297_swarm_ch10_w297_10.png)

*Teaching figure (synthetic).* Cycle-297 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle295_swarm_ch10_w295_10.png)

*Teaching figure (synthetic).* Cycle-295 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle293_swarm_ch10_w293_10.png)

*Teaching figure (synthetic).* Cycle-293 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle291_swarm_ch10_w291_10.png)

*Teaching figure (synthetic).* Cycle-291 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle289_swarm_ch10_w289_10.png)

*Teaching figure (synthetic).* Cycle-289 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle287_swarm_ch10_w287_10.png)

*Teaching figure (synthetic).* Cycle-287 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle285_swarm_ch10_w285_10.png)

*Teaching figure (synthetic).* Cycle-285 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle283_swarm_ch10_w283_10.png)

*Teaching figure (synthetic).* Cycle-283 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle281_swarm_ch10_w281_10.png)

*Teaching figure (synthetic).* Cycle-281 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle279_swarm_ch10_w279_10.png)

*Teaching figure (synthetic).* Cycle-279 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle277_swarm_ch10_w277_10.png)

*Teaching figure (synthetic).* Cycle-277 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle275_swarm_ch10_w275_10.png)

*Teaching figure (synthetic).* Cycle-275 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle273_swarm_ch10_w273_10.png)

*Teaching figure (synthetic).* Cycle-273 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle271_swarm_ch10_w271_10.png)

*Teaching figure (synthetic).* Cycle-271 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle269_swarm_ch10_w269_10.png)

*Teaching figure (synthetic).* Cycle-269 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle267_swarm_ch10_w267_10.png)

*Teaching figure (synthetic).* Cycle-267 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle265_swarm_ch10_w265_10.png)

*Teaching figure (synthetic).* Cycle-265 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle263_swarm_ch10_w263_10.png)

*Teaching figure (synthetic).* Cycle-263 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle261_swarm_ch10_w261_10.png)

*Teaching figure (synthetic).* Cycle-261 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle259_swarm_ch10_w259_10.png)

*Teaching figure (synthetic).* Cycle-259 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle257_swarm_ch10_w257_10.png)

*Teaching figure (synthetic).* Cycle-257 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle255_swarm_ch10_w255_10.png)

*Teaching figure (synthetic).* Cycle-255 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle253_swarm_ch10_w253_10.png)

*Teaching figure (synthetic).* Cycle-253 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle251_swarm_ch10_w251_10.png)

*Teaching figure (synthetic).* Cycle-251 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle249_swarm_ch10_w249_10.png)

*Teaching figure (synthetic).* Cycle-249 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle247_swarm_ch10_w247_10.png)

*Teaching figure (synthetic).* Cycle-247 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle245_swarm_ch10_w245_10.png)

*Teaching figure (synthetic).* Cycle-245 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle243_swarm_ch10_w243_10.png)

*Teaching figure (synthetic).* Cycle-243 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle241_swarm_ch10_w241_10.png)

*Teaching figure (synthetic).* Cycle-241 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle239_swarm_ch10_w239_10.png)

*Teaching figure (synthetic).* Cycle-239 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle237_swarm_ch10_w237_10.png)

*Teaching figure (synthetic).* Cycle-237 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle235_swarm_ch10_w235_10.png)

*Teaching figure (synthetic).* Cycle-235 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle233_swarm_ch10_w233_10.png)

*Teaching figure (synthetic).* Cycle-233 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle231_swarm_ch10_w231_10.png)

*Teaching figure (synthetic).* Cycle-231 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle229_swarm_ch10_w229_10.png)

*Teaching figure (synthetic).* Cycle-229 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle227_swarm_ch10_w227_10.png)

*Teaching figure (synthetic).* Cycle-227 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle225_swarm_ch10_w225_10.png)

*Teaching figure (synthetic).* Cycle-225 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle223_swarm_ch10_w223_10.png)

*Teaching figure (synthetic).* Cycle-223 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle221_swarm_ch10_w221_10.png)

*Teaching figure (synthetic).* Cycle-221 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle219_swarm_ch10_w219_10.png)

*Teaching figure (synthetic).* Cycle-219 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle217_swarm_ch10_w217_10.png)

*Teaching figure (synthetic).* Cycle-217 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle215_swarm_ch10_w215_10.png)

*Teaching figure (synthetic).* Cycle-215 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle213_swarm_ch10_w213_10.png)

*Teaching figure (synthetic).* Cycle-213 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle211_swarm_ch10_w211_10.png)

*Teaching figure (synthetic).* Cycle-211 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle209_swarm_ch10_w209_10.png)

*Teaching figure (synthetic).* Cycle-209 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle207_swarm_ch10_w207_10.png)

*Teaching figure (synthetic).* Cycle-207 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle205_swarm_ch10_w205_10.png)

*Teaching figure (synthetic).* Cycle-205 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle203_swarm_ch10_w203_10.png)

*Teaching figure (synthetic).* Cycle-203 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle201_swarm_ch10_w201_10.png)

*Teaching figure (synthetic).* Cycle-201 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle199_swarm_ch10_w199_10.png)

*Teaching figure (synthetic).* Cycle-199 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle197_swarm_ch10_w197_10.png)

*Teaching figure (synthetic).* Cycle-197 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle195_swarm_ch10_w195_10.png)

*Teaching figure (synthetic).* Cycle-195 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle193_swarm_ch10_w193_10.png)

*Teaching figure (synthetic).* Cycle-193 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle191_swarm_ch10_w191_10.png)

*Teaching figure (synthetic).* Cycle-191 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle189_swarm_ch10_w189_10.png)

*Teaching figure (synthetic).* Cycle-189 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle187_swarm_ch10_w187_10.png)

*Teaching figure (synthetic).* Cycle-187 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle185_swarm_ch10_w185_10.png)

*Teaching figure (synthetic).* Cycle-185 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle183_swarm_ch10_w183_10.png)

*Teaching figure (synthetic).* Cycle-183 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle181_swarm_ch10_w181_10.png)

*Teaching figure (synthetic).* Cycle-181 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle179_swarm_ch10_w179_10.png)

*Teaching figure (synthetic).* Cycle-179 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle177_swarm_ch10_w177_10.png)

*Teaching figure (synthetic).* Cycle-177 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle175_swarm_ch10_w175_10.png)

*Teaching figure (synthetic).* Cycle-175 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle173_swarm_ch10_w173_10.png)

*Teaching figure (synthetic).* Cycle-173 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle171_swarm_ch10_w171_10.png)

*Teaching figure (synthetic).* Cycle-171 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle169_swarm_ch10_w169_10.png)

*Teaching figure (synthetic).* Cycle-169 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle167_swarm_ch10_w167_10.png)

*Teaching figure (synthetic).* Cycle-167 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle165_swarm_ch10_w165_10.png)

*Teaching figure (synthetic).* Cycle-165 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle163_swarm_ch10_w163_10.png)

*Teaching figure (synthetic).* Cycle-163 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle161_swarm_ch10_w161_10.png)

*Teaching figure (synthetic).* Cycle-161 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle159_swarm_ch10_w159_10.png)

*Teaching figure (synthetic).* Cycle-159 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle157_swarm_ch10_w157_10.png)

*Teaching figure (synthetic).* Cycle-157 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle155_swarm_ch10_w155_10.png)

*Teaching figure (synthetic).* Cycle-155 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle153_swarm_ch10_w153_10.png)

*Teaching figure (synthetic).* Cycle-153 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle151_swarm_ch10_w151_10.png)

*Teaching figure (synthetic).* Cycle-151 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle149_swarm_ch10_w149_10.png)

*Teaching figure (synthetic).* Cycle-149 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle147_swarm_ch10_w147_10.png)

*Teaching figure (synthetic).* Cycle-147 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle145_swarm_ch10_w145_10.png)

*Teaching figure (synthetic).* Cycle-145 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle143_swarm_ch10_w143_10.png)

*Teaching figure (synthetic).* Cycle-143 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle141_swarm_ch10_w141_10.png)

*Teaching figure (synthetic).* Cycle-141 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle139_swarm_ch10_w139_10.png)

*Teaching figure (synthetic).* Cycle-139 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle137_swarm_ch10_w137_10.png)

*Teaching figure (synthetic).* Cycle-137 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle135_swarm_ch10_w135_10.png)

*Teaching figure (synthetic).* Cycle-135 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle133_swarm_ch10_w133_10.png)

*Teaching figure (synthetic).* Cycle-133 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle131_swarm_ch10_w131_10.png)

*Teaching figure (synthetic).* Cycle-131 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle129_swarm_ch10_w129_10.png)

*Teaching figure (synthetic).* Cycle-129 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle127_swarm_ch10_w127_10.png)

*Teaching figure (synthetic).* Cycle-127 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle125_swarm_ch10_w125_10.png)

*Teaching figure (synthetic).* Cycle-125 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle123_swarm_ch10_w123_10.png)

*Teaching figure (synthetic).* Cycle-123 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle121_swarm_ch10_w121_10.png)

*Teaching figure (synthetic).* Cycle-121 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle119_swarm_ch10_w119_10.png)

*Teaching figure (synthetic).* Cycle-119 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle117_swarm_ch10_w117_10.png)

*Teaching figure (synthetic).* Cycle-117 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle115_swarm_ch10_w115_10.png)

*Teaching figure (synthetic).* Cycle-115 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle113_swarm_ch10_w113_10.png)

*Teaching figure (synthetic).* Cycle-113 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle111_swarm_ch10_w111_10.png)

*Teaching figure (synthetic).* Cycle-111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle109_swarm_ch10_w109_10.png)

*Teaching figure (synthetic).* Cycle-109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle107_swarm_ch10_w107_10.png)

*Teaching figure (synthetic).* Cycle-107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle105_swarm_ch10_w105_10.png)

*Teaching figure (synthetic).* Cycle-105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle103_swarm_ch10_w103_10.png)

*Teaching figure (synthetic).* Cycle-103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle101_swarm_ch10_w101_10.png)

*Teaching figure (synthetic).* Cycle-101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle99_swarm_ch10_w99_10.png)

*Teaching figure (synthetic).* Cycle-99 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle97_swarm_ch10_w97_10.png)

*Teaching figure (synthetic).* Cycle-97 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle95_swarm_ch10_w95_10.png)

*Teaching figure (synthetic).* Cycle-95 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle93_swarm_ch10_w93_10.png)

*Teaching figure (synthetic).* Cycle-93 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle91_swarm_ch10_w91_10.png)

*Teaching figure (synthetic).* Cycle-91 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle89_swarm_ch10_w89_10.png)

*Teaching figure (synthetic).* Cycle-89 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle87_swarm_ch10_w87_10.png)

*Teaching figure (synthetic).* Cycle-87 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle85_swarm_ch10_w85_10.png)

*Teaching figure (synthetic).* Cycle-85 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle83_swarm_ch10_w83_10.png)

*Teaching figure (synthetic).* Cycle-83 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle81_swarm_ch10_w81_10.png)

*Teaching figure (synthetic).* Cycle-81 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle79_swarm_ch10_w79_10.png)

*Teaching figure (synthetic).* Cycle-79 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle77_swarm_ch10_w77_10.png)

*Teaching figure (synthetic).* Cycle-77 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle75_swarm_ch10_w75_10.png)

*Teaching figure (synthetic).* Cycle-75 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle73_swarm_ch10_w73_10.png)

*Teaching figure (synthetic).* Cycle-73 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle71_swarm_ch10_w71_10.png)

*Teaching figure (synthetic).* Cycle-71 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle69_swarm_ch10_w69_10.png)

*Teaching figure (synthetic).* Cycle-69 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle67_swarm_ch10_w67_10.png)

*Teaching figure (synthetic).* Cycle-67 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle65_swarm_ch10_w65_10.png)

*Teaching figure (synthetic).* Cycle-65 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle63_swarm_ch10_w63_10.png)

*Teaching figure (synthetic).* Cycle-63 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle61_swarm_ch10_w61_10.png)

*Teaching figure (synthetic).* Cycle-61 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle59_swarm_ch10_c59j.png)

*Teaching figure (synthetic).* Cycle-59 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle57_swarm_ch10_c57j.png)

*Teaching figure (synthetic).* Cycle-57 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle55_swarm_ch10_sucra_arr.png)

*Teaching figure (synthetic).* Cycle-55 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle53_swarm_ch10_pool_abs.png)

*Teaching figure (synthetic).* Cycle-53 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle51_swarm_ch10_funnel_abs.png)

*Teaching figure (synthetic).* Cycle-51 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle49_swarm_ch10_het_i2.png)

*Teaching figure (synthetic).* Cycle-49 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle47_swarm_ch10_grade_domains.png)

*Teaching figure (synthetic).* Cycle-47 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle45_swarm_ch10_study_spread.png)

*Teaching figure (synthetic).* Cycle-45 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle43_swarm_ch10_nma_rank.png)

*Teaching figure (synthetic).* Cycle-43 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle41_swarm_ch10_grade_abs.png)

*Teaching figure (synthetic).* Cycle-41 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle39_swarm_ch10_funnel.png)

*Teaching figure (synthetic).* Cycle-39 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 10 (original scientific teaching figure).](../assets/figures/cycle37_swarm_ch10_rr_vs_arr.png)

*Teaching figure (synthetic).* Cycle-37 densify scientific residual (ch01–14).


A systematic review is a scientific investigation in its own right, treating the primary literature as its sampled population. The naive assumption that evidence synthesis is an automatic ascent to higher truth is a dangerous fallacy. Pooling does not wash away bias; it frequently concentrates it, laundering flawed primary studies through the perceived impartiality of complex statistics. A meta-analysis of systematically biased trials yields a highly precise summary of a distorted literature. When clinical practice guidelines uncritically cite that meta-analysis, they industrialize the distortion, embedding it into pathway defaults and electronic health record order sets. Stroke neurology is an intensely guideline-driven specialty—governing decisions such as intravenous thrombolysis windows, blood pressure targets following intracerebral hemorrhage, secondary prevention antithrombotics, and the timing of carotid revascularization. Consequently, the appraisal of evidence synthesis products is a fundamental clinical skill, not an abstract exercise for methodologists or medical librarians.

The synthesis architecture begins with a rigorously defined question. A review asking 'What is the best treatment for acute ischemic stroke?' is unfocused and methodologically bankrupt. Rigorous reviews utilize the PICO framework: Population, Intervention, Comparator, and Outcomes (or PECO for Exposures). For prognostic models, the framework shifts to Population, Index prognostic factor, Outcomes, and Horizon. The exact boundaries of the PICO formulation dictate the scientific validity of the pooling. If a meta-analysis merges trials of early-generation intra-arterial urokinase with modern stent-retriever mechanical thrombectomy under the single umbrella of 'reperfusion therapy,' the resulting pooled effect size is a meaningless chimera. Scope decisions are foundational scientific decisions.

Beyond the question lies the sampling frame. The search strategy must be exhaustive. A literature search restricted to PubMed and English-language publications guarantees selection bias. High-quality systematic reviews scour multiple databases (Embase, Cochrane Central), trial registries (ClinicalTrials.gov), and gray literature to counter publication bias—the phenomenon where small, neutral, or negative trials vanish into the proverbial file drawer. If a meta-analysis relies exclusively on published literature, it models a highly curated, overly optimistic version of reality. Evidence synthesis is thus entirely dependent on the integrity of its search and extraction processes, necessitating dual independent screening to prevent subjective exclusion.

Finally, meta-analysis—the statistical aggregation of quantitative results—is strictly an optional extension of a systematic review. Not all systematically retrieved evidence should be mathematically pooled. When the included studies exhibit severe clinical heterogeneity, featuring completely divergent populations or measuring functionally different outcomes, calculating a single summary statistic is a methodological failure. In such instances, a structured narrative synthesis mapping the direction of effects is scientifically superior to an irresponsible, mathematically invalid pooled diamond.

## Named Frameworks and Checklists for Synthesis and Guidelines

The infrastructure of evidence synthesis relies on established reporting guidelines and methodological frameworks. PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) governs the reporting of the review itself, ensuring transparent documentation of the search strategy, screening process, and data extraction. MOOSE (Meta-analysis of Observational Studies in Epidemiology) provides a similar scaffolding for non-randomized data. These are reporting checklists; they do not guarantee scientific validity, only transparency. A PRISMA-compliant meta-analysis can still be fundamentally flawed if the underlying studies are confounded.

For assessing the primary studies, the Cochrane Risk of Bias tool (RoB 2) is the standard for randomized trials. It forces reviewers to evaluate the randomization process, deviations from intended interventions, missing outcome data, measurement of the outcome, and selection of the reported result. ROBINS-I (Risk Of Bias In Non-randomized Studies - of Interventions) serves the equivalent role for observational data, explicitly evaluating confounding, selection bias, information bias, and reporting bias against a hypothetical 'target trial' ideal. Crucially, applying these tools requires domain expertise; evaluating confounding in a stroke registry requires knowing that baseline NIHSS, age, and time-to-presentation are critical, non-negotiable confounders.

AMSTAR 2 (A MeaSurement Tool to Assess systematic Reviews) serves as a validated appraisal instrument for evaluating the methodological quality of the systematic review itself. It penalizes reviews that fail to pre-register their protocols on platforms like PROSPERO, fail to justify the selection of study designs, or neglect to integrate risk of bias into the interpretation of the pooled results.

At the apex of the synthesis pyramid lies GRADE (Grading of Recommendations Assessment, Development and Evaluation). GRADE separates the certainty of evidence from the strength of recommendation. Certainty begins as 'High' for RCTs and 'Low' for observational studies, subsequently rated down for risk of bias, inconsistency, indirectness, imprecision, or publication bias, and occasionally rated up for massive magnitudes of effect or dose-response gradients. Finally, AGREE II (Appraisal of Guidelines for Research & Evaluation) provides a framework for evaluating the methodological rigor and transparency of the clinical practice guidelines that emerge from the GRADE process.

## Quantitative Reasoning: The Mathematics of Meta-Analysis

A meta-analysis is fundamentally a weighted average of study estimates. If we define the effect estimate of study i as Y_i and its standard error as SE_i, mathematical logic dictates that the most precise studies (those with the smallest variance) should contribute the most information to the pool. In the fixed-effect (or common-effect) model, the inverse-variance weight is defined as w_i = 1 / (SE_i^2). The pooled effect estimate is the sum of the weighted effects divided by the sum of the weights: Pool = Sum(w_i * Y_i) / Sum(w_i). The variance of this pooled estimate is exactly 1 / Sum(w_i), allowing direct calculation of standard errors, z-scores, and confidence intervals.

The fixed-effect model operates under the strict epistemological assumption that every included study is estimating the exact same true underlying parameter (mu). In this paradigm, the only reason Study A and Study B report differing effect sizes is random sampling error. However, biology and trial execution are rarely this uniform. Clinical heterogeneity inevitably introduces statistical heterogeneity.

Cochran's Q statistic tests the null hypothesis that all studies share a single true effect. It is calculated as the sum of squared deviations of each study's estimate from the pooled estimate, weighted by w_i: Q = Sum(w_i * (Y_i - Pool)^2). Because Q is acutely sensitive to the number of studies (degrees of freedom, df), the I-squared metric is deployed to provide a percentage representation of the variance attributable to heterogeneity rather than sampling error: I^2 = max(0, (Q - df)/Q) * 100%. The absolute between-study variance, quantified in the units of the effect measure, is denoted by the parameter tau-squared (tau^2). When tau-squared is greater than zero, random-effects models incorporate it into the fundamental weighting architecture.

In a random-effects model (frequently using the DerSimonian-Laird or Restricted Maximum Likelihood estimators), the weight is modified to w_i* = 1 / (SE_i^2 + tau^2). This mathematically subtle adjustment triggers massive clinical consequences. As between-study variance (tau-squared) grows large, the denominator for all studies becomes dominated by tau-squared rather than the study's internal precision (SE_i^2). Consequently, the weights converge toward equality. A small, biased, single-center trial of 50 patients will forcibly command nearly the same analytical weight as a rigorous, multicenter mega-trial of 5,000 patients. This structural vulnerability dictates that random-effects pooling must be approached with extreme caution, particularly when the included studies vary heavily in methodological quality.

![Fixed-effect weights favor precise mega-trials; random-effects (τ² > 0) equalizes weights and inflates small-trial influence (original teaching figure).](../assets/figures/cycle4_swarm_ch10_fe_re_weights.png)

*Teaching figure (synthetic).* When τ² enters the denominator, relative weights shift away from the mega-trial toward noisy small studies. Always convert any pooled RR into local ARR/NNT; meta-regression subgroups remain observational (prediction ≠ causation).

![Study ARRs with pooled mean CI versus a wider prediction interval for the next study; if the PI includes 0, guideline action must stay conditional (original teaching figure).](../assets/figures/cycle8_swarm_ch10_pred_interval_arr.png)

*Teaching figure (synthetic).* A tight mean CI can coexist with a prediction interval that still includes null or harm. Transport absolute effects with heterogeneity honesty—not only the pooled point.

![Relative RR forest looks homogeneous while absolute ARR forest ranks high-risk populations first (original teaching figure).](../assets/figures/cycle15_swarm_ch10_forest_abs_rd.png)

*Teaching figure (synthetic).* Pool and report absolute RD/NNT for decision transport—not RR alone.

## Fully Worked Example: Pooling Dual Antiplatelet Therapy in Minor Stroke

Scenario: You are evaluating a meta-analysis of dual antiplatelet therapy (DAPT) versus aspirin monotherapy for the prevention of recurrent stroke within 90 days following a high-risk TIA or minor acute ischemic stroke. Two major randomized controlled trials dominate the literature. You will compute the fixed-effect pooled risk ratio (RR), construct the 95% confidence interval, and critically convert the relative effect into absolute clinical metrics (ARR and NNT) based on baseline risk.

```
Study 1 (e.g., Asian population):
  DAPT: 200 recurrent strokes / 2500 patients -> Risk_tx = 0.080
  Aspirin: 300 recurrent strokes / 2500 patients -> Risk_ct = 0.120
  Relative Risk (RR_1) = 0.080 / 0.120 = 0.6667
  Natural Log RR (ln_RR_1) = ln(0.6667) = -0.4055
  SE_1^2 = 1/200 - 1/2500 + 1/300 - 1/2500 = 0.007533
  SE_1 = sqrt(0.007533) = 0.0868
  Weight (w_1) = 1 / SE_1^2 = 132.74

Study 2 (e.g., International population):
  DAPT: 120 recurrent strokes / 2000 patients -> Risk_tx = 0.060
  Aspirin: 160 recurrent strokes / 2000 patients -> Risk_ct = 0.080
  Relative Risk (RR_2) = 0.060 / 0.080 = 0.7500
  Natural Log RR (ln_RR_2) = ln(0.7500) = -0.2877
  SE_2^2 = 1/120 - 1/2000 + 1/160 - 1/2000 = 0.013583
  SE_2 = sqrt(0.013583) = 0.1165
  Weight (w_2) = 1 / SE_2^2 = 73.62
```

We synthesize the independent studies utilizing inverse-variance weighting for a fixed-effect model. The total weight is Sum(w) = 132.74 + 73.62 = 206.36. The weighted sum of the effect estimates is Sum(w * ln_RR) = (132.74 * -0.4055) + (73.62 * -0.2877) = -53.82 - 21.18 = -75.00. The pooled natural log relative risk is -75.00 / 206.36 = -0.3634. The variance of this pooled estimate is 1 / Sum(w) = 0.004846. The standard error is sqrt(0.004846) = 0.0696.

To construct the 95% confidence interval (CI) on the natural logarithmic scale, multiply the standard error by 1.96. The margin of error is 1.96 * 0.0696 = 0.1364. Thus, the 95% CI for pooled ln(RR) is -0.3634 +/- 0.1364, or approximately [-0.4998, -0.2270]. Exponentiating returns the clinical relative-risk scale: pooled RR = exp(-0.3634) = 0.695, with 95% CI [exp(-0.4998), exp(-0.2270)] ≈ [0.607, 0.797]. The meta-analysis demonstrates a statistically significant ~30.5% relative risk reduction in recurrent stroke with DAPT.

Relative estimates satisfy statistical requirements, but clinical action demands absolute effects. Suppose baseline risk (Control Event Rate, CER) is 10%. Using pooled RR 0.695, ARR = CER * (1 - RR) = 0.10 * 0.305 = 0.0305 (3.05%). NNT = 1 / ARR ≈ 32.8, rounding to 33. If CER is only 4%, ARR compresses to 0.0122 (1.22%) and NNT rises to about 82. This translation prevents the illusion that one RR applies symmetrically across all baseline-risk strata.

*(Intermediates recomputed from event counts with consistent rounding; verified by `scripts/verify_math_examples.py`.)*

## Guidelines, GRADE, and the Translation of Evidence

![GRADE certainty ladder translated into absolute-effect language from high ARR confidence to very-low unknown absolute effect (original teaching figure).](../assets/figures/cycle12_swarm_ch10_grade_abs.png)

*Teaching figure (synthetic).* Guideline certainty is about absolute patient outcomes—not adjective strength alone. Low certainty means do not rewrite pathways on a fragile ARR.


Clinical practice guidelines exist to bridge the gap between abstract evidence synthesis and concrete clinical action. However, the prestige of the issuing society (e.g., AHA/ASA, ESO) does not automatically guarantee methodological rigor. Trustworthy guidelines are formulated using transparent frameworks such as GRADE, which systematically divorces the evaluation of evidence certainty from the formulation of recommendation strength. The certainty of evidence reflects a purely epistemological judgment: how confident are we that the true effect lies reasonably close to the pooled estimate? GRADE mandates that randomized controlled trials start at 'High' certainty, while observational studies originate at 'Low'. These baseline ratings are then aggressively modified based on identified systemic flaws.

Reviewers rate down certainty for five primary reasons. Risk of bias targets systemic flaws in trial execution (e.g., unblinded assessment of modified Rankin Scale scores). Inconsistency isolates unexplained, severe heterogeneity in effect directions across studies. Indirectness penalizes extrapolation, such as applying evidence from mild strokes to severe strokes, or substituting surrogate endpoints (TICI scores) in place of functional outcomes. Imprecision triggers a downgrade when the confidence interval is so wide that it crosses clinical decision thresholds, failing to definitively rule out harm or lack of benefit. Finally, publication bias demands a downgrade when asymmetric funnel plots or missing registry data suggest selective reporting. Conversely, observational data can be rated up in rare instances if the magnitude of the causal effect is overwhelming and robust against unmeasured confounding, such as the initial observational proof for mechanical thrombectomy.

Once certainty is securely established, the panel determines the strength of the recommendation: typically 'Strong' or 'Weak' (often termed 'Conditional'). This step is inherently subjective, incorporating resource allocation, patient values, and the balance of absolute benefits to harms. A strong recommendation signifies that the overwhelming majority of fully informed patients would choose the intervention, allowing clinicians to deploy it as a standard default. A weak or conditional recommendation implies that patient values and baseline risks dictate variation; the intervention is appropriate for some but not all. A premier failure mode in evidence-based medicine is treating a weak recommendation as a draconian legal mandate. Weak recommendations are explicit, intentional invitations for shared decision-making.

## Pitfalls and Failure Modes in Evidence Synthesis

![Publication bias funnel residual: small-study asymmetry inflates published absolute ARR vs large-trial truth (original teaching figure).](../assets/figures/cycle18_swarm_ch10_funnel_abs.png)

*Teaching figure (synthetic).* Correct absolute RD/NNT for small-study bias before guideline strength talk.

- Garbage In, Garbage Out (GIGO): Pooling fundamentally confounded observational data yields a highly precise, statistically significant, but causally false estimate. The synthesis flawlessly inherits the flawed causal structure of its worst inputs.
- The Ecological Fallacy in Meta-Regression: Regressing trial-level summary statistics (like average age or median time-to-treatment) against effect sizes. Study-level relationships consistently fail to mirror patient-level biology. Prediction at the group level strictly does not equal causation at the individual level.
- The Random-Effects Paradox: Automatically shifting to a random-effects model when statistical heterogeneity (I-squared) breaches an arbitrary threshold. This mathematically penalizes massive, precise mega-trials and artificially inflates the influence of small, noisy, single-center studies highly susceptible to publication bias.
- Uncritical Worship of I-Squared: Treating I-squared as an absolute diagnostic metric of clinical incompatibility. I-squared is a ratio of variance. A massive I-squared can emerge purely because the included mega-trials have negligible sampling error, even if their point estimates are clinically indistinguishable.
- Surrogate Endpoint Substitution: Pooling radiographic or biomarker outcomes (e.g., recanalization rates, hematoma expansion, aneurysm occlusion) and directly mapping those synthetic benefits to clinical disability recommendations without validating the specific causal pathway.
- Outcome Switching and Protocol Drift: Failing to contrast the published meta-analysis primary outcome against its PROSPERO registry protocol. Synthesis authors frequently and covertly shift endpoints post-hoc to secure a statistically significant narrative.
- Disconnected Clinical Implementation: Recommending population-wide clinical interventions based solely on a pooled Relative Risk, entirely ignoring that the Absolute Risk Reduction (and accompanying NNT) diminishes radically in lower-risk baseline patient phenotypes.
- Conflating Significance with Importance: Achieving p < 0.001 in a meta-analysis of 100,000 patients merely proves the effect is not exactly zero. An Odds Ratio of 0.98 may be highly statistically significant but remains clinically microscopic and entirely irrelevant.
- File Drawer Annihilation: Assuming the visible, published literature is the complete scientific literature. Without rigorously examining trial registries for unpublished null results, the meta-analysis represents a heavily filtered, commercially optimistic reality.
- Prediction Conflated with Causation: Assuming that a subgroup effect identified purely through meta-regression represents a causal biological interaction. Subgroups in meta-analyses are strictly observational, predictive patterns heavily subjected to extreme, unmeasured confounding.

## Clinical and Epidemiologic Notes

Clinical Note: Navigating Subgroup Creep in Acute Stroke. Stroke trials frequently report neutral primary outcomes but showcase statistically significant benefits in post-hoc subgroups (e.g., specific time windows or highly selected advanced imaging profiles). When meta-analyses pool these specific, opportunistic subgroups across multiple negative trials, the resulting diamond is a statistical illusion. Trace the subgroup to its origin: was it pre-specified and stratified at randomization in the primary trials? If not, the pooled estimate is observational and highly susceptible to selection bias, barring strong guideline recommendations without confirmatory testing.

Epidemiologic Note: Individual Patient Data (IPD) vs Aggregate Meta-Analysis. The absolute gold standard of synthesis is the IPD meta-analysis, epitomized by the HERMES collaboration in endovascular thrombectomy. By acquiring raw, patient-level data, methodologists rigorously adjust for baseline confounders uniformly across all trials and execute genuine, properly powered interaction tests for causal effect modifiers (e.g., collateral status, precise time-to-puncture). Aggregate data meta-analyses are trapped using study-level averages, severely crippling any causal claims about patient-level covariates.

Clinical Note: Interpreting Non-Inferiority Meta-Analyses. Pooling non-inferiority trials (such as those comparing direct oral anticoagulants to warfarin) demands extraordinary methodological discipline. The pooled confidence interval must completely exclude the pre-specified, clinically justified non-inferiority margin. Crucially, high heterogeneity in a non-inferiority meta-analysis is lethal. If studies vary wildly in their execution quality, the resulting 'noise' forcefully pushes the relative risk toward the null (1.0), artificially creating the appearance of equivalence. Poor trial quality heavily biases non-inferiority meta-analyses toward success.

Epidemiologic Note: The Causal Failure of Observational Synthesis. Synthesizing observational cohort studies regarding stroke prognosis or treatment effectiveness is an exercise in precision engineering of a biased estimate. If fifteen cohort studies fail to properly adjust for prestroke frailty, their meta-analysis will confidently report a spurious association with an incredibly narrow confidence interval. Prediction does not transform into causation simply because the sample size scales. A massive dataset of confounded observations remains fundamentally confounded.

Clinical Note: Local Pathway Implementation vs Global Guidelines. Guidelines are engineered for average populations under standard conditions. Your institutional stroke pathway must tightly integrate guideline recommendations with local resource constraints, patient demographics, and operational feasibility. Implementing a 'Strong' recommendation for rapid carotid endarterectomy within 48 hours requires surgical availability and advanced imaging triage that may not exist locally. Appraising synthesis dictates asking not just 'does this work?' but 'does this work safely within my specific clinical ecosystem?'

## Cross-Links to Other Chapters

- Chapter 2: Causal Inference and DAGs — Essential for understanding why observational meta-analyses inherit the exact confounding structure of their constituent studies. Pooling does not create exchangeability.
- Chapter 5: Bias and Confounding — Provides the foundational architecture for understanding the specific causal domains assessed by the RoB 2 and ROBINS-I checklists.
- Chapter 6: Trial Design — Explains the mechanical requirements of randomization and allocation concealment that protect studies from bias, dictating their analytical weight in rigorous syntheses.
- Chapter 8: Observational Studies — Details the inherent limitations of cohort and case-control studies, demonstrating why synthesizing them requires immense caution regarding unmeasured confounding.
- Chapter 11: Diagnostic Accuracy — Extends the principles of evidence synthesis to bivariate meta-analyses of sensitivity and specificity for advanced neuroimaging modalities.


![fig58_composite_endpoint.png original teaching graphic](../assets/figures/fig58_composite_endpoint.png)

*Original teaching graphic (fig58_composite_endpoint.png).*

## Chapter summary

Evidence synthesis is a disciplined, scientific process demanding rigorous methodology, not a mechanical exercise in aggregating data to achieve statistical significance. Systematic reviews require precise PICO formulation, exhaustive search strategies to combat publication bias, and unapologetic critical appraisal using frameworks like RoB 2. Meta-analysis, while mathematically powerful, is strictly optional and frequently dangerous if misapplied. Fixed-effect models assume a singular underlying truth, weighting heavily toward precise mega-trials, whereas random-effects models accommodate variance but paradoxically inflate the influence of small, noisy studies. Clinical interpretation mandates translating relative metrics (RR, OR) into absolute effects (ARR, NNT) securely anchored to specific patient baseline risks. Furthermore, clinical practice guidelines must be interrogated through the GRADE framework to surgically separate the epistemological certainty of evidence from the value-driven strength of clinical recommendations. Ultimately, pooling data never resolves fundamental flaws in causal inference; a meta-analysis of confounded studies perfectly predicts a causal illusion. Rigorous appraisal of synthesis is the final defense mechanism preventing flawed science from becoming institutionalized medical dogma.

## Practice and reflection

1. 1. Construct a highly specific PICO question for an intervention you frequently prescribe in neurology (e.g., patent foramen ovale closure for cryptogenic stroke). How would altering the 'Population' criteria from 'any PFO' to 'high-risk PFO' fundamentally change the resulting meta-analysis?
2. 2. Retrieve the forest plot from a major recent stroke meta-analysis. Deliberately ignore the summary diamond at the bottom. What do the individual study point estimates and confidence intervals independently communicate about between-study heterogeneity?
3. 3. Using the standard error formula for a log relative risk, prove mathematically why an adequately powered, massive randomized trial dominates the weighting scheme of a fixed-effect meta-analysis.
4. 4. Explain the Random-Effects Paradox to a junior resident. Why does the introduction of tau-squared into the weighting denominator artificially inflate the influence of small, potentially biased studies?
5. 5. You are presented with a meta-analysis showing an odds ratio of 0.85 (p=0.04) for a novel neuroprotectant. Assume your patient has a baseline risk of 5% for the primary outcome. Calculate the Absolute Risk Reduction (ARR) and Number Needed to Treat (NNT). Is the intervention clinically meaningful?
6. 6. Examine the Cochrane Risk of Bias 2 (RoB 2) tool. Differentiate between 'deviations from intended interventions' and 'missing outcome data'. How do these flaws uniquely corrupt acute stroke trials?
7. 7. A meta-analysis of ten observational registries concludes that delayed initiation of oral anticoagulants after ischemic stroke causes higher rates of hemorrhagic transformation. Apply the principle of 'Prediction != Causation' to deconstruct this claim. What unmeasured confounders likely drive this association?
8. 8. Review a recent guideline from the AHA/ASA or ESO. Locate a 'Strong' recommendation based on 'Moderate' or 'Low' certainty evidence. Justify how the guideline panel reached this conclusion, focusing on values, preferences, and the risk/benefit asymmetry.
9. 9. Analyze the concept of the Ecological Fallacy in meta-regression. If a meta-analysis plots average trial age against the trial effect size and finds a positive correlation, why is it mathematically invalid to assume that older individual patients experience a greater treatment effect?
10. 10. Defend the argument that a comprehensive systematic review without a meta-analysis (a narrative synthesis) is often scientifically superior to a meta-analysis that irresponsibly pools clinically incompatible studies.

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


![fig90_bayes_update.png original teaching graphic](../assets/figures/fig90_bayes_update.png)

*Original teaching graphic (fig90_bayes_update.png).*
