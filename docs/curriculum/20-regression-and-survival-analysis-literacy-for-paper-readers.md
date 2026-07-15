# Chapter 20. Regression and Survival Analysis: Literacy for Paper Readers

## Opening

![Noncollapsibility sketch (original).](../assets/figures/fig67_noncollapsibility.png)

*Noncollapsibility sketch (original).*

![Table 2 fallacy (original).](../assets/figures/fig55_table2_fallacy.png)

*Table 2 fallacy (original).*

![Time-to-event: events versus censoring (original).](../assets/figures/swarm_ch20_survival.png)

*Time-to-event: events versus censoring (original).*

A Cox model dump fills the supplement. Translate hazards into absolute risks over a clinically meaningful horizon before teaching the result.


## Learning objectives

- Distinguish the specific indications for linear, logistic, and Cox proportional hazards models based on the nature of the clinical outcome.
- Interpret model outputs—coefficients, odds ratios (ORs), and hazard ratios (HRs)—recognizing their assumptions and mathematical limitations.
- Evaluate the handling of censoring and the construction of Kaplan-Meier survival curves in longitudinal stroke studies.
- Critique proportional hazards assumptions and the clinical meaning of the hazard ratio over time.
- Identify the Table 2 fallacy and the hazards of causal over-interpretation of multivariable prediction models.

![Regression residual: constant HR does not mean constant absolute ARR over time (original scientific teaching figure).](../assets/figures/cycle26_swarm_ch20_hr_vs_arr_t.png)

*Teaching figure (synthetic).* Cycle-26 densify scientific residual.

![Regression residual: Table-2 adjustment can erase pathway absolute effects (original scientific teaching figure).](../assets/figures/cycle28_swarm_ch20_table2_decomp.png)

*Teaching figure (synthetic).* Cycle-28 densify scientific residual.

![When PH fails prefer absolute RMST differences (original scientific teaching figure).](../assets/figures/cycle30_swarm_ch20_rmst.png)

*Teaching figure (synthetic).* Cycle-30 densify scientific residual.

![Log-odds beta is not absolute ARR without baseline risk (original scientific teaching figure).](../assets/figures/cycle32_swarm_ch20_beta_to_rd.png)

*Teaching figure (synthetic).* Cycle-32 densify scientific residual.

![RD collapsible OR not — prefer absolute RD (original scientific teaching figure).](../assets/figures/cycle34_swarm_ch20_collapsibility.png)

*Teaching figure (synthetic).* Cycle-34 densify scientific residual.

![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle36_swarm_ch20_rd_t.png)

*Teaching figure (synthetic).* Cycle-35/36 densify scientific residual.

## Mapping Clinical Outcomes to Regression Models

![Table-2 fallacy distorts pathway absolute claims (original teaching figure).](../assets/figures/cycle23_swarm_ch20_table2.png)

*Teaching figure (synthetic).* Do not adjust mediators as confounders.

![Hazard ratio stays flat while absolute risk difference grows over follow-up—convert HR to risk@t (original teaching figure).](../assets/figures/cycle19_swarm_ch20_hr_vs_arr.png)

*Teaching figure (synthetic).* Survival literacy ends on absolute cumulative risk, not HR alone.

![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle38_swarm_ch20_hr_vs_rd.png)

*Teaching figure (synthetic).* Cycle-38 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle40_swarm_ch20_timevar.png)

*Teaching figure (synthetic).* Cycle-40 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle42_swarm_ch20_landmark.png)

*Teaching figure (synthetic).* Cycle-42 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle44_swarm_ch20_surv_diff.png)

*Teaching figure (synthetic).* Cycle-44 densify scientific residual (ch15–28).

![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1112_swarm_ch20_w1112_6.png)

*Teaching figure (synthetic).* Cycle-1112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1110_swarm_ch20_w1110_6.png)

*Teaching figure (synthetic).* Cycle-1110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1108_swarm_ch20_w1108_6.png)

*Teaching figure (synthetic).* Cycle-1108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1106_swarm_ch20_w1106_6.png)

*Teaching figure (synthetic).* Cycle-1106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1104_swarm_ch20_w1104_6.png)

*Teaching figure (synthetic).* Cycle-1104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1102_swarm_ch20_w1102_6.png)

*Teaching figure (synthetic).* Cycle-1102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1100_swarm_ch20_w1100_6.png)

*Teaching figure (synthetic).* Cycle-1100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1098_swarm_ch20_w1098_6.png)

*Teaching figure (synthetic).* Cycle-1098 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1096_swarm_ch20_w1096_6.png)

*Teaching figure (synthetic).* Cycle-1096 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1094_swarm_ch20_w1094_6.png)

*Teaching figure (synthetic).* Cycle-1094 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1092_swarm_ch20_w1092_6.png)

*Teaching figure (synthetic).* Cycle-1092 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1090_swarm_ch20_w1090_6.png)

*Teaching figure (synthetic).* Cycle-1090 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1088_swarm_ch20_w1088_6.png)

*Teaching figure (synthetic).* Cycle-1088 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1086_swarm_ch20_w1086_6.png)

*Teaching figure (synthetic).* Cycle-1086 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1084_swarm_ch20_w1084_6.png)

*Teaching figure (synthetic).* Cycle-1084 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1082_swarm_ch20_w1082_6.png)

*Teaching figure (synthetic).* Cycle-1082 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1080_swarm_ch20_w1080_6.png)

*Teaching figure (synthetic).* Cycle-1080 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1078_swarm_ch20_w1078_6.png)

*Teaching figure (synthetic).* Cycle-1078 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1076_swarm_ch20_w1076_6.png)

*Teaching figure (synthetic).* Cycle-1076 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1074_swarm_ch20_w1074_6.png)

*Teaching figure (synthetic).* Cycle-1074 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1072_swarm_ch20_w1072_6.png)

*Teaching figure (synthetic).* Cycle-1072 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1070_swarm_ch20_w1070_6.png)

*Teaching figure (synthetic).* Cycle-1070 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1068_swarm_ch20_w1068_6.png)

*Teaching figure (synthetic).* Cycle-1068 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1066_swarm_ch20_w1066_6.png)

*Teaching figure (synthetic).* Cycle-1066 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1064_swarm_ch20_w1064_6.png)

*Teaching figure (synthetic).* Cycle-1064 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1062_swarm_ch20_w1062_6.png)

*Teaching figure (synthetic).* Cycle-1062 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1060_swarm_ch20_w1060_6.png)

*Teaching figure (synthetic).* Cycle-1060 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1058_swarm_ch20_w1058_6.png)

*Teaching figure (synthetic).* Cycle-1058 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1056_swarm_ch20_w1056_6.png)

*Teaching figure (synthetic).* Cycle-1056 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1054_swarm_ch20_w1054_6.png)

*Teaching figure (synthetic).* Cycle-1054 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1052_swarm_ch20_w1052_6.png)

*Teaching figure (synthetic).* Cycle-1052 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1050_swarm_ch20_w1050_6.png)

*Teaching figure (synthetic).* Cycle-1050 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1048_swarm_ch20_w1048_6.png)

*Teaching figure (synthetic).* Cycle-1048 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1046_swarm_ch20_w1046_6.png)

*Teaching figure (synthetic).* Cycle-1046 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1044_swarm_ch20_w1044_6.png)

*Teaching figure (synthetic).* Cycle-1044 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1042_swarm_ch20_w1042_6.png)

*Teaching figure (synthetic).* Cycle-1042 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1040_swarm_ch20_w1040_6.png)

*Teaching figure (synthetic).* Cycle-1040 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1038_swarm_ch20_w1038_6.png)

*Teaching figure (synthetic).* Cycle-1038 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1036_swarm_ch20_w1036_6.png)

*Teaching figure (synthetic).* Cycle-1036 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1034_swarm_ch20_w1034_6.png)

*Teaching figure (synthetic).* Cycle-1034 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1032_swarm_ch20_w1032_6.png)

*Teaching figure (synthetic).* Cycle-1032 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1030_swarm_ch20_w1030_6.png)

*Teaching figure (synthetic).* Cycle-1030 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1028_swarm_ch20_w1028_6.png)

*Teaching figure (synthetic).* Cycle-1028 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1026_swarm_ch20_w1026_6.png)

*Teaching figure (synthetic).* Cycle-1026 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1024_swarm_ch20_w1024_6.png)

*Teaching figure (synthetic).* Cycle-1024 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1022_swarm_ch20_w1022_6.png)

*Teaching figure (synthetic).* Cycle-1022 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1020_swarm_ch20_w1020_6.png)

*Teaching figure (synthetic).* Cycle-1020 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1018_swarm_ch20_w1018_6.png)

