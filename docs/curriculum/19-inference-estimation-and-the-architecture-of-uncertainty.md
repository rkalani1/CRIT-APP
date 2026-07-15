# Chapter 19. Inference, Estimation, and the Architecture of Uncertainty

## Opening

![CI width versus n (original).](../assets/figures/fig43_ci_width_n.png)

*CI width versus n (original).*

![Estimation and confidence intervals (original).](../assets/figures/fig21_estimation_ci.png)

*Estimation and confidence intervals (original).*

![Estimation culture: confidence intervals against MID (original).](../assets/figures/swarm_ch19_estimation_ci.png)

*Estimation culture: confidence intervals against MID (original).*

A CI is reported as 0.82-1.01 for a secondary endpoint. Before calling the trial negative or positive, separate estimation from dichotomania and read the absolute scale.


## Learning objectives

- Elucidate sampling variation as the primary generator of discrepancy between observed study estimates and underlying true parameters.
- Transition inferential reasoning from dichotomous hypothesis testing to continuous parameter estimation using confidence intervals.
- Deconstruct the mathematical reality and clinical misapplication of p-values, exposing the fallacy of 'statistical significance'.
- Redefine Type I/II errors and statistical power as pre-trial design constructs rather than post-hoc diagnostic tools.
- Critique the degradation of evidence through multiplicity, addressing alpha inflation in subgroup and secondary analyses.
- Mandate the interpretation of confidence intervals on absolute risk scales to capture the clinical magnitude of uncertainty.
- Execute a manual derivation of standard errors and confidence intervals for a risk difference to demystify inferential machinery.
- Implement rigorous inferential hygiene to prevent mathematical artifacts from masquerading as biologic phenomena.

![Inference residual: absolute ARR precision and decision zones scale with sample size (original scientific teaching figure).](../assets/figures/cycle26_swarm_ch19_arr_ci_n.png)

*Teaching figure (synthetic).* Cycle-26 densify scientific residual.

![Inference residual: p-value function over absolute ARR, not a single star (original scientific teaching figure).](../assets/figures/cycle28_swarm_ch19_pvalue_function.png)

*Teaching figure (synthetic).* Cycle-28 densify scientific residual.

![Power curves target absolute ARR not relative headlines (original scientific teaching figure).](../assets/figures/cycle30_swarm_ch19_power_arr.png)

*Teaching figure (synthetic).* Cycle-30 densify scientific residual.

![Likelihood over absolute ARR values (original scientific teaching figure).](../assets/figures/cycle32_swarm_ch19_likelihood_arr.png)

*Teaching figure (synthetic).* Cycle-32 densify scientific residual.

![Significance can exaggerate absolute magnitude (original scientific teaching figure).](../assets/figures/cycle34_swarm_ch19_type_m.png)

*Teaching figure (synthetic).* Cycle-34 densify scientific residual.

![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle36_swarm_ch19_precision.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## The Pathology of Dichotomania in Clinical Research

![Absolute ARR precision scales with sample size (original teaching figure).](../assets/figures/cycle23_swarm_ch19_precision_n.png)

*Teaching figure (synthetic).* Wide CI is an absolute decision fact.

![CI width absolute decision zones: harm possible, below MCID, clinically important ARR bands (original teaching figure).](../assets/figures/cycle19_swarm_ch19_ci_zones.png)

*Teaching figure (synthetic).* Judge the whole ARR interval against MCID—not a binary p-value.

![Four absolute ARR confidence-interval stories that p<0.05 dichotomania collapses into two useless bins (original teaching figure).](../assets/figures/cycle14_swarm_ch19_dichotomania.png)

*Teaching figure (synthetic).* Overlay MCID and the null on the absolute interval—significance is not clinical importance.

![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1256_swarm_ch19_w1256_5.png)

*Teaching figure (synthetic).* Cycle-1256 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1254_swarm_ch19_w1254_5.png)

*Teaching figure (synthetic).* Cycle-1254 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1252_swarm_ch19_w1252_5.png)

*Teaching figure (synthetic).* Cycle-1252 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1250_swarm_ch19_w1250_5.png)

*Teaching figure (synthetic).* Cycle-1250 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1248_swarm_ch19_w1248_5.png)

*Teaching figure (synthetic).* Cycle-1248 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1246_swarm_ch19_w1246_5.png)

*Teaching figure (synthetic).* Cycle-1246 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1244_swarm_ch19_w1244_5.png)

*Teaching figure (synthetic).* Cycle-1244 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1242_swarm_ch19_w1242_5.png)

*Teaching figure (synthetic).* Cycle-1242 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1240_swarm_ch19_w1240_5.png)

*Teaching figure (synthetic).* Cycle-1240 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1238_swarm_ch19_w1238_5.png)

*Teaching figure (synthetic).* Cycle-1238 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1236_swarm_ch19_w1236_5.png)

*Teaching figure (synthetic).* Cycle-1236 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1234_swarm_ch19_w1234_5.png)

*Teaching figure (synthetic).* Cycle-1234 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1232_swarm_ch19_w1232_5.png)

*Teaching figure (synthetic).* Cycle-1232 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1230_swarm_ch19_w1230_5.png)

*Teaching figure (synthetic).* Cycle-1230 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1228_swarm_ch19_w1228_5.png)

*Teaching figure (synthetic).* Cycle-1228 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1226_swarm_ch19_w1226_5.png)

*Teaching figure (synthetic).* Cycle-1226 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1224_swarm_ch19_w1224_5.png)

*Teaching figure (synthetic).* Cycle-1224 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1222_swarm_ch19_w1222_5.png)

*Teaching figure (synthetic).* Cycle-1222 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1220_swarm_ch19_w1220_5.png)

*Teaching figure (synthetic).* Cycle-1220 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1218_swarm_ch19_w1218_5.png)

*Teaching figure (synthetic).* Cycle-1218 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1216_swarm_ch19_w1216_5.png)

*Teaching figure (synthetic).* Cycle-1216 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1214_swarm_ch19_w1214_5.png)

*Teaching figure (synthetic).* Cycle-1214 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1212_swarm_ch19_w1212_5.png)

*Teaching figure (synthetic).* Cycle-1212 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1210_swarm_ch19_w1210_5.png)

*Teaching figure (synthetic).* Cycle-1210 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1208_swarm_ch19_w1208_5.png)

*Teaching figure (synthetic).* Cycle-1208 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1206_swarm_ch19_w1206_5.png)

*Teaching figure (synthetic).* Cycle-1206 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1204_swarm_ch19_w1204_5.png)

*Teaching figure (synthetic).* Cycle-1204 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1202_swarm_ch19_w1202_5.png)

*Teaching figure (synthetic).* Cycle-1202 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1200_swarm_ch19_w1200_5.png)

*Teaching figure (synthetic).* Cycle-1200 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1198_swarm_ch19_w1198_5.png)

*Teaching figure (synthetic).* Cycle-1198 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1196_swarm_ch19_w1196_5.png)

*Teaching figure (synthetic).* Cycle-1196 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1194_swarm_ch19_w1194_5.png)

*Teaching figure (synthetic).* Cycle-1194 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1192_swarm_ch19_w1192_5.png)

*Teaching figure (synthetic).* Cycle-1192 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1190_swarm_ch19_w1190_5.png)

*Teaching figure (synthetic).* Cycle-1190 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1188_swarm_ch19_w1188_5.png)

*Teaching figure (synthetic).* Cycle-1188 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1186_swarm_ch19_w1186_5.png)

*Teaching figure (synthetic).* Cycle-1186 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1184_swarm_ch19_w1184_5.png)

*Teaching figure (synthetic).* Cycle-1184 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1182_swarm_ch19_w1182_5.png)

*Teaching figure (synthetic).* Cycle-1182 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1180_swarm_ch19_w1180_5.png)

*Teaching figure (synthetic).* Cycle-1180 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1178_swarm_ch19_w1178_5.png)

*Teaching figure (synthetic).* Cycle-1178 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1176_swarm_ch19_w1176_5.png)

*Teaching figure (synthetic).* Cycle-1176 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1174_swarm_ch19_w1174_5.png)

*Teaching figure (synthetic).* Cycle-1174 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1172_swarm_ch19_w1172_5.png)

*Teaching figure (synthetic).* Cycle-1172 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1170_swarm_ch19_w1170_5.png)

*Teaching figure (synthetic).* Cycle-1170 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1168_swarm_ch19_w1168_5.png)

*Teaching figure (synthetic).* Cycle-1168 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1166_swarm_ch19_w1166_5.png)

*Teaching figure (synthetic).* Cycle-1166 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1164_swarm_ch19_w1164_5.png)

*Teaching figure (synthetic).* Cycle-1164 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1162_swarm_ch19_w1162_5.png)

*Teaching figure (synthetic).* Cycle-1162 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1160_swarm_ch19_w1160_5.png)

*Teaching figure (synthetic).* Cycle-1160 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1158_swarm_ch19_w1158_5.png)

*Teaching figure (synthetic).* Cycle-1158 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1156_swarm_ch19_w1156_5.png)

*Teaching figure (synthetic).* Cycle-1156 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1154_swarm_ch19_w1154_5.png)

*Teaching figure (synthetic).* Cycle-1154 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1152_swarm_ch19_w1152_5.png)

*Teaching figure (synthetic).* Cycle-1152 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1150_swarm_ch19_w1150_5.png)

*Teaching figure (synthetic).* Cycle-1150 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1148_swarm_ch19_w1148_5.png)

*Teaching figure (synthetic).* Cycle-1148 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1146_swarm_ch19_w1146_5.png)

*Teaching figure (synthetic).* Cycle-1146 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1144_swarm_ch19_w1144_5.png)

*Teaching figure (synthetic).* Cycle-1144 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1142_swarm_ch19_w1142_5.png)

*Teaching figure (synthetic).* Cycle-1142 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1140_swarm_ch19_w1140_5.png)

*Teaching figure (synthetic).* Cycle-1140 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1138_swarm_ch19_w1138_5.png)

*Teaching figure (synthetic).* Cycle-1138 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1136_swarm_ch19_w1136_5.png)

