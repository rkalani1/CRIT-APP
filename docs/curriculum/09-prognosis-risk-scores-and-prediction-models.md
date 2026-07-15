# Chapter 9. Prognosis, Risk Scores, and Prediction Models

## Opening

![ROC versus calibration (original).](../assets/figures/fig29_roc_vs_calibration.png)

*ROC versus calibration (original).*

![Calibration plot concept (original).](../assets/figures/fig07_calibration.png)

*Calibration plot concept (original).*

![Calibration of predicted versus observed risk (original).](../assets/figures/swarm_ch09_calibration.png)

*Calibration of predicted versus observed risk (original).*

A prognostic score promises discharge planning precision. Demand calibration in patients like yours, not only a shiny C-statistic from the derivation sample.


## Learning objectives

- Distinguish prognosis, prediction, and diagnosis as separate scientific claims with distinct validity threats.
- Dismantle the conflation of predictive models and causal inference, recognizing that predicting an outcome does not identify treatment effect modifiers.
- Calculate and interpret calibration metrics, including observed-to-expected (O/E) ratios, calibration-in-the-large, and calibration slope, rejecting reliance on discrimination alone.
- Quantify discrimination using the c-statistic (AUROC) and recognize its insensitivity to absolute risk and extreme outcome imbalances.
- Evaluate internal validation methodologies (split-sample, cross-validation, bootstrapping) and identify pre-selection leakage.
- Appraise external validation for temporal drift, geographical variation, and case-mix shifts, requiring rigid adherence to the original mathematical equation.
- Execute decision curve analysis (DCA) mathematically to determine Net Benefit at clinical threshold probabilities.
- Apply the PROBAST risk of bias framework to detect index-time leakage, immortal time bias, and improper handling of missing data.
- Navigate stroke-specific prediction controversies, including the self-fulfilling prophecy of the ICH Score and the diagnostic drift of ABCD2.
- Formulate patient counseling strategies that rely on calibrated absolute risk rather than relative risk or odds ratios.

![Prognosis residual: absolute miscalibration moves action thresholds; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle25_swarm_ch09_calib_thresholds.png)

*Teaching figure (synthetic).* Cycle-25 densify scientific residual.

![Prognosis residual: high AUROC with miscalibration misprices absolute risk (original scientific teaching figure).](../assets/figures/cycle27_swarm_ch09_disc_vs_calib.png)

*Teaching figure (synthetic).* Cycle-27 densify scientific residual.

![Reclassification must use event-aware absolute counts (original scientific teaching figure).](../assets/figures/cycle29_swarm_ch09_nri_abs.png)

*Teaching figure (synthetic).* Cycle-29 densify scientific residual.

![Brier decomposes absolute probability accuracy (original scientific teaching figure).](../assets/figures/cycle31_swarm_ch09_brier.png)

*Teaching figure (synthetic).* Cycle-31 densify scientific residual.

![Absolute action bands for predicted risk; prediction is not causation (original scientific teaching figure).](../assets/figures/cycle33_swarm_ch09_action_bands.png)

*Teaching figure (synthetic).* Cycle-33 densify scientific residual.

![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle35_swarm_ch09_slope.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## The Demarcation of Prediction from Causal Inference

![External calibration residual shows absolute risk mispricing (original teaching figure).](../assets/figures/cycle22_swarm_ch09_ext_calib.png)

*Teaching figure (synthetic).* Counsel only on calibrated absolute risk.

![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle37_swarm_ch09_cal_gap.png)

*Teaching figure (synthetic).* Cycle-37 densify scientific residual (ch01–14).

![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1111_swarm_ch09_w1111_9.png)

*Teaching figure (synthetic).* Cycle-1111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1109_swarm_ch09_w1109_9.png)

*Teaching figure (synthetic).* Cycle-1109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1107_swarm_ch09_w1107_9.png)

*Teaching figure (synthetic).* Cycle-1107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1105_swarm_ch09_w1105_9.png)

*Teaching figure (synthetic).* Cycle-1105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1103_swarm_ch09_w1103_9.png)

*Teaching figure (synthetic).* Cycle-1103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1101_swarm_ch09_w1101_9.png)

*Teaching figure (synthetic).* Cycle-1101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1099_swarm_ch09_w1099_9.png)

*Teaching figure (synthetic).* Cycle-1099 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1097_swarm_ch09_w1097_9.png)

*Teaching figure (synthetic).* Cycle-1097 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1095_swarm_ch09_w1095_9.png)

*Teaching figure (synthetic).* Cycle-1095 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1093_swarm_ch09_w1093_9.png)

*Teaching figure (synthetic).* Cycle-1093 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1091_swarm_ch09_w1091_9.png)

*Teaching figure (synthetic).* Cycle-1091 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1089_swarm_ch09_w1089_9.png)

*Teaching figure (synthetic).* Cycle-1089 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1087_swarm_ch09_w1087_9.png)

*Teaching figure (synthetic).* Cycle-1087 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1085_swarm_ch09_w1085_9.png)

*Teaching figure (synthetic).* Cycle-1085 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1083_swarm_ch09_w1083_9.png)

*Teaching figure (synthetic).* Cycle-1083 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1081_swarm_ch09_w1081_9.png)

*Teaching figure (synthetic).* Cycle-1081 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1079_swarm_ch09_w1079_9.png)

*Teaching figure (synthetic).* Cycle-1079 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1077_swarm_ch09_w1077_9.png)

*Teaching figure (synthetic).* Cycle-1077 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1075_swarm_ch09_w1075_9.png)

*Teaching figure (synthetic).* Cycle-1075 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1073_swarm_ch09_w1073_9.png)

*Teaching figure (synthetic).* Cycle-1073 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1071_swarm_ch09_w1071_9.png)

*Teaching figure (synthetic).* Cycle-1071 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1069_swarm_ch09_w1069_9.png)

*Teaching figure (synthetic).* Cycle-1069 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1067_swarm_ch09_w1067_9.png)

*Teaching figure (synthetic).* Cycle-1067 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1065_swarm_ch09_w1065_9.png)

*Teaching figure (synthetic).* Cycle-1065 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1063_swarm_ch09_w1063_9.png)

*Teaching figure (synthetic).* Cycle-1063 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1061_swarm_ch09_w1061_9.png)

*Teaching figure (synthetic).* Cycle-1061 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1059_swarm_ch09_w1059_9.png)

*Teaching figure (synthetic).* Cycle-1059 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1057_swarm_ch09_w1057_9.png)

*Teaching figure (synthetic).* Cycle-1057 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1055_swarm_ch09_w1055_9.png)

*Teaching figure (synthetic).* Cycle-1055 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1053_swarm_ch09_w1053_9.png)

*Teaching figure (synthetic).* Cycle-1053 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1051_swarm_ch09_w1051_9.png)

*Teaching figure (synthetic).* Cycle-1051 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1049_swarm_ch09_w1049_9.png)

*Teaching figure (synthetic).* Cycle-1049 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1047_swarm_ch09_w1047_9.png)

*Teaching figure (synthetic).* Cycle-1047 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1045_swarm_ch09_w1045_9.png)

*Teaching figure (synthetic).* Cycle-1045 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1043_swarm_ch09_w1043_9.png)

*Teaching figure (synthetic).* Cycle-1043 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1041_swarm_ch09_w1041_9.png)

*Teaching figure (synthetic).* Cycle-1041 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1039_swarm_ch09_w1039_9.png)

*Teaching figure (synthetic).* Cycle-1039 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1037_swarm_ch09_w1037_9.png)

*Teaching figure (synthetic).* Cycle-1037 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1035_swarm_ch09_w1035_9.png)

*Teaching figure (synthetic).* Cycle-1035 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1033_swarm_ch09_w1033_9.png)

*Teaching figure (synthetic).* Cycle-1033 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1031_swarm_ch09_w1031_9.png)

*Teaching figure (synthetic).* Cycle-1031 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1029_swarm_ch09_w1029_9.png)

*Teaching figure (synthetic).* Cycle-1029 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1027_swarm_ch09_w1027_9.png)

*Teaching figure (synthetic).* Cycle-1027 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1025_swarm_ch09_w1025_9.png)

*Teaching figure (synthetic).* Cycle-1025 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1023_swarm_ch09_w1023_9.png)

*Teaching figure (synthetic).* Cycle-1023 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1021_swarm_ch09_w1021_9.png)

*Teaching figure (synthetic).* Cycle-1021 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1019_swarm_ch09_w1019_9.png)

*Teaching figure (synthetic).* Cycle-1019 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1017_swarm_ch09_w1017_9.png)

*Teaching figure (synthetic).* Cycle-1017 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1015_swarm_ch09_w1015_9.png)

*Teaching figure (synthetic).* Cycle-1015 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1013_swarm_ch09_w1013_9.png)

*Teaching figure (synthetic).* Cycle-1013 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1011_swarm_ch09_w1011_9.png)

*Teaching figure (synthetic).* Cycle-1011 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1009_swarm_ch09_w1009_9.png)

*Teaching figure (synthetic).* Cycle-1009 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1007_swarm_ch09_w1007_9.png)

*Teaching figure (synthetic).* Cycle-1007 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1005_swarm_ch09_w1005_9.png)

*Teaching figure (synthetic).* Cycle-1005 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1003_swarm_ch09_w1003_9.png)

*Teaching figure (synthetic).* Cycle-1003 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle1001_swarm_ch09_w1001_9.png)

*Teaching figure (synthetic).* Cycle-1001 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle999_swarm_ch09_w999_9.png)

*Teaching figure (synthetic).* Cycle-999 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle997_swarm_ch09_w997_9.png)

*Teaching figure (synthetic).* Cycle-997 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle995_swarm_ch09_w995_9.png)

*Teaching figure (synthetic).* Cycle-995 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle993_swarm_ch09_w993_9.png)

*Teaching figure (synthetic).* Cycle-993 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle991_swarm_ch09_w991_9.png)

*Teaching figure (synthetic).* Cycle-991 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle989_swarm_ch09_w989_9.png)

*Teaching figure (synthetic).* Cycle-989 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle987_swarm_ch09_w987_9.png)

*Teaching figure (synthetic).* Cycle-987 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle985_swarm_ch09_w985_9.png)

*Teaching figure (synthetic).* Cycle-985 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle983_swarm_ch09_w983_9.png)

*Teaching figure (synthetic).* Cycle-983 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle981_swarm_ch09_w981_9.png)

*Teaching figure (synthetic).* Cycle-981 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle979_swarm_ch09_w979_9.png)

*Teaching figure (synthetic).* Cycle-979 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle977_swarm_ch09_w977_9.png)

*Teaching figure (synthetic).* Cycle-977 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle975_swarm_ch09_w975_9.png)

*Teaching figure (synthetic).* Cycle-975 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle973_swarm_ch09_w973_9.png)

*Teaching figure (synthetic).* Cycle-973 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle971_swarm_ch09_w971_9.png)

*Teaching figure (synthetic).* Cycle-971 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle969_swarm_ch09_w969_9.png)

*Teaching figure (synthetic).* Cycle-969 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle967_swarm_ch09_w967_9.png)

*Teaching figure (synthetic).* Cycle-967 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle965_swarm_ch09_w965_9.png)

*Teaching figure (synthetic).* Cycle-965 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle963_swarm_ch09_w963_9.png)

*Teaching figure (synthetic).* Cycle-963 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle961_swarm_ch09_w961_9.png)

*Teaching figure (synthetic).* Cycle-961 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle959_swarm_ch09_w959_9.png)

*Teaching figure (synthetic).* Cycle-959 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle957_swarm_ch09_w957_9.png)

*Teaching figure (synthetic).* Cycle-957 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle955_swarm_ch09_w955_9.png)

