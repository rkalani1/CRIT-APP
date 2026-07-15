# Chapter 27. Missing Data, Multiplicity, Interim Analyses, and Fragility

## Opening

![Missingness mechanisms (original).](../assets/figures/fig44_missingness_mechs.png)

*Missingness mechanisms (original).*

![Fragility and missingness (original).](../assets/figures/fig17_fragility_missing.png)

*Fragility and missingness (original).*

![Fragility and missingness mechanisms (original).](../assets/figures/swarm_ch27_fragility_missing.png)

*Fragility and missingness mechanisms (original).*

Interim looks early and the primary endpoint is fragile. Ask missingness, multiplicity, and what would reverse the conclusion with a few events.


## Learning objectives

- Classify missing data mechanisms (MCAR, MAR, MNAR) and map their implications onto neurologic follow-up.
- Critique last observation carried forward (LOCF) and complete-case analysis as analytically hazardous in acute stroke trials.
- Appraise statistical multiplicity—ranging from unadjusted secondary endpoint sweeps to hidden subgroup analyses.
- Interpret interim analyses and the distinct biases introduced by early stopping for benefit versus early stopping for futility or harm.
- Deploy the fragility index and related heuristics to stress-test the robustness of dichotomous endpoints in modest-sized stroke trials.
- Identify analytic flexibility and the consequent 'spin' that frames post hoc data exploration as confirmatory evidence.
- Construct a rigorous journal-club framework to systematically interrogate trial plumbing before advocating practice changes.

![Fragility residual: p less than 0.05 with thin absolute margins remains fragile (original scientific teaching figure).](../assets/figures/cycle26_swarm_ch27_fragility_surface.png)

*Teaching figure (synthetic).* Cycle-26 densify scientific residual.

![Missing-data residual: MNAR can dominate absolute effect estimates (original scientific teaching figure).](../assets/figures/cycle28_swarm_ch27_missingness_bias.png)

*Teaching figure (synthetic).* Cycle-28 densify scientific residual.

![Multiplicity inflates false absolute ARR wins (original scientific teaching figure).](../assets/figures/cycle30_swarm_ch27_fwer.png)

*Teaching figure (synthetic).* Cycle-30 densify scientific residual.

![Early stopping can lock inflated absolute effects (original scientific teaching figure).](../assets/figures/cycle32_swarm_ch27_interim_arr.png)

*Teaching figure (synthetic).* Cycle-32 densify scientific residual.

![Alpha spending raises n needed for absolute ARR (original scientific teaching figure).](../assets/figures/cycle34_swarm_ch27_alpha_n.png)

*Teaching figure (synthetic).* Cycle-34 densify scientific residual.

![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle36_swarm_ch27_mnar.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## The Plumbing of Trial Analysis: Why Significance Often Crumbles

![Thin absolute margins despite p-significance residual (original teaching figure).](../assets/figures/cycle24_swarm_ch27_thin_margin.png)

*Teaching figure (synthetic).* FI/FQ before lock-in.

![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle38_swarm_ch27_fragility.png)

*Teaching figure (synthetic).* Cycle-38 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle40_swarm_ch27_missing_bound.png)

*Teaching figure (synthetic).* Cycle-40 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle42_swarm_ch27_alpha_spend.png)

*Teaching figure (synthetic).* Cycle-42 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle44_swarm_ch27_tipping.png)

*Teaching figure (synthetic).* Cycle-44 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle536_swarm_ch27_w536_13.png)

*Teaching figure (synthetic).* Cycle-536 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle534_swarm_ch27_w534_13.png)

*Teaching figure (synthetic).* Cycle-534 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle532_swarm_ch27_w532_13.png)

*Teaching figure (synthetic).* Cycle-532 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle530_swarm_ch27_w530_13.png)

*Teaching figure (synthetic).* Cycle-530 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle528_swarm_ch27_w528_13.png)

*Teaching figure (synthetic).* Cycle-528 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle526_swarm_ch27_w526_13.png)

*Teaching figure (synthetic).* Cycle-526 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle524_swarm_ch27_w524_13.png)

*Teaching figure (synthetic).* Cycle-524 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle522_swarm_ch27_w522_13.png)

*Teaching figure (synthetic).* Cycle-522 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle520_swarm_ch27_w520_13.png)

*Teaching figure (synthetic).* Cycle-520 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle518_swarm_ch27_w518_13.png)

*Teaching figure (synthetic).* Cycle-518 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle516_swarm_ch27_w516_13.png)

*Teaching figure (synthetic).* Cycle-516 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle514_swarm_ch27_w514_13.png)

*Teaching figure (synthetic).* Cycle-514 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle512_swarm_ch27_w512_13.png)

*Teaching figure (synthetic).* Cycle-512 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle510_swarm_ch27_w510_13.png)

*Teaching figure (synthetic).* Cycle-510 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle508_swarm_ch27_w508_13.png)

*Teaching figure (synthetic).* Cycle-508 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle506_swarm_ch27_w506_13.png)

*Teaching figure (synthetic).* Cycle-506 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle504_swarm_ch27_w504_13.png)