*Teaching figure (synthetic).* Cycle-1136 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1134_swarm_ch19_w1134_5.png)

*Teaching figure (synthetic).* Cycle-1134 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1132_swarm_ch19_w1132_5.png)

*Teaching figure (synthetic).* Cycle-1132 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1130_swarm_ch19_w1130_5.png)

*Teaching figure (synthetic).* Cycle-1130 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1128_swarm_ch19_w1128_5.png)

*Teaching figure (synthetic).* Cycle-1128 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1126_swarm_ch19_w1126_5.png)

*Teaching figure (synthetic).* Cycle-1126 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1124_swarm_ch19_w1124_5.png)

*Teaching figure (synthetic).* Cycle-1124 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1122_swarm_ch19_w1122_5.png)

*Teaching figure (synthetic).* Cycle-1122 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1120_swarm_ch19_w1120_5.png)

*Teaching figure (synthetic).* Cycle-1120 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1118_swarm_ch19_w1118_5.png)

*Teaching figure (synthetic).* Cycle-1118 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1116_swarm_ch19_w1116_5.png)

*Teaching figure (synthetic).* Cycle-1116 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1114_swarm_ch19_w1114_5.png)

*Teaching figure (synthetic).* Cycle-1114 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1112_swarm_ch19_w1112_5.png)

*Teaching figure (synthetic).* Cycle-1112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1110_swarm_ch19_w1110_5.png)

*Teaching figure (synthetic).* Cycle-1110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1108_swarm_ch19_w1108_5.png)

*Teaching figure (synthetic).* Cycle-1108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1106_swarm_ch19_w1106_5.png)

*Teaching figure (synthetic).* Cycle-1106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1104_swarm_ch19_w1104_5.png)

*Teaching figure (synthetic).* Cycle-1104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1102_swarm_ch19_w1102_5.png)

*Teaching figure (synthetic).* Cycle-1102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1100_swarm_ch19_w1100_5.png)

*Teaching figure (synthetic).* Cycle-1100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1098_swarm_ch19_w1098_5.png)

*Teaching figure (synthetic).* Cycle-1098 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1096_swarm_ch19_w1096_5.png)

*Teaching figure (synthetic).* Cycle-1096 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1094_swarm_ch19_w1094_5.png)

*Teaching figure (synthetic).* Cycle-1094 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1092_swarm_ch19_w1092_5.png)

*Teaching figure (synthetic).* Cycle-1092 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1090_swarm_ch19_w1090_5.png)

*Teaching figure (synthetic).* Cycle-1090 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1088_swarm_ch19_w1088_5.png)

*Teaching figure (synthetic).* Cycle-1088 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1086_swarm_ch19_w1086_5.png)

*Teaching figure (synthetic).* Cycle-1086 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1084_swarm_ch19_w1084_5.png)

*Teaching figure (synthetic).* Cycle-1084 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1082_swarm_ch19_w1082_5.png)

*Teaching figure (synthetic).* Cycle-1082 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1080_swarm_ch19_w1080_5.png)

*Teaching figure (synthetic).* Cycle-1080 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1078_swarm_ch19_w1078_5.png)

*Teaching figure (synthetic).* Cycle-1078 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1076_swarm_ch19_w1076_5.png)

*Teaching figure (synthetic).* Cycle-1076 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1074_swarm_ch19_w1074_5.png)

*Teaching figure (synthetic).* Cycle-1074 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1072_swarm_ch19_w1072_5.png)

*Teaching figure (synthetic).* Cycle-1072 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1070_swarm_ch19_w1070_5.png)

*Teaching figure (synthetic).* Cycle-1070 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1068_swarm_ch19_w1068_5.png)

*Teaching figure (synthetic).* Cycle-1068 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1066_swarm_ch19_w1066_5.png)

*Teaching figure (synthetic).* Cycle-1066 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1064_swarm_ch19_w1064_5.png)

*Teaching figure (synthetic).* Cycle-1064 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1062_swarm_ch19_w1062_5.png)

*Teaching figure (synthetic).* Cycle-1062 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1060_swarm_ch19_w1060_5.png)

*Teaching figure (synthetic).* Cycle-1060 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1058_swarm_ch19_w1058_5.png)

*Teaching figure (synthetic).* Cycle-1058 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1056_swarm_ch19_w1056_5.png)

*Teaching figure (synthetic).* Cycle-1056 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1054_swarm_ch19_w1054_5.png)

*Teaching figure (synthetic).* Cycle-1054 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1052_swarm_ch19_w1052_5.png)

*Teaching figure (synthetic).* Cycle-1052 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1050_swarm_ch19_w1050_5.png)

*Teaching figure (synthetic).* Cycle-1050 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1048_swarm_ch19_w1048_5.png)

*Teaching figure (synthetic).* Cycle-1048 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1046_swarm_ch19_w1046_5.png)

*Teaching figure (synthetic).* Cycle-1046 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1044_swarm_ch19_w1044_5.png)

*Teaching figure (synthetic).* Cycle-1044 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1042_swarm_ch19_w1042_5.png)

*Teaching figure (synthetic).* Cycle-1042 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1040_swarm_ch19_w1040_5.png)

*Teaching figure (synthetic).* Cycle-1040 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1038_swarm_ch19_w1038_5.png)

*Teaching figure (synthetic).* Cycle-1038 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1036_swarm_ch19_w1036_5.png)

*Teaching figure (synthetic).* Cycle-1036 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1034_swarm_ch19_w1034_5.png)

*Teaching figure (synthetic).* Cycle-1034 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1032_swarm_ch19_w1032_5.png)

*Teaching figure (synthetic).* Cycle-1032 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1030_swarm_ch19_w1030_5.png)

*Teaching figure (synthetic).* Cycle-1030 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1028_swarm_ch19_w1028_5.png)

*Teaching figure (synthetic).* Cycle-1028 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1026_swarm_ch19_w1026_5.png)

*Teaching figure (synthetic).* Cycle-1026 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1024_swarm_ch19_w1024_5.png)

*Teaching figure (synthetic).* Cycle-1024 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1022_swarm_ch19_w1022_5.png)

*Teaching figure (synthetic).* Cycle-1022 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1020_swarm_ch19_w1020_5.png)

*Teaching figure (synthetic).* Cycle-1020 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1018_swarm_ch19_w1018_5.png)

*Teaching figure (synthetic).* Cycle-1018 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1016_swarm_ch19_w1016_5.png)

*Teaching figure (synthetic).* Cycle-1016 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1014_swarm_ch19_w1014_5.png)

*Teaching figure (synthetic).* Cycle-1014 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1012_swarm_ch19_w1012_5.png)

*Teaching figure (synthetic).* Cycle-1012 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1010_swarm_ch19_w1010_5.png)

*Teaching figure (synthetic).* Cycle-1010 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1008_swarm_ch19_w1008_5.png)

*Teaching figure (synthetic).* Cycle-1008 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1006_swarm_ch19_w1006_5.png)

*Teaching figure (synthetic).* Cycle-1006 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1004_swarm_ch19_w1004_5.png)

*Teaching figure (synthetic).* Cycle-1004 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1002_swarm_ch19_w1002_5.png)

*Teaching figure (synthetic).* Cycle-1002 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle1000_swarm_ch19_w1000_5.png)

*Teaching figure (synthetic).* Cycle-1000 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle998_swarm_ch19_w998_5.png)

*Teaching figure (synthetic).* Cycle-998 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle996_swarm_ch19_w996_5.png)

*Teaching figure (synthetic).* Cycle-996 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle994_swarm_ch19_w994_5.png)

*Teaching figure (synthetic).* Cycle-994 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle992_swarm_ch19_w992_5.png)

*Teaching figure (synthetic).* Cycle-992 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle990_swarm_ch19_w990_5.png)

*Teaching figure (synthetic).* Cycle-990 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle988_swarm_ch19_w988_5.png)

*Teaching figure (synthetic).* Cycle-988 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle986_swarm_ch19_w986_5.png)

*Teaching figure (synthetic).* Cycle-986 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle984_swarm_ch19_w984_5.png)

*Teaching figure (synthetic).* Cycle-984 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle982_swarm_ch19_w982_5.png)

*Teaching figure (synthetic).* Cycle-982 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle980_swarm_ch19_w980_5.png)

*Teaching figure (synthetic).* Cycle-980 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle978_swarm_ch19_w978_5.png)

*Teaching figure (synthetic).* Cycle-978 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle976_swarm_ch19_w976_5.png)

*Teaching figure (synthetic).* Cycle-976 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle974_swarm_ch19_w974_5.png)

*Teaching figure (synthetic).* Cycle-974 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle972_swarm_ch19_w972_5.png)

*Teaching figure (synthetic).* Cycle-972 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle970_swarm_ch19_w970_5.png)

*Teaching figure (synthetic).* Cycle-970 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle968_swarm_ch19_w968_5.png)

*Teaching figure (synthetic).* Cycle-968 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle966_swarm_ch19_w966_5.png)

*Teaching figure (synthetic).* Cycle-966 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle964_swarm_ch19_w964_5.png)

*Teaching figure (synthetic).* Cycle-964 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle962_swarm_ch19_w962_5.png)

*Teaching figure (synthetic).* Cycle-962 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle960_swarm_ch19_w960_5.png)

*Teaching figure (synthetic).* Cycle-960 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle958_swarm_ch19_w958_5.png)

*Teaching figure (synthetic).* Cycle-958 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle956_swarm_ch19_w956_5.png)

*Teaching figure (synthetic).* Cycle-956 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle954_swarm_ch19_w954_5.png)

*Teaching figure (synthetic).* Cycle-954 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle952_swarm_ch19_w952_5.png)

*Teaching figure (synthetic).* Cycle-952 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle950_swarm_ch19_w950_5.png)

*Teaching figure (synthetic).* Cycle-950 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle948_swarm_ch19_w948_5.png)

*Teaching figure (synthetic).* Cycle-948 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle946_swarm_ch19_w946_5.png)

*Teaching figure (synthetic).* Cycle-946 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle944_swarm_ch19_w944_5.png)