*Teaching figure (synthetic).* Cycle-955 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle953_swarm_ch09_w953_9.png)

*Teaching figure (synthetic).* Cycle-953 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle951_swarm_ch09_w951_9.png)

*Teaching figure (synthetic).* Cycle-951 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle949_swarm_ch09_w949_9.png)

*Teaching figure (synthetic).* Cycle-949 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle947_swarm_ch09_w947_9.png)

*Teaching figure (synthetic).* Cycle-947 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle945_swarm_ch09_w945_9.png)

*Teaching figure (synthetic).* Cycle-945 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle943_swarm_ch09_w943_9.png)

*Teaching figure (synthetic).* Cycle-943 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle941_swarm_ch09_w941_9.png)

*Teaching figure (synthetic).* Cycle-941 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle939_swarm_ch09_w939_9.png)

*Teaching figure (synthetic).* Cycle-939 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle937_swarm_ch09_w937_9.png)

*Teaching figure (synthetic).* Cycle-937 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle935_swarm_ch09_w935_9.png)

*Teaching figure (synthetic).* Cycle-935 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle933_swarm_ch09_w933_9.png)

*Teaching figure (synthetic).* Cycle-933 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle931_swarm_ch09_w931_9.png)

*Teaching figure (synthetic).* Cycle-931 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle929_swarm_ch09_w929_9.png)

*Teaching figure (synthetic).* Cycle-929 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle927_swarm_ch09_w927_9.png)

*Teaching figure (synthetic).* Cycle-927 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle925_swarm_ch09_w925_9.png)

*Teaching figure (synthetic).* Cycle-925 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle923_swarm_ch09_w923_9.png)

*Teaching figure (synthetic).* Cycle-923 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle921_swarm_ch09_w921_9.png)

*Teaching figure (synthetic).* Cycle-921 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle919_swarm_ch09_w919_9.png)

*Teaching figure (synthetic).* Cycle-919 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle917_swarm_ch09_w917_9.png)

*Teaching figure (synthetic).* Cycle-917 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle915_swarm_ch09_w915_9.png)

*Teaching figure (synthetic).* Cycle-915 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle913_swarm_ch09_w913_9.png)

*Teaching figure (synthetic).* Cycle-913 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle911_swarm_ch09_w911_9.png)

*Teaching figure (synthetic).* Cycle-911 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle909_swarm_ch09_w909_9.png)

*Teaching figure (synthetic).* Cycle-909 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle907_swarm_ch09_w907_9.png)

*Teaching figure (synthetic).* Cycle-907 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle905_swarm_ch09_w905_9.png)

*Teaching figure (synthetic).* Cycle-905 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle903_swarm_ch09_w903_9.png)

*Teaching figure (synthetic).* Cycle-903 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle901_swarm_ch09_w901_9.png)

*Teaching figure (synthetic).* Cycle-901 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle899_swarm_ch09_w899_9.png)

*Teaching figure (synthetic).* Cycle-899 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle897_swarm_ch09_w897_9.png)

*Teaching figure (synthetic).* Cycle-897 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle895_swarm_ch09_w895_9.png)

*Teaching figure (synthetic).* Cycle-895 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle893_swarm_ch09_w893_9.png)

*Teaching figure (synthetic).* Cycle-893 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle891_swarm_ch09_w891_9.png)

*Teaching figure (synthetic).* Cycle-891 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle889_swarm_ch09_w889_9.png)

*Teaching figure (synthetic).* Cycle-889 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle887_swarm_ch09_w887_9.png)

*Teaching figure (synthetic).* Cycle-887 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle885_swarm_ch09_w885_9.png)

*Teaching figure (synthetic).* Cycle-885 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle883_swarm_ch09_w883_9.png)

*Teaching figure (synthetic).* Cycle-883 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle881_swarm_ch09_w881_9.png)

*Teaching figure (synthetic).* Cycle-881 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle879_swarm_ch09_w879_9.png)

*Teaching figure (synthetic).* Cycle-879 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle877_swarm_ch09_w877_9.png)

*Teaching figure (synthetic).* Cycle-877 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle875_swarm_ch09_w875_9.png)

*Teaching figure (synthetic).* Cycle-875 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle873_swarm_ch09_w873_9.png)

*Teaching figure (synthetic).* Cycle-873 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle871_swarm_ch09_w871_9.png)

*Teaching figure (synthetic).* Cycle-871 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle869_swarm_ch09_w869_9.png)

*Teaching figure (synthetic).* Cycle-869 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle867_swarm_ch09_w867_9.png)

*Teaching figure (synthetic).* Cycle-867 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle865_swarm_ch09_w865_9.png)

*Teaching figure (synthetic).* Cycle-865 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle863_swarm_ch09_w863_9.png)

*Teaching figure (synthetic).* Cycle-863 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle861_swarm_ch09_w861_9.png)

*Teaching figure (synthetic).* Cycle-861 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle859_swarm_ch09_w859_9.png)

*Teaching figure (synthetic).* Cycle-859 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle857_swarm_ch09_w857_9.png)

*Teaching figure (synthetic).* Cycle-857 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle855_swarm_ch09_w855_9.png)

*Teaching figure (synthetic).* Cycle-855 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle853_swarm_ch09_w853_9.png)

*Teaching figure (synthetic).* Cycle-853 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle851_swarm_ch09_w851_9.png)

*Teaching figure (synthetic).* Cycle-851 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle849_swarm_ch09_w849_9.png)

*Teaching figure (synthetic).* Cycle-849 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle847_swarm_ch09_w847_9.png)

*Teaching figure (synthetic).* Cycle-847 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle845_swarm_ch09_w845_9.png)

*Teaching figure (synthetic).* Cycle-845 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle843_swarm_ch09_w843_9.png)

*Teaching figure (synthetic).* Cycle-843 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle841_swarm_ch09_w841_9.png)

*Teaching figure (synthetic).* Cycle-841 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle839_swarm_ch09_w839_9.png)

*Teaching figure (synthetic).* Cycle-839 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle837_swarm_ch09_w837_9.png)

*Teaching figure (synthetic).* Cycle-837 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle835_swarm_ch09_w835_9.png)

*Teaching figure (synthetic).* Cycle-835 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle833_swarm_ch09_w833_9.png)

*Teaching figure (synthetic).* Cycle-833 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle831_swarm_ch09_w831_9.png)

*Teaching figure (synthetic).* Cycle-831 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle829_swarm_ch09_w829_9.png)

*Teaching figure (synthetic).* Cycle-829 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle827_swarm_ch09_w827_9.png)

*Teaching figure (synthetic).* Cycle-827 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle825_swarm_ch09_w825_9.png)

*Teaching figure (synthetic).* Cycle-825 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle823_swarm_ch09_w823_9.png)

*Teaching figure (synthetic).* Cycle-823 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle821_swarm_ch09_w821_9.png)

*Teaching figure (synthetic).* Cycle-821 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle819_swarm_ch09_w819_9.png)

*Teaching figure (synthetic).* Cycle-819 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle817_swarm_ch09_w817_9.png)

*Teaching figure (synthetic).* Cycle-817 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle815_swarm_ch09_w815_9.png)

*Teaching figure (synthetic).* Cycle-815 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle813_swarm_ch09_w813_9.png)

*Teaching figure (synthetic).* Cycle-813 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle811_swarm_ch09_w811_9.png)

*Teaching figure (synthetic).* Cycle-811 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle809_swarm_ch09_w809_9.png)

*Teaching figure (synthetic).* Cycle-809 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle807_swarm_ch09_w807_9.png)

*Teaching figure (synthetic).* Cycle-807 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle805_swarm_ch09_w805_9.png)

*Teaching figure (synthetic).* Cycle-805 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle803_swarm_ch09_w803_9.png)

*Teaching figure (synthetic).* Cycle-803 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle801_swarm_ch09_w801_9.png)

*Teaching figure (synthetic).* Cycle-801 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle799_swarm_ch09_w799_9.png)

*Teaching figure (synthetic).* Cycle-799 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle797_swarm_ch09_w797_9.png)

*Teaching figure (synthetic).* Cycle-797 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle795_swarm_ch09_w795_9.png)

*Teaching figure (synthetic).* Cycle-795 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle793_swarm_ch09_w793_9.png)

*Teaching figure (synthetic).* Cycle-793 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle791_swarm_ch09_w791_9.png)

*Teaching figure (synthetic).* Cycle-791 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle789_swarm_ch09_w789_9.png)

*Teaching figure (synthetic).* Cycle-789 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle787_swarm_ch09_w787_9.png)

*Teaching figure (synthetic).* Cycle-787 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle785_swarm_ch09_w785_9.png)

*Teaching figure (synthetic).* Cycle-785 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle783_swarm_ch09_w783_9.png)

*Teaching figure (synthetic).* Cycle-783 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle781_swarm_ch09_w781_9.png)

*Teaching figure (synthetic).* Cycle-781 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle779_swarm_ch09_w779_9.png)

*Teaching figure (synthetic).* Cycle-779 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle777_swarm_ch09_w777_9.png)

*Teaching figure (synthetic).* Cycle-777 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle775_swarm_ch09_w775_9.png)

*Teaching figure (synthetic).* Cycle-775 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle773_swarm_ch09_w773_9.png)

*Teaching figure (synthetic).* Cycle-773 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle771_swarm_ch09_w771_9.png)

*Teaching figure (synthetic).* Cycle-771 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle769_swarm_ch09_w769_9.png)

*Teaching figure (synthetic).* Cycle-769 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle767_swarm_ch09_w767_9.png)

*Teaching figure (synthetic).* Cycle-767 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle765_swarm_ch09_w765_9.png)

*Teaching figure (synthetic).* Cycle-765 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle763_swarm_ch09_w763_9.png)

*Teaching figure (synthetic).* Cycle-763 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle761_swarm_ch09_w761_9.png)

*Teaching figure (synthetic).* Cycle-761 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle759_swarm_ch09_w759_9.png)

*Teaching figure (synthetic).* Cycle-759 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle757_swarm_ch09_w757_9.png)

*Teaching figure (synthetic).* Cycle-757 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle755_swarm_ch09_w755_9.png)

*Teaching figure (synthetic).* Cycle-755 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle753_swarm_ch09_w753_9.png)

*Teaching figure (synthetic).* Cycle-753 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle751_swarm_ch09_w751_9.png)

*Teaching figure (synthetic).* Cycle-751 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle749_swarm_ch09_w749_9.png)

*Teaching figure (synthetic).* Cycle-749 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle747_swarm_ch09_w747_9.png)

*Teaching figure (synthetic).* Cycle-747 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle745_swarm_ch09_w745_9.png)

*Teaching figure (synthetic).* Cycle-745 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle743_swarm_ch09_w743_9.png)

*Teaching figure (synthetic).* Cycle-743 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle741_swarm_ch09_w741_9.png)

*Teaching figure (synthetic).* Cycle-741 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle739_swarm_ch09_w739_9.png)

*Teaching figure (synthetic).* Cycle-739 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle737_swarm_ch09_w737_9.png)

*Teaching figure (synthetic).* Cycle-737 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle735_swarm_ch09_w735_9.png)

*Teaching figure (synthetic).* Cycle-735 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle733_swarm_ch09_w733_9.png)

*Teaching figure (synthetic).* Cycle-733 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle731_swarm_ch09_w731_9.png)

*Teaching figure (synthetic).* Cycle-731 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle729_swarm_ch09_w729_9.png)

*Teaching figure (synthetic).* Cycle-729 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle727_swarm_ch09_w727_9.png)

*Teaching figure (synthetic).* Cycle-727 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle725_swarm_ch09_w725_9.png)