*Teaching figure (synthetic).* Cycle-504 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle502_swarm_ch27_w502_13.png)

*Teaching figure (synthetic).* Cycle-502 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle500_swarm_ch27_w500_13.png)

*Teaching figure (synthetic).* Cycle-500 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle498_swarm_ch27_w498_13.png)

*Teaching figure (synthetic).* Cycle-498 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle496_swarm_ch27_w496_13.png)

*Teaching figure (synthetic).* Cycle-496 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle494_swarm_ch27_w494_13.png)

*Teaching figure (synthetic).* Cycle-494 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle492_swarm_ch27_w492_13.png)

*Teaching figure (synthetic).* Cycle-492 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle490_swarm_ch27_w490_13.png)

*Teaching figure (synthetic).* Cycle-490 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle488_swarm_ch27_w488_13.png)

*Teaching figure (synthetic).* Cycle-488 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle486_swarm_ch27_w486_13.png)

*Teaching figure (synthetic).* Cycle-486 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle484_swarm_ch27_w484_13.png)

*Teaching figure (synthetic).* Cycle-484 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle482_swarm_ch27_w482_13.png)

*Teaching figure (synthetic).* Cycle-482 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle480_swarm_ch27_w480_13.png)

*Teaching figure (synthetic).* Cycle-480 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle478_swarm_ch27_w478_13.png)

*Teaching figure (synthetic).* Cycle-478 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle476_swarm_ch27_w476_13.png)

*Teaching figure (synthetic).* Cycle-476 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle474_swarm_ch27_w474_13.png)

*Teaching figure (synthetic).* Cycle-474 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle472_swarm_ch27_w472_13.png)

*Teaching figure (synthetic).* Cycle-472 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle470_swarm_ch27_w470_13.png)

*Teaching figure (synthetic).* Cycle-470 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle468_swarm_ch27_w468_13.png)

*Teaching figure (synthetic).* Cycle-468 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle466_swarm_ch27_w466_13.png)

*Teaching figure (synthetic).* Cycle-466 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle464_swarm_ch27_w464_13.png)

*Teaching figure (synthetic).* Cycle-464 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle462_swarm_ch27_w462_13.png)

*Teaching figure (synthetic).* Cycle-462 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle460_swarm_ch27_w460_13.png)

*Teaching figure (synthetic).* Cycle-460 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle458_swarm_ch27_w458_13.png)

*Teaching figure (synthetic).* Cycle-458 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle456_swarm_ch27_w456_13.png)

*Teaching figure (synthetic).* Cycle-456 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle454_swarm_ch27_w454_13.png)

*Teaching figure (synthetic).* Cycle-454 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle452_swarm_ch27_w452_13.png)

*Teaching figure (synthetic).* Cycle-452 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle450_swarm_ch27_w450_13.png)

*Teaching figure (synthetic).* Cycle-450 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle448_swarm_ch27_w448_13.png)

*Teaching figure (synthetic).* Cycle-448 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle446_swarm_ch27_w446_13.png)

*Teaching figure (synthetic).* Cycle-446 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle444_swarm_ch27_w444_13.png)

*Teaching figure (synthetic).* Cycle-444 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle442_swarm_ch27_w442_13.png)

*Teaching figure (synthetic).* Cycle-442 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle440_swarm_ch27_w440_13.png)

*Teaching figure (synthetic).* Cycle-440 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle438_swarm_ch27_w438_13.png)

*Teaching figure (synthetic).* Cycle-438 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle436_swarm_ch27_w436_13.png)

*Teaching figure (synthetic).* Cycle-436 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle434_swarm_ch27_w434_13.png)

*Teaching figure (synthetic).* Cycle-434 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle432_swarm_ch27_w432_13.png)

*Teaching figure (synthetic).* Cycle-432 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle430_swarm_ch27_w430_13.png)

*Teaching figure (synthetic).* Cycle-430 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle428_swarm_ch27_w428_13.png)

*Teaching figure (synthetic).* Cycle-428 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle426_swarm_ch27_w426_13.png)

*Teaching figure (synthetic).* Cycle-426 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle424_swarm_ch27_w424_13.png)

*Teaching figure (synthetic).* Cycle-424 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle422_swarm_ch27_w422_13.png)

*Teaching figure (synthetic).* Cycle-422 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle420_swarm_ch27_w420_13.png)

*Teaching figure (synthetic).* Cycle-420 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle418_swarm_ch27_w418_13.png)

*Teaching figure (synthetic).* Cycle-418 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle416_swarm_ch27_w416_13.png)

*Teaching figure (synthetic).* Cycle-416 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle414_swarm_ch27_w414_13.png)

*Teaching figure (synthetic).* Cycle-414 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle412_swarm_ch27_w412_13.png)

*Teaching figure (synthetic).* Cycle-412 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle410_swarm_ch27_w410_13.png)

*Teaching figure (synthetic).* Cycle-410 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle408_swarm_ch27_w408_13.png)

*Teaching figure (synthetic).* Cycle-408 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle406_swarm_ch27_w406_13.png)