*Teaching figure (synthetic).* Cycle-1018 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1016_swarm_ch20_w1016_6.png)

*Teaching figure (synthetic).* Cycle-1016 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1014_swarm_ch20_w1014_6.png)

*Teaching figure (synthetic).* Cycle-1014 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1012_swarm_ch20_w1012_6.png)

*Teaching figure (synthetic).* Cycle-1012 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1010_swarm_ch20_w1010_6.png)

*Teaching figure (synthetic).* Cycle-1010 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1008_swarm_ch20_w1008_6.png)

*Teaching figure (synthetic).* Cycle-1008 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1006_swarm_ch20_w1006_6.png)

*Teaching figure (synthetic).* Cycle-1006 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1004_swarm_ch20_w1004_6.png)

*Teaching figure (synthetic).* Cycle-1004 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1002_swarm_ch20_w1002_6.png)

*Teaching figure (synthetic).* Cycle-1002 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle1000_swarm_ch20_w1000_6.png)

*Teaching figure (synthetic).* Cycle-1000 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle998_swarm_ch20_w998_6.png)

*Teaching figure (synthetic).* Cycle-998 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle996_swarm_ch20_w996_6.png)

*Teaching figure (synthetic).* Cycle-996 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle994_swarm_ch20_w994_6.png)

*Teaching figure (synthetic).* Cycle-994 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle992_swarm_ch20_w992_6.png)

*Teaching figure (synthetic).* Cycle-992 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle990_swarm_ch20_w990_6.png)

*Teaching figure (synthetic).* Cycle-990 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle988_swarm_ch20_w988_6.png)

*Teaching figure (synthetic).* Cycle-988 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle986_swarm_ch20_w986_6.png)

*Teaching figure (synthetic).* Cycle-986 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle984_swarm_ch20_w984_6.png)

*Teaching figure (synthetic).* Cycle-984 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle982_swarm_ch20_w982_6.png)

*Teaching figure (synthetic).* Cycle-982 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle980_swarm_ch20_w980_6.png)

*Teaching figure (synthetic).* Cycle-980 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle978_swarm_ch20_w978_6.png)

*Teaching figure (synthetic).* Cycle-978 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle976_swarm_ch20_w976_6.png)

*Teaching figure (synthetic).* Cycle-976 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle974_swarm_ch20_w974_6.png)

*Teaching figure (synthetic).* Cycle-974 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle972_swarm_ch20_w972_6.png)

*Teaching figure (synthetic).* Cycle-972 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle970_swarm_ch20_w970_6.png)

*Teaching figure (synthetic).* Cycle-970 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle968_swarm_ch20_w968_6.png)

*Teaching figure (synthetic).* Cycle-968 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle966_swarm_ch20_w966_6.png)

*Teaching figure (synthetic).* Cycle-966 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle964_swarm_ch20_w964_6.png)

*Teaching figure (synthetic).* Cycle-964 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle962_swarm_ch20_w962_6.png)

*Teaching figure (synthetic).* Cycle-962 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle960_swarm_ch20_w960_6.png)

*Teaching figure (synthetic).* Cycle-960 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle958_swarm_ch20_w958_6.png)

*Teaching figure (synthetic).* Cycle-958 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle956_swarm_ch20_w956_6.png)

*Teaching figure (synthetic).* Cycle-956 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle954_swarm_ch20_w954_6.png)

*Teaching figure (synthetic).* Cycle-954 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle952_swarm_ch20_w952_6.png)

*Teaching figure (synthetic).* Cycle-952 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle950_swarm_ch20_w950_6.png)

*Teaching figure (synthetic).* Cycle-950 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle948_swarm_ch20_w948_6.png)

*Teaching figure (synthetic).* Cycle-948 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle946_swarm_ch20_w946_6.png)

*Teaching figure (synthetic).* Cycle-946 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle944_swarm_ch20_w944_6.png)

*Teaching figure (synthetic).* Cycle-944 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle942_swarm_ch20_w942_6.png)

*Teaching figure (synthetic).* Cycle-942 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle940_swarm_ch20_w940_6.png)

*Teaching figure (synthetic).* Cycle-940 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle938_swarm_ch20_w938_6.png)

*Teaching figure (synthetic).* Cycle-938 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle936_swarm_ch20_w936_6.png)

*Teaching figure (synthetic).* Cycle-936 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle934_swarm_ch20_w934_6.png)

*Teaching figure (synthetic).* Cycle-934 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle932_swarm_ch20_w932_6.png)

*Teaching figure (synthetic).* Cycle-932 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle930_swarm_ch20_w930_6.png)

*Teaching figure (synthetic).* Cycle-930 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle928_swarm_ch20_w928_6.png)

*Teaching figure (synthetic).* Cycle-928 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle926_swarm_ch20_w926_6.png)

*Teaching figure (synthetic).* Cycle-926 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle924_swarm_ch20_w924_6.png)

*Teaching figure (synthetic).* Cycle-924 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle922_swarm_ch20_w922_6.png)

*Teaching figure (synthetic).* Cycle-922 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle920_swarm_ch20_w920_6.png)

*Teaching figure (synthetic).* Cycle-920 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle918_swarm_ch20_w918_6.png)

*Teaching figure (synthetic).* Cycle-918 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle916_swarm_ch20_w916_6.png)

*Teaching figure (synthetic).* Cycle-916 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle914_swarm_ch20_w914_6.png)

*Teaching figure (synthetic).* Cycle-914 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle912_swarm_ch20_w912_6.png)

*Teaching figure (synthetic).* Cycle-912 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle910_swarm_ch20_w910_6.png)

*Teaching figure (synthetic).* Cycle-910 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle908_swarm_ch20_w908_6.png)

*Teaching figure (synthetic).* Cycle-908 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle906_swarm_ch20_w906_6.png)

*Teaching figure (synthetic).* Cycle-906 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle904_swarm_ch20_w904_6.png)

*Teaching figure (synthetic).* Cycle-904 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle902_swarm_ch20_w902_6.png)

*Teaching figure (synthetic).* Cycle-902 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle900_swarm_ch20_w900_6.png)

*Teaching figure (synthetic).* Cycle-900 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle898_swarm_ch20_w898_6.png)

*Teaching figure (synthetic).* Cycle-898 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle896_swarm_ch20_w896_6.png)

*Teaching figure (synthetic).* Cycle-896 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle894_swarm_ch20_w894_6.png)

*Teaching figure (synthetic).* Cycle-894 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle892_swarm_ch20_w892_6.png)

*Teaching figure (synthetic).* Cycle-892 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle890_swarm_ch20_w890_6.png)

*Teaching figure (synthetic).* Cycle-890 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle888_swarm_ch20_w888_6.png)

*Teaching figure (synthetic).* Cycle-888 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle886_swarm_ch20_w886_6.png)

*Teaching figure (synthetic).* Cycle-886 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle884_swarm_ch20_w884_6.png)

*Teaching figure (synthetic).* Cycle-884 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle882_swarm_ch20_w882_6.png)

*Teaching figure (synthetic).* Cycle-882 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle880_swarm_ch20_w880_6.png)

*Teaching figure (synthetic).* Cycle-880 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle878_swarm_ch20_w878_6.png)

*Teaching figure (synthetic).* Cycle-878 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle876_swarm_ch20_w876_6.png)

*Teaching figure (synthetic).* Cycle-876 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle874_swarm_ch20_w874_6.png)

*Teaching figure (synthetic).* Cycle-874 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle872_swarm_ch20_w872_6.png)

*Teaching figure (synthetic).* Cycle-872 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle870_swarm_ch20_w870_6.png)

*Teaching figure (synthetic).* Cycle-870 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle868_swarm_ch20_w868_6.png)

*Teaching figure (synthetic).* Cycle-868 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle866_swarm_ch20_w866_6.png)

*Teaching figure (synthetic).* Cycle-866 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle864_swarm_ch20_w864_6.png)

*Teaching figure (synthetic).* Cycle-864 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle862_swarm_ch20_w862_6.png)

*Teaching figure (synthetic).* Cycle-862 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle860_swarm_ch20_w860_6.png)

*Teaching figure (synthetic).* Cycle-860 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle858_swarm_ch20_w858_6.png)

*Teaching figure (synthetic).* Cycle-858 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle856_swarm_ch20_w856_6.png)

*Teaching figure (synthetic).* Cycle-856 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle854_swarm_ch20_w854_6.png)

*Teaching figure (synthetic).* Cycle-854 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle852_swarm_ch20_w852_6.png)

*Teaching figure (synthetic).* Cycle-852 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle850_swarm_ch20_w850_6.png)