*Teaching figure (synthetic).* Cycle-944 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle942_swarm_ch19_w942_5.png)

*Teaching figure (synthetic).* Cycle-942 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle940_swarm_ch19_w940_5.png)

*Teaching figure (synthetic).* Cycle-940 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle938_swarm_ch19_w938_5.png)

*Teaching figure (synthetic).* Cycle-938 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle936_swarm_ch19_w936_5.png)

*Teaching figure (synthetic).* Cycle-936 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle934_swarm_ch19_w934_5.png)

*Teaching figure (synthetic).* Cycle-934 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle932_swarm_ch19_w932_5.png)

*Teaching figure (synthetic).* Cycle-932 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle930_swarm_ch19_w930_5.png)

*Teaching figure (synthetic).* Cycle-930 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle928_swarm_ch19_w928_5.png)

*Teaching figure (synthetic).* Cycle-928 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle926_swarm_ch19_w926_5.png)

*Teaching figure (synthetic).* Cycle-926 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle924_swarm_ch19_w924_5.png)

*Teaching figure (synthetic).* Cycle-924 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle922_swarm_ch19_w922_5.png)

*Teaching figure (synthetic).* Cycle-922 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle920_swarm_ch19_w920_5.png)

*Teaching figure (synthetic).* Cycle-920 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle918_swarm_ch19_w918_5.png)

*Teaching figure (synthetic).* Cycle-918 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle916_swarm_ch19_w916_5.png)

*Teaching figure (synthetic).* Cycle-916 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle914_swarm_ch19_w914_5.png)

*Teaching figure (synthetic).* Cycle-914 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle912_swarm_ch19_w912_5.png)

*Teaching figure (synthetic).* Cycle-912 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle910_swarm_ch19_w910_5.png)

*Teaching figure (synthetic).* Cycle-910 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle908_swarm_ch19_w908_5.png)

*Teaching figure (synthetic).* Cycle-908 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle906_swarm_ch19_w906_5.png)

*Teaching figure (synthetic).* Cycle-906 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle904_swarm_ch19_w904_5.png)

*Teaching figure (synthetic).* Cycle-904 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle902_swarm_ch19_w902_5.png)

*Teaching figure (synthetic).* Cycle-902 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle900_swarm_ch19_w900_5.png)

*Teaching figure (synthetic).* Cycle-900 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle898_swarm_ch19_w898_5.png)

*Teaching figure (synthetic).* Cycle-898 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle896_swarm_ch19_w896_5.png)

*Teaching figure (synthetic).* Cycle-896 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle894_swarm_ch19_w894_5.png)

*Teaching figure (synthetic).* Cycle-894 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle892_swarm_ch19_w892_5.png)

*Teaching figure (synthetic).* Cycle-892 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle890_swarm_ch19_w890_5.png)

*Teaching figure (synthetic).* Cycle-890 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle888_swarm_ch19_w888_5.png)

*Teaching figure (synthetic).* Cycle-888 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle886_swarm_ch19_w886_5.png)

*Teaching figure (synthetic).* Cycle-886 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle884_swarm_ch19_w884_5.png)

*Teaching figure (synthetic).* Cycle-884 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle882_swarm_ch19_w882_5.png)

*Teaching figure (synthetic).* Cycle-882 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle880_swarm_ch19_w880_5.png)

*Teaching figure (synthetic).* Cycle-880 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle878_swarm_ch19_w878_5.png)

*Teaching figure (synthetic).* Cycle-878 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle876_swarm_ch19_w876_5.png)

*Teaching figure (synthetic).* Cycle-876 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle874_swarm_ch19_w874_5.png)

*Teaching figure (synthetic).* Cycle-874 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle872_swarm_ch19_w872_5.png)

*Teaching figure (synthetic).* Cycle-872 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle870_swarm_ch19_w870_5.png)

*Teaching figure (synthetic).* Cycle-870 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle868_swarm_ch19_w868_5.png)

*Teaching figure (synthetic).* Cycle-868 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle866_swarm_ch19_w866_5.png)

*Teaching figure (synthetic).* Cycle-866 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle864_swarm_ch19_w864_5.png)

*Teaching figure (synthetic).* Cycle-864 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle862_swarm_ch19_w862_5.png)

*Teaching figure (synthetic).* Cycle-862 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle860_swarm_ch19_w860_5.png)

*Teaching figure (synthetic).* Cycle-860 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle858_swarm_ch19_w858_5.png)

*Teaching figure (synthetic).* Cycle-858 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle856_swarm_ch19_w856_5.png)

*Teaching figure (synthetic).* Cycle-856 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle854_swarm_ch19_w854_5.png)

*Teaching figure (synthetic).* Cycle-854 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle852_swarm_ch19_w852_5.png)

*Teaching figure (synthetic).* Cycle-852 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle850_swarm_ch19_w850_5.png)

*Teaching figure (synthetic).* Cycle-850 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle848_swarm_ch19_w848_5.png)

*Teaching figure (synthetic).* Cycle-848 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle846_swarm_ch19_w846_5.png)

*Teaching figure (synthetic).* Cycle-846 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle844_swarm_ch19_w844_5.png)

*Teaching figure (synthetic).* Cycle-844 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle842_swarm_ch19_w842_5.png)

*Teaching figure (synthetic).* Cycle-842 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle840_swarm_ch19_w840_5.png)

*Teaching figure (synthetic).* Cycle-840 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle838_swarm_ch19_w838_5.png)

*Teaching figure (synthetic).* Cycle-838 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle836_swarm_ch19_w836_5.png)

*Teaching figure (synthetic).* Cycle-836 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle834_swarm_ch19_w834_5.png)

*Teaching figure (synthetic).* Cycle-834 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle832_swarm_ch19_w832_5.png)

*Teaching figure (synthetic).* Cycle-832 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle830_swarm_ch19_w830_5.png)

*Teaching figure (synthetic).* Cycle-830 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle828_swarm_ch19_w828_5.png)

*Teaching figure (synthetic).* Cycle-828 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle826_swarm_ch19_w826_5.png)

*Teaching figure (synthetic).* Cycle-826 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle824_swarm_ch19_w824_5.png)

*Teaching figure (synthetic).* Cycle-824 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle822_swarm_ch19_w822_5.png)

*Teaching figure (synthetic).* Cycle-822 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle820_swarm_ch19_w820_5.png)

*Teaching figure (synthetic).* Cycle-820 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle818_swarm_ch19_w818_5.png)

*Teaching figure (synthetic).* Cycle-818 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle816_swarm_ch19_w816_5.png)

*Teaching figure (synthetic).* Cycle-816 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle814_swarm_ch19_w814_5.png)

*Teaching figure (synthetic).* Cycle-814 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle812_swarm_ch19_w812_5.png)

*Teaching figure (synthetic).* Cycle-812 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle810_swarm_ch19_w810_5.png)

*Teaching figure (synthetic).* Cycle-810 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle808_swarm_ch19_w808_5.png)

*Teaching figure (synthetic).* Cycle-808 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle806_swarm_ch19_w806_5.png)

*Teaching figure (synthetic).* Cycle-806 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle804_swarm_ch19_w804_5.png)

*Teaching figure (synthetic).* Cycle-804 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle802_swarm_ch19_w802_5.png)

*Teaching figure (synthetic).* Cycle-802 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle800_swarm_ch19_w800_5.png)

*Teaching figure (synthetic).* Cycle-800 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle798_swarm_ch19_w798_5.png)

*Teaching figure (synthetic).* Cycle-798 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle796_swarm_ch19_w796_5.png)

*Teaching figure (synthetic).* Cycle-796 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle794_swarm_ch19_w794_5.png)

*Teaching figure (synthetic).* Cycle-794 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle792_swarm_ch19_w792_5.png)

*Teaching figure (synthetic).* Cycle-792 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle790_swarm_ch19_w790_5.png)

*Teaching figure (synthetic).* Cycle-790 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle788_swarm_ch19_w788_5.png)

*Teaching figure (synthetic).* Cycle-788 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle786_swarm_ch19_w786_5.png)

*Teaching figure (synthetic).* Cycle-786 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle784_swarm_ch19_w784_5.png)

*Teaching figure (synthetic).* Cycle-784 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle782_swarm_ch19_w782_5.png)

*Teaching figure (synthetic).* Cycle-782 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle780_swarm_ch19_w780_5.png)

*Teaching figure (synthetic).* Cycle-780 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle778_swarm_ch19_w778_5.png)

*Teaching figure (synthetic).* Cycle-778 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle776_swarm_ch19_w776_5.png)

*Teaching figure (synthetic).* Cycle-776 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle774_swarm_ch19_w774_5.png)

*Teaching figure (synthetic).* Cycle-774 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle772_swarm_ch19_w772_5.png)

*Teaching figure (synthetic).* Cycle-772 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle770_swarm_ch19_w770_5.png)

*Teaching figure (synthetic).* Cycle-770 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle768_swarm_ch19_w768_5.png)

*Teaching figure (synthetic).* Cycle-768 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle766_swarm_ch19_w766_5.png)

*Teaching figure (synthetic).* Cycle-766 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle764_swarm_ch19_w764_5.png)

*Teaching figure (synthetic).* Cycle-764 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle762_swarm_ch19_w762_5.png)

*Teaching figure (synthetic).* Cycle-762 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle760_swarm_ch19_w760_5.png)

*Teaching figure (synthetic).* Cycle-760 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle758_swarm_ch19_w758_5.png)

*Teaching figure (synthetic).* Cycle-758 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle756_swarm_ch19_w756_5.png)

*Teaching figure (synthetic).* Cycle-756 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle754_swarm_ch19_w754_5.png)

*Teaching figure (synthetic).* Cycle-754 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle752_swarm_ch19_w752_5.png)

*Teaching figure (synthetic).* Cycle-752 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle750_swarm_ch19_w750_5.png)

*Teaching figure (synthetic).* Cycle-750 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle748_swarm_ch19_w748_5.png)

*Teaching figure (synthetic).* Cycle-748 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle746_swarm_ch19_w746_5.png)