*Teaching figure (synthetic).* Cycle-406 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle404_swarm_ch27_w404_13.png)

*Teaching figure (synthetic).* Cycle-404 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle402_swarm_ch27_w402_13.png)

*Teaching figure (synthetic).* Cycle-402 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle400_swarm_ch27_w400_13.png)

*Teaching figure (synthetic).* Cycle-400 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle398_swarm_ch27_w398_13.png)

*Teaching figure (synthetic).* Cycle-398 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle396_swarm_ch27_w396_13.png)

*Teaching figure (synthetic).* Cycle-396 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle394_swarm_ch27_w394_13.png)

*Teaching figure (synthetic).* Cycle-394 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle392_swarm_ch27_w392_13.png)

*Teaching figure (synthetic).* Cycle-392 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle390_swarm_ch27_w390_13.png)

*Teaching figure (synthetic).* Cycle-390 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle388_swarm_ch27_w388_13.png)

*Teaching figure (synthetic).* Cycle-388 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle386_swarm_ch27_w386_13.png)

*Teaching figure (synthetic).* Cycle-386 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle384_swarm_ch27_w384_13.png)

*Teaching figure (synthetic).* Cycle-384 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle382_swarm_ch27_w382_13.png)

*Teaching figure (synthetic).* Cycle-382 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle380_swarm_ch27_w380_13.png)

*Teaching figure (synthetic).* Cycle-380 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle378_swarm_ch27_w378_13.png)

*Teaching figure (synthetic).* Cycle-378 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle376_swarm_ch27_w376_13.png)

*Teaching figure (synthetic).* Cycle-376 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle374_swarm_ch27_w374_13.png)

*Teaching figure (synthetic).* Cycle-374 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle372_swarm_ch27_w372_13.png)

*Teaching figure (synthetic).* Cycle-372 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle370_swarm_ch27_w370_13.png)

*Teaching figure (synthetic).* Cycle-370 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle368_swarm_ch27_w368_13.png)

*Teaching figure (synthetic).* Cycle-368 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle366_swarm_ch27_w366_13.png)

*Teaching figure (synthetic).* Cycle-366 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle364_swarm_ch27_w364_13.png)

*Teaching figure (synthetic).* Cycle-364 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle362_swarm_ch27_w362_13.png)

*Teaching figure (synthetic).* Cycle-362 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle360_swarm_ch27_w360_13.png)

*Teaching figure (synthetic).* Cycle-360 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle358_swarm_ch27_w358_13.png)

*Teaching figure (synthetic).* Cycle-358 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle356_swarm_ch27_w356_13.png)

*Teaching figure (synthetic).* Cycle-356 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle354_swarm_ch27_w354_13.png)

*Teaching figure (synthetic).* Cycle-354 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle352_swarm_ch27_w352_13.png)

*Teaching figure (synthetic).* Cycle-352 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle350_swarm_ch27_w350_13.png)

*Teaching figure (synthetic).* Cycle-350 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle348_swarm_ch27_w348_13.png)

*Teaching figure (synthetic).* Cycle-348 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle346_swarm_ch27_w346_13.png)

*Teaching figure (synthetic).* Cycle-346 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle344_swarm_ch27_w344_13.png)

*Teaching figure (synthetic).* Cycle-344 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle342_swarm_ch27_w342_13.png)

*Teaching figure (synthetic).* Cycle-342 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle340_swarm_ch27_w340_13.png)

*Teaching figure (synthetic).* Cycle-340 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle338_swarm_ch27_w338_13.png)

*Teaching figure (synthetic).* Cycle-338 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle336_swarm_ch27_w336_13.png)

*Teaching figure (synthetic).* Cycle-336 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle334_swarm_ch27_w334_13.png)

*Teaching figure (synthetic).* Cycle-334 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle332_swarm_ch27_w332_13.png)

*Teaching figure (synthetic).* Cycle-332 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle330_swarm_ch27_w330_13.png)

*Teaching figure (synthetic).* Cycle-330 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle328_swarm_ch27_w328_13.png)

*Teaching figure (synthetic).* Cycle-328 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle326_swarm_ch27_w326_13.png)

*Teaching figure (synthetic).* Cycle-326 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle324_swarm_ch27_w324_13.png)

*Teaching figure (synthetic).* Cycle-324 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle322_swarm_ch27_w322_13.png)

*Teaching figure (synthetic).* Cycle-322 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle320_swarm_ch27_w320_13.png)

*Teaching figure (synthetic).* Cycle-320 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle318_swarm_ch27_w318_13.png)

*Teaching figure (synthetic).* Cycle-318 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle316_swarm_ch27_w316_13.png)

*Teaching figure (synthetic).* Cycle-316 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle314_swarm_ch27_w314_13.png)

*Teaching figure (synthetic).* Cycle-314 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle312_swarm_ch27_w312_13.png)

*Teaching figure (synthetic).* Cycle-312 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle310_swarm_ch27_w310_13.png)

*Teaching figure (synthetic).* Cycle-310 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle308_swarm_ch27_w308_13.png)