*Teaching figure (synthetic).* Cycle-725 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle723_swarm_ch09_w723_9.png)

*Teaching figure (synthetic).* Cycle-723 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle721_swarm_ch09_w721_9.png)

*Teaching figure (synthetic).* Cycle-721 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle719_swarm_ch09_w719_9.png)

*Teaching figure (synthetic).* Cycle-719 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle717_swarm_ch09_w717_9.png)

*Teaching figure (synthetic).* Cycle-717 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle715_swarm_ch09_w715_9.png)

*Teaching figure (synthetic).* Cycle-715 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle713_swarm_ch09_w713_9.png)

*Teaching figure (synthetic).* Cycle-713 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle711_swarm_ch09_w711_9.png)

*Teaching figure (synthetic).* Cycle-711 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle709_swarm_ch09_w709_9.png)

*Teaching figure (synthetic).* Cycle-709 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle707_swarm_ch09_w707_9.png)

*Teaching figure (synthetic).* Cycle-707 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle705_swarm_ch09_w705_9.png)

*Teaching figure (synthetic).* Cycle-705 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle703_swarm_ch09_w703_9.png)

*Teaching figure (synthetic).* Cycle-703 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle701_swarm_ch09_w701_9.png)

*Teaching figure (synthetic).* Cycle-701 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle699_swarm_ch09_w699_9.png)

*Teaching figure (synthetic).* Cycle-699 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle697_swarm_ch09_w697_9.png)

*Teaching figure (synthetic).* Cycle-697 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle695_swarm_ch09_w695_9.png)

*Teaching figure (synthetic).* Cycle-695 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle693_swarm_ch09_w693_9.png)

*Teaching figure (synthetic).* Cycle-693 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle691_swarm_ch09_w691_9.png)

*Teaching figure (synthetic).* Cycle-691 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle689_swarm_ch09_w689_9.png)

*Teaching figure (synthetic).* Cycle-689 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle687_swarm_ch09_w687_9.png)

*Teaching figure (synthetic).* Cycle-687 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle685_swarm_ch09_w685_9.png)

*Teaching figure (synthetic).* Cycle-685 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle683_swarm_ch09_w683_9.png)

*Teaching figure (synthetic).* Cycle-683 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle681_swarm_ch09_w681_9.png)

*Teaching figure (synthetic).* Cycle-681 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle679_swarm_ch09_w679_9.png)

*Teaching figure (synthetic).* Cycle-679 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle677_swarm_ch09_w677_9.png)

*Teaching figure (synthetic).* Cycle-677 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle675_swarm_ch09_w675_9.png)

*Teaching figure (synthetic).* Cycle-675 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle673_swarm_ch09_w673_9.png)

*Teaching figure (synthetic).* Cycle-673 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle671_swarm_ch09_w671_9.png)

*Teaching figure (synthetic).* Cycle-671 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle669_swarm_ch09_w669_9.png)

*Teaching figure (synthetic).* Cycle-669 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle667_swarm_ch09_w667_9.png)

*Teaching figure (synthetic).* Cycle-667 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle665_swarm_ch09_w665_9.png)

*Teaching figure (synthetic).* Cycle-665 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle663_swarm_ch09_w663_9.png)

*Teaching figure (synthetic).* Cycle-663 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle661_swarm_ch09_w661_9.png)

*Teaching figure (synthetic).* Cycle-661 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle659_swarm_ch09_w659_9.png)

*Teaching figure (synthetic).* Cycle-659 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle657_swarm_ch09_w657_9.png)

*Teaching figure (synthetic).* Cycle-657 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle655_swarm_ch09_w655_9.png)

*Teaching figure (synthetic).* Cycle-655 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle653_swarm_ch09_w653_9.png)

*Teaching figure (synthetic).* Cycle-653 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle651_swarm_ch09_w651_9.png)

*Teaching figure (synthetic).* Cycle-651 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle649_swarm_ch09_w649_9.png)

*Teaching figure (synthetic).* Cycle-649 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle647_swarm_ch09_w647_9.png)

*Teaching figure (synthetic).* Cycle-647 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle645_swarm_ch09_w645_9.png)

*Teaching figure (synthetic).* Cycle-645 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle643_swarm_ch09_w643_9.png)

*Teaching figure (synthetic).* Cycle-643 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle641_swarm_ch09_w641_9.png)

*Teaching figure (synthetic).* Cycle-641 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle639_swarm_ch09_w639_9.png)

*Teaching figure (synthetic).* Cycle-639 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle637_swarm_ch09_w637_9.png)

*Teaching figure (synthetic).* Cycle-637 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle635_swarm_ch09_w635_9.png)

*Teaching figure (synthetic).* Cycle-635 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle633_swarm_ch09_w633_9.png)

*Teaching figure (synthetic).* Cycle-633 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle631_swarm_ch09_w631_9.png)

*Teaching figure (synthetic).* Cycle-631 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle629_swarm_ch09_w629_9.png)

*Teaching figure (synthetic).* Cycle-629 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle627_swarm_ch09_w627_9.png)

*Teaching figure (synthetic).* Cycle-627 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle625_swarm_ch09_w625_9.png)

*Teaching figure (synthetic).* Cycle-625 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle623_swarm_ch09_w623_9.png)

*Teaching figure (synthetic).* Cycle-623 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle621_swarm_ch09_w621_9.png)

*Teaching figure (synthetic).* Cycle-621 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle619_swarm_ch09_w619_9.png)

*Teaching figure (synthetic).* Cycle-619 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle617_swarm_ch09_w617_9.png)

*Teaching figure (synthetic).* Cycle-617 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle615_swarm_ch09_w615_9.png)

*Teaching figure (synthetic).* Cycle-615 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle613_swarm_ch09_w613_9.png)

*Teaching figure (synthetic).* Cycle-613 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle611_swarm_ch09_w611_9.png)

*Teaching figure (synthetic).* Cycle-611 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle609_swarm_ch09_w609_9.png)

*Teaching figure (synthetic).* Cycle-609 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle607_swarm_ch09_w607_9.png)

*Teaching figure (synthetic).* Cycle-607 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle605_swarm_ch09_w605_9.png)

*Teaching figure (synthetic).* Cycle-605 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle603_swarm_ch09_w603_9.png)

*Teaching figure (synthetic).* Cycle-603 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle601_swarm_ch09_w601_9.png)

*Teaching figure (synthetic).* Cycle-601 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle599_swarm_ch09_w599_9.png)

*Teaching figure (synthetic).* Cycle-599 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle597_swarm_ch09_w597_9.png)

*Teaching figure (synthetic).* Cycle-597 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle595_swarm_ch09_w595_9.png)

*Teaching figure (synthetic).* Cycle-595 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle593_swarm_ch09_w593_9.png)

*Teaching figure (synthetic).* Cycle-593 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle591_swarm_ch09_w591_9.png)

*Teaching figure (synthetic).* Cycle-591 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle589_swarm_ch09_w589_9.png)

*Teaching figure (synthetic).* Cycle-589 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle587_swarm_ch09_w587_9.png)

*Teaching figure (synthetic).* Cycle-587 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle585_swarm_ch09_w585_9.png)

*Teaching figure (synthetic).* Cycle-585 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle583_swarm_ch09_w583_9.png)

*Teaching figure (synthetic).* Cycle-583 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle581_swarm_ch09_w581_9.png)

*Teaching figure (synthetic).* Cycle-581 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle579_swarm_ch09_w579_9.png)

*Teaching figure (synthetic).* Cycle-579 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle577_swarm_ch09_w577_9.png)

*Teaching figure (synthetic).* Cycle-577 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle575_swarm_ch09_w575_9.png)

*Teaching figure (synthetic).* Cycle-575 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle573_swarm_ch09_w573_9.png)

*Teaching figure (synthetic).* Cycle-573 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle571_swarm_ch09_w571_9.png)

*Teaching figure (synthetic).* Cycle-571 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle569_swarm_ch09_w569_9.png)

*Teaching figure (synthetic).* Cycle-569 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle567_swarm_ch09_w567_9.png)

*Teaching figure (synthetic).* Cycle-567 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle565_swarm_ch09_w565_9.png)

*Teaching figure (synthetic).* Cycle-565 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle563_swarm_ch09_w563_9.png)

*Teaching figure (synthetic).* Cycle-563 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle561_swarm_ch09_w561_9.png)

*Teaching figure (synthetic).* Cycle-561 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle559_swarm_ch09_w559_9.png)

*Teaching figure (synthetic).* Cycle-559 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle557_swarm_ch09_w557_9.png)

*Teaching figure (synthetic).* Cycle-557 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle555_swarm_ch09_w555_9.png)

*Teaching figure (synthetic).* Cycle-555 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle553_swarm_ch09_w553_9.png)

*Teaching figure (synthetic).* Cycle-553 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle551_swarm_ch09_w551_9.png)

*Teaching figure (synthetic).* Cycle-551 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle549_swarm_ch09_w549_9.png)

*Teaching figure (synthetic).* Cycle-549 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle547_swarm_ch09_w547_9.png)

*Teaching figure (synthetic).* Cycle-547 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle545_swarm_ch09_w545_9.png)

*Teaching figure (synthetic).* Cycle-545 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle543_swarm_ch09_w543_9.png)

*Teaching figure (synthetic).* Cycle-543 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle541_swarm_ch09_w541_9.png)

*Teaching figure (synthetic).* Cycle-541 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle539_swarm_ch09_w539_9.png)

*Teaching figure (synthetic).* Cycle-539 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle537_swarm_ch09_w537_9.png)

*Teaching figure (synthetic).* Cycle-537 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle535_swarm_ch09_w535_9.png)

*Teaching figure (synthetic).* Cycle-535 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle533_swarm_ch09_w533_9.png)

*Teaching figure (synthetic).* Cycle-533 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle531_swarm_ch09_w531_9.png)

*Teaching figure (synthetic).* Cycle-531 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle529_swarm_ch09_w529_9.png)

*Teaching figure (synthetic).* Cycle-529 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle527_swarm_ch09_w527_9.png)

*Teaching figure (synthetic).* Cycle-527 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle525_swarm_ch09_w525_9.png)

*Teaching figure (synthetic).* Cycle-525 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle523_swarm_ch09_w523_9.png)

*Teaching figure (synthetic).* Cycle-523 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle521_swarm_ch09_w521_9.png)

*Teaching figure (synthetic).* Cycle-521 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle519_swarm_ch09_w519_9.png)

*Teaching figure (synthetic).* Cycle-519 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle517_swarm_ch09_w517_9.png)

*Teaching figure (synthetic).* Cycle-517 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle515_swarm_ch09_w515_9.png)

*Teaching figure (synthetic).* Cycle-515 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle513_swarm_ch09_w513_9.png)

*Teaching figure (synthetic).* Cycle-513 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle511_swarm_ch09_w511_9.png)

*Teaching figure (synthetic).* Cycle-511 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle509_swarm_ch09_w509_9.png)

*Teaching figure (synthetic).* Cycle-509 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle507_swarm_ch09_w507_9.png)

*Teaching figure (synthetic).* Cycle-507 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle505_swarm_ch09_w505_9.png)

*Teaching figure (synthetic).* Cycle-505 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle503_swarm_ch09_w503_9.png)

*Teaching figure (synthetic).* Cycle-503 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle501_swarm_ch09_w501_9.png)

*Teaching figure (synthetic).* Cycle-501 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle499_swarm_ch09_w499_9.png)

*Teaching figure (synthetic).* Cycle-499 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle497_swarm_ch09_w497_9.png)

*Teaching figure (synthetic).* Cycle-497 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle495_swarm_ch09_w495_9.png)