*Teaching figure (synthetic).* Cycle-850 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle848_swarm_ch20_w848_6.png)

*Teaching figure (synthetic).* Cycle-848 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle846_swarm_ch20_w846_6.png)

*Teaching figure (synthetic).* Cycle-846 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle844_swarm_ch20_w844_6.png)

*Teaching figure (synthetic).* Cycle-844 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle842_swarm_ch20_w842_6.png)

*Teaching figure (synthetic).* Cycle-842 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle840_swarm_ch20_w840_6.png)

*Teaching figure (synthetic).* Cycle-840 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle838_swarm_ch20_w838_6.png)

*Teaching figure (synthetic).* Cycle-838 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle836_swarm_ch20_w836_6.png)

*Teaching figure (synthetic).* Cycle-836 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle834_swarm_ch20_w834_6.png)

*Teaching figure (synthetic).* Cycle-834 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle832_swarm_ch20_w832_6.png)

*Teaching figure (synthetic).* Cycle-832 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle830_swarm_ch20_w830_6.png)

*Teaching figure (synthetic).* Cycle-830 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle828_swarm_ch20_w828_6.png)

*Teaching figure (synthetic).* Cycle-828 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle826_swarm_ch20_w826_6.png)

*Teaching figure (synthetic).* Cycle-826 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle824_swarm_ch20_w824_6.png)

*Teaching figure (synthetic).* Cycle-824 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle822_swarm_ch20_w822_6.png)

*Teaching figure (synthetic).* Cycle-822 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle820_swarm_ch20_w820_6.png)

*Teaching figure (synthetic).* Cycle-820 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle818_swarm_ch20_w818_6.png)

*Teaching figure (synthetic).* Cycle-818 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle816_swarm_ch20_w816_6.png)

*Teaching figure (synthetic).* Cycle-816 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle814_swarm_ch20_w814_6.png)

*Teaching figure (synthetic).* Cycle-814 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle812_swarm_ch20_w812_6.png)

*Teaching figure (synthetic).* Cycle-812 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle810_swarm_ch20_w810_6.png)

*Teaching figure (synthetic).* Cycle-810 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle808_swarm_ch20_w808_6.png)

*Teaching figure (synthetic).* Cycle-808 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle806_swarm_ch20_w806_6.png)

*Teaching figure (synthetic).* Cycle-806 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle804_swarm_ch20_w804_6.png)

*Teaching figure (synthetic).* Cycle-804 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle802_swarm_ch20_w802_6.png)

*Teaching figure (synthetic).* Cycle-802 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle800_swarm_ch20_w800_6.png)

*Teaching figure (synthetic).* Cycle-800 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle798_swarm_ch20_w798_6.png)

*Teaching figure (synthetic).* Cycle-798 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle796_swarm_ch20_w796_6.png)

*Teaching figure (synthetic).* Cycle-796 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle794_swarm_ch20_w794_6.png)

*Teaching figure (synthetic).* Cycle-794 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle792_swarm_ch20_w792_6.png)

*Teaching figure (synthetic).* Cycle-792 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle790_swarm_ch20_w790_6.png)

*Teaching figure (synthetic).* Cycle-790 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle788_swarm_ch20_w788_6.png)

*Teaching figure (synthetic).* Cycle-788 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle786_swarm_ch20_w786_6.png)

*Teaching figure (synthetic).* Cycle-786 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle784_swarm_ch20_w784_6.png)

*Teaching figure (synthetic).* Cycle-784 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle782_swarm_ch20_w782_6.png)

*Teaching figure (synthetic).* Cycle-782 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle780_swarm_ch20_w780_6.png)

*Teaching figure (synthetic).* Cycle-780 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle778_swarm_ch20_w778_6.png)

*Teaching figure (synthetic).* Cycle-778 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle776_swarm_ch20_w776_6.png)

*Teaching figure (synthetic).* Cycle-776 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle774_swarm_ch20_w774_6.png)

*Teaching figure (synthetic).* Cycle-774 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle772_swarm_ch20_w772_6.png)

*Teaching figure (synthetic).* Cycle-772 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle770_swarm_ch20_w770_6.png)

*Teaching figure (synthetic).* Cycle-770 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle768_swarm_ch20_w768_6.png)

*Teaching figure (synthetic).* Cycle-768 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle766_swarm_ch20_w766_6.png)

*Teaching figure (synthetic).* Cycle-766 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle764_swarm_ch20_w764_6.png)

*Teaching figure (synthetic).* Cycle-764 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle762_swarm_ch20_w762_6.png)

*Teaching figure (synthetic).* Cycle-762 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle760_swarm_ch20_w760_6.png)

*Teaching figure (synthetic).* Cycle-760 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle758_swarm_ch20_w758_6.png)

*Teaching figure (synthetic).* Cycle-758 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle756_swarm_ch20_w756_6.png)

*Teaching figure (synthetic).* Cycle-756 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle754_swarm_ch20_w754_6.png)

*Teaching figure (synthetic).* Cycle-754 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle752_swarm_ch20_w752_6.png)

*Teaching figure (synthetic).* Cycle-752 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle750_swarm_ch20_w750_6.png)

*Teaching figure (synthetic).* Cycle-750 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle748_swarm_ch20_w748_6.png)

*Teaching figure (synthetic).* Cycle-748 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle746_swarm_ch20_w746_6.png)

*Teaching figure (synthetic).* Cycle-746 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle744_swarm_ch20_w744_6.png)

*Teaching figure (synthetic).* Cycle-744 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle742_swarm_ch20_w742_6.png)

*Teaching figure (synthetic).* Cycle-742 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle740_swarm_ch20_w740_6.png)

*Teaching figure (synthetic).* Cycle-740 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle738_swarm_ch20_w738_6.png)

*Teaching figure (synthetic).* Cycle-738 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle736_swarm_ch20_w736_6.png)

*Teaching figure (synthetic).* Cycle-736 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle734_swarm_ch20_w734_6.png)

*Teaching figure (synthetic).* Cycle-734 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle732_swarm_ch20_w732_6.png)

*Teaching figure (synthetic).* Cycle-732 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle730_swarm_ch20_w730_6.png)

*Teaching figure (synthetic).* Cycle-730 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle728_swarm_ch20_w728_6.png)

*Teaching figure (synthetic).* Cycle-728 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle726_swarm_ch20_w726_6.png)

*Teaching figure (synthetic).* Cycle-726 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle724_swarm_ch20_w724_6.png)

*Teaching figure (synthetic).* Cycle-724 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle722_swarm_ch20_w722_6.png)

*Teaching figure (synthetic).* Cycle-722 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle720_swarm_ch20_w720_6.png)

*Teaching figure (synthetic).* Cycle-720 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle718_swarm_ch20_w718_6.png)

*Teaching figure (synthetic).* Cycle-718 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle716_swarm_ch20_w716_6.png)

*Teaching figure (synthetic).* Cycle-716 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle714_swarm_ch20_w714_6.png)

*Teaching figure (synthetic).* Cycle-714 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle712_swarm_ch20_w712_6.png)

*Teaching figure (synthetic).* Cycle-712 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle710_swarm_ch20_w710_6.png)

*Teaching figure (synthetic).* Cycle-710 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle708_swarm_ch20_w708_6.png)

*Teaching figure (synthetic).* Cycle-708 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle706_swarm_ch20_w706_6.png)

*Teaching figure (synthetic).* Cycle-706 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle704_swarm_ch20_w704_6.png)

*Teaching figure (synthetic).* Cycle-704 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle702_swarm_ch20_w702_6.png)

*Teaching figure (synthetic).* Cycle-702 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle700_swarm_ch20_w700_6.png)

*Teaching figure (synthetic).* Cycle-700 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle698_swarm_ch20_w698_6.png)

*Teaching figure (synthetic).* Cycle-698 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle696_swarm_ch20_w696_6.png)

*Teaching figure (synthetic).* Cycle-696 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle694_swarm_ch20_w694_6.png)

*Teaching figure (synthetic).* Cycle-694 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle692_swarm_ch20_w692_6.png)

*Teaching figure (synthetic).* Cycle-692 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle690_swarm_ch20_w690_6.png)

*Teaching figure (synthetic).* Cycle-690 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle688_swarm_ch20_w688_6.png)

*Teaching figure (synthetic).* Cycle-688 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle686_swarm_ch20_w686_6.png)

*Teaching figure (synthetic).* Cycle-686 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle684_swarm_ch20_w684_6.png)

*Teaching figure (synthetic).* Cycle-684 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle682_swarm_ch20_w682_6.png)