*Teaching figure (synthetic).* Cycle-308 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle306_swarm_ch27_w306_13.png)

*Teaching figure (synthetic).* Cycle-306 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle304_swarm_ch27_w304_13.png)

*Teaching figure (synthetic).* Cycle-304 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle302_swarm_ch27_w302_13.png)

*Teaching figure (synthetic).* Cycle-302 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle300_swarm_ch27_w300_13.png)

*Teaching figure (synthetic).* Cycle-300 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle298_swarm_ch27_w298_13.png)

*Teaching figure (synthetic).* Cycle-298 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle296_swarm_ch27_w296_13.png)

*Teaching figure (synthetic).* Cycle-296 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle294_swarm_ch27_w294_13.png)

*Teaching figure (synthetic).* Cycle-294 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle292_swarm_ch27_w292_13.png)

*Teaching figure (synthetic).* Cycle-292 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle290_swarm_ch27_w290_13.png)

*Teaching figure (synthetic).* Cycle-290 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle288_swarm_ch27_w288_13.png)

*Teaching figure (synthetic).* Cycle-288 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle286_swarm_ch27_w286_13.png)

*Teaching figure (synthetic).* Cycle-286 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle284_swarm_ch27_w284_13.png)

*Teaching figure (synthetic).* Cycle-284 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle282_swarm_ch27_w282_13.png)

*Teaching figure (synthetic).* Cycle-282 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle280_swarm_ch27_w280_13.png)

*Teaching figure (synthetic).* Cycle-280 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle278_swarm_ch27_w278_13.png)

*Teaching figure (synthetic).* Cycle-278 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle276_swarm_ch27_w276_13.png)

*Teaching figure (synthetic).* Cycle-276 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle274_swarm_ch27_w274_13.png)

*Teaching figure (synthetic).* Cycle-274 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle272_swarm_ch27_w272_13.png)

*Teaching figure (synthetic).* Cycle-272 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle270_swarm_ch27_w270_13.png)

*Teaching figure (synthetic).* Cycle-270 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle268_swarm_ch27_w268_13.png)

*Teaching figure (synthetic).* Cycle-268 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle266_swarm_ch27_w266_13.png)

*Teaching figure (synthetic).* Cycle-266 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle264_swarm_ch27_w264_13.png)

*Teaching figure (synthetic).* Cycle-264 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle262_swarm_ch27_w262_13.png)

*Teaching figure (synthetic).* Cycle-262 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle260_swarm_ch27_w260_13.png)

*Teaching figure (synthetic).* Cycle-260 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle258_swarm_ch27_w258_13.png)

*Teaching figure (synthetic).* Cycle-258 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle256_swarm_ch27_w256_13.png)

*Teaching figure (synthetic).* Cycle-256 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle254_swarm_ch27_w254_13.png)

*Teaching figure (synthetic).* Cycle-254 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle252_swarm_ch27_w252_13.png)

*Teaching figure (synthetic).* Cycle-252 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle250_swarm_ch27_w250_13.png)

*Teaching figure (synthetic).* Cycle-250 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle248_swarm_ch27_w248_13.png)

*Teaching figure (synthetic).* Cycle-248 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle246_swarm_ch27_w246_13.png)

*Teaching figure (synthetic).* Cycle-246 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle244_swarm_ch27_w244_13.png)

*Teaching figure (synthetic).* Cycle-244 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle242_swarm_ch27_w242_13.png)

*Teaching figure (synthetic).* Cycle-242 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle240_swarm_ch27_w240_13.png)

*Teaching figure (synthetic).* Cycle-240 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle238_swarm_ch27_w238_13.png)

*Teaching figure (synthetic).* Cycle-238 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle236_swarm_ch27_w236_13.png)

*Teaching figure (synthetic).* Cycle-236 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle234_swarm_ch27_w234_13.png)

*Teaching figure (synthetic).* Cycle-234 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle232_swarm_ch27_w232_13.png)

*Teaching figure (synthetic).* Cycle-232 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle230_swarm_ch27_w230_13.png)

*Teaching figure (synthetic).* Cycle-230 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle228_swarm_ch27_w228_13.png)

*Teaching figure (synthetic).* Cycle-228 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle226_swarm_ch27_w226_13.png)

*Teaching figure (synthetic).* Cycle-226 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle224_swarm_ch27_w224_13.png)

*Teaching figure (synthetic).* Cycle-224 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle222_swarm_ch27_w222_13.png)

*Teaching figure (synthetic).* Cycle-222 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle220_swarm_ch27_w220_13.png)

*Teaching figure (synthetic).* Cycle-220 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle218_swarm_ch27_w218_13.png)

*Teaching figure (synthetic).* Cycle-218 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle216_swarm_ch27_w216_13.png)

*Teaching figure (synthetic).* Cycle-216 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle214_swarm_ch27_w214_13.png)

*Teaching figure (synthetic).* Cycle-214 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle212_swarm_ch27_w212_13.png)

*Teaching figure (synthetic).* Cycle-212 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle210_swarm_ch27_w210_13.png)

*Teaching figure (synthetic).* Cycle-210 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle208_swarm_ch27_w208_13.png)