*Teaching figure (synthetic).* Cycle-495 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle493_swarm_ch09_w493_9.png)

*Teaching figure (synthetic).* Cycle-493 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle491_swarm_ch09_w491_9.png)

*Teaching figure (synthetic).* Cycle-491 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle489_swarm_ch09_w489_9.png)

*Teaching figure (synthetic).* Cycle-489 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle487_swarm_ch09_w487_9.png)

*Teaching figure (synthetic).* Cycle-487 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle485_swarm_ch09_w485_9.png)

*Teaching figure (synthetic).* Cycle-485 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle483_swarm_ch09_w483_9.png)

*Teaching figure (synthetic).* Cycle-483 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle481_swarm_ch09_w481_9.png)

*Teaching figure (synthetic).* Cycle-481 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle479_swarm_ch09_w479_9.png)

*Teaching figure (synthetic).* Cycle-479 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle477_swarm_ch09_w477_9.png)

*Teaching figure (synthetic).* Cycle-477 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle475_swarm_ch09_w475_9.png)

*Teaching figure (synthetic).* Cycle-475 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle473_swarm_ch09_w473_9.png)

*Teaching figure (synthetic).* Cycle-473 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle471_swarm_ch09_w471_9.png)

*Teaching figure (synthetic).* Cycle-471 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle469_swarm_ch09_w469_9.png)

*Teaching figure (synthetic).* Cycle-469 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle467_swarm_ch09_w467_9.png)

*Teaching figure (synthetic).* Cycle-467 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle465_swarm_ch09_w465_9.png)

*Teaching figure (synthetic).* Cycle-465 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle463_swarm_ch09_w463_9.png)

*Teaching figure (synthetic).* Cycle-463 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle461_swarm_ch09_w461_9.png)

*Teaching figure (synthetic).* Cycle-461 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle459_swarm_ch09_w459_9.png)

*Teaching figure (synthetic).* Cycle-459 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle457_swarm_ch09_w457_9.png)

*Teaching figure (synthetic).* Cycle-457 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle455_swarm_ch09_w455_9.png)

*Teaching figure (synthetic).* Cycle-455 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle453_swarm_ch09_w453_9.png)

*Teaching figure (synthetic).* Cycle-453 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle451_swarm_ch09_w451_9.png)

*Teaching figure (synthetic).* Cycle-451 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle449_swarm_ch09_w449_9.png)

*Teaching figure (synthetic).* Cycle-449 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle447_swarm_ch09_w447_9.png)

*Teaching figure (synthetic).* Cycle-447 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle445_swarm_ch09_w445_9.png)

*Teaching figure (synthetic).* Cycle-445 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle443_swarm_ch09_w443_9.png)

*Teaching figure (synthetic).* Cycle-443 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle441_swarm_ch09_w441_9.png)

*Teaching figure (synthetic).* Cycle-441 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle439_swarm_ch09_w439_9.png)

*Teaching figure (synthetic).* Cycle-439 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle437_swarm_ch09_w437_9.png)

*Teaching figure (synthetic).* Cycle-437 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle435_swarm_ch09_w435_9.png)

*Teaching figure (synthetic).* Cycle-435 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle433_swarm_ch09_w433_9.png)

*Teaching figure (synthetic).* Cycle-433 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle431_swarm_ch09_w431_9.png)

*Teaching figure (synthetic).* Cycle-431 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle429_swarm_ch09_w429_9.png)

*Teaching figure (synthetic).* Cycle-429 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle427_swarm_ch09_w427_9.png)

*Teaching figure (synthetic).* Cycle-427 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle425_swarm_ch09_w425_9.png)

*Teaching figure (synthetic).* Cycle-425 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle423_swarm_ch09_w423_9.png)

*Teaching figure (synthetic).* Cycle-423 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle421_swarm_ch09_w421_9.png)

*Teaching figure (synthetic).* Cycle-421 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle419_swarm_ch09_w419_9.png)

*Teaching figure (synthetic).* Cycle-419 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle417_swarm_ch09_w417_9.png)

*Teaching figure (synthetic).* Cycle-417 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle415_swarm_ch09_w415_9.png)

*Teaching figure (synthetic).* Cycle-415 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle413_swarm_ch09_w413_9.png)

*Teaching figure (synthetic).* Cycle-413 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle411_swarm_ch09_w411_9.png)

*Teaching figure (synthetic).* Cycle-411 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle409_swarm_ch09_w409_9.png)

*Teaching figure (synthetic).* Cycle-409 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle407_swarm_ch09_w407_9.png)

*Teaching figure (synthetic).* Cycle-407 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle405_swarm_ch09_w405_9.png)

*Teaching figure (synthetic).* Cycle-405 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle403_swarm_ch09_w403_9.png)

*Teaching figure (synthetic).* Cycle-403 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle401_swarm_ch09_w401_9.png)

*Teaching figure (synthetic).* Cycle-401 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle399_swarm_ch09_w399_9.png)

*Teaching figure (synthetic).* Cycle-399 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle397_swarm_ch09_w397_9.png)

*Teaching figure (synthetic).* Cycle-397 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle395_swarm_ch09_w395_9.png)

*Teaching figure (synthetic).* Cycle-395 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle393_swarm_ch09_w393_9.png)

*Teaching figure (synthetic).* Cycle-393 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle391_swarm_ch09_w391_9.png)

*Teaching figure (synthetic).* Cycle-391 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle389_swarm_ch09_w389_9.png)

*Teaching figure (synthetic).* Cycle-389 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle387_swarm_ch09_w387_9.png)

*Teaching figure (synthetic).* Cycle-387 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle385_swarm_ch09_w385_9.png)

*Teaching figure (synthetic).* Cycle-385 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle383_swarm_ch09_w383_9.png)

*Teaching figure (synthetic).* Cycle-383 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle381_swarm_ch09_w381_9.png)

*Teaching figure (synthetic).* Cycle-381 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle379_swarm_ch09_w379_9.png)

*Teaching figure (synthetic).* Cycle-379 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle377_swarm_ch09_w377_9.png)

*Teaching figure (synthetic).* Cycle-377 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle375_swarm_ch09_w375_9.png)

*Teaching figure (synthetic).* Cycle-375 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle373_swarm_ch09_w373_9.png)

*Teaching figure (synthetic).* Cycle-373 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle371_swarm_ch09_w371_9.png)

*Teaching figure (synthetic).* Cycle-371 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle369_swarm_ch09_w369_9.png)

*Teaching figure (synthetic).* Cycle-369 densify scientific residual.


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle367_swarm_ch09_w367_9.png)

*Teaching figure (synthetic).* Cycle-367 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle365_swarm_ch09_w365_9.png)

*Teaching figure (synthetic).* Cycle-365 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle363_swarm_ch09_w363_9.png)

*Teaching figure (synthetic).* Cycle-363 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle361_swarm_ch09_w361_9.png)

*Teaching figure (synthetic).* Cycle-361 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle359_swarm_ch09_w359_9.png)

*Teaching figure (synthetic).* Cycle-359 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle357_swarm_ch09_w357_9.png)

*Teaching figure (synthetic).* Cycle-357 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle355_swarm_ch09_w355_9.png)

*Teaching figure (synthetic).* Cycle-355 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle353_swarm_ch09_w353_9.png)

*Teaching figure (synthetic).* Cycle-353 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle351_swarm_ch09_w351_9.png)

*Teaching figure (synthetic).* Cycle-351 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle349_swarm_ch09_w349_9.png)

*Teaching figure (synthetic).* Cycle-349 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle347_swarm_ch09_w347_9.png)

*Teaching figure (synthetic).* Cycle-347 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle345_swarm_ch09_w345_9.png)

*Teaching figure (synthetic).* Cycle-345 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle343_swarm_ch09_w343_9.png)

*Teaching figure (synthetic).* Cycle-343 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle341_swarm_ch09_w341_9.png)

*Teaching figure (synthetic).* Cycle-341 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle339_swarm_ch09_w339_9.png)

*Teaching figure (synthetic).* Cycle-339 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle337_swarm_ch09_w337_9.png)

*Teaching figure (synthetic).* Cycle-337 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle335_swarm_ch09_w335_9.png)

*Teaching figure (synthetic).* Cycle-335 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle333_swarm_ch09_w333_9.png)

*Teaching figure (synthetic).* Cycle-333 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle331_swarm_ch09_w331_9.png)

*Teaching figure (synthetic).* Cycle-331 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle329_swarm_ch09_w329_9.png)

*Teaching figure (synthetic).* Cycle-329 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle327_swarm_ch09_w327_9.png)

*Teaching figure (synthetic).* Cycle-327 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle325_swarm_ch09_w325_9.png)

*Teaching figure (synthetic).* Cycle-325 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle323_swarm_ch09_w323_9.png)

*Teaching figure (synthetic).* Cycle-323 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle321_swarm_ch09_w321_9.png)

*Teaching figure (synthetic).* Cycle-321 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle319_swarm_ch09_w319_9.png)

*Teaching figure (synthetic).* Cycle-319 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle317_swarm_ch09_w317_9.png)

*Teaching figure (synthetic).* Cycle-317 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle315_swarm_ch09_w315_9.png)

*Teaching figure (synthetic).* Cycle-315 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle313_swarm_ch09_w313_9.png)

*Teaching figure (synthetic).* Cycle-313 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle311_swarm_ch09_w311_9.png)

*Teaching figure (synthetic).* Cycle-311 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle309_swarm_ch09_w309_9.png)

*Teaching figure (synthetic).* Cycle-309 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle307_swarm_ch09_w307_9.png)

*Teaching figure (synthetic).* Cycle-307 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle305_swarm_ch09_w305_9.png)

*Teaching figure (synthetic).* Cycle-305 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle303_swarm_ch09_w303_9.png)

*Teaching figure (synthetic).* Cycle-303 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle301_swarm_ch09_w301_9.png)

*Teaching figure (synthetic).* Cycle-301 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle299_swarm_ch09_w299_9.png)

*Teaching figure (synthetic).* Cycle-299 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle297_swarm_ch09_w297_9.png)

*Teaching figure (synthetic).* Cycle-297 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle295_swarm_ch09_w295_9.png)

*Teaching figure (synthetic).* Cycle-295 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle293_swarm_ch09_w293_9.png)

*Teaching figure (synthetic).* Cycle-293 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle291_swarm_ch09_w291_9.png)

*Teaching figure (synthetic).* Cycle-291 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle289_swarm_ch09_w289_9.png)

*Teaching figure (synthetic).* Cycle-289 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle287_swarm_ch09_w287_9.png)

*Teaching figure (synthetic).* Cycle-287 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle285_swarm_ch09_w285_9.png)

*Teaching figure (synthetic).* Cycle-285 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle283_swarm_ch09_w283_9.png)

*Teaching figure (synthetic).* Cycle-283 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle281_swarm_ch09_w281_9.png)

*Teaching figure (synthetic).* Cycle-281 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle279_swarm_ch09_w279_9.png)

*Teaching figure (synthetic).* Cycle-279 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle277_swarm_ch09_w277_9.png)

*Teaching figure (synthetic).* Cycle-277 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle275_swarm_ch09_w275_9.png)

*Teaching figure (synthetic).* Cycle-275 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle273_swarm_ch09_w273_9.png)

*Teaching figure (synthetic).* Cycle-273 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle271_swarm_ch09_w271_9.png)

*Teaching figure (synthetic).* Cycle-271 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle269_swarm_ch09_w269_9.png)

*Teaching figure (synthetic).* Cycle-269 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle267_swarm_ch09_w267_9.png)

*Teaching figure (synthetic).* Cycle-267 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle265_swarm_ch09_w265_9.png)