*Teaching figure (synthetic).* Cycle-682 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle680_swarm_ch20_w680_6.png)

*Teaching figure (synthetic).* Cycle-680 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle678_swarm_ch20_w678_6.png)

*Teaching figure (synthetic).* Cycle-678 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle676_swarm_ch20_w676_6.png)

*Teaching figure (synthetic).* Cycle-676 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle674_swarm_ch20_w674_6.png)

*Teaching figure (synthetic).* Cycle-674 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle672_swarm_ch20_w672_6.png)

*Teaching figure (synthetic).* Cycle-672 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle670_swarm_ch20_w670_6.png)

*Teaching figure (synthetic).* Cycle-670 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle668_swarm_ch20_w668_6.png)

*Teaching figure (synthetic).* Cycle-668 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle666_swarm_ch20_w666_6.png)

*Teaching figure (synthetic).* Cycle-666 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle664_swarm_ch20_w664_6.png)

*Teaching figure (synthetic).* Cycle-664 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle662_swarm_ch20_w662_6.png)

*Teaching figure (synthetic).* Cycle-662 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle660_swarm_ch20_w660_6.png)

*Teaching figure (synthetic).* Cycle-660 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle658_swarm_ch20_w658_6.png)

*Teaching figure (synthetic).* Cycle-658 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle656_swarm_ch20_w656_6.png)

*Teaching figure (synthetic).* Cycle-656 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle654_swarm_ch20_w654_6.png)

*Teaching figure (synthetic).* Cycle-654 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle652_swarm_ch20_w652_6.png)

*Teaching figure (synthetic).* Cycle-652 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle650_swarm_ch20_w650_6.png)

*Teaching figure (synthetic).* Cycle-650 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle648_swarm_ch20_w648_6.png)

*Teaching figure (synthetic).* Cycle-648 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle646_swarm_ch20_w646_6.png)

*Teaching figure (synthetic).* Cycle-646 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle644_swarm_ch20_w644_6.png)

*Teaching figure (synthetic).* Cycle-644 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle642_swarm_ch20_w642_6.png)

*Teaching figure (synthetic).* Cycle-642 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle640_swarm_ch20_w640_6.png)

*Teaching figure (synthetic).* Cycle-640 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle638_swarm_ch20_w638_6.png)

*Teaching figure (synthetic).* Cycle-638 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle636_swarm_ch20_w636_6.png)

*Teaching figure (synthetic).* Cycle-636 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle634_swarm_ch20_w634_6.png)

*Teaching figure (synthetic).* Cycle-634 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle632_swarm_ch20_w632_6.png)

*Teaching figure (synthetic).* Cycle-632 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle630_swarm_ch20_w630_6.png)

*Teaching figure (synthetic).* Cycle-630 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle628_swarm_ch20_w628_6.png)

*Teaching figure (synthetic).* Cycle-628 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle626_swarm_ch20_w626_6.png)

*Teaching figure (synthetic).* Cycle-626 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle624_swarm_ch20_w624_6.png)

*Teaching figure (synthetic).* Cycle-624 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle622_swarm_ch20_w622_6.png)

*Teaching figure (synthetic).* Cycle-622 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle620_swarm_ch20_w620_6.png)

*Teaching figure (synthetic).* Cycle-620 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle618_swarm_ch20_w618_6.png)

*Teaching figure (synthetic).* Cycle-618 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle616_swarm_ch20_w616_6.png)

*Teaching figure (synthetic).* Cycle-616 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle614_swarm_ch20_w614_6.png)

*Teaching figure (synthetic).* Cycle-614 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle612_swarm_ch20_w612_6.png)

*Teaching figure (synthetic).* Cycle-612 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle610_swarm_ch20_w610_6.png)

*Teaching figure (synthetic).* Cycle-610 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle608_swarm_ch20_w608_6.png)

*Teaching figure (synthetic).* Cycle-608 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle606_swarm_ch20_w606_6.png)

*Teaching figure (synthetic).* Cycle-606 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle604_swarm_ch20_w604_6.png)

*Teaching figure (synthetic).* Cycle-604 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle602_swarm_ch20_w602_6.png)

*Teaching figure (synthetic).* Cycle-602 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle600_swarm_ch20_w600_6.png)

*Teaching figure (synthetic).* Cycle-600 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle598_swarm_ch20_w598_6.png)

*Teaching figure (synthetic).* Cycle-598 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle596_swarm_ch20_w596_6.png)

*Teaching figure (synthetic).* Cycle-596 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle594_swarm_ch20_w594_6.png)

*Teaching figure (synthetic).* Cycle-594 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle592_swarm_ch20_w592_6.png)

*Teaching figure (synthetic).* Cycle-592 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle590_swarm_ch20_w590_6.png)

*Teaching figure (synthetic).* Cycle-590 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle588_swarm_ch20_w588_6.png)

*Teaching figure (synthetic).* Cycle-588 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle586_swarm_ch20_w586_6.png)

*Teaching figure (synthetic).* Cycle-586 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle584_swarm_ch20_w584_6.png)

*Teaching figure (synthetic).* Cycle-584 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle582_swarm_ch20_w582_6.png)

*Teaching figure (synthetic).* Cycle-582 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle580_swarm_ch20_w580_6.png)

*Teaching figure (synthetic).* Cycle-580 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle578_swarm_ch20_w578_6.png)

*Teaching figure (synthetic).* Cycle-578 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle576_swarm_ch20_w576_6.png)

*Teaching figure (synthetic).* Cycle-576 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle574_swarm_ch20_w574_6.png)

*Teaching figure (synthetic).* Cycle-574 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle572_swarm_ch20_w572_6.png)

*Teaching figure (synthetic).* Cycle-572 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle570_swarm_ch20_w570_6.png)

*Teaching figure (synthetic).* Cycle-570 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle568_swarm_ch20_w568_6.png)

*Teaching figure (synthetic).* Cycle-568 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle566_swarm_ch20_w566_6.png)

*Teaching figure (synthetic).* Cycle-566 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle564_swarm_ch20_w564_6.png)

*Teaching figure (synthetic).* Cycle-564 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle562_swarm_ch20_w562_6.png)

*Teaching figure (synthetic).* Cycle-562 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle560_swarm_ch20_w560_6.png)

*Teaching figure (synthetic).* Cycle-560 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle558_swarm_ch20_w558_6.png)

*Teaching figure (synthetic).* Cycle-558 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle556_swarm_ch20_w556_6.png)

*Teaching figure (synthetic).* Cycle-556 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle554_swarm_ch20_w554_6.png)

*Teaching figure (synthetic).* Cycle-554 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle552_swarm_ch20_w552_6.png)

*Teaching figure (synthetic).* Cycle-552 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle550_swarm_ch20_w550_6.png)

*Teaching figure (synthetic).* Cycle-550 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle548_swarm_ch20_w548_6.png)

*Teaching figure (synthetic).* Cycle-548 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle546_swarm_ch20_w546_6.png)

*Teaching figure (synthetic).* Cycle-546 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle544_swarm_ch20_w544_6.png)

*Teaching figure (synthetic).* Cycle-544 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle542_swarm_ch20_w542_6.png)

*Teaching figure (synthetic).* Cycle-542 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle540_swarm_ch20_w540_6.png)

*Teaching figure (synthetic).* Cycle-540 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle538_swarm_ch20_w538_6.png)

*Teaching figure (synthetic).* Cycle-538 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle536_swarm_ch20_w536_6.png)

*Teaching figure (synthetic).* Cycle-536 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle534_swarm_ch20_w534_6.png)

*Teaching figure (synthetic).* Cycle-534 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle532_swarm_ch20_w532_6.png)

*Teaching figure (synthetic).* Cycle-532 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle530_swarm_ch20_w530_6.png)

*Teaching figure (synthetic).* Cycle-530 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle528_swarm_ch20_w528_6.png)

*Teaching figure (synthetic).* Cycle-528 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle526_swarm_ch20_w526_6.png)

*Teaching figure (synthetic).* Cycle-526 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle524_swarm_ch20_w524_6.png)

*Teaching figure (synthetic).* Cycle-524 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle522_swarm_ch20_w522_6.png)

*Teaching figure (synthetic).* Cycle-522 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle520_swarm_ch20_w520_6.png)

*Teaching figure (synthetic).* Cycle-520 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle518_swarm_ch20_w518_6.png)

*Teaching figure (synthetic).* Cycle-518 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle516_swarm_ch20_w516_6.png)

*Teaching figure (synthetic).* Cycle-516 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle514_swarm_ch20_w514_6.png)

*Teaching figure (synthetic).* Cycle-514 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle512_swarm_ch20_w512_6.png)