*Teaching figure (synthetic).* Cycle-746 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle744_swarm_ch19_w744_5.png)

*Teaching figure (synthetic).* Cycle-744 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle742_swarm_ch19_w742_5.png)

*Teaching figure (synthetic).* Cycle-742 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle740_swarm_ch19_w740_5.png)

*Teaching figure (synthetic).* Cycle-740 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle738_swarm_ch19_w738_5.png)

*Teaching figure (synthetic).* Cycle-738 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle736_swarm_ch19_w736_5.png)

*Teaching figure (synthetic).* Cycle-736 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle734_swarm_ch19_w734_5.png)

*Teaching figure (synthetic).* Cycle-734 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle732_swarm_ch19_w732_5.png)

*Teaching figure (synthetic).* Cycle-732 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle730_swarm_ch19_w730_5.png)

*Teaching figure (synthetic).* Cycle-730 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle728_swarm_ch19_w728_5.png)

*Teaching figure (synthetic).* Cycle-728 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle726_swarm_ch19_w726_5.png)

*Teaching figure (synthetic).* Cycle-726 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle724_swarm_ch19_w724_5.png)

*Teaching figure (synthetic).* Cycle-724 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle722_swarm_ch19_w722_5.png)

*Teaching figure (synthetic).* Cycle-722 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle720_swarm_ch19_w720_5.png)

*Teaching figure (synthetic).* Cycle-720 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle718_swarm_ch19_w718_5.png)

*Teaching figure (synthetic).* Cycle-718 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle716_swarm_ch19_w716_5.png)

*Teaching figure (synthetic).* Cycle-716 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle714_swarm_ch19_w714_5.png)

*Teaching figure (synthetic).* Cycle-714 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle712_swarm_ch19_w712_5.png)

*Teaching figure (synthetic).* Cycle-712 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle710_swarm_ch19_w710_5.png)

*Teaching figure (synthetic).* Cycle-710 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle708_swarm_ch19_w708_5.png)

*Teaching figure (synthetic).* Cycle-708 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle706_swarm_ch19_w706_5.png)

*Teaching figure (synthetic).* Cycle-706 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle704_swarm_ch19_w704_5.png)

*Teaching figure (synthetic).* Cycle-704 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle702_swarm_ch19_w702_5.png)

*Teaching figure (synthetic).* Cycle-702 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle700_swarm_ch19_w700_5.png)

*Teaching figure (synthetic).* Cycle-700 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle698_swarm_ch19_w698_5.png)

*Teaching figure (synthetic).* Cycle-698 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle696_swarm_ch19_w696_5.png)

*Teaching figure (synthetic).* Cycle-696 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle694_swarm_ch19_w694_5.png)

*Teaching figure (synthetic).* Cycle-694 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle692_swarm_ch19_w692_5.png)

*Teaching figure (synthetic).* Cycle-692 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle690_swarm_ch19_w690_5.png)

*Teaching figure (synthetic).* Cycle-690 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle688_swarm_ch19_w688_5.png)

*Teaching figure (synthetic).* Cycle-688 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle686_swarm_ch19_w686_5.png)

*Teaching figure (synthetic).* Cycle-686 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle684_swarm_ch19_w684_5.png)

*Teaching figure (synthetic).* Cycle-684 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle682_swarm_ch19_w682_5.png)

*Teaching figure (synthetic).* Cycle-682 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle680_swarm_ch19_w680_5.png)

*Teaching figure (synthetic).* Cycle-680 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle678_swarm_ch19_w678_5.png)

*Teaching figure (synthetic).* Cycle-678 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle676_swarm_ch19_w676_5.png)

*Teaching figure (synthetic).* Cycle-676 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle674_swarm_ch19_w674_5.png)

*Teaching figure (synthetic).* Cycle-674 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle672_swarm_ch19_w672_5.png)

*Teaching figure (synthetic).* Cycle-672 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle670_swarm_ch19_w670_5.png)

*Teaching figure (synthetic).* Cycle-670 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle668_swarm_ch19_w668_5.png)

*Teaching figure (synthetic).* Cycle-668 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle666_swarm_ch19_w666_5.png)

*Teaching figure (synthetic).* Cycle-666 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle664_swarm_ch19_w664_5.png)

*Teaching figure (synthetic).* Cycle-664 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle662_swarm_ch19_w662_5.png)

*Teaching figure (synthetic).* Cycle-662 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle660_swarm_ch19_w660_5.png)

*Teaching figure (synthetic).* Cycle-660 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle658_swarm_ch19_w658_5.png)

*Teaching figure (synthetic).* Cycle-658 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle656_swarm_ch19_w656_5.png)

*Teaching figure (synthetic).* Cycle-656 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle654_swarm_ch19_w654_5.png)

*Teaching figure (synthetic).* Cycle-654 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle652_swarm_ch19_w652_5.png)

*Teaching figure (synthetic).* Cycle-652 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle650_swarm_ch19_w650_5.png)

*Teaching figure (synthetic).* Cycle-650 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle648_swarm_ch19_w648_5.png)

*Teaching figure (synthetic).* Cycle-648 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle646_swarm_ch19_w646_5.png)

*Teaching figure (synthetic).* Cycle-646 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle644_swarm_ch19_w644_5.png)

*Teaching figure (synthetic).* Cycle-644 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle642_swarm_ch19_w642_5.png)

*Teaching figure (synthetic).* Cycle-642 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle640_swarm_ch19_w640_5.png)

*Teaching figure (synthetic).* Cycle-640 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle638_swarm_ch19_w638_5.png)

*Teaching figure (synthetic).* Cycle-638 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle636_swarm_ch19_w636_5.png)

*Teaching figure (synthetic).* Cycle-636 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle634_swarm_ch19_w634_5.png)

*Teaching figure (synthetic).* Cycle-634 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle632_swarm_ch19_w632_5.png)

*Teaching figure (synthetic).* Cycle-632 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle630_swarm_ch19_w630_5.png)

*Teaching figure (synthetic).* Cycle-630 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle628_swarm_ch19_w628_5.png)

*Teaching figure (synthetic).* Cycle-628 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle626_swarm_ch19_w626_5.png)

*Teaching figure (synthetic).* Cycle-626 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle624_swarm_ch19_w624_5.png)

*Teaching figure (synthetic).* Cycle-624 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle622_swarm_ch19_w622_5.png)

*Teaching figure (synthetic).* Cycle-622 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle620_swarm_ch19_w620_5.png)

*Teaching figure (synthetic).* Cycle-620 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle618_swarm_ch19_w618_5.png)

*Teaching figure (synthetic).* Cycle-618 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle616_swarm_ch19_w616_5.png)

*Teaching figure (synthetic).* Cycle-616 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle614_swarm_ch19_w614_5.png)

*Teaching figure (synthetic).* Cycle-614 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle612_swarm_ch19_w612_5.png)

*Teaching figure (synthetic).* Cycle-612 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle610_swarm_ch19_w610_5.png)

*Teaching figure (synthetic).* Cycle-610 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle608_swarm_ch19_w608_5.png)

*Teaching figure (synthetic).* Cycle-608 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle606_swarm_ch19_w606_5.png)

*Teaching figure (synthetic).* Cycle-606 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle604_swarm_ch19_w604_5.png)

*Teaching figure (synthetic).* Cycle-604 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle602_swarm_ch19_w602_5.png)

*Teaching figure (synthetic).* Cycle-602 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle600_swarm_ch19_w600_5.png)

*Teaching figure (synthetic).* Cycle-600 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle598_swarm_ch19_w598_5.png)

*Teaching figure (synthetic).* Cycle-598 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle596_swarm_ch19_w596_5.png)

*Teaching figure (synthetic).* Cycle-596 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle594_swarm_ch19_w594_5.png)

*Teaching figure (synthetic).* Cycle-594 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle592_swarm_ch19_w592_5.png)

*Teaching figure (synthetic).* Cycle-592 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle590_swarm_ch19_w590_5.png)

*Teaching figure (synthetic).* Cycle-590 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle588_swarm_ch19_w588_5.png)

*Teaching figure (synthetic).* Cycle-588 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle586_swarm_ch19_w586_5.png)

*Teaching figure (synthetic).* Cycle-586 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle584_swarm_ch19_w584_5.png)

*Teaching figure (synthetic).* Cycle-584 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle582_swarm_ch19_w582_5.png)

*Teaching figure (synthetic).* Cycle-582 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle580_swarm_ch19_w580_5.png)

*Teaching figure (synthetic).* Cycle-580 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle578_swarm_ch19_w578_5.png)

*Teaching figure (synthetic).* Cycle-578 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle576_swarm_ch19_w576_5.png)

*Teaching figure (synthetic).* Cycle-576 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle574_swarm_ch19_w574_5.png)

*Teaching figure (synthetic).* Cycle-574 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle572_swarm_ch19_w572_5.png)

*Teaching figure (synthetic).* Cycle-572 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle570_swarm_ch19_w570_5.png)

*Teaching figure (synthetic).* Cycle-570 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle568_swarm_ch19_w568_5.png)

*Teaching figure (synthetic).* Cycle-568 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle566_swarm_ch19_w566_5.png)

*Teaching figure (synthetic).* Cycle-566 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle564_swarm_ch19_w564_5.png)

*Teaching figure (synthetic).* Cycle-564 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle562_swarm_ch19_w562_5.png)

*Teaching figure (synthetic).* Cycle-562 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle560_swarm_ch19_w560_5.png)

*Teaching figure (synthetic).* Cycle-560 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle558_swarm_ch19_w558_5.png)

*Teaching figure (synthetic).* Cycle-558 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle556_swarm_ch19_w556_5.png)

*Teaching figure (synthetic).* Cycle-556 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle554_swarm_ch19_w554_5.png)

*Teaching figure (synthetic).* Cycle-554 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle552_swarm_ch19_w552_5.png)

*Teaching figure (synthetic).* Cycle-552 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle550_swarm_ch19_w550_5.png)

*Teaching figure (synthetic).* Cycle-550 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle548_swarm_ch19_w548_5.png)

*Teaching figure (synthetic).* Cycle-548 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle546_swarm_ch19_w546_5.png)