*Teaching figure (synthetic).* Cycle-208 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle206_swarm_ch27_w206_13.png)

*Teaching figure (synthetic).* Cycle-206 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle204_swarm_ch27_w204_13.png)

*Teaching figure (synthetic).* Cycle-204 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle202_swarm_ch27_w202_13.png)

*Teaching figure (synthetic).* Cycle-202 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle200_swarm_ch27_w200_13.png)

*Teaching figure (synthetic).* Cycle-200 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle198_swarm_ch27_w198_13.png)

*Teaching figure (synthetic).* Cycle-198 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle196_swarm_ch27_w196_13.png)

*Teaching figure (synthetic).* Cycle-196 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle194_swarm_ch27_w194_13.png)

*Teaching figure (synthetic).* Cycle-194 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle192_swarm_ch27_w192_13.png)

*Teaching figure (synthetic).* Cycle-192 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle190_swarm_ch27_w190_13.png)

*Teaching figure (synthetic).* Cycle-190 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle188_swarm_ch27_w188_13.png)

*Teaching figure (synthetic).* Cycle-188 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle186_swarm_ch27_w186_13.png)

*Teaching figure (synthetic).* Cycle-186 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle184_swarm_ch27_w184_13.png)

*Teaching figure (synthetic).* Cycle-184 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle182_swarm_ch27_w182_13.png)

*Teaching figure (synthetic).* Cycle-182 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle180_swarm_ch27_w180_13.png)

*Teaching figure (synthetic).* Cycle-180 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle178_swarm_ch27_w178_13.png)

*Teaching figure (synthetic).* Cycle-178 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle176_swarm_ch27_w176_13.png)

*Teaching figure (synthetic).* Cycle-176 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle174_swarm_ch27_w174_13.png)

*Teaching figure (synthetic).* Cycle-174 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle172_swarm_ch27_w172_13.png)

*Teaching figure (synthetic).* Cycle-172 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle170_swarm_ch27_w170_13.png)

*Teaching figure (synthetic).* Cycle-170 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle168_swarm_ch27_w168_13.png)

*Teaching figure (synthetic).* Cycle-168 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle166_swarm_ch27_w166_13.png)

*Teaching figure (synthetic).* Cycle-166 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle164_swarm_ch27_w164_13.png)

*Teaching figure (synthetic).* Cycle-164 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle162_swarm_ch27_w162_13.png)

*Teaching figure (synthetic).* Cycle-162 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle160_swarm_ch27_w160_13.png)

*Teaching figure (synthetic).* Cycle-160 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle158_swarm_ch27_w158_13.png)

*Teaching figure (synthetic).* Cycle-158 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle156_swarm_ch27_w156_13.png)

*Teaching figure (synthetic).* Cycle-156 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle154_swarm_ch27_w154_13.png)

*Teaching figure (synthetic).* Cycle-154 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle152_swarm_ch27_w152_13.png)

*Teaching figure (synthetic).* Cycle-152 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle150_swarm_ch27_w150_13.png)

*Teaching figure (synthetic).* Cycle-150 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle148_swarm_ch27_w148_13.png)

*Teaching figure (synthetic).* Cycle-148 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle146_swarm_ch27_w146_13.png)

*Teaching figure (synthetic).* Cycle-146 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle144_swarm_ch27_w144_13.png)

*Teaching figure (synthetic).* Cycle-144 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle142_swarm_ch27_w142_13.png)

*Teaching figure (synthetic).* Cycle-142 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle140_swarm_ch27_w140_13.png)

*Teaching figure (synthetic).* Cycle-140 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle138_swarm_ch27_w138_13.png)

*Teaching figure (synthetic).* Cycle-138 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle136_swarm_ch27_w136_13.png)

*Teaching figure (synthetic).* Cycle-136 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle134_swarm_ch27_w134_13.png)

*Teaching figure (synthetic).* Cycle-134 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle132_swarm_ch27_w132_13.png)

*Teaching figure (synthetic).* Cycle-132 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle130_swarm_ch27_w130_13.png)

*Teaching figure (synthetic).* Cycle-130 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle128_swarm_ch27_w128_13.png)

*Teaching figure (synthetic).* Cycle-128 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle126_swarm_ch27_w126_13.png)

*Teaching figure (synthetic).* Cycle-126 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle124_swarm_ch27_w124_13.png)

*Teaching figure (synthetic).* Cycle-124 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle122_swarm_ch27_w122_13.png)

*Teaching figure (synthetic).* Cycle-122 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle120_swarm_ch27_w120_13.png)

*Teaching figure (synthetic).* Cycle-120 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle118_swarm_ch27_w118_13.png)

*Teaching figure (synthetic).* Cycle-118 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle116_swarm_ch27_w116_13.png)

*Teaching figure (synthetic).* Cycle-116 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle114_swarm_ch27_w114_13.png)

*Teaching figure (synthetic).* Cycle-114 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle112_swarm_ch27_w112_13.png)

*Teaching figure (synthetic).* Cycle-112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle110_swarm_ch27_w110_13.png)