*Teaching figure (synthetic).* Cycle-265 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle263_swarm_ch09_w263_9.png)

*Teaching figure (synthetic).* Cycle-263 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle261_swarm_ch09_w261_9.png)

*Teaching figure (synthetic).* Cycle-261 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle259_swarm_ch09_w259_9.png)

*Teaching figure (synthetic).* Cycle-259 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle257_swarm_ch09_w257_9.png)

*Teaching figure (synthetic).* Cycle-257 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle255_swarm_ch09_w255_9.png)

*Teaching figure (synthetic).* Cycle-255 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle253_swarm_ch09_w253_9.png)

*Teaching figure (synthetic).* Cycle-253 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle251_swarm_ch09_w251_9.png)

*Teaching figure (synthetic).* Cycle-251 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle249_swarm_ch09_w249_9.png)

*Teaching figure (synthetic).* Cycle-249 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle247_swarm_ch09_w247_9.png)

*Teaching figure (synthetic).* Cycle-247 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle245_swarm_ch09_w245_9.png)

*Teaching figure (synthetic).* Cycle-245 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle243_swarm_ch09_w243_9.png)

*Teaching figure (synthetic).* Cycle-243 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle241_swarm_ch09_w241_9.png)

*Teaching figure (synthetic).* Cycle-241 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle239_swarm_ch09_w239_9.png)

*Teaching figure (synthetic).* Cycle-239 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle237_swarm_ch09_w237_9.png)

*Teaching figure (synthetic).* Cycle-237 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle235_swarm_ch09_w235_9.png)

*Teaching figure (synthetic).* Cycle-235 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle233_swarm_ch09_w233_9.png)

*Teaching figure (synthetic).* Cycle-233 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle231_swarm_ch09_w231_9.png)

*Teaching figure (synthetic).* Cycle-231 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle229_swarm_ch09_w229_9.png)

*Teaching figure (synthetic).* Cycle-229 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle227_swarm_ch09_w227_9.png)

*Teaching figure (synthetic).* Cycle-227 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle225_swarm_ch09_w225_9.png)

*Teaching figure (synthetic).* Cycle-225 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle223_swarm_ch09_w223_9.png)

*Teaching figure (synthetic).* Cycle-223 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle221_swarm_ch09_w221_9.png)

*Teaching figure (synthetic).* Cycle-221 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle219_swarm_ch09_w219_9.png)

*Teaching figure (synthetic).* Cycle-219 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle217_swarm_ch09_w217_9.png)

*Teaching figure (synthetic).* Cycle-217 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle215_swarm_ch09_w215_9.png)

*Teaching figure (synthetic).* Cycle-215 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle213_swarm_ch09_w213_9.png)

*Teaching figure (synthetic).* Cycle-213 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle211_swarm_ch09_w211_9.png)

*Teaching figure (synthetic).* Cycle-211 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle209_swarm_ch09_w209_9.png)

*Teaching figure (synthetic).* Cycle-209 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle207_swarm_ch09_w207_9.png)

*Teaching figure (synthetic).* Cycle-207 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle205_swarm_ch09_w205_9.png)

*Teaching figure (synthetic).* Cycle-205 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle203_swarm_ch09_w203_9.png)

*Teaching figure (synthetic).* Cycle-203 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle201_swarm_ch09_w201_9.png)

*Teaching figure (synthetic).* Cycle-201 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle199_swarm_ch09_w199_9.png)

*Teaching figure (synthetic).* Cycle-199 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle197_swarm_ch09_w197_9.png)

*Teaching figure (synthetic).* Cycle-197 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle195_swarm_ch09_w195_9.png)

*Teaching figure (synthetic).* Cycle-195 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle193_swarm_ch09_w193_9.png)

*Teaching figure (synthetic).* Cycle-193 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle191_swarm_ch09_w191_9.png)

*Teaching figure (synthetic).* Cycle-191 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle189_swarm_ch09_w189_9.png)

*Teaching figure (synthetic).* Cycle-189 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle187_swarm_ch09_w187_9.png)

*Teaching figure (synthetic).* Cycle-187 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle185_swarm_ch09_w185_9.png)

*Teaching figure (synthetic).* Cycle-185 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle183_swarm_ch09_w183_9.png)

*Teaching figure (synthetic).* Cycle-183 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle181_swarm_ch09_w181_9.png)

*Teaching figure (synthetic).* Cycle-181 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle179_swarm_ch09_w179_9.png)

*Teaching figure (synthetic).* Cycle-179 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle177_swarm_ch09_w177_9.png)

*Teaching figure (synthetic).* Cycle-177 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle175_swarm_ch09_w175_9.png)

*Teaching figure (synthetic).* Cycle-175 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle173_swarm_ch09_w173_9.png)

*Teaching figure (synthetic).* Cycle-173 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle171_swarm_ch09_w171_9.png)

*Teaching figure (synthetic).* Cycle-171 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle169_swarm_ch09_w169_9.png)

*Teaching figure (synthetic).* Cycle-169 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle167_swarm_ch09_w167_9.png)

*Teaching figure (synthetic).* Cycle-167 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle165_swarm_ch09_w165_9.png)

*Teaching figure (synthetic).* Cycle-165 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle163_swarm_ch09_w163_9.png)

*Teaching figure (synthetic).* Cycle-163 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle161_swarm_ch09_w161_9.png)

*Teaching figure (synthetic).* Cycle-161 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle159_swarm_ch09_w159_9.png)

*Teaching figure (synthetic).* Cycle-159 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle157_swarm_ch09_w157_9.png)

*Teaching figure (synthetic).* Cycle-157 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle155_swarm_ch09_w155_9.png)

*Teaching figure (synthetic).* Cycle-155 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle153_swarm_ch09_w153_9.png)

*Teaching figure (synthetic).* Cycle-153 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle151_swarm_ch09_w151_9.png)

*Teaching figure (synthetic).* Cycle-151 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle149_swarm_ch09_w149_9.png)

*Teaching figure (synthetic).* Cycle-149 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle147_swarm_ch09_w147_9.png)

*Teaching figure (synthetic).* Cycle-147 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle145_swarm_ch09_w145_9.png)

*Teaching figure (synthetic).* Cycle-145 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle143_swarm_ch09_w143_9.png)

*Teaching figure (synthetic).* Cycle-143 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle141_swarm_ch09_w141_9.png)

*Teaching figure (synthetic).* Cycle-141 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle139_swarm_ch09_w139_9.png)

*Teaching figure (synthetic).* Cycle-139 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle137_swarm_ch09_w137_9.png)

*Teaching figure (synthetic).* Cycle-137 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle135_swarm_ch09_w135_9.png)

*Teaching figure (synthetic).* Cycle-135 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle133_swarm_ch09_w133_9.png)

*Teaching figure (synthetic).* Cycle-133 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle131_swarm_ch09_w131_9.png)

*Teaching figure (synthetic).* Cycle-131 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle129_swarm_ch09_w129_9.png)

*Teaching figure (synthetic).* Cycle-129 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle127_swarm_ch09_w127_9.png)

*Teaching figure (synthetic).* Cycle-127 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle125_swarm_ch09_w125_9.png)

*Teaching figure (synthetic).* Cycle-125 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle123_swarm_ch09_w123_9.png)

*Teaching figure (synthetic).* Cycle-123 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle121_swarm_ch09_w121_9.png)

*Teaching figure (synthetic).* Cycle-121 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle119_swarm_ch09_w119_9.png)

*Teaching figure (synthetic).* Cycle-119 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle117_swarm_ch09_w117_9.png)

*Teaching figure (synthetic).* Cycle-117 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle115_swarm_ch09_w115_9.png)

*Teaching figure (synthetic).* Cycle-115 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle113_swarm_ch09_w113_9.png)

*Teaching figure (synthetic).* Cycle-113 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle111_swarm_ch09_w111_9.png)

*Teaching figure (synthetic).* Cycle-111 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle109_swarm_ch09_w109_9.png)

*Teaching figure (synthetic).* Cycle-109 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle107_swarm_ch09_w107_9.png)

*Teaching figure (synthetic).* Cycle-107 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle105_swarm_ch09_w105_9.png)

*Teaching figure (synthetic).* Cycle-105 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle103_swarm_ch09_w103_9.png)

*Teaching figure (synthetic).* Cycle-103 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle101_swarm_ch09_w101_9.png)

*Teaching figure (synthetic).* Cycle-101 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle99_swarm_ch09_w99_9.png)

*Teaching figure (synthetic).* Cycle-99 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle97_swarm_ch09_w97_9.png)

*Teaching figure (synthetic).* Cycle-97 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle95_swarm_ch09_w95_9.png)

*Teaching figure (synthetic).* Cycle-95 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle93_swarm_ch09_w93_9.png)

*Teaching figure (synthetic).* Cycle-93 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle91_swarm_ch09_w91_9.png)

*Teaching figure (synthetic).* Cycle-91 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle89_swarm_ch09_w89_9.png)

*Teaching figure (synthetic).* Cycle-89 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle87_swarm_ch09_w87_9.png)

*Teaching figure (synthetic).* Cycle-87 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle85_swarm_ch09_w85_9.png)

*Teaching figure (synthetic).* Cycle-85 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle83_swarm_ch09_w83_9.png)

*Teaching figure (synthetic).* Cycle-83 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle81_swarm_ch09_w81_9.png)

*Teaching figure (synthetic).* Cycle-81 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle79_swarm_ch09_w79_9.png)

*Teaching figure (synthetic).* Cycle-79 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle77_swarm_ch09_w77_9.png)

*Teaching figure (synthetic).* Cycle-77 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle75_swarm_ch09_w75_9.png)

*Teaching figure (synthetic).* Cycle-75 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle73_swarm_ch09_w73_9.png)

*Teaching figure (synthetic).* Cycle-73 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle71_swarm_ch09_w71_9.png)

*Teaching figure (synthetic).* Cycle-71 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle69_swarm_ch09_w69_9.png)

*Teaching figure (synthetic).* Cycle-69 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle67_swarm_ch09_w67_9.png)

*Teaching figure (synthetic).* Cycle-67 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle65_swarm_ch09_w65_9.png)

*Teaching figure (synthetic).* Cycle-65 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle63_swarm_ch09_w63_9.png)

*Teaching figure (synthetic).* Cycle-63 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle61_swarm_ch09_w61_9.png)

*Teaching figure (synthetic).* Cycle-61 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle59_swarm_ch09_c59i.png)

*Teaching figure (synthetic).* Cycle-59 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle57_swarm_ch09_c57i.png)

*Teaching figure (synthetic).* Cycle-57 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle55_swarm_ch09_ext_cal.png)

*Teaching figure (synthetic).* Cycle-55 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle53_swarm_ch09_pred_cause.png)

*Teaching figure (synthetic).* Cycle-53 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle51_swarm_ch09_overfit_cal.png)

*Teaching figure (synthetic).* Cycle-51 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle49_swarm_ch09_recal.png)

*Teaching figure (synthetic).* Cycle-49 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle47_swarm_ch09_optimism.png)

*Teaching figure (synthetic).* Cycle-47 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle45_swarm_ch09_calplot.png)

*Teaching figure (synthetic).* Cycle-45 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle43_swarm_ch09_extval.png)

*Teaching figure (synthetic).* Cycle-43 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle41_swarm_ch09_cal_vs_auc.png)

*Teaching figure (synthetic).* Cycle-41 densify scientific residual (ch01–14).


![Cycle densify scientific residual for chapter 09 (original scientific teaching figure).](../assets/figures/cycle39_swarm_ch09_overfit.png)

*Teaching figure (synthetic).* Cycle-39 densify scientific residual (ch01–14).