*Teaching figure (synthetic).* Cycle-546 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle544_swarm_ch19_w544_5.png)

*Teaching figure (synthetic).* Cycle-544 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle542_swarm_ch19_w542_5.png)

*Teaching figure (synthetic).* Cycle-542 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle540_swarm_ch19_w540_5.png)

*Teaching figure (synthetic).* Cycle-540 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle538_swarm_ch19_w538_5.png)

*Teaching figure (synthetic).* Cycle-538 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle536_swarm_ch19_w536_5.png)

*Teaching figure (synthetic).* Cycle-536 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle534_swarm_ch19_w534_5.png)

*Teaching figure (synthetic).* Cycle-534 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle532_swarm_ch19_w532_5.png)

*Teaching figure (synthetic).* Cycle-532 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle530_swarm_ch19_w530_5.png)

*Teaching figure (synthetic).* Cycle-530 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle528_swarm_ch19_w528_5.png)

*Teaching figure (synthetic).* Cycle-528 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle526_swarm_ch19_w526_5.png)

*Teaching figure (synthetic).* Cycle-526 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle524_swarm_ch19_w524_5.png)

*Teaching figure (synthetic).* Cycle-524 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle522_swarm_ch19_w522_5.png)

*Teaching figure (synthetic).* Cycle-522 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle520_swarm_ch19_w520_5.png)

*Teaching figure (synthetic).* Cycle-520 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle518_swarm_ch19_w518_5.png)

*Teaching figure (synthetic).* Cycle-518 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle516_swarm_ch19_w516_5.png)

*Teaching figure (synthetic).* Cycle-516 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle514_swarm_ch19_w514_5.png)

*Teaching figure (synthetic).* Cycle-514 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle512_swarm_ch19_w512_5.png)

*Teaching figure (synthetic).* Cycle-512 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle510_swarm_ch19_w510_5.png)

*Teaching figure (synthetic).* Cycle-510 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle508_swarm_ch19_w508_5.png)

*Teaching figure (synthetic).* Cycle-508 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle506_swarm_ch19_w506_5.png)

*Teaching figure (synthetic).* Cycle-506 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle504_swarm_ch19_w504_5.png)

*Teaching figure (synthetic).* Cycle-504 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle502_swarm_ch19_w502_5.png)

*Teaching figure (synthetic).* Cycle-502 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle500_swarm_ch19_w500_5.png)

*Teaching figure (synthetic).* Cycle-500 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle498_swarm_ch19_w498_5.png)

*Teaching figure (synthetic).* Cycle-498 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle496_swarm_ch19_w496_5.png)

*Teaching figure (synthetic).* Cycle-496 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle494_swarm_ch19_w494_5.png)

*Teaching figure (synthetic).* Cycle-494 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle492_swarm_ch19_w492_5.png)

*Teaching figure (synthetic).* Cycle-492 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle490_swarm_ch19_w490_5.png)

*Teaching figure (synthetic).* Cycle-490 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle488_swarm_ch19_w488_5.png)

*Teaching figure (synthetic).* Cycle-488 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle486_swarm_ch19_w486_5.png)

*Teaching figure (synthetic).* Cycle-486 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle484_swarm_ch19_w484_5.png)

*Teaching figure (synthetic).* Cycle-484 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle482_swarm_ch19_w482_5.png)

*Teaching figure (synthetic).* Cycle-482 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle480_swarm_ch19_w480_5.png)

*Teaching figure (synthetic).* Cycle-480 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle478_swarm_ch19_w478_5.png)

*Teaching figure (synthetic).* Cycle-478 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle476_swarm_ch19_w476_5.png)

*Teaching figure (synthetic).* Cycle-476 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle474_swarm_ch19_w474_5.png)

*Teaching figure (synthetic).* Cycle-474 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle472_swarm_ch19_w472_5.png)

*Teaching figure (synthetic).* Cycle-472 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle470_swarm_ch19_w470_5.png)

*Teaching figure (synthetic).* Cycle-470 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle468_swarm_ch19_w468_5.png)

*Teaching figure (synthetic).* Cycle-468 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle466_swarm_ch19_w466_5.png)

*Teaching figure (synthetic).* Cycle-466 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle464_swarm_ch19_w464_5.png)

*Teaching figure (synthetic).* Cycle-464 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle462_swarm_ch19_w462_5.png)

*Teaching figure (synthetic).* Cycle-462 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle460_swarm_ch19_w460_5.png)

*Teaching figure (synthetic).* Cycle-460 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle458_swarm_ch19_w458_5.png)

*Teaching figure (synthetic).* Cycle-458 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle456_swarm_ch19_w456_5.png)

*Teaching figure (synthetic).* Cycle-456 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle454_swarm_ch19_w454_5.png)

*Teaching figure (synthetic).* Cycle-454 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle452_swarm_ch19_w452_5.png)

*Teaching figure (synthetic).* Cycle-452 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle450_swarm_ch19_w450_5.png)

*Teaching figure (synthetic).* Cycle-450 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle448_swarm_ch19_w448_5.png)

*Teaching figure (synthetic).* Cycle-448 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle446_swarm_ch19_w446_5.png)

*Teaching figure (synthetic).* Cycle-446 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle444_swarm_ch19_w444_5.png)

*Teaching figure (synthetic).* Cycle-444 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle442_swarm_ch19_w442_5.png)

*Teaching figure (synthetic).* Cycle-442 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle440_swarm_ch19_w440_5.png)

*Teaching figure (synthetic).* Cycle-440 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle438_swarm_ch19_w438_5.png)

*Teaching figure (synthetic).* Cycle-438 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle436_swarm_ch19_w436_5.png)

*Teaching figure (synthetic).* Cycle-436 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle434_swarm_ch19_w434_5.png)

*Teaching figure (synthetic).* Cycle-434 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle432_swarm_ch19_w432_5.png)

*Teaching figure (synthetic).* Cycle-432 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle430_swarm_ch19_w430_5.png)

*Teaching figure (synthetic).* Cycle-430 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle428_swarm_ch19_w428_5.png)

*Teaching figure (synthetic).* Cycle-428 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle426_swarm_ch19_w426_5.png)

*Teaching figure (synthetic).* Cycle-426 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle424_swarm_ch19_w424_5.png)

*Teaching figure (synthetic).* Cycle-424 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle422_swarm_ch19_w422_5.png)

*Teaching figure (synthetic).* Cycle-422 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle420_swarm_ch19_w420_5.png)

*Teaching figure (synthetic).* Cycle-420 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle418_swarm_ch19_w418_5.png)

*Teaching figure (synthetic).* Cycle-418 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle416_swarm_ch19_w416_5.png)

*Teaching figure (synthetic).* Cycle-416 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle414_swarm_ch19_w414_5.png)

*Teaching figure (synthetic).* Cycle-414 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle412_swarm_ch19_w412_5.png)

*Teaching figure (synthetic).* Cycle-412 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle410_swarm_ch19_w410_5.png)

*Teaching figure (synthetic).* Cycle-410 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle408_swarm_ch19_w408_5.png)

*Teaching figure (synthetic).* Cycle-408 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle406_swarm_ch19_w406_5.png)

*Teaching figure (synthetic).* Cycle-406 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle404_swarm_ch19_w404_5.png)

*Teaching figure (synthetic).* Cycle-404 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle402_swarm_ch19_w402_5.png)

*Teaching figure (synthetic).* Cycle-402 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle400_swarm_ch19_w400_5.png)

*Teaching figure (synthetic).* Cycle-400 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle398_swarm_ch19_w398_5.png)

*Teaching figure (synthetic).* Cycle-398 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle396_swarm_ch19_w396_5.png)

*Teaching figure (synthetic).* Cycle-396 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle394_swarm_ch19_w394_5.png)

*Teaching figure (synthetic).* Cycle-394 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle392_swarm_ch19_w392_5.png)

*Teaching figure (synthetic).* Cycle-392 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle390_swarm_ch19_w390_5.png)

*Teaching figure (synthetic).* Cycle-390 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle388_swarm_ch19_w388_5.png)

*Teaching figure (synthetic).* Cycle-388 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle386_swarm_ch19_w386_5.png)

*Teaching figure (synthetic).* Cycle-386 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle384_swarm_ch19_w384_5.png)

*Teaching figure (synthetic).* Cycle-384 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle382_swarm_ch19_w382_5.png)

*Teaching figure (synthetic).* Cycle-382 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle380_swarm_ch19_w380_5.png)

*Teaching figure (synthetic).* Cycle-380 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle378_swarm_ch19_w378_5.png)

*Teaching figure (synthetic).* Cycle-378 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle376_swarm_ch19_w376_5.png)

*Teaching figure (synthetic).* Cycle-376 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle374_swarm_ch19_w374_5.png)

*Teaching figure (synthetic).* Cycle-374 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle372_swarm_ch19_w372_5.png)

*Teaching figure (synthetic).* Cycle-372 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle370_swarm_ch19_w370_5.png)

*Teaching figure (synthetic).* Cycle-370 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle368_swarm_ch19_w368_5.png)

*Teaching figure (synthetic).* Cycle-368 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle366_swarm_ch19_w366_5.png)

*Teaching figure (synthetic).* Cycle-366 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle364_swarm_ch19_w364_5.png)

*Teaching figure (synthetic).* Cycle-364 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle362_swarm_ch19_w362_5.png)

*Teaching figure (synthetic).* Cycle-362 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle360_swarm_ch19_w360_5.png)

*Teaching figure (synthetic).* Cycle-360 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle358_swarm_ch19_w358_5.png)

*Teaching figure (synthetic).* Cycle-358 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle356_swarm_ch19_w356_5.png)

*Teaching figure (synthetic).* Cycle-356 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle354_swarm_ch19_w354_5.png)

*Teaching figure (synthetic).* Cycle-354 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle352_swarm_ch19_w352_5.png)

*Teaching figure (synthetic).* Cycle-352 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle350_swarm_ch19_w350_5.png)

*Teaching figure (synthetic).* Cycle-350 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle348_swarm_ch19_w348_5.png)