*Teaching figure (synthetic).* Cycle-110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle108_swarm_ch27_w108_13.png)

*Teaching figure (synthetic).* Cycle-108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle106_swarm_ch27_w106_13.png)

*Teaching figure (synthetic).* Cycle-106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle104_swarm_ch27_w104_13.png)

*Teaching figure (synthetic).* Cycle-104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle102_swarm_ch27_w102_13.png)

*Teaching figure (synthetic).* Cycle-102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle100_swarm_ch27_w100_13.png)

*Teaching figure (synthetic).* Cycle-100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle98_swarm_ch27_w98_13.png)

*Teaching figure (synthetic).* Cycle-98 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle96_swarm_ch27_w96_13.png)

*Teaching figure (synthetic).* Cycle-96 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle94_swarm_ch27_w94_13.png)

*Teaching figure (synthetic).* Cycle-94 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle92_swarm_ch27_w92_13.png)

*Teaching figure (synthetic).* Cycle-92 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle90_swarm_ch27_w90_13.png)

*Teaching figure (synthetic).* Cycle-90 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle88_swarm_ch27_w88_13.png)

*Teaching figure (synthetic).* Cycle-88 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle86_swarm_ch27_w86_13.png)

*Teaching figure (synthetic).* Cycle-86 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle84_swarm_ch27_w84_13.png)

*Teaching figure (synthetic).* Cycle-84 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle82_swarm_ch27_w82_13.png)

*Teaching figure (synthetic).* Cycle-82 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle80_swarm_ch27_w80_13.png)

*Teaching figure (synthetic).* Cycle-80 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle78_swarm_ch27_w78_13.png)

*Teaching figure (synthetic).* Cycle-78 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle76_swarm_ch27_w76_13.png)

*Teaching figure (synthetic).* Cycle-76 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle74_swarm_ch27_w74_13.png)

*Teaching figure (synthetic).* Cycle-74 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle72_swarm_ch27_w72_13.png)

*Teaching figure (synthetic).* Cycle-72 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle70_swarm_ch27_w70_13.png)

*Teaching figure (synthetic).* Cycle-70 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle68_swarm_ch27_w68_13.png)

*Teaching figure (synthetic).* Cycle-68 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle66_swarm_ch27_w66_13.png)

*Teaching figure (synthetic).* Cycle-66 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle64_swarm_ch27_w64_13.png)

*Teaching figure (synthetic).* Cycle-64 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle62_swarm_ch27_w62_13.png)

*Teaching figure (synthetic).* Cycle-62 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle60_swarm_ch27_c60m.png)

*Teaching figure (synthetic).* Cycle-60 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle58_swarm_ch27_c58m.png)

*Teaching figure (synthetic).* Cycle-58 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle56_swarm_ch27_tip_abs.png)

*Teaching figure (synthetic).* Cycle-56 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle54_swarm_ch27_frag_idx.png)

*Teaching figure (synthetic).* Cycle-54 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle52_swarm_ch27_alpha_abs.png)

*Teaching figure (synthetic).* Cycle-52 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle50_swarm_ch27_miss_arr.png)

*Teaching figure (synthetic).* Cycle-50 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle48_swarm_ch27_fwer.png)

*Teaching figure (synthetic).* Cycle-48 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 27 (original scientific teaching figure).](../assets/figures/cycle46_swarm_ch27_fragility.png)

*Teaching figure (synthetic).* Cycle-46 densify scientific residual (ch15–28).






Physicians are conditioned to inspect randomization, blinding, and primary endpoint definitions with extreme care, yet often ignore the analytic plumbing that underwrites the reported p-value. A trial claiming a revolutionary endovascular therapy benefit may harbor missing 90-day modified Rankin Scale (mRS) data on 10% of the cohort, undocumented alpha spending across multiple interim peeks, and a dozen unadjusted secondary endpoints mined for significance. This is not mere statistical pedantry. These methodological choices determine whether a reported hazard ratio reflects a stable biological truth or a fragile statistical mirage.

Stroke research is uniquely vulnerable to these specific analytic threats. Delayed functional outcomes (e.g., 90- or 180-day mRS) suffer structural missingness as patients disperse to skilled nursing facilities or home care. Radiographic endpoints produce highly correlated, multiple comparisons (infarct core, penumbra, collateral grade). Acute interventions often test modest effect sizes where a handful of outcome reclassifications can obliterate statistical significance. The appraiser's job is to deconstruct this plumbing. If a trial's conclusions cannot survive plausible missing-data assumptions, multiplicity penalties, and minor event-count perturbations, those conclusions should not dictate regional stroke protocols.

## Missingness Mechanisms: MCAR, MAR, and MNAR

Missing data are rarely just missing; they carry structural information. Missing Completely at Random (MCAR) implies that the probability of missingness is entirely independent of any patient characteristic or outcome. True MCAR is exceptional in clinical neuroscience—perhaps a corrupted MR angiogram file or a lost case report form. Under MCAR, a complete-case analysis is unbiased but inefficient.