Clinical neurology generates scoring systems at a relentless pace. The National Institutes of Health Stroke Scale (NIHSS) originated as a reproducible severity measure but rapidly mutated into a prognostic heuristic. The ICH Score predicts thirty-day mortality after intracerebral hemorrhage. The ABCD2 score stratifies the short-term probability of stroke following a transient ischemic attack. Modern machine learning algorithms digest raw non-contrast computed tomography images to predict large vessel occlusion, while others aggregate electronic health record data to forecast malignant cerebral edema. Despite this saturation, the fundamental error committed by clinicians and researchers alike is conflating a prediction model with a causal model. This conflation routinely poisons journal clubs and distorts clinical guidelines.

A prediction paper claims that a mathematical function of inputs, measured at a strict index time, maps to the probability of a future state with a quantified degree of accuracy. It operates entirely within the domain of joint probability distributions. It does not claim that intervening on those input variables will change the outcome. A causal treatment paper, by contrast, claims that changing an exposure directly alters the trajectory of the outcome, operating within the domain of counterfactuals (as established in Chapter 3). The distinction is absolute and non-negotiable.

If an observational stroke registry derives a multivariable logistic regression model for ninety-day functional independence and reports that statin use at admission carries an odds ratio of 1.4, this constitutes a predictive association. It indicates that statin users, within the specific context and confounding structure of that dataset, possess a higher probability of a favorable outcome. It explicitly does not mean that initiating a statin in the emergency department causes the good outcome. The statin variable acts as a proxy; it likely identifies patients who have consistent primary care access, fewer swallowing deficits, or lower baseline frailty. When audiences pivot seamlessly from an impressive area under the receiver operating characteristic curve (AUROC) to concluding 'we should treat these patients differently based on these variables,' they commit a severe category error. Prediction tools rank patients by risk; they do not identify which patients benefit from a specific intervention. Identifying benefit requires treatment effect heterogeneity analysis within a causal framework.

This chapter establishes a rigorous critical appraisal framework for prognosis and prediction literature. It dismantles the false idol of discrimination (AUROC), elevating calibration and clinical utility as the definitive measures of a prediction model's worth. It enforces strict time zero discipline, penalizes algorithmic overfitting, demands stringent validation structures, and applies the TRIPOD reporting guidelines alongside the PROBAST risk of bias tool. By the end of this chapter, you will possess the quantitative vocabulary to dismantle flawed predictive claims and implement mathematically sound decision analysis at the bedside.

## Taxonomy of Claims: Prognosis, Prediction, and Diagnosis

Scientific claims in the medical literature divide into diagnostic, prognostic, and causal categories. Diagnosis asks: What is the true state of the patient right now? Diagnostic accuracy models (detailed in Chapter 4) classify current, unseen states by referencing a gold standard. Does this specific patient have a large vessel occlusion? Is this lobar hemorrhage secondary to cerebral amyloid angiopathy? The dominant threats to validity in diagnostic modeling center on the reference standard itself—specifically verification bias, spectrum bias, and the use of imperfect or subjective gold standards. In diagnostic studies, the predictor and the outcome occur synchronously.

Prognosis asks: What will happen to this patient in the future under a defined, existing clinical care pathway? What is the probability of symptomatic intracranial hemorrhage after the administration of intravenous alteplase? What is the chance of regaining independent ambulation at six months post-stroke? Prognosis inherently involves the forward passage of time. Consequently, its primary validity threats involve longitudinal mechanics: loss to follow-up (informative censoring), competing risks (such as death occurring prior to the planned functional assessment), and secular changes in the standard of care over the follow-up period.

Prediction refers to the statistical machinery utilized to estimate individualized probabilities. Modern literature uses the term 'prediction model' loosely to encompass both diagnostic classifiers and prognostic risk scores. This conflation is problematic because time enforces a strict logic on prognostic prediction that diagnostic modeling lacks. A diagnostic algorithm for large vessel occlusion on CT angiography evaluates synchronous pixels. A prognostic algorithm for ninety-day modified Rankin Scale (mRS) must strictly segregate data available at the exact moment of prediction from events that unfold subsequently. Your first task as an appraiser is forcing clarity: Is the model estimating a concurrent state or forecasting a future event?

Crucially, prognosis is not equivalent to the natural history of a disease under a state of therapeutic nihilism. Modern neurological care is intensely interventional. Prognostic models estimated in the era of mechanical thrombectomy describe outcomes under that specific prevailing care regime. They are valid for counseling only if the patient receives that standard of care. If authors imply their prognostic model identifies patients who 'need' thrombectomy without formally estimating the interaction between the baseline features and the treatment effect (a causal claim), they have overstepped the mathematical boundaries of their design.

## Anatomy of a Prediction Model: Time Zero, Predictors, and Horizon

The structural integrity of a prediction model rests on three pillars: time zero, the predictor set, and the prediction horizon. Time zero (or index time) is the precise, definable moment in the clinical workflow when the model is intended to be executed. A model's validity hinges entirely on uncompromising adherence to time zero discipline. If a tool is designed to guide emergency department triage prior to advanced neuroimaging, its time zero is the moment of emergency department arrival. At that precise second, age, vital signs, and baseline NIHSS are knowable. Final infarct volume, door-to-needle time, and hospital-acquired complications are not.

Index-time leakage constitutes a fatal flaw in predictive modeling. Leakage occurs when information from the future—or information generated as a consequence of the outcome pathway—surreptitiously bleeds into the predictor set. A classic failure mode in the stroke literature involves predicting ninety-day functional outcome using 'final infarct volume on day 3 MRI' or 'discharge disposition' as baseline features for an admission model. These variables correlate massively with the outcome precisely because they are intermediate steps on the causal pathway to that outcome. Incorporating them inflates apparent accuracy to near-perfect levels, but renders the model clinically useless. A clinician cannot input a discharge disposition on day one.

Electronic health record models are uniquely vulnerable to stealth leakage. A billing code for 'cerebral edema' might be timestamped at hospital day three, but if the researcher crudely pulls all codes associated with the encounter into a 'baseline' matrix, the future has leaked into the past. Clinical notes utilized for natural language processing routinely contain trailing information; an admission note dictated twelve hours after arrival may casually reference the patient's subsequent deterioration or response to initial therapy. Timestamp discipline must be absolute. The appraiser must ask: Could a conscientious clinician, standing at time zero, execute this equation using only data mathematically confirmed to exist at that moment?

The prediction horizon is the specific future time point at which the outcome is ascertained. A prediction of mortality at seven days represents a fundamentally different biological construct than mortality at one year. The horizon must align with the clinical decision being made at time zero. Furthermore, the predictors (features) must be rigidly defined, reproducible across different health systems, and measured without knowledge of the future outcome. When dealing with continuous predictors such as age, systolic blood pressure, or glucose, categorization (e.g., dichotomizing age at 80 years) is a destructive practice. It discards immense amounts of information, slashes statistical power, and enforces a biologically implausible assumption of a flat risk profile on either side of the arbitrary threshold. Continuous relationships must be modeled using splines or fractional polynomials to preserve the natural density of the clinical data.

![Horizon-specific absolute cumulative risks for high- vs low-risk strata; deployment needs calibration at that horizon plus an action that changes care—not a causal treat license (original teaching figure).](../assets/figures/cycle8_swarm_ch09_horizon_risk.png)

*Teaching figure (synthetic).* Prognosis is a calendar of absolute risks, not a single AUROC. Match the horizon to the decision, recalibrate to local mix, and remember prediction ≠ causation for treatment choice.

## Quantitative Reasoning: Discrimination

![Discrimination ranks patients; absolute treat policy needs calibrated thresholds—pred≠cause (original teaching figure).](../assets/figures/cycle18_swarm_ch09_disc_vs_decision.png)

*Teaching figure (synthetic).* High AUROC is not a treat license; thresholds and causal ARR are separate claims.

Discrimination quantifies a prediction model's ability to separate patients who experience the outcome from those who do not. It asks a strictly relative question: Does the algorithm consistently assign higher predicted probabilities to the cohort of patients who actually suffer the event compared to those who remain event-free?

For binary outcomes, discrimination is almost universally quantified by the c-statistic (concordance statistic), which is mathematically equivalent to the Area Under the Receiver Operating Characteristic curve (AUROC). To comprehend the c-statistic precisely, consider all possible pairs of patients in a dataset where exactly one patient experienced the event and the other did not. A pair is deemed 'concordant' if the model assigned a higher predicted probability to the patient who had the event. The c-statistic is simply the proportion of these pairs that are concordant. The formula is: c = (Number of concordant pairs + 0.5 * Number of tied pairs) / (Total discordant and concordant pairs).

An AUROC of 0.50 indicates random guessing; the model is equally likely to assign a higher probability to the non-event patient. An AUROC of 1.0 indicates flawless mathematical separation. An AUROC of 0.75 means that if you randomly select one patient who died and one who lived, there is a 75% probability the model assigned a higher mortality risk to the patient who died. In survival analysis scenarios—where time-to-event data is subject to censoring—Harrell's C-index serves as the standard analog, calculating concordance only among pairs of patients whose temporal ordering of events is definitively knowable.

The neurology literature systematically fetishizes AUROC, treating it as the ultimate proxy for clinical value. This is a profound analytic error. AUROC measures rank-order separation only; it contains exactly zero information regarding absolute risk accuracy. A model could assign probabilities of 0.001 and 0.002 to two patients, or alternatively 0.98 and 0.99. If the higher numerical risk is always assigned to the patient with the event, the AUROC remains a perfect 1.0, even if the absolute values are absurdly detached from clinical reality. A model that perfectly ranks patients but tells them all they have a 99% chance of death is useless for counseling.

Furthermore, AUROC is perilously insensitive to localized performance and highly vulnerable to dataset imbalance. In scenarios with extremely rare outcomes (e.g., predicting an event that occurs in 1% of the cohort), Precision-Recall curves are vastly superior to ROC curves. The standard ROC curve plots Sensitivity (True Positive Rate) against 1 - Specificity (False Positive Rate). Because True Negatives massively dominate the denominator of the False Positive Rate in rare events, the ROC curve is pulled artificially high, presenting a deceptively excellent profile. The Precision-Recall curve, conversely, plots Positive Predictive Value (Precision) against Sensitivity (Recall), mercilessly exposing the model's struggle to identify true positives amid a crushing volume of false alarms.

## Quantitative Reasoning: Calibration

![Absolute calibration bands: predicted vs observed risk; high score is for counseling, not a treat license without causal ARR (original teaching figure).](../assets/figures/cycle15_swarm_ch09_calib_abs_bands.png)

*Teaching figure (synthetic).* Pred ≠ cause: calibrate absolute risk freely; invent pathway NNTs only from causal contrasts.

Calibration measures the degree of agreement between estimated probabilities and the actual observed frequencies of the outcome. It asks the definitive absolute question: If the model dictates that a patient has a 20% risk of symptomatic intracerebral hemorrhage, and we assemble 100 identical patients, do approximately 20 of them actually bleed?

Calibration is the single most critical metric for any prediction model intended to guide clinical decision-making, direct resource allocation, or facilitate patient counseling. A poorly calibrated model with a high AUROC is actively dangerous; it dispenses incorrect absolute risks with unwarranted mathematical confidence. Calibration must be assessed across multiple dimensions.

Calibration-in-the-large compares the overall mean predicted probability to the overall observed event rate in the entire dataset. If the model predicts an average cohort risk of 15%, but the actual observed event rate is 30%, the model is systematically underpredicting. The simplest summary of calibration-in-the-large is the Observed/Expected (O/E) ratio: Total Observed Events divided by Total Expected Events (the sum of all predicted probabilities). The ideal O/E ratio is exactly 1.0.