*Teaching figure (synthetic).* Cycle-348 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle346_swarm_ch19_w346_5.png)

*Teaching figure (synthetic).* Cycle-346 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle344_swarm_ch19_w344_5.png)

*Teaching figure (synthetic).* Cycle-344 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle342_swarm_ch19_w342_5.png)

*Teaching figure (synthetic).* Cycle-342 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle340_swarm_ch19_w340_5.png)

*Teaching figure (synthetic).* Cycle-340 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle338_swarm_ch19_w338_5.png)

*Teaching figure (synthetic).* Cycle-338 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle336_swarm_ch19_w336_5.png)

*Teaching figure (synthetic).* Cycle-336 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle334_swarm_ch19_w334_5.png)

*Teaching figure (synthetic).* Cycle-334 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle332_swarm_ch19_w332_5.png)

*Teaching figure (synthetic).* Cycle-332 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle330_swarm_ch19_w330_5.png)

*Teaching figure (synthetic).* Cycle-330 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle328_swarm_ch19_w328_5.png)

*Teaching figure (synthetic).* Cycle-328 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle326_swarm_ch19_w326_5.png)

*Teaching figure (synthetic).* Cycle-326 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle324_swarm_ch19_w324_5.png)

*Teaching figure (synthetic).* Cycle-324 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle322_swarm_ch19_w322_5.png)

*Teaching figure (synthetic).* Cycle-322 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle320_swarm_ch19_w320_5.png)

*Teaching figure (synthetic).* Cycle-320 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle318_swarm_ch19_w318_5.png)

*Teaching figure (synthetic).* Cycle-318 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle316_swarm_ch19_w316_5.png)

*Teaching figure (synthetic).* Cycle-316 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle314_swarm_ch19_w314_5.png)

*Teaching figure (synthetic).* Cycle-314 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle312_swarm_ch19_w312_5.png)

*Teaching figure (synthetic).* Cycle-312 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle310_swarm_ch19_w310_5.png)

*Teaching figure (synthetic).* Cycle-310 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle308_swarm_ch19_w308_5.png)

*Teaching figure (synthetic).* Cycle-308 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle306_swarm_ch19_w306_5.png)

*Teaching figure (synthetic).* Cycle-306 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle304_swarm_ch19_w304_5.png)

*Teaching figure (synthetic).* Cycle-304 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle302_swarm_ch19_w302_5.png)

*Teaching figure (synthetic).* Cycle-302 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle300_swarm_ch19_w300_5.png)

*Teaching figure (synthetic).* Cycle-300 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle298_swarm_ch19_w298_5.png)

*Teaching figure (synthetic).* Cycle-298 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle296_swarm_ch19_w296_5.png)

*Teaching figure (synthetic).* Cycle-296 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle294_swarm_ch19_w294_5.png)

*Teaching figure (synthetic).* Cycle-294 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle292_swarm_ch19_w292_5.png)

*Teaching figure (synthetic).* Cycle-292 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle290_swarm_ch19_w290_5.png)

*Teaching figure (synthetic).* Cycle-290 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle288_swarm_ch19_w288_5.png)

*Teaching figure (synthetic).* Cycle-288 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle286_swarm_ch19_w286_5.png)

*Teaching figure (synthetic).* Cycle-286 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle284_swarm_ch19_w284_5.png)

*Teaching figure (synthetic).* Cycle-284 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle282_swarm_ch19_w282_5.png)

*Teaching figure (synthetic).* Cycle-282 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle280_swarm_ch19_w280_5.png)

*Teaching figure (synthetic).* Cycle-280 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle278_swarm_ch19_w278_5.png)

*Teaching figure (synthetic).* Cycle-278 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle276_swarm_ch19_w276_5.png)

*Teaching figure (synthetic).* Cycle-276 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle274_swarm_ch19_w274_5.png)

*Teaching figure (synthetic).* Cycle-274 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle272_swarm_ch19_w272_5.png)

*Teaching figure (synthetic).* Cycle-272 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle270_swarm_ch19_w270_5.png)

*Teaching figure (synthetic).* Cycle-270 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle268_swarm_ch19_w268_5.png)

*Teaching figure (synthetic).* Cycle-268 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle266_swarm_ch19_w266_5.png)

*Teaching figure (synthetic).* Cycle-266 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle264_swarm_ch19_w264_5.png)

*Teaching figure (synthetic).* Cycle-264 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle262_swarm_ch19_w262_5.png)

*Teaching figure (synthetic).* Cycle-262 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle260_swarm_ch19_w260_5.png)

*Teaching figure (synthetic).* Cycle-260 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle258_swarm_ch19_w258_5.png)

*Teaching figure (synthetic).* Cycle-258 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle256_swarm_ch19_w256_5.png)

*Teaching figure (synthetic).* Cycle-256 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle254_swarm_ch19_w254_5.png)

*Teaching figure (synthetic).* Cycle-254 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle252_swarm_ch19_w252_5.png)

*Teaching figure (synthetic).* Cycle-252 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle250_swarm_ch19_w250_5.png)

*Teaching figure (synthetic).* Cycle-250 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle248_swarm_ch19_w248_5.png)

*Teaching figure (synthetic).* Cycle-248 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle246_swarm_ch19_w246_5.png)

*Teaching figure (synthetic).* Cycle-246 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle244_swarm_ch19_w244_5.png)

*Teaching figure (synthetic).* Cycle-244 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle242_swarm_ch19_w242_5.png)

*Teaching figure (synthetic).* Cycle-242 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle240_swarm_ch19_w240_5.png)

*Teaching figure (synthetic).* Cycle-240 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle238_swarm_ch19_w238_5.png)

*Teaching figure (synthetic).* Cycle-238 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle236_swarm_ch19_w236_5.png)

*Teaching figure (synthetic).* Cycle-236 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle234_swarm_ch19_w234_5.png)

*Teaching figure (synthetic).* Cycle-234 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle232_swarm_ch19_w232_5.png)

*Teaching figure (synthetic).* Cycle-232 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle230_swarm_ch19_w230_5.png)

*Teaching figure (synthetic).* Cycle-230 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle228_swarm_ch19_w228_5.png)

*Teaching figure (synthetic).* Cycle-228 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle226_swarm_ch19_w226_5.png)

*Teaching figure (synthetic).* Cycle-226 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle224_swarm_ch19_w224_5.png)

*Teaching figure (synthetic).* Cycle-224 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle222_swarm_ch19_w222_5.png)

*Teaching figure (synthetic).* Cycle-222 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle220_swarm_ch19_w220_5.png)

*Teaching figure (synthetic).* Cycle-220 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle218_swarm_ch19_w218_5.png)

*Teaching figure (synthetic).* Cycle-218 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle216_swarm_ch19_w216_5.png)

*Teaching figure (synthetic).* Cycle-216 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle214_swarm_ch19_w214_5.png)

*Teaching figure (synthetic).* Cycle-214 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle212_swarm_ch19_w212_5.png)

*Teaching figure (synthetic).* Cycle-212 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle210_swarm_ch19_w210_5.png)

*Teaching figure (synthetic).* Cycle-210 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle208_swarm_ch19_w208_5.png)

*Teaching figure (synthetic).* Cycle-208 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle206_swarm_ch19_w206_5.png)

*Teaching figure (synthetic).* Cycle-206 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle204_swarm_ch19_w204_5.png)

*Teaching figure (synthetic).* Cycle-204 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle202_swarm_ch19_w202_5.png)

*Teaching figure (synthetic).* Cycle-202 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle200_swarm_ch19_w200_5.png)

*Teaching figure (synthetic).* Cycle-200 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle198_swarm_ch19_w198_5.png)

*Teaching figure (synthetic).* Cycle-198 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle196_swarm_ch19_w196_5.png)

*Teaching figure (synthetic).* Cycle-196 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle194_swarm_ch19_w194_5.png)

*Teaching figure (synthetic).* Cycle-194 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle192_swarm_ch19_w192_5.png)

*Teaching figure (synthetic).* Cycle-192 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle190_swarm_ch19_w190_5.png)

*Teaching figure (synthetic).* Cycle-190 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle188_swarm_ch19_w188_5.png)

*Teaching figure (synthetic).* Cycle-188 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle186_swarm_ch19_w186_5.png)

*Teaching figure (synthetic).* Cycle-186 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle184_swarm_ch19_w184_5.png)

*Teaching figure (synthetic).* Cycle-184 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle182_swarm_ch19_w182_5.png)

*Teaching figure (synthetic).* Cycle-182 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle180_swarm_ch19_w180_5.png)

*Teaching figure (synthetic).* Cycle-180 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle178_swarm_ch19_w178_5.png)

*Teaching figure (synthetic).* Cycle-178 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle176_swarm_ch19_w176_5.png)

*Teaching figure (synthetic).* Cycle-176 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle174_swarm_ch19_w174_5.png)

*Teaching figure (synthetic).* Cycle-174 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle172_swarm_ch19_w172_5.png)

*Teaching figure (synthetic).* Cycle-172 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle170_swarm_ch19_w170_5.png)

*Teaching figure (synthetic).* Cycle-170 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle168_swarm_ch19_w168_5.png)

*Teaching figure (synthetic).* Cycle-168 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle166_swarm_ch19_w166_5.png)

*Teaching figure (synthetic).* Cycle-166 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle164_swarm_ch19_w164_5.png)

*Teaching figure (synthetic).* Cycle-164 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle162_swarm_ch19_w162_5.png)

*Teaching figure (synthetic).* Cycle-162 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle160_swarm_ch19_w160_5.png)

*Teaching figure (synthetic).* Cycle-160 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle158_swarm_ch19_w158_5.png)

*Teaching figure (synthetic).* Cycle-158 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle156_swarm_ch19_w156_5.png)

*Teaching figure (synthetic).* Cycle-156 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle154_swarm_ch19_w154_5.png)

*Teaching figure (synthetic).* Cycle-154 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle152_swarm_ch19_w152_5.png)

*Teaching figure (synthetic).* Cycle-152 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle150_swarm_ch19_w150_5.png)