Missing at Random (MAR) assumes that missingness can be fully explained by observed baseline covariates, and that conditional on these observed data, missingness does not depend on the unobserved outcome itself. For instance, if 90-day mRS is more often missing in patients with severe admission NIHSS and older age, but within those specific strata the missingness is random, the data are MAR. This assumption licenses techniques like multiple imputation or inverse probability weighting. However, MAR is a strong, unverifiable assumption, not a mathematical certainty.

Missing Not at Random (MNAR) is the most menacing mechanism. Here, the probability of missingness depends on the unobserved value itself, even after conditioning on all available covariates. If families of patients with devastating disability (mRS 5) refuse follow-up interviews precisely because of that disability, the data are MNAR. Standard imputation models under MAR will systematically underestimate the true disability burden. In stroke trials, MNAR is highly prevalent and demands rigorous sensitivity analyses, such as tipping-point testing or worst-case scenario imputation.

## The Fallacy of LOCF and Complete-Case Analysis

Historically, neurologists relied on Last Observation Carried Forward (LOCF) to patch missing data. If a day-30 mRS is available but day-90 is missing, LOCF simply pastes the day-30 value into the day-90 slot. This assumes stroke recovery is a flat line, freezing early disability and aggressively ignoring the realities of late rehabilitation or subsequent complications. LOCF is not a conservative strategy; it can bias effect estimates in either direction depending on the timing and differential rates of dropout between treatment arms. It is a scientifically indefensible practice in modern stroke trials.

Conversely, complete-case analysis simply deletes any patient with missing data. If the missingness mechanism is MAR or MNAR, this introduces severe selection bias, effectively analyzing a healthier, highly selected sub-cohort rather than the intention-to-treat population. Robust trials must favor principled approaches: mixed-effects models for repeated measures, multiple imputation under specified MAR models, and explicit stress-testing of those assumptions via MNAR sensitivity analysis.

## Multiplicity: The Garden of Forking Paths

Multiplicity inflates the family-wise error rate when multiple statistical tests are conducted without adjusting the threshold for significance. Testing twenty secondary endpoints at an unadjusted alpha of 0.05 virtually guarantees a false positive by chance alone. In stroke literature, this manifests as authors quietly abandoning a null primary endpoint (e.g., mRS 0-1) to trumpet a nominally significant secondary endpoint (e.g., ordinal shift analysis or early neurological improvement).

This behavior capitalizes on analytic flexibility. The 'garden of forking paths' describes the myriad choices researchers make after seeing the data: selecting specific covariate adjustments, defining subgroups (e.g., fast versus slow progressors), or choosing varying time windows. To defend against multiplicity, appraisers must demand pre-specified, locked statistical analysis plans. Legitimate strategies include hierarchical testing (where secondary endpoints are only tested if the primary is significant) or alpha-spending techniques like Bonferroni or Hochberg procedures. Unadjusted subgroup findings must be strictly relegated to hypothesis generation.

![Family-wise type I error rises with the number of unadjusted secondary tests at α=0.05; appraisal defenses include SAP lock, hierarchy, and alpha spending (original teaching figure).](../assets/figures/cycle2_swarm_ch27_multiplicity_fwer.png)

*Teaching figure (synthetic).* Under independent tests at unadjusted α = 0.05, family-wise error is already ~40% by about ten secondaries and ~64% by twenty. A null primary plus a nominally “significant” unadjusted secondary is hypothesis-generating spin, not confirmatory evidence for a stroke pathway change.

## Interim Analyses and Early Stopping

![Interim ARR path can freeze an inflated absolute effect at early looks versus completed-trial ARR (original teaching figure).](../assets/figures/cycle13_swarm_ch27_early_stop.png)

*Teaching figure (synthetic).* Early stopping for benefit tends to overestimate absolute effects—pair stopped ARR with bias awareness and MCID.


Adaptive trial designs frequently employ interim analyses, governed by Data and Safety Monitoring Boards (DSMBs), to stop trials early for overwhelming efficacy, futility, or harm. While ethically justified, early stopping for benefit introduces systematic bias. A trial halted early for efficacy has often caught a random high in the sampling distribution, resulting in a grossly exaggerated point estimate of the treatment effect. Subsequent meta-analyses invariably show 'regression to the truth,' with attenuated effect sizes.