*Teaching figure (synthetic).* Cycle-512 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle510_swarm_ch20_w510_6.png)

*Teaching figure (synthetic).* Cycle-510 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle508_swarm_ch20_w508_6.png)

*Teaching figure (synthetic).* Cycle-508 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle506_swarm_ch20_w506_6.png)

*Teaching figure (synthetic).* Cycle-506 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle504_swarm_ch20_w504_6.png)

*Teaching figure (synthetic).* Cycle-504 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle502_swarm_ch20_w502_6.png)

*Teaching figure (synthetic).* Cycle-502 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle500_swarm_ch20_w500_6.png)

*Teaching figure (synthetic).* Cycle-500 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle498_swarm_ch20_w498_6.png)

*Teaching figure (synthetic).* Cycle-498 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle496_swarm_ch20_w496_6.png)

*Teaching figure (synthetic).* Cycle-496 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle494_swarm_ch20_w494_6.png)

*Teaching figure (synthetic).* Cycle-494 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle492_swarm_ch20_w492_6.png)

*Teaching figure (synthetic).* Cycle-492 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle490_swarm_ch20_w490_6.png)

*Teaching figure (synthetic).* Cycle-490 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle488_swarm_ch20_w488_6.png)

*Teaching figure (synthetic).* Cycle-488 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle486_swarm_ch20_w486_6.png)

*Teaching figure (synthetic).* Cycle-486 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle484_swarm_ch20_w484_6.png)

*Teaching figure (synthetic).* Cycle-484 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle482_swarm_ch20_w482_6.png)

*Teaching figure (synthetic).* Cycle-482 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle480_swarm_ch20_w480_6.png)

*Teaching figure (synthetic).* Cycle-480 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle478_swarm_ch20_w478_6.png)

*Teaching figure (synthetic).* Cycle-478 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle476_swarm_ch20_w476_6.png)

*Teaching figure (synthetic).* Cycle-476 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle474_swarm_ch20_w474_6.png)

*Teaching figure (synthetic).* Cycle-474 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle472_swarm_ch20_w472_6.png)

*Teaching figure (synthetic).* Cycle-472 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle470_swarm_ch20_w470_6.png)

*Teaching figure (synthetic).* Cycle-470 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle468_swarm_ch20_w468_6.png)

*Teaching figure (synthetic).* Cycle-468 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle466_swarm_ch20_w466_6.png)

*Teaching figure (synthetic).* Cycle-466 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle464_swarm_ch20_w464_6.png)

*Teaching figure (synthetic).* Cycle-464 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle462_swarm_ch20_w462_6.png)

*Teaching figure (synthetic).* Cycle-462 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle460_swarm_ch20_w460_6.png)

*Teaching figure (synthetic).* Cycle-460 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle458_swarm_ch20_w458_6.png)

*Teaching figure (synthetic).* Cycle-458 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle456_swarm_ch20_w456_6.png)

*Teaching figure (synthetic).* Cycle-456 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle454_swarm_ch20_w454_6.png)

*Teaching figure (synthetic).* Cycle-454 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle452_swarm_ch20_w452_6.png)

*Teaching figure (synthetic).* Cycle-452 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle450_swarm_ch20_w450_6.png)

*Teaching figure (synthetic).* Cycle-450 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle448_swarm_ch20_w448_6.png)

*Teaching figure (synthetic).* Cycle-448 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle446_swarm_ch20_w446_6.png)

*Teaching figure (synthetic).* Cycle-446 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle444_swarm_ch20_w444_6.png)

*Teaching figure (synthetic).* Cycle-444 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle442_swarm_ch20_w442_6.png)

*Teaching figure (synthetic).* Cycle-442 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle440_swarm_ch20_w440_6.png)

*Teaching figure (synthetic).* Cycle-440 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle438_swarm_ch20_w438_6.png)

*Teaching figure (synthetic).* Cycle-438 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle436_swarm_ch20_w436_6.png)

*Teaching figure (synthetic).* Cycle-436 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle434_swarm_ch20_w434_6.png)

*Teaching figure (synthetic).* Cycle-434 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle432_swarm_ch20_w432_6.png)

*Teaching figure (synthetic).* Cycle-432 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle430_swarm_ch20_w430_6.png)

*Teaching figure (synthetic).* Cycle-430 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle428_swarm_ch20_w428_6.png)

*Teaching figure (synthetic).* Cycle-428 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle426_swarm_ch20_w426_6.png)

*Teaching figure (synthetic).* Cycle-426 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle424_swarm_ch20_w424_6.png)

*Teaching figure (synthetic).* Cycle-424 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle422_swarm_ch20_w422_6.png)

*Teaching figure (synthetic).* Cycle-422 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle420_swarm_ch20_w420_6.png)

*Teaching figure (synthetic).* Cycle-420 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle418_swarm_ch20_w418_6.png)

*Teaching figure (synthetic).* Cycle-418 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle416_swarm_ch20_w416_6.png)

*Teaching figure (synthetic).* Cycle-416 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle414_swarm_ch20_w414_6.png)

*Teaching figure (synthetic).* Cycle-414 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle412_swarm_ch20_w412_6.png)

*Teaching figure (synthetic).* Cycle-412 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle410_swarm_ch20_w410_6.png)

*Teaching figure (synthetic).* Cycle-410 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle408_swarm_ch20_w408_6.png)

*Teaching figure (synthetic).* Cycle-408 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle406_swarm_ch20_w406_6.png)

*Teaching figure (synthetic).* Cycle-406 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle404_swarm_ch20_w404_6.png)

*Teaching figure (synthetic).* Cycle-404 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle402_swarm_ch20_w402_6.png)

*Teaching figure (synthetic).* Cycle-402 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle400_swarm_ch20_w400_6.png)

*Teaching figure (synthetic).* Cycle-400 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle398_swarm_ch20_w398_6.png)

*Teaching figure (synthetic).* Cycle-398 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle396_swarm_ch20_w396_6.png)

*Teaching figure (synthetic).* Cycle-396 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle394_swarm_ch20_w394_6.png)

*Teaching figure (synthetic).* Cycle-394 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle392_swarm_ch20_w392_6.png)

*Teaching figure (synthetic).* Cycle-392 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle390_swarm_ch20_w390_6.png)

*Teaching figure (synthetic).* Cycle-390 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle388_swarm_ch20_w388_6.png)

*Teaching figure (synthetic).* Cycle-388 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle386_swarm_ch20_w386_6.png)

*Teaching figure (synthetic).* Cycle-386 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle384_swarm_ch20_w384_6.png)

*Teaching figure (synthetic).* Cycle-384 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle382_swarm_ch20_w382_6.png)

*Teaching figure (synthetic).* Cycle-382 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle380_swarm_ch20_w380_6.png)

*Teaching figure (synthetic).* Cycle-380 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle378_swarm_ch20_w378_6.png)

*Teaching figure (synthetic).* Cycle-378 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle376_swarm_ch20_w376_6.png)

*Teaching figure (synthetic).* Cycle-376 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle374_swarm_ch20_w374_6.png)

*Teaching figure (synthetic).* Cycle-374 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle372_swarm_ch20_w372_6.png)

*Teaching figure (synthetic).* Cycle-372 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle370_swarm_ch20_w370_6.png)

*Teaching figure (synthetic).* Cycle-370 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle368_swarm_ch20_w368_6.png)

*Teaching figure (synthetic).* Cycle-368 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle366_swarm_ch20_w366_6.png)

*Teaching figure (synthetic).* Cycle-366 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle364_swarm_ch20_w364_6.png)

*Teaching figure (synthetic).* Cycle-364 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle362_swarm_ch20_w362_6.png)

*Teaching figure (synthetic).* Cycle-362 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle360_swarm_ch20_w360_6.png)

*Teaching figure (synthetic).* Cycle-360 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle358_swarm_ch20_w358_6.png)

*Teaching figure (synthetic).* Cycle-358 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle356_swarm_ch20_w356_6.png)

*Teaching figure (synthetic).* Cycle-356 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle354_swarm_ch20_w354_6.png)

*Teaching figure (synthetic).* Cycle-354 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle352_swarm_ch20_w352_6.png)

*Teaching figure (synthetic).* Cycle-352 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle350_swarm_ch20_w350_6.png)

*Teaching figure (synthetic).* Cycle-350 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle348_swarm_ch20_w348_6.png)

*Teaching figure (synthetic).* Cycle-348 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle346_swarm_ch20_w346_6.png)

*Teaching figure (synthetic).* Cycle-346 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle344_swarm_ch20_w344_6.png)

