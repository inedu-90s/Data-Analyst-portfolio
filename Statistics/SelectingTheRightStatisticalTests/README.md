# Statistical Test Application Report using SPSS
_A practical walkthrough of choosing and applying statistical tests on a simulated dataset._

## 1. Comparing MUAC at Endline by Group (Independent Samples T-Test)

**Variables**  
- `muac_endline`: Continuous  
- `intervention_group`: Categorical (Control vs Intervention)

**Sample Type**  
- Independent groups

**Test Used**  
- Independent Samples T-Test

**SPSS Navigation**  
> Analyze → Compare Means → Independent-Samples T Test

**Results**  
- t(298) = -1.154  
- p = 0.249  
- Mean Difference = -0.27 cm

**Interpretation**  
No statistically significant difference in MUAC at endline between intervention and control groups.

---

## 2. Comparing MUAC Before and After (Paired Samples T-Test)

**Variables**  
- `muac_baseline`, `muac_endline`: Continuous

**Sample Type**  
- Paired (same individuals)

**Test Used**  
- Paired Samples T-Test

**SPSS Navigation**  
> Analyze → Compare Means → Paired-Samples T Test

**Results**  
- t(299) = 3.118  
- p = 0.002  
- Mean increase = 0.52 cm

**Interpretation**  
Statistically significant improvement in MUAC after the intervention.

---

## 3. Association Between Gender and Stunting (Chi-Square Test)

**Variables**  
- `gender`, `stunted`: Categorical

**Sample Type**  
- Independent groups

**Test Used**  
- Chi-Square Test of Independence

**SPSS Navigation**  
> Analyze → Descriptive Statistics → Crosstabs → Statistics → Tick "Chi-square"

**Results**  
- χ²(1) = 0.471  
- p = 0.492

**Interpretation**  
No significant association between gender and stunting.

---

## 4. Comparing Weight Z-Scores Across Regions (One-Way ANOVA)

**Variables**  
- `weight_zscore`: Continuous  
- `region`: Categorical (4 groups)

**Test Used**  
- One-Way ANOVA

**SPSS Navigation**  
> Analyze → Compare Means → One-Way ANOVA

**Results**  
- F(3, 296) = 1.144  
- p = 0.332

**Interpretation**  
No statistically significant difference in weight Z-scores across regions.

---

## 5. Predicting Weight Z-Score (Linear Regression)

**Outcome Variable**  
- `weight_zscore`: Continuous

**Predictors**  
- `muac_endline` (continuous)  
- `age` (continuous)  
- `gender` (categorical)

**SPSS Navigation**  
> Analyze → Regression → Linear

**Results**

| Predictor     | Coef. | p-value |  
|---------------|--------|---------|  
| MUAC          | 0.035  | 0.304   |  
| Age           | -0.007 | 0.320   |  
| Gender (Male) | -0.100 | 0.467   |  

**R-squared**: 0.009

**Interpretation**  
None of the predictors significantly predict weight Z-score; the model explains less than 1% of the variance.


---

## 🧾 Conclusion

This analysis demonstrates the correct application and interpretation of various statistical tests in SPSS. Each test was selected based on:
- Type of variable
- Number of groups
- Relationship (independent or paired)

---

## 📂 Files
- Simulated Dataset: `Dataset_.csv`
- Report: This markdown file

---

_This report is part of my practical data analysis series for program evaluation, M&E, and public health analytics._