Calibration curves (calibration plots) provide a granular visualization of this relationship across the entire risk spectrum. Patients are grouped by their predicted probability (e.g., into deciles, or utilizing smoothing techniques such as loess regression). The mean predicted probability within each group (plotted on the x-axis) is graphed against the observed proportion of events in that same group (plotted on the y-axis). The ideal calibration curve aligns perfectly with the 45-degree line of identity (y = x). A calibration plot is mathematically summarized by a calibration intercept and a calibration slope, derived by fitting a logistic regression of the observed binary outcome on the log-odds of the predicted probability. The calibration intercept reflects calibration-in-the-large; an ideal intercept is 0. An intercept of -0.5 indicates the model systematically overpredicts risk across the entire cohort. The calibration slope indicates the spread or extremeness of the predictions. The ideal slope is 1.0. A slope less than 1.0 signifies that the predictions are too extreme (high risks are overestimated, low risks are underestimated), which is the classic, unassailable signature of model overfitting. A slope greater than 1.0 indicates predictions are too narrow, suffering from excessive regression to the mean.

The Brier Score provides an omnibus measure of predictive accuracy, inextricably blending both discrimination and calibration. It is calculated as the mean squared difference between the predicted probability and the actual outcome (coded strictly as 1 for an event and 0 for no event). The formula is: Brier Score = (1/N) * sum(predicted_i - observed_i)^2. For a model predicting an event with a 50% baseline prevalence, blind random guessing yields a Brier score of 0.25. Lower Brier scores indicate superior overall performance, but a low Brier score does not absolve the researcher from presenting a detailed calibration plot.

## Development, Overfitting, and Optimism

![Optimism-corrected and external AUROC fall from derivation hype; absolute calibration fails first on overfit models (original teaching figure).](../assets/figures/cycle11_swarm_ch09_optimism_cal.png)

*Teaching figure (synthetic).* Do not counsel or threshold on derivation AUROC. Demand optimism correction and external absolute calibration.


When researchers feed a dataset containing 200 acute stroke patients and 40 baseline clinical variables into a multivariable logistic regression or a random forest algorithm, the mathematical machinery will aggressively fit the data. It will inevitably locate patterns that appear to predict the outcome with extraordinary precision. Unfortunately, the vast majority of what it discovers is noise—random statistical fluctuations idiosyncratic to those specific 200 patients.

This phenomenon is overfitting. Apparent performance (the AUROC and calibration metrics calculated on the exact same dataset utilized to train the model) is systematically and severely biased upward. It is an optimistic mathematical illusion. Optimism is defined as the quantitative difference between the apparent performance on the training data and the true performance expected when the model is applied to unseen, exchangeable patients. The primary driver of optimism is a low number of Events Per Variable (EPV). Historical rules of thumb mandated a minimum of 10 events per candidate predictor, though modern simulation studies demonstrate even this is frequently insufficient. While modern penalization methods (like Ridge or Lasso regression) mitigate this, extreme feature-to-event ratios remain computationally fatal. Critically, 'variable' refers to all candidate variables evaluated at any point during the modeling process, not merely the final variables surviving in the published equation. If authors tested 50 variables univariately to identify the 5 that 'worked,' they have spent 50 degrees of freedom, guaranteeing massive optimism.

Internal validation is the statistical methodology employed to quantify and correct for this optimism without requiring a separate external dataset. There are three primary approaches. First, split-sample validation (e.g., randomly holding out 30% of the data for testing) is historically common but statistically indefensible in small datasets. It squanders valuable training data, and the final evaluation relies entirely on a single, potentially anomalous holdout set. Second, cross-validation (e.g., 10-fold) partitions the data into 10 groups, training the model on 9 and testing on 1, iterating this process until all groups have served as the test set. This provides a more stable estimate of performance. Third, bootstrapping serves as the statistical gold standard for internal validation. It involves drawing hundreds of random samples (with replacement) from the original dataset, each exactly the same size as the original. The entire modeling process is executed on each bootstrap sample, and the resulting model is evaluated on the original dataset to calculate the optimism. This optimism is averaged across all bootstrap iterations and subtracted from the apparent performance to yield the optimism-corrected AUROC or C-statistic.

Crucially, internal validation is entirely worthless unless it wraps the entire modeling pipeline. If investigators perform univariable screening, select the significant variables, and then perform cross-validation or bootstrapping only on the final multivariable equation, they have committed 'pre-selection leakage.' The validation step fails to penalize the model for the massive optimism induced by the initial univariable screening, rendering the internal validation performative theater rather than rigorous science.

## External Validation and Transportability

Internal validation proves only that the mathematics are sound within the source population. External validation tests whether the underlying clinical biology transports to a new population. Without strict external validation, a prediction model is merely a localized hypothesis. External validation demands testing the model on a dataset collected by entirely different investigators, at a different institution, or in a distinctly different time period. The original model equation—complete with the exact intercept and unmodified beta coefficients—must be applied blindly to the new data. Re-estimating the coefficients on the new data is not validation; it is model updating.

Prediction models fail external validation for three primary reasons. First, True Overfitting: The original model captured statistical noise rather than biological signal, which obviously fails to replicate in new patients. Second, Case-mix variation: The external cohort possesses a different distribution of predictor variables or a different baseline risk. If a prediction tool for malignant middle cerebral artery syndrome is developed in a tertiary referral center (which receives a high prevalence of massive, catastrophic strokes) and tested in a community hospital (which sees a lower prevalence), the discrimination might remain stable, but the calibration will systematically drift, rendering absolute risk predictions inaccurate.

Third, Temporal drift: Medical care is not static. The ASTRAL score, developed in the early 2010s to predict 90-day outcomes after acute ischemic stroke, assigns points for time delay and initial severity. In the modern era of endovascular thrombectomy, the prognostic implications of a proximal large vessel occlusion have been radically altered. A model developed in 2012 will systematically overpredict catastrophic outcomes for thrombectomy-eligible patients in 2026. This phenomenon is temporal drift driven by a changing interventional regime. It necessitates formal recalibration (adjusting the intercept and slope to fit the new treatment era) or continuous algorithmic updating. An uncalibrated legacy score is a clinical hazard.

## Decision Curve Analysis and Clinical Utility

Calibration links theoretical probabilities to biological reality. Decision Curve Analysis (DCA) links those probabilities to actionable clinical utility. An AUROC of 0.85 cannot, under any circumstances, tell you if a model is useful to a clinician. Consider a predictive model designed to identify patients requiring a decompressive hemicraniectomy. Should we deploy it? That depends entirely on the threshold at which surgeons act, the profound harm of a false positive (inflicting an unnecessary craniectomy and resulting massive morbidity), and the fatal harm of a false negative (missed opportunity, resulting in herniation and death).

DCA requires the explicit definition of a Threshold Probability (Pt). Pt is the specific risk level at which a clinician is perfectly indifferent between taking the action and withholding it. If you decide to order a high-risk CT angiogram for a patient with a transient ischemic attack only if the probability of an underlying severe stenosis exceeds 10%, your Pt is 10%. This threshold inherently encodes the clinician's judgment regarding the relative harm of a false positive versus a false negative. Specifically, the harm ratio is calculated as Pt / (1 - Pt). At a 10% threshold, you are mathematically stating that missing a true positive is 9 times worse than enduring a false positive (0.10 / 0.90 = 1/9).

Decision Curve Analysis calculates the Net Benefit of using the prediction model across a continuous range of plausible threshold probabilities. The formula for Net Benefit is: Net Benefit = (True Positives / N) - (False Positives / N) * (Pt / (1 - Pt)). The subtraction of the weighted false positives ensures that the model is penalized according to the specific clinical harms defined by the threshold.

In a standard DCA plot, the Net Benefit of the prediction model (y-axis) is graphed against the Threshold Probability (x-axis). Crucially, the model is compared simultaneously against two default clinical strategies: 1) Treat All (acting as if everyone has the outcome). The Net Benefit line for 'Treat All' slopes downward as the threshold increases, crossing zero exactly at the overall prevalence of the disease in the cohort. 2) Treat None (acting as if nobody has the outcome). The Net Benefit for 'Treat None' is exactly zero across all thresholds.

A prediction model demonstrates genuine clinical utility if, and only if, its Net Benefit curve lies above both the 'Treat All' and 'Treat None' lines across a clinically reasonable range of thresholds. If a stroke model only demonstrates positive Net Benefit at thresholds of 80-90% for a highly consequential surgical intervention, but neurosurgeons actually intervene at a 20% threshold, the model is entirely useless in clinical practice, regardless of its statistical significance or AUROC. DCA forces prediction research out of the realm of abstract mathematics and into the brutal reality of clinical tradeoffs.

![High predicted risk is not a causal license to treat; decision-curve net benefit must beat treat-all and treat-none in the clinical Pt band (original teaching figure).](../assets/figures/cycle5_swarm_ch09_pred_vs_causal_dca.png)

*Teaching figure (synthetic).* Prognostic association (e.g., statin-at-admission OR) ranks risk; only calibrated absolute risk plus utility at a stated threshold justifies deployment. Prediction is not causation for treatment choice.

## Named Frameworks: TRIPOD and PROBAST

TRIPOD (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis) serves as the definitive EQUATOR network guideline for reporting prediction research. It acts as a defense against opaque methodology. TRIPOD demands explicit detailing of the study setting, inclusion criteria, rigorous definitions of predictors and outcomes, the explicit handling of missing data (differentiating biased complete-case deletion from multiple imputation), complete model specification, and the transparent reporting of both discrimination and calibration measures with confidence intervals.

PROBAST (Prediction model Risk Of Bias Assessment Tool) is the corresponding appraisal instrument used to evaluate the methodological quality of the published model. PROBAST forces the appraiser to evaluate Risk of Bias systematically across four critical domains: Participants (detecting inappropriate exclusions or highly selected cohorts), Predictors (identifying predictors defined using knowledge from the future), Outcome (flagging subjective outcomes adjudicated with unblinded knowledge of the predictors), and Analysis.

The Analysis domain in PROBAST is particularly unforgiving. It flags continuous variables that have been inappropriately dichotomized, models that ignore competing risks in survival data, studies suffering from insufficient events per variable, and pipelines that lack rigorous optimism correction. When reviewing a prediction paper, the clinical epidemiologist must mentally execute the PROBAST checklist. If the authors discard 40% of their cohort because of a missing NIHSS subscore (complete-case analysis), they have introduced severe selection bias. If they test 100 variables on a dataset with 50 events using automated stepwise selection and report an AUROC of 0.92 without bootstrapping, the model is hallucinating. PROBAST provides the vocabulary to reject these papers unequivocally.

## A Fully Worked Example: Evaluating a Post-Thrombectomy Prognostic Score

Scenario: A recent publication proposes the 'REPERFUSE-3' score to predict 90-day catastrophic outcome (defined as mRS 5-6) following mechanical thrombectomy. The authors develop the score on a cohort of 1,000 patients, observing 270 events (27% baseline prevalence). They assign points as follows: Age > 75 (1 point), Admission NIHSS > 15 (1 point), and Core Volume > 50cc (1 point). The maximum score is 3. They report an AUROC of 0.75 and conclude the model 'can guide aggressive end-of-life decision making in the neuro-ICU.' They provide the following raw validation data: Score 0 (N=300, Predicted Risk 0.05, Observed Events 15); Score 1 (N=400, Predicted Risk 0.15, Observed Events 80); Score 2 (N=200, Predicted Risk 0.40, Observed Events 90); Score 3 (N=100, Predicted Risk 0.85, Observed Events 85).