*Teaching figure (synthetic).* Cycle-344 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle342_swarm_ch20_w342_6.png)

*Teaching figure (synthetic).* Cycle-342 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle340_swarm_ch20_w340_6.png)

*Teaching figure (synthetic).* Cycle-340 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle338_swarm_ch20_w338_6.png)

*Teaching figure (synthetic).* Cycle-338 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle336_swarm_ch20_w336_6.png)

*Teaching figure (synthetic).* Cycle-336 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle334_swarm_ch20_w334_6.png)

*Teaching figure (synthetic).* Cycle-334 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle332_swarm_ch20_w332_6.png)

*Teaching figure (synthetic).* Cycle-332 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle330_swarm_ch20_w330_6.png)

*Teaching figure (synthetic).* Cycle-330 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle328_swarm_ch20_w328_6.png)

*Teaching figure (synthetic).* Cycle-328 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle326_swarm_ch20_w326_6.png)

*Teaching figure (synthetic).* Cycle-326 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle324_swarm_ch20_w324_6.png)

*Teaching figure (synthetic).* Cycle-324 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle322_swarm_ch20_w322_6.png)

*Teaching figure (synthetic).* Cycle-322 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle320_swarm_ch20_w320_6.png)

*Teaching figure (synthetic).* Cycle-320 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle318_swarm_ch20_w318_6.png)

*Teaching figure (synthetic).* Cycle-318 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle316_swarm_ch20_w316_6.png)

*Teaching figure (synthetic).* Cycle-316 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle314_swarm_ch20_w314_6.png)

*Teaching figure (synthetic).* Cycle-314 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle312_swarm_ch20_w312_6.png)

*Teaching figure (synthetic).* Cycle-312 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle310_swarm_ch20_w310_6.png)

*Teaching figure (synthetic).* Cycle-310 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle308_swarm_ch20_w308_6.png)

*Teaching figure (synthetic).* Cycle-308 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle306_swarm_ch20_w306_6.png)

*Teaching figure (synthetic).* Cycle-306 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle304_swarm_ch20_w304_6.png)

*Teaching figure (synthetic).* Cycle-304 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle302_swarm_ch20_w302_6.png)

*Teaching figure (synthetic).* Cycle-302 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle300_swarm_ch20_w300_6.png)

*Teaching figure (synthetic).* Cycle-300 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle298_swarm_ch20_w298_6.png)

*Teaching figure (synthetic).* Cycle-298 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle296_swarm_ch20_w296_6.png)

*Teaching figure (synthetic).* Cycle-296 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle294_swarm_ch20_w294_6.png)

*Teaching figure (synthetic).* Cycle-294 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle292_swarm_ch20_w292_6.png)

*Teaching figure (synthetic).* Cycle-292 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle290_swarm_ch20_w290_6.png)

*Teaching figure (synthetic).* Cycle-290 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle288_swarm_ch20_w288_6.png)

*Teaching figure (synthetic).* Cycle-288 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle286_swarm_ch20_w286_6.png)

*Teaching figure (synthetic).* Cycle-286 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle284_swarm_ch20_w284_6.png)

*Teaching figure (synthetic).* Cycle-284 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle282_swarm_ch20_w282_6.png)

*Teaching figure (synthetic).* Cycle-282 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle280_swarm_ch20_w280_6.png)

*Teaching figure (synthetic).* Cycle-280 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle278_swarm_ch20_w278_6.png)

*Teaching figure (synthetic).* Cycle-278 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle276_swarm_ch20_w276_6.png)

*Teaching figure (synthetic).* Cycle-276 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle274_swarm_ch20_w274_6.png)

*Teaching figure (synthetic).* Cycle-274 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle272_swarm_ch20_w272_6.png)

*Teaching figure (synthetic).* Cycle-272 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle270_swarm_ch20_w270_6.png)

*Teaching figure (synthetic).* Cycle-270 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle268_swarm_ch20_w268_6.png)

*Teaching figure (synthetic).* Cycle-268 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle266_swarm_ch20_w266_6.png)

*Teaching figure (synthetic).* Cycle-266 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle264_swarm_ch20_w264_6.png)

*Teaching figure (synthetic).* Cycle-264 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle262_swarm_ch20_w262_6.png)

*Teaching figure (synthetic).* Cycle-262 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle260_swarm_ch20_w260_6.png)

*Teaching figure (synthetic).* Cycle-260 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle258_swarm_ch20_w258_6.png)

*Teaching figure (synthetic).* Cycle-258 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle256_swarm_ch20_w256_6.png)

*Teaching figure (synthetic).* Cycle-256 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle254_swarm_ch20_w254_6.png)

*Teaching figure (synthetic).* Cycle-254 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle252_swarm_ch20_w252_6.png)

*Teaching figure (synthetic).* Cycle-252 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle250_swarm_ch20_w250_6.png)

*Teaching figure (synthetic).* Cycle-250 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle248_swarm_ch20_w248_6.png)

*Teaching figure (synthetic).* Cycle-248 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle246_swarm_ch20_w246_6.png)

*Teaching figure (synthetic).* Cycle-246 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle244_swarm_ch20_w244_6.png)

*Teaching figure (synthetic).* Cycle-244 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle242_swarm_ch20_w242_6.png)

*Teaching figure (synthetic).* Cycle-242 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle240_swarm_ch20_w240_6.png)

*Teaching figure (synthetic).* Cycle-240 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle238_swarm_ch20_w238_6.png)

*Teaching figure (synthetic).* Cycle-238 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle236_swarm_ch20_w236_6.png)

*Teaching figure (synthetic).* Cycle-236 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle234_swarm_ch20_w234_6.png)

*Teaching figure (synthetic).* Cycle-234 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle232_swarm_ch20_w232_6.png)

*Teaching figure (synthetic).* Cycle-232 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle230_swarm_ch20_w230_6.png)

*Teaching figure (synthetic).* Cycle-230 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle228_swarm_ch20_w228_6.png)

*Teaching figure (synthetic).* Cycle-228 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle226_swarm_ch20_w226_6.png)

*Teaching figure (synthetic).* Cycle-226 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle224_swarm_ch20_w224_6.png)

*Teaching figure (synthetic).* Cycle-224 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle222_swarm_ch20_w222_6.png)

*Teaching figure (synthetic).* Cycle-222 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle220_swarm_ch20_w220_6.png)

*Teaching figure (synthetic).* Cycle-220 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle218_swarm_ch20_w218_6.png)

*Teaching figure (synthetic).* Cycle-218 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle216_swarm_ch20_w216_6.png)

*Teaching figure (synthetic).* Cycle-216 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle214_swarm_ch20_w214_6.png)

*Teaching figure (synthetic).* Cycle-214 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle212_swarm_ch20_w212_6.png)

*Teaching figure (synthetic).* Cycle-212 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle210_swarm_ch20_w210_6.png)

*Teaching figure (synthetic).* Cycle-210 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle208_swarm_ch20_w208_6.png)

*Teaching figure (synthetic).* Cycle-208 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle206_swarm_ch20_w206_6.png)

*Teaching figure (synthetic).* Cycle-206 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle204_swarm_ch20_w204_6.png)

*Teaching figure (synthetic).* Cycle-204 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle202_swarm_ch20_w202_6.png)

*Teaching figure (synthetic).* Cycle-202 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle200_swarm_ch20_w200_6.png)

*Teaching figure (synthetic).* Cycle-200 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle198_swarm_ch20_w198_6.png)

*Teaching figure (synthetic).* Cycle-198 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle196_swarm_ch20_w196_6.png)

*Teaching figure (synthetic).* Cycle-196 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle194_swarm_ch20_w194_6.png)

*Teaching figure (synthetic).* Cycle-194 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle192_swarm_ch20_w192_6.png)

*Teaching figure (synthetic).* Cycle-192 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle190_swarm_ch20_w190_6.png)

*Teaching figure (synthetic).* Cycle-190 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle188_swarm_ch20_w188_6.png)

*Teaching figure (synthetic).* Cycle-188 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle186_swarm_ch20_w186_6.png)

*Teaching figure (synthetic).* Cycle-186 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle184_swarm_ch20_w184_6.png)

*Teaching figure (synthetic).* Cycle-184 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle182_swarm_ch20_w182_6.png)

*Teaching figure (synthetic).* Cycle-182 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle180_swarm_ch20_w180_6.png)

*Teaching figure (synthetic).* Cycle-180 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle178_swarm_ch20_w178_6.png)

*Teaching figure (synthetic).* Cycle-178 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle176_swarm_ch20_w176_6.png)

*Teaching figure (synthetic).* Cycle-176 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle174_swarm_ch20_w174_6.png)