*Teaching figure (synthetic).* Cycle-150 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle148_swarm_ch19_w148_5.png)

*Teaching figure (synthetic).* Cycle-148 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle146_swarm_ch19_w146_5.png)

*Teaching figure (synthetic).* Cycle-146 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle144_swarm_ch19_w144_5.png)

*Teaching figure (synthetic).* Cycle-144 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle142_swarm_ch19_w142_5.png)

*Teaching figure (synthetic).* Cycle-142 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle140_swarm_ch19_w140_5.png)

*Teaching figure (synthetic).* Cycle-140 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle138_swarm_ch19_w138_5.png)

*Teaching figure (synthetic).* Cycle-138 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle136_swarm_ch19_w136_5.png)

*Teaching figure (synthetic).* Cycle-136 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle134_swarm_ch19_w134_5.png)

*Teaching figure (synthetic).* Cycle-134 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle132_swarm_ch19_w132_5.png)

*Teaching figure (synthetic).* Cycle-132 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle130_swarm_ch19_w130_5.png)

*Teaching figure (synthetic).* Cycle-130 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle128_swarm_ch19_w128_5.png)

*Teaching figure (synthetic).* Cycle-128 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle126_swarm_ch19_w126_5.png)

*Teaching figure (synthetic).* Cycle-126 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle124_swarm_ch19_w124_5.png)

*Teaching figure (synthetic).* Cycle-124 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle122_swarm_ch19_w122_5.png)

*Teaching figure (synthetic).* Cycle-122 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle120_swarm_ch19_w120_5.png)

*Teaching figure (synthetic).* Cycle-120 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle118_swarm_ch19_w118_5.png)

*Teaching figure (synthetic).* Cycle-118 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle116_swarm_ch19_w116_5.png)

*Teaching figure (synthetic).* Cycle-116 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle114_swarm_ch19_w114_5.png)

*Teaching figure (synthetic).* Cycle-114 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle112_swarm_ch19_w112_5.png)

*Teaching figure (synthetic).* Cycle-112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle110_swarm_ch19_w110_5.png)

*Teaching figure (synthetic).* Cycle-110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle108_swarm_ch19_w108_5.png)

*Teaching figure (synthetic).* Cycle-108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle106_swarm_ch19_w106_5.png)

*Teaching figure (synthetic).* Cycle-106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle104_swarm_ch19_w104_5.png)

*Teaching figure (synthetic).* Cycle-104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle102_swarm_ch19_w102_5.png)

*Teaching figure (synthetic).* Cycle-102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle100_swarm_ch19_w100_5.png)

*Teaching figure (synthetic).* Cycle-100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle98_swarm_ch19_w98_5.png)

*Teaching figure (synthetic).* Cycle-98 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle96_swarm_ch19_w96_5.png)

*Teaching figure (synthetic).* Cycle-96 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle94_swarm_ch19_w94_5.png)

*Teaching figure (synthetic).* Cycle-94 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle92_swarm_ch19_w92_5.png)

*Teaching figure (synthetic).* Cycle-92 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle90_swarm_ch19_w90_5.png)

*Teaching figure (synthetic).* Cycle-90 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle88_swarm_ch19_w88_5.png)

*Teaching figure (synthetic).* Cycle-88 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle86_swarm_ch19_w86_5.png)

*Teaching figure (synthetic).* Cycle-86 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle84_swarm_ch19_w84_5.png)

*Teaching figure (synthetic).* Cycle-84 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle82_swarm_ch19_w82_5.png)

*Teaching figure (synthetic).* Cycle-82 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle80_swarm_ch19_w80_5.png)

*Teaching figure (synthetic).* Cycle-80 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle78_swarm_ch19_w78_5.png)

*Teaching figure (synthetic).* Cycle-78 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle76_swarm_ch19_w76_5.png)

*Teaching figure (synthetic).* Cycle-76 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle74_swarm_ch19_w74_5.png)

*Teaching figure (synthetic).* Cycle-74 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle72_swarm_ch19_w72_5.png)

*Teaching figure (synthetic).* Cycle-72 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle70_swarm_ch19_w70_5.png)

*Teaching figure (synthetic).* Cycle-70 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle68_swarm_ch19_w68_5.png)

*Teaching figure (synthetic).* Cycle-68 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle66_swarm_ch19_w66_5.png)

*Teaching figure (synthetic).* Cycle-66 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle64_swarm_ch19_w64_5.png)

*Teaching figure (synthetic).* Cycle-64 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle62_swarm_ch19_w62_5.png)

*Teaching figure (synthetic).* Cycle-62 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle60_swarm_ch19_c60e.png)

*Teaching figure (synthetic).* Cycle-60 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle58_swarm_ch19_c58e.png)

*Teaching figure (synthetic).* Cycle-58 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle56_swarm_ch19_seq_fpr.png)

*Teaching figure (synthetic).* Cycle-56 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle54_swarm_ch19_se_arr.png)

*Teaching figure (synthetic).* Cycle-54 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle52_swarm_ch19_opt_stop.png)

*Teaching figure (synthetic).* Cycle-52 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle50_swarm_ch19_ci_width.png)

*Teaching figure (synthetic).* Cycle-50 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle48_swarm_ch19_compat_int.png)

*Teaching figure (synthetic).* Cycle-48 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle46_swarm_ch19_se_n.png)

*Teaching figure (synthetic).* Cycle-46 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle44_swarm_ch19_sequential.png)

*Teaching figure (synthetic).* Cycle-44 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle42_swarm_ch19_optional_stop.png)

*Teaching figure (synthetic).* Cycle-42 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle40_swarm_ch19_compat.png)

*Teaching figure (synthetic).* Cycle-40 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 19 (original scientific teaching figure).](../assets/figures/cycle38_swarm_ch19_arr_precision.png)

*Teaching figure (synthetic).* Cycle-38 densify scientific residual (ch15–28).



Neurologic literature remains deeply afflicted by dichotomania—the compulsive categorization of continuous evidence into 'positive' or 'negative' bins based on an arbitrary mathematical boundary, typically alpha = 0.05. This cognitive distortion causes clinicians to equate a p-value of 0.04 with definitive truth and a p-value of 0.06 with statistical noise. The reality is that chance is a continuous threat to precision, and treating inferential statistics as a categorical verdict fundamentally misunderstands the architecture of uncertainty.

Statistical inference is an exercise in estimation, not adjudication. The goal of a clinical trial is not to prove that an effect is exactly zero or not zero, but to estimate the magnitude of the effect and quantify the precision of that estimate. By elevating the p-value above the confidence interval, readers systematically ignore the clinical importance of the point estimate and the plausible range of alternative truths contained within the data. A rigorously designed but imprecise study of absolute benefits is infinitely more useful for patient care than a highly significant, massively confounded artifact.

- Random error (chance) affects precision; systematic error (bias) corrupts validity.
- Hypothesis testing cannot rescue invalid estimates derived from confounded data.
- A 'nonsignificant' result does not prove equivalence or absence of effect.
- A 'statistically significant' result does not establish biologic importance or causal truth.

## Sampling Variation and the Illusion of Replication Failure

Assume a fixed, universal truth: a specific neuroprotectant reduces 90-day mortality by exactly 4.0 percentage points. If we were to theoretically execute 100 identical trials, each enrolling 300 patients from the exact same population, the observed risk differences would not uniformly be 4.0 percent. The estimates would scatter around the true value, yielding results like 1.2 percent, 7.8 percent, and perhaps −0.5 percent. This scatter is sampling variation. It is the inevitable consequence of measuring a sample rather than a census.

When two legitimate stroke trials report divergent point estimates, the discrepancy is frequently weaponized by factions to claim structural flaws or paradigm shifts. Often, it is merely sampling variation operating exactly as probability theory dictates. Precision is overwhelmingly a function of the event count, not simply the total denominator. A massive cohort with 20 outcome events will yield desperately unstable estimates compared to a smaller trial with 300 events. Confidence intervals explicitly quantify this expected scatter; overlapping intervals across trials generally suggest compatibility with a shared underlying truth, not a crisis of replication.

## Estimation Culture and Confidence Interval Interpretation

The standard error (SE) is the foundational metric of precision, approximating the standard deviation of the sampling distribution for a given statistic. It measures how wildly our estimate would fluctuate upon repeated sampling. A confidence interval (CI) operationalizes the standard error. For a 95% Wald interval, we essentially take the point estimate and extend roughly 1.96 standard errors in both directions. The frequentist definition of a 95% CI—that 95% of such intervals computed over infinite repetitions will capture the true parameter—is mathematically correct but clinically sterile.

For appraisal, adopt the compatibility interpretation: the confidence interval delineates the spectrum of effect sizes that are reasonably compatible with the observed data, conditional on the statistical model and its assumptions being flawless. Values clustered near the point estimate are highly compatible; values at the extreme limits are marginally compatible; values outside the interval are highly incompatible. This framework immediately neutralizes dichotomania.

Under estimation culture, an absolute risk reduction (ARR) of 3.0% (95% CI, −1.0% to 7.0%) is never dismissed as 'negative.' It is accurately characterized as structurally imprecise data compatible with both a clinically vital 7.0% absolute benefit and a trivial 1.0% absolute harm. Conversely, an ARR of 0.2% (95% CI, 0.1% to 0.3%) is statistically significant but clinically microscopic. Decision-making requires overlaying the interval against the minimum clinically important difference, not just the null value.

![Four synthetic absolute-risk CIs classified against the null and a minimum clinically important difference (original teaching figure).](../assets/figures/cycle2_ch19_ci_compatibility.png)

*Teaching figure (synthetic).* Interval A rules out both the null and an MCID miss—actionable if valid. Interval B is “nonsignificant” yet compatible with large benefit *and* small harm—imprecise, not negative. Interval C is significant but clinically tiny. Interval D keeps harm on the table. Dichotomania at p = 0.05 collapses these four distinct decision problems into two useless bins.

![Precision without honesty: narrow biased ARR CIs miss the true absolute effect while wide honest intervals still straddle decision thresholds (original teaching figure).](../assets/figures/cycle7_swarm_ch19_precision_bias_arr.png)