Appraisers must distinguish between strict alpha-spending boundaries (e.g., O'Brien-Fleming, which requires massive evidence early on) and liberal boundaries. Furthermore, stopping for futility does not prove equivalence; it merely confirms that the trial is unlikely to demonstrate the pre-specified absolute difference. Undisclosed interim 'peeks' at the data without statistical penalty are fatal to the integrity of the reported p-value.

![Early stopping for benefit inflates the interim ARR; later replications regress toward the true absolute effect (original teaching figure).](../assets/figures/cycle2_swarm_ch27_early_stop_bias.png)

*Teaching figure (synthetic).* An early efficacy stop can catch a random high (here 14 pp ARR) while the generative truth is 6 pp; completed and replication estimates regress. Down-weight magnitude from early-stopped stroke trials, insist on absolute risks with CIs, and remember futility stops do not prove equivalence.

## The Fragility Index: Stress-Testing Statistical Significance

![Fragility index residual: few event flips can null absolute ARR despite p<0.05 (original teaching figure).](../assets/figures/cycle20_swarm_ch27_fragility_abs.png)

*Teaching figure (synthetic).* Stress-test the absolute ledger—FI and FQ before pathway lock.


The fragility index operationalizes the vulnerability of a statistically significant dichotomous outcome. It calculates the minimum number of patients whose status would have to flip from 'non-event' to 'event' in the treatment arm to render the trial result statistically non-significant (p >= 0.05). In acute stroke trials, where sample sizes are often modest (e.g., N=200 per arm) and absolute risk reductions sit in the 5-10% range, the fragility index is frequently in the single digits.

If a dual-antiplatelet trial claims superiority based on a p-value of 0.043, but a fragility index of 3 indicates that merely three more strokes in the active arm would erase the significance, the evidentiary foundation is incredibly brittle. When the number of patients lost to follow-up exceeds the fragility index, the trial's conclusion rests entirely on untestable missing-data assumptions. While the fragility index has mathematical limitations and should not replace confidence intervals, it is an unparalleled heuristic for deflating statistical hubris.

![Fragility index versus lost-to-follow-up counts: when LTFU exceeds FI, significance is assumption-bound (original teaching figure).](../assets/figures/cycle2_ch27_fragility_ltfu.png)

*Teaching figure (synthetic).* Trial P has FI well above LTFU—more robust to missing outcomes. Trials Q and R have LTFU ≥ FI, so a handful of unobserved events (or MNAR disability) can erase “significance.” Always pair the fragility index with the missing-primary-outcome count and demand tipping-point sensitivity before rewriting stroke pathways.

![Fragility index of a few flipped events can erase p<0.05 while ARR still sits below MCID; if missing outcomes exceed fragility, absolute claims are assumption-bound (original teaching figure).](../assets/figures/cycle9_swarm_ch27_fragility.png)

*Teaching figure (synthetic).* Stress-test significance in event counts and against MCID. Statistically fragile *and* clinically modest results do not rewrite pathways.

## Analytic Flexibility and the Architecture of Spin

Analytic flexibility provides the raw material for spin—the systemic rhetorical distortion of trial results. Spin occurs when authors emphasize relative risk reductions while obscuring marginal absolute differences, elevate unadjusted secondary findings to the abstract's conclusion, or frame statistically non-significant primary outcomes as 'trends toward benefit.' Spin is the clinical translation of p-hacking.

Defeating spin requires a disciplined appraisal architecture. The reader must first secure the protocol's primary endpoint, calculate the absolute risk difference independently, evaluate the missingness proportion against the event counts, and discount any unadjusted secondary claims. If your independent interpretation of the primary data contradicts the authors' conclusion, you have identified spin.

## Clinical and Epidemiologic Notes

Clinical Note: When adopting a novel stroke intervention—particularly one involving complex logistics like mobile stroke units or extended-window thrombectomy—demand an evidence base that is not fragile. If flipping a half-dozen outcomes invalidates the trial, wait for confirmatory data before rewriting institutional protocols.

Methodologic Note: Do not conflate statistical significance with evidentiary robustness. A p-value of 0.04 in an underpowered subgroup with 12% missing data is mathematical noise dressed in academic formatting.

Epidemiologic Note: Anticipate missing data in trial design rather than attempting to rescue it with post hoc statistical gymnastics. Rigorous follow-up infrastructure is vastly superior to complex imputation models.


![fig75_instrumental_variable.png original teaching graphic](../assets/figures/fig75_instrumental_variable.png)

*Original teaching graphic (fig75_instrumental_variable.png).*

## Chapter summary

Statistical significance is an output; the analytic plumbing that generates it determines its validity. Missing data mechanisms (MCAR, MAR, MNAR) require principled handling, as crude methods like LOCF and complete-case analysis introduce severe bias in neurologic outcomes. Unpenalized multiplicity and analytic flexibility construct a 'garden of forking paths' that generates false positives. Interim analyses and early stopping for benefit systematically overestimate effect sizes, demanding cautious interpretation. The fragility index serves as a crucial heuristic, revealing how easily minor outcome perturbations can collapse a significant result. Ultimately, discerning neurologists must aggressively interrogate a trial's missingness, multiplicity control, and fragility to strip away authorial spin and determine true clinical utility.

## Practice and reflection

1. Select a recent endovascular trial stopped early for efficacy. Calculate its fragility index and compare it to the number of patients lost to follow-up.
2. Identify a stroke trial where a secondary endpoint is emphasized in the abstract. Trace the alpha-spending protocol to determine if the finding is statistically valid.
3. Explain why a complete-case analysis of 90-day mRS outcomes is likely biased under an MNAR assumption, focusing on stroke severity and mortality.
4. Critique the use of LOCF in a hypothetical secondary prevention trial tracking recurrent TIA over 12 months.
5. Draft a brief policy for your stroke center defining the required evidentiary robustness (fragility, missing data limits) before a new protocol is adopted.

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