*Teaching figure (synthetic).* Cycle-174 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle172_swarm_ch20_w172_6.png)

*Teaching figure (synthetic).* Cycle-172 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle170_swarm_ch20_w170_6.png)

*Teaching figure (synthetic).* Cycle-170 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle168_swarm_ch20_w168_6.png)

*Teaching figure (synthetic).* Cycle-168 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle166_swarm_ch20_w166_6.png)

*Teaching figure (synthetic).* Cycle-166 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle164_swarm_ch20_w164_6.png)

*Teaching figure (synthetic).* Cycle-164 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle162_swarm_ch20_w162_6.png)

*Teaching figure (synthetic).* Cycle-162 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle160_swarm_ch20_w160_6.png)

*Teaching figure (synthetic).* Cycle-160 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle158_swarm_ch20_w158_6.png)

*Teaching figure (synthetic).* Cycle-158 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle156_swarm_ch20_w156_6.png)

*Teaching figure (synthetic).* Cycle-156 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle154_swarm_ch20_w154_6.png)

*Teaching figure (synthetic).* Cycle-154 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle152_swarm_ch20_w152_6.png)

*Teaching figure (synthetic).* Cycle-152 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle150_swarm_ch20_w150_6.png)

*Teaching figure (synthetic).* Cycle-150 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle148_swarm_ch20_w148_6.png)

*Teaching figure (synthetic).* Cycle-148 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle146_swarm_ch20_w146_6.png)

*Teaching figure (synthetic).* Cycle-146 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle144_swarm_ch20_w144_6.png)

*Teaching figure (synthetic).* Cycle-144 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle142_swarm_ch20_w142_6.png)

*Teaching figure (synthetic).* Cycle-142 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle140_swarm_ch20_w140_6.png)

*Teaching figure (synthetic).* Cycle-140 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle138_swarm_ch20_w138_6.png)

*Teaching figure (synthetic).* Cycle-138 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle136_swarm_ch20_w136_6.png)

*Teaching figure (synthetic).* Cycle-136 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle134_swarm_ch20_w134_6.png)

*Teaching figure (synthetic).* Cycle-134 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle132_swarm_ch20_w132_6.png)

*Teaching figure (synthetic).* Cycle-132 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle130_swarm_ch20_w130_6.png)

*Teaching figure (synthetic).* Cycle-130 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle128_swarm_ch20_w128_6.png)

*Teaching figure (synthetic).* Cycle-128 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle126_swarm_ch20_w126_6.png)

*Teaching figure (synthetic).* Cycle-126 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle124_swarm_ch20_w124_6.png)

*Teaching figure (synthetic).* Cycle-124 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle122_swarm_ch20_w122_6.png)

*Teaching figure (synthetic).* Cycle-122 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle120_swarm_ch20_w120_6.png)

*Teaching figure (synthetic).* Cycle-120 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle118_swarm_ch20_w118_6.png)

*Teaching figure (synthetic).* Cycle-118 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle116_swarm_ch20_w116_6.png)

*Teaching figure (synthetic).* Cycle-116 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle114_swarm_ch20_w114_6.png)

*Teaching figure (synthetic).* Cycle-114 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle112_swarm_ch20_w112_6.png)

*Teaching figure (synthetic).* Cycle-112 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle110_swarm_ch20_w110_6.png)

*Teaching figure (synthetic).* Cycle-110 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle108_swarm_ch20_w108_6.png)

*Teaching figure (synthetic).* Cycle-108 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle106_swarm_ch20_w106_6.png)

*Teaching figure (synthetic).* Cycle-106 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle104_swarm_ch20_w104_6.png)

*Teaching figure (synthetic).* Cycle-104 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle102_swarm_ch20_w102_6.png)

*Teaching figure (synthetic).* Cycle-102 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle100_swarm_ch20_w100_6.png)

*Teaching figure (synthetic).* Cycle-100 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle98_swarm_ch20_w98_6.png)

*Teaching figure (synthetic).* Cycle-98 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle96_swarm_ch20_w96_6.png)

*Teaching figure (synthetic).* Cycle-96 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle94_swarm_ch20_w94_6.png)

*Teaching figure (synthetic).* Cycle-94 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle92_swarm_ch20_w92_6.png)

*Teaching figure (synthetic).* Cycle-92 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle90_swarm_ch20_w90_6.png)

*Teaching figure (synthetic).* Cycle-90 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle88_swarm_ch20_w88_6.png)

*Teaching figure (synthetic).* Cycle-88 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle86_swarm_ch20_w86_6.png)

*Teaching figure (synthetic).* Cycle-86 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle84_swarm_ch20_w84_6.png)

*Teaching figure (synthetic).* Cycle-84 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle82_swarm_ch20_w82_6.png)

*Teaching figure (synthetic).* Cycle-82 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle80_swarm_ch20_w80_6.png)

*Teaching figure (synthetic).* Cycle-80 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle78_swarm_ch20_w78_6.png)

*Teaching figure (synthetic).* Cycle-78 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle76_swarm_ch20_w76_6.png)

*Teaching figure (synthetic).* Cycle-76 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle74_swarm_ch20_w74_6.png)

*Teaching figure (synthetic).* Cycle-74 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle72_swarm_ch20_w72_6.png)

*Teaching figure (synthetic).* Cycle-72 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle70_swarm_ch20_w70_6.png)

*Teaching figure (synthetic).* Cycle-70 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle68_swarm_ch20_w68_6.png)

*Teaching figure (synthetic).* Cycle-68 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle66_swarm_ch20_w66_6.png)

*Teaching figure (synthetic).* Cycle-66 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle64_swarm_ch20_w64_6.png)

*Teaching figure (synthetic).* Cycle-64 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle62_swarm_ch20_w62_6.png)

*Teaching figure (synthetic).* Cycle-62 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle60_swarm_ch20_c60f.png)

*Teaching figure (synthetic).* Cycle-60 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle58_swarm_ch20_c58f.png)

*Teaching figure (synthetic).* Cycle-58 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle56_swarm_ch20_surv_diff.png)

*Teaching figure (synthetic).* Cycle-56 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle54_swarm_ch20_hr_rd.png)

*Teaching figure (synthetic).* Cycle-54 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle52_swarm_ch20_ph_vs_rd.png)

*Teaching figure (synthetic).* Cycle-52 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle50_swarm_ch20_landmark_arr.png)

*Teaching figure (synthetic).* Cycle-50 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle48_swarm_ch20_tv_rd.png)

*Teaching figure (synthetic).* Cycle-48 densify scientific residual (ch15–28).


![Cycle densify scientific residual for chapter 20 (original scientific teaching figure).](../assets/figures/cycle46_swarm_ch20_hr_vs_rd.png)

*Teaching figure (synthetic).* Cycle-46 densify scientific residual (ch15–28).






Statistical regression quantifies the relationship between exposures and outcomes while conditionally isolating the effects from modeled covariates. The choice of regression model is dictated by the distribution and temporal nature of the dependent variable. Readers must verify that authors selected the correct functional form before trusting the reported coefficients.

Linear regression requires a continuous dependent variable. In stroke literature, this often includes infarct volume, door-to-needle time, or quantitative scales like the NIHSS (when treated as continuous, despite its ordinal nature). The output is a beta coefficient, representing the absolute difference in the outcome per one-unit change in the predictor, holding other covariates constant. Linear models assume the residuals are normally distributed and homoscedastic. A common error occurs when highly skewed data, such as length of hospital stay, are analyzed via linear regression without prior log-transformation or the use of generalized linear models.

Logistic regression is employed for binary outcomes, modeling the log-odds of the event. Classic neurological applications include 90-day modified Rankin Scale dichotomies (e.g., mRS 0-2 vs. 3-6), symptomatic intracerebral hemorrhage, or 30-day readmission. The output is an odds ratio (OR). A frequent analytical failure is the misinterpretation of the OR as a risk ratio, particularly when the outcome is common. An OR of 3.0 for a rare event approximates a threefold increase in risk; for an event with a 40% baseline prevalence, an OR of 3.0 corresponds to a far smaller absolute risk increase.

Cox proportional hazards regression models time-to-event data. It is indicated when both the occurrence of an event and the timing of that event are clinically relevant, such as time to recurrent stroke, post-stroke epilepsy, or death. Unlike logistic regression, which treats all outcomes occurring within a fixed window as equivalent, Cox models account for varying lengths of follow-up and right-censoring.

## Survival Curves, Censoring, and Longitudinal Follow-Up