*Teaching figure (synthetic).* Estimation culture is not “narrower is better.” A precise wrong ARR rewrites pathways faster than an imprecise honest one. If the ARR CI includes 0, the NNT interval runs to infinity—say so explicitly.

```
THE ESTIMATION HEURISTIC
------------------------
1. Identify the point estimate on the absolute scale.
2. Identify the bounds of the 95% CI.
3. Locate the null value (0 for differences, 1 for ratios).
4. Locate the minimum clinically important difference (MCID).
5. Determine compatibility: Does the CI include the MCID? The null? Meaningful harm?
6. Conclude: Is the precision sufficient to alter clinical pathways, assuming zero bias?
```

## The P-Value: Mathematical Reality Versus Clinical Fiction

The p-value is perhaps the most chronically misunderstood metric in biomedicine. Formally, it is the probability of observing a test statistic at least as extreme as the one calculated, assuming that the null hypothesis is true and that all background assumptions of the statistical model are perfectly met. It is fundamentally a measure of data surprise under a highly specific, often implausible scenario (the sharp null).

The p-value does NOT represent the probability that the null hypothesis is true. It does NOT represent the probability that the finding is a 'fluke.' It provides absolutely no information regarding the magnitude, clinical relevance, or causal reality of the estimated effect. A p-value of 0.001 in an administrative database of five million patients can comfortably correspond to an effect size so minuscule it is irrelevant to human health. Conversely, a p-value of 0.15 in a trial of 80 patients may obscure a massive therapeutic signal drowning in random error.

When authors state 'there was no difference between groups (p = 0.30)', they are committing an inferential error. The correct statement is 'the data were insufficiently precise to reject the null hypothesis of zero difference.' A large p-value simply indicates that the observed data are not highly surprising if the true effect were zero. It does not confirm that the true effect is zero. Readers must relentlessly demand the absolute point estimate and its confidence interval whenever a p-value is presented.

## Type I Errors, Type II Errors, and the Misuse of Power

In the Neyman-Pearson framework of hypothesis testing, a Type I error (alpha) occurs when a true null hypothesis is incorrectly rejected—a false positive. A Type II error (beta) occurs when a false null hypothesis fails to be rejected—a false negative. Statistical power (1 - beta) is the pre-study probability that the trial will successfully reject the null, assuming the true effect size is exactly as specified in the design phase.

Crucially, power is an architectural tool used before data collection to size the cohort. Once the data are collected and the confidence interval is calculated, power becomes entirely irrelevant for interpreting the results. Calculating 'post hoc power' using the observed effect size is a mathematical tautology that merely repackages the p-value; a non-significant p-value will unconditionally yield low post hoc power. If a trial fails to cross the alpha threshold, do not dismiss it as 'underpowered'—a term that implies the treatment works but the sample was too small. Instead, analyze the confidence interval to determine if the trial's precision formally excludes meaningful clinical benefit.

## The Multiplicity Penalty: Subgroups and Secondary Endpoints

![Multiplicity multiplies expected false positives and claimed significant findings when secondaries and post-hoc tests accumulate (original teaching figure).](../assets/figures/cycle12_swarm_ch19_multiplicity.png)

*Teaching figure (synthetic).* Each extra unadjusted test is an absolute false-discovery risk. Pre-specify, correct, or treat as hypothesis-generating only.


If an investigator executes 20 independent tests on data where the true effect is uniformly zero, probability dictates that one test will cross the p < 0.05 threshold purely by chance. In stroke research, the combination of secondary endpoints, functional dichotomies, and intricate subgroup stratifications easily generates dozens of unadjusted comparisons. Without rigorous pre-specification and alpha-spending controls (e.g., hierarchical testing, Bonferroni, Hochberg), the family-wise error rate inflates violently, degrading the literature with false-positive noise.

Subgroup analyses are notoriously vulnerable. An overall trial may be flat, but the investigators discover a 'significant' benefit in right-sided occlusions treated between 3 and 4.5 hours. Without a formal test for interaction demonstrating that the treatment effect genuinely differs across the stratum, such findings are overwhelmingly likely to be statistical illusions born of sampling variation in tiny strata. Treat exploratory subgroup findings as hypotheses requiring independent replication, never as actionable clinical directives.

## Absolute Effects and the Arithmetic of NNT

Relative measures of effect (RR, OR, HR) are mathematically stable across varying baseline risks, making them useful for meta-analysis but deceptive for clinical application. A relative risk reduction of 50% sounds transformative. If the baseline risk of the event is 20%, the absolute risk reduction (ARR) is a substantial 10%. If the baseline risk is 0.2%, the ARR is a trivial 0.1%. Clinical decision-making demands the absolute scale.

The Number Needed to Treat (NNT = 1 / ARR) translates absolute probability into a frequency format. However, NNT point estimates presented without confidence intervals project a false certainty. When computing a confidence interval for an NNT based on an ARR interval that crosses zero, the math becomes non-linear and fractures through infinity. An ARR CI of −1.0% to 5.0% translates to an NNT interval encompassing benefit (NNT 20 down to infinity) and harm (Number Needed to Harm [NNH] of 100). Therefore, expressing the uncertainty primarily through absolute risk differences (e.g., 'between 1 more and 5 fewer events per 100 patients') is far more transparent than manipulating disjointed NNT ranges.

![When an ARR confidence interval includes the null, the reciprocal NNT interval fractures through infinity into an NNH limb (original teaching figure).](../assets/figures/cycle4_swarm_ch19_nnt_ci_infinity.png)

*Teaching figure (synthetic).* Point ARR 2 pp with 95% CI −1 to +5 pp is compatible with harm, null, and benefit. Do not print a lone NNT; prefer absolute event-count language (“between 1 more and 5 fewer events per 100”).

## Manual Derivation: Exposing the Inferential Machinery

To demystify the black box of statistical software, we manually derive a risk difference and its confidence interval. Consider a hypothetical trial evaluating a neuroprotectant against standard care. The outcome is mortality at 90 days.

```
OBSERVED DATA
-------------
Control Group (R0): 45 deaths / 250 patients = 0.180 (18.0%)
Treatment Group (R1): 30 deaths / 250 patients = 0.120 (12.0%)

ESTIMATES
---------
Absolute Risk Reduction (ARR) = R0 - R1 = 0.180 - 0.120 = 0.060 (6.0%)
Point NNT = 1 / 0.060 = 16.7

STANDARD ERRORS (SE = sqrt[ p*(1-p) / n ])
---------------
SE(R0) = sqrt[ 0.180 * 0.820 / 250 ] = sqrt[ 0.0005904 ] = 0.0243
SE(R1) = sqrt[ 0.120 * 0.880 / 250 ] = sqrt[ 0.0004224 ] = 0.0206

SE(ARR) = sqrt[ SE(R0)^2 + SE(R1)^2 ]
SE(ARR) = sqrt[ 0.0005904 + 0.0004224 ] = sqrt[ 0.0010128 ] = 0.0318

95% CONFIDENCE INTERVAL (ARR +/- 1.96 * SE)
-----------------------
Margin of Error = 1.96 * 0.0318 = 0.0623
95% CI = 0.060 +/- 0.0623
95% CI = -0.0023 to 0.1223 (-0.2% to 12.2%)
```

This manual calculation yields an ARR of 6.0% with a 95% CI ranging from a 0.2% absolute increase in mortality to a 12.2% absolute decrease. Because the interval crosses zero, the p-value will inevitably be greater than 0.05. A dichotomaniac dismisses the trial as 'negative.' A practitioner of estimation culture recognizes that while the data are mathematically compatible with trivial harm, they are substantially more compatible with massive clinical benefit (e.g., up to 12 fewer deaths per 100 patients). The study is not negative; it is severely imprecise and mandates further investigation, not abandonment.


![fig64_calibration_deciles.png original teaching graphic](../assets/figures/fig64_calibration_deciles.png)

*Original teaching graphic (fig64_calibration_deciles.png).*

## Chapter summary

Statistical inference in neurology must abandon the binary constraints of hypothesis testing in favor of continuous parameter estimation. Sampling variation dictates that repeated observations of a true phenomenon will yield disparate point estimates; confidence intervals quantify this structural scatter. P-values assess the surprise of the data under a strict null hypothesis, failing entirely to measure the magnitude or clinical reality of an effect. Concepts like statistical power and Type I/II errors are architectural tools for trial design, utterly devoid of utility for interpreting post-hoc findings. Unregulated multiplicity in subgroups and secondary endpoints severely degrades evidentiary integrity. Absolute effects, particularly the Absolute Risk Reduction, must anchor clinical interpretation, as relative measures inherently camouflage the magnitude of patient-level impact. The ultimate mandate of appraisal is prioritizing validity over precision: an infinitely narrow confidence interval surrounding a structurally biased estimate is nothing more than a precise lie.

## Practice and reflection

1. Calculate the absolute risk reduction, the standard error of the difference, and the 95% confidence interval for a hypothetical trial where Control mortality is 22% (N=400) and Treatment mortality is 18% (N=400).
2. Draft a formal critique of a peer-reviewed abstract that concludes a neuroprotectant 'does not work' based strictly on a primary endpoint p-value of 0.07.
3. Differentiate between the mathematical definition of a frequentist 95% confidence interval and the clinical application of the 'compatibility interval' framework.
4. Examine a recent endovascular trial and catalog all unadjusted secondary endpoints and subgroup analyses; calculate the probability of at least one false positive assuming a family-wise null.
5. Translate a relative risk of 0.60 (95% CI, 0.45-0.85) into absolute risk reductions assuming a baseline event rate of 2%, and again assuming a baseline event rate of 25%. Discuss the divergent clinical imperatives.
6. Articulate the logical fallacy of calculating 'post hoc power' for an primary endpoint that failed to achieve statistical significance.
7. Explain the non-linear discontinuity that occurs when attempting to calculate a Number Needed to Treat (NNT) confidence interval derived from an ARR interval that crosses the null.
8. Construct an argument for why a highly significant p-value (p < 0.001) in an observational registry of 500,000 patients provides functionally zero evidence of a causal relationship.

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