Step 1: Appraisal of the Claim and Time Zero. The proposed clinical action is 'end-of-life decision making.' The predictors (age, NIHSS, core volume) are available at admission, prior to thrombectomy. However, the score is named 'REPERFUSE' and the cohort consists exclusively of post-thrombectomy patients. Did the modeling process include final reperfusion status (e.g., TICI score)? If so, time zero is post-procedure, and the tool cannot be used for pre-procedure counseling. If not, time zero is pre-procedure, but the model is conditioned on the patient actually undergoing the procedure.

Step 2: Calibration Check via O/E Ratios. Let us manually calculate the Observed/Expected (O/E) ratio for Score 3. The Expected number of events = N * Predicted Risk = 100 * 0.85 = 85. The Observed number of events is 85. The O/E ratio = 85 / 85 = 1.0. At the extreme high end, calibration is perfect. Now analyze Score 0: Expected events = 300 * 0.05 = 15. Observed events = 15. The O/E ratio = 15 / 15 = 1.0. The calibration is remarkably precise across the risk spectrum, indicating the authors have likely performed rigorous penalization or recalibration. The absolute risks are trustworthy.

Step 3: Calculating Discrimination Intuition. The absolute risk difference between a maximum score of 3 (85% observed risk) and a minimum score of 0 (5% observed risk) is 80%. The model clearly separates the highest and lowest risk groups effectively, which mathematically aligns with the reported AUROC of 0.75. However, separating extremes is easy; the clinical challenge lies in managing the intermediate groups.

Step 4: Net Benefit at a Clinical Threshold. Suppose an attending physician would formally consider palliation (the action) only if the risk of mRS 5-6 exceeds 50%. This defines the Threshold Probability (Pt = 0.50). The harm ratio is Pt / (1 - Pt) = 0.50 / 0.50 = 1. This equates to a clinical judgment that inappropriately withdrawing care (a false positive) is exactly equal in harm to prolonging intensive care in a patient destined for a catastrophic outcome (a false negative). To calculate Net Benefit for the model at this threshold, we act (palliate) only if the Score is 3 (since its Predicted Risk of 0.85 > 0.50).

True Positives (TP) = patients with Score 3 who actually achieved mRS 5-6 = 85. False Positives (FP) = patients with Score 3 who did NOT achieve mRS 5-6 = 100 - 85 = 15. Total N = 1000. Model Net Benefit = (TP / N) - (FP / N) * Harm Ratio = (85 / 1000) - (15 / 1000) * 1 = 0.085 - 0.015 = 0.070.

Step 5: Comparing to Default Strategies. We must compare this Model Net Benefit to the default strategies. Treat All (palliate everyone in the cohort): TP = all 270 events. FP = all 730 non-events. Net Benefit (Treat All) = (270 / 1000) - (730 / 1000) * 1 = 0.270 - 0.730 = -0.460. Treat None (palliate no one): Net Benefit is exactly 0. Because the Model Net Benefit (0.070) is greater than both Treat None (0) and Treat All (-0.460), the model demonstrates mathematical clinical utility at a 50% threshold. The value 0.070 indicates that utilizing the model is equivalent to identifying 7 additional true positive catastrophic outcomes per 100 patients, with no false positive penalty.

Step 6: Sensitivity to Thresholds. What if the clinician requires a much higher certainty to palliate, setting the Threshold Probability at 90%? At Pt = 0.90, the Harm Ratio is 0.90 / 0.10 = 9 (inappropriately withdrawing care is 9 times worse). Under this strict threshold, no score category exceeds the 90% predicted risk mark (Score 3 maxes out at 85%). Therefore, the model never triggers the action. The True Positives are 0, False Positives are 0, and the Model Net Benefit becomes 0, rendering it perfectly equivalent to the 'Treat None' strategy. The model is completely useless for a clinician operating at a 90% threshold. This dynamic vividly illustrates why AUROC is clinically blind; utility is inextricably bound to the clinician's threshold for action.

## Pitfalls and Failure Modes in Neurologic Prediction

- Dichotomania: Taking an information-dense, continuous variable—such as exact systolic blood pressure, core volume in milliliters, or chronological age—and brutally severing it into binary categories ('Hypertension Yes/No' or 'Age > 65'). This destructive practice forces the model to assume that all patients aged 66 are biologically identical to patients aged 95, while simultaneously assuming they are radically different from a patient aged 64. It obliterates statistical power, ensures miscalibration at the extremes, and represents a profound failure of quantitative reasoning.
- The Immortal Time Fallacy in Prediction: Defining a study cohort strictly as 'patients who underwent a 90-day follow-up MRI.' This inclusion criterion guarantees that any patient who died prior to day 90 is systematically excluded from the dataset. If the researcher subsequently builds a model predicting 90-day functional independence, the resulting algorithm is entirely conditional on survival. It cannot be applied to a newly admitted patient in the emergency department, because the clinician at time zero does not possess the future knowledge of whether the patient will survive to day 90.
- Competing Risks Ignored: Attempting to predict the risk of a recurrent stroke over a 5-year horizon in an elderly, highly comorbid population without accounting for the competing risk of non-stroke cardiovascular death. Standard Kaplan-Meier methodologies will systematically overestimate the probability of recurrent stroke because they falsely assume that censored patients (e.g., those who died of a myocardial infarction in year 2) still possessed the biological capacity to experience a stroke in year 4. Cumulative incidence functions must be utilized to calculate accurate absolute risks in the presence of competing events (detailed in Chapter 11).
- Uncalibrated Machine Learning: Modern complex algorithms—such as deep neural networks and extreme gradient boosting machines—frequently achieve exceptionally high AUROC scores by meticulously mapping highly non-linear feature spaces. However, their raw outputs are often non-calibrated pseudo-probabilities that do not align with true event rates. They require secondary, post-hoc calibration layers (utilizing techniques like Platt scaling or isotonic regression) to transform their outputs into trustworthy absolute risks. If a paper boasts a random forest with an AUROC of 0.92 but fails to provide a calibration plot, the absolute percentages output by the model must be treated as mathematically suspect.

## Clinical and Epidemiologic Notes

- Clinical Note — The CHADS-VASc vs HAS-BLED Illusion: Clinicians frequently calculate the CHADS-VASc score to estimate stroke risk and the HAS-BLED score to estimate hemorrhage risk when deciding on anticoagulation for atrial fibrillation. This ritual feels like precision medicine, but it ignores a fundamental epidemiologic reality: the risk factors heavily overlap. Age, hypertension, and prior stroke increase both scores simultaneously. A patient with a high stroke risk almost invariably has a high bleeding risk. Furthermore, neither score predicts the treatment effect of anticoagulants; they are pure prognostic scores for outcomes under natural history or usual care. Using them as causal effect modifiers—assuming that a high CHADS-VASc score mathematically guarantees a massive relative risk reduction from direct oral anticoagulants—is a conceptual leap not proven by the prediction models themselves. They calculate baseline risk, not treatment benefit.
- Epidemiologic Note — The ABCD2 Score and Diagnostic Drift: The ABCD2 score was rigorously designed to predict the short-term risk of stroke following a transient ischemic attack. Initial internal validations demonstrated excellent discrimination. However, subsequent independent external validations in real-world emergency departments often revealed catastrophic drops in performance (e.g., AUROCs plummeting from 0.80 to 0.60). The failure was epidemiologic. The original derivation cohorts were heavily enriched with true, neurologically confirmed TIAs. The independent, real-world validation cohorts included massive numbers of TIA mimics (migraines, focal seizures, functional presentations). The model failed transportability due to diagnostic case-mix variation. A tool intended to triage undifferentiated ED patients must be validated on a cohort of undifferentiated ED patients, not a curated registry.
- Clinical Note — Algorithmic Nihilism and the ICH Score: The ICH Score is deeply embedded in the culture of neurocritical care. It functions as a prognostic score predicting 30-day mortality. However, if clinicians utilize a high ICH Score (e.g., a 4 or 5) as the primary justification to withdraw life-sustaining therapy on hospital day one, the predictive model transforms into a lethal self-fulfilling prophecy. The patients die primarily because aggressive care is withdrawn, which then seamlessly reinforces the model's high mortality prediction when the data is added to subsequent registries. This 'algorithmic nihilism' requires prediction researchers to rigorously segregate mortality occurring under maximal aggressive care from mortality directly resulting from the withdrawal of care. Failure to do so corrupts the prediction.
- Research Design Note — Absolute Effects over Relative Risks: When evaluating a prognostic model for clinical application, the appraiser must ignore the odds ratios and hazard ratios generated for individual predictors. An odds ratio of 4.0 for a specific biomarker is clinically useless if the baseline absolute risk of the event is 0.1%. Patients do not conceptualize their lives in odds ratios; they require their risk expressed on the absolute probability scale. Always demand that models generate absolute probabilities, which translate directly into Absolute Risk Reduction (ARR) and Number Needed to Treat (NNT) if an intervention with a known relative efficacy is subsequently applied. The mathematical relationship is unbreakable: ARR = Absolute Risk * Relative Risk Reduction, and NNT = 1 / ARR. Absolute risk is the only currency that matters at the bedside.


![fig54_surrogate_trap.png original teaching graphic](../assets/figures/fig54_surrogate_trap.png)

*Original teaching graphic (fig54_surrogate_trap.png).*

## Chapter summary

Prognosis and prediction models execute a fundamentally different scientific task than randomized trials or diagnostic accuracy studies; they forecast future probabilities based on present data, without making causal claims about treatment effects. Rigorous appraisal requires absolute adherence to a defined time zero, ensuring no future data leaks into the predictor set. Discrimination (AUROC) merely ranks patients, while calibration provides the absolute risk accuracy essential for clinical counseling and bedside decision-making. Overfitting must be neutralized through internal validation techniques like bootstrapping, while external validation remains mandatory to detect temporal drift and case-mix variation. Ultimately, models must move beyond probabilities; Decision Curve Analysis translates risk accuracy into clinical utility by quantifying Net Benefit across the spectrum of clinician thresholds. Applying the PROBAST framework protects the clinician from adopting mathematically optimistic, uncalibrated models that fail at the bedside.

## Practice and reflection

1. Select a recent stroke risk score publication. Write a single sentence strictly defining the intended population, the precise time zero, the predictor set, the outcome, and the prediction horizon. Flag any predictor that violates time zero discipline.
2. Explain to a junior resident, utilizing plain language, how a prediction model can achieve an AUROC of 0.85 yet be actively dangerous for counseling patients regarding absolute risk.
3. Using a hypothetical dataset of 1000 patients with a 20% baseline prevalence of poor outcome, calculate the Net Benefit of a 'Treat All' strategy at a threshold probability of 30%.
4. Outline a comprehensive external validation protocol for an admission ICH expansion model, explicitly addressing the threats of geographical case-mix variation and temporal changes in blood pressure management.
5. Identify a published neurology paper that relies entirely on split-sample internal validation for a multivariable model. Describe how executing bootstrap validation on the full pipeline would likely alter their reported performance.
6. Review the PROBAST criteria. Explain why discarding 20% of a cohort due to missing continuous predictor data (complete-case analysis) introduces an unacceptable risk of bias.
7. Contrast the clinical utility of the ICH Score when used to stratify patients for a clinical trial versus when used to guide the withdrawal of life-sustaining therapy on hospital day one.
8. A paper reports an odds ratio of 3.5 for a novel biomarker predicting 90-day stroke recurrence. The baseline risk of recurrence is 2%. Calculate the absolute risk for a patient with the biomarker, and determine the Number Needed to Treat if an intervention reduces the relative risk by 30%.

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


![fig89_km_atrisk.png original teaching graphic](../assets/figures/fig89_km_atrisk.png)

*Original teaching graphic (fig89_km_atrisk.png).*