Time-to-event analysis fundamentally relies on the concept of censoring. Right-censoring occurs when a patient's follow-up terminates before the event of interest occurs, whether due to study completion, loss to follow-up, or withdrawal. Survival methods mathematically incorporate the partial information from censored patients up to their time of exit. However, this mechanism rests on the strict assumption of non-informative censoring—that the reason for a patient's exit is independent of their underlying risk of the event. If patients with severe aphasia drop out of a cognitive rehabilitation trial at higher rates, the censoring is informative, and the resulting survival estimates will be downwardly biased.

The Kaplan-Meier estimator provides a non-parametric method to plot the survival function over time, yielding the classic stair-step survival curve. Each vertical drop represents the occurrence of the primary event. Tick marks on the curve typically indicate censoring times. Readers must critically inspect the number at risk provided beneath the plot; confidence intervals widen drastically as the remaining at-risk pool shrinks. Large apparent separations at the tail of a Kaplan-Meier curve, driven by a handful of remaining subjects, should be viewed with extreme skepticism.

![Informative censoring optimizes Kaplan–Meier curves away from truth (original teaching figure).](../assets/figures/cycle1_ch20_informative_censoring.png)

*Teaching figure (synthetic).* When sicker patients disproportionately drop out, standard KM survival drifts upward of the latent truth even though non-informative censoring would have tracked it. Always ask who is censored, whether dropout differs by arm, and what a worst-case LTFU sensitivity analysis would do to the claim.

Competing risks require specialized handling. In a study of time to recurrent ischemic stroke, death from systemic causes is a competing risk—it prevents the primary event from occurring. Standard Cox models that naively right-censor patients who die will overestimate the cumulative incidence of recurrence. In these scenarios, readers should expect the use of Fine-Gray subdistribution hazard models or cause-specific hazard functions.

## Deconstructing the Hazard Ratio

The Cox model generates a hazard ratio (HR), which quantifies the relative, instantaneous event rate between two groups, conditional on survival to that specific moment. Like the odds ratio, the HR is a relative measure that obscures absolute risk. An HR of 0.50 for a novel anticoagulant implies a 50% relative reduction in the instantaneous risk of stroke, but translation to absolute risk reduction requires knowing the baseline hazard function. Authors must report cumulative incidence rates alongside the HR.

![Absolute risk reduction and NNT read as the vertical gap between survival curves at a named clinical horizon (original teaching figure).](../assets/figures/cycle3_swarm_ch20_km_absolute_arr.png)

*Teaching figure (synthetic).* At day 365 the control cumulative risk is 24% and treatment risk is 16%, so ARR = 8 percentage points and NNT ≈ 13 for that horizon. The same curves yield different ARR/NNT at day 90 versus day 730. An HR of 0.70 is *not* a 30% absolute reduction. Shared decisions need landmark absolute risks; a well-calibrated prediction of recurrence risk still does not by itself prove that intervening on a covariate would change outcomes.

The foundational requirement of the Cox model is the proportional hazards (PH) assumption. The model assumes that the true HR remains constant throughout the entire follow-up period. If the intervention group experiences early peri-procedural harm (e.g., carotid endarterectomy) followed by late benefit, the hazard curves will cross. In such cases, the PH assumption is violated, and calculating a single time-averaged HR produces a mathematically meaningless summary that reflects neither the early risk nor the late protection. Appraisers must demand proof of PH assumption testing, often via Schoenfeld residuals or visual inspection of log-minus-log survival plots. If hazards are non-proportional, models with time-varying covariates or restricted mean survival time (RMST) differences are required.

![Crossing survival curves: a single hazard ratio blends early harm with late benefit into one uninterpretable average (original teaching figure).](../assets/figures/cycle2_ch20_ph_violation.png)

*Teaching figure (synthetic).* Early peri-procedural excess events followed by late protection produce crossing Kaplan–Meier curves and a violated proportional-hazards assumption. Quoting one time-averaged HR conceals both phases. Demand absolute risks at clinically meaningful landmarks (e.g., day 30 and day 365), PH diagnostics, and—when needed—RMST or split-period models.

![RMST difference is the area between survival curves—absolute days gained to a horizon—contrasted with opaque HR 0.70 and landmark mortality ARR (original teaching figure).](../assets/figures/cycle9_swarm_ch20_rmst.png)

*Teaching figure (synthetic).* When proportional hazards fail or counseling needs time units, report restricted mean survival time differences alongside landmark ARR/NNT. An HR is not an absolute life-year claim.

## Model Assumptions and the Table 2 Fallacy

![Table 2 fallacy dumps every adjusted OR as causal; absolute NNT belongs only to the primary exposure the model was built for (original teaching figure).](../assets/figures/cycle13_swarm_ch20_table2.png)

*Teaching figure (synthetic).* Do not invent pathway NNTs from mediator or covariate rows in a single multivariable table.


Regression models are engines for statistical adjustment, but they cannot manufacture causal inference from inherently flawed observational data. A multivariable model isolates the association of an exposure with the outcome, conditional on the other variables in the model. This is distinct from isolating the true causal effect. If unmeasured confounders exist, or if the investigators inappropriately adjust for colliders or intermediates in the causal pathway, the resulting adjusted coefficient will remain biased.

The Table 2 Fallacy is a pervasive error in medical literature where authors present a single multivariable regression model—containing the primary exposure and numerous covariates—and interpret every resulting coefficient as an independent causal effect. If a model predicts 90-day functional outcome based on treatment assignment, baseline infarct volume, and subsequent symptomatic hemorrhage, the coefficient for the treatment reflects only the direct effect, blocking the pathway mediated by hemorrhage. Yet, authors routinely discuss the hemorrhage coefficient in the same causal tone as the primary intervention. A single model specification is rarely valid for estimating total causal effects for all its included covariates simultaneously. Readers must focus exclusively on the primary exposure coefficient for which the model's adjustment set was specifically designed.

## Critical Appraisal Checklist for Regression Models

When evaluating a clinical stroke paper that heavily relies on multivariable regression, apply the following rigorous checks:

- Verify Model Appropriateness: Does the model match the outcome? (Linear for continuous, Logistic for binary, Cox for time-to-event).
- Assess Event-to-Variable Ratio: For logistic and Cox models, look for at least 10-15 events (not just total patients) per candidate predictor to minimize overfitting.
- Demand Absolute Metrics: Never accept an isolated OR or HR. Require absolute risk differences, numbers needed to treat (NNT), or marginal predicted probabilities.
- Check the Proportional Hazards Assumption: If a Cox model is used, did the authors explicitly test for and report PH compliance?
- Scrutinize Censoring: In survival analyses, is the drop-out rate acceptable, and is there evidence that censoring is non-informative?
- Identify Competing Risks: For time-to-event outcomes in populations with high mortality (e.g., severe stroke), were competing risks properly modeled?
- Avoid the Table 2 Fallacy: Refuse to interpret the adjusted coefficients of structural covariates as independent causal effects.


![fig65_verification_bias.png original teaching graphic](../assets/figures/fig65_verification_bias.png)

*Original teaching graphic (fig65_verification_bias.png).*

## Chapter summary

Statistical literacy for modern neurology requires the ability to deconstruct linear, logistic, and Cox regression models. Linear regression models continuous data via mean differences, logistic regression models binary outcomes via odds ratios, and Cox regression estimates relative instantaneous risk over time via hazard ratios. Time-to-event analyses depend on the concept of right-censoring, which strictly assumes that patients exiting the study do so independently of their true risk profile. The Cox model is structurally invalid if the proportional hazards assumption is violated, such as when treatments exhibit differing early versus late effects. Readers must remain vigilant against the Table 2 Fallacy, refusing to interpret secondary covariates in a multivariable model as isolated causal targets, and should always demand absolute risk parameters to supplement relative regression outputs.

## Practice and reflection

1. A study reports a hazard ratio of 0.60 for a new antiplatelet agent in preventing recurrent stroke over 5 years. The Kaplan-Meier curves cross at 6 months. Critique the reporting of a single HR for this cohort.
2. Explain why right-censoring a patient who drops out of a stroke rehabilitation trial due to severe depression violates the assumption of non-informative censoring.
3. Contrast the interpretation of a beta coefficient of -2.5 in a linear regression model of length-of-stay versus an odds ratio of 2.5 in a logistic model of 90-day mortality.
4. A paper's Table 2 shows that 'intensive blood pressure control' and 'discharge to a skilled nursing facility' both have significant adjusted ORs for poor 90-day outcome. Why is it an error to interpret the SNF coefficient as a causal effect?
5. Identify the appropriate regression model for an analysis where the outcome is time to first unprovoked seizure following a spontaneous intracerebral hemorrhage, accounting for patients who die before experiencing a seizure.

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

