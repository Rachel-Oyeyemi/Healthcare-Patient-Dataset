# Exploratory Data Analysis Report

## Structural Overview
- Rows: 55,500
- Columns: 15
- Target: `Test Results`
- Target classes: Normal, Abnormal, Inconclusive
- Missing values: 0
- Exact duplicates: 534 (0.96%)

## Data Types
Numerical: Age, Billing Amount, Room Number. Dates: Date of Admission, Discharge Date. Remaining fields are categorical or text.

## Quality Findings
1. No natural primary key; create a surrogate `admission_id`.
2. Remove 534 exact duplicate rows before analysis.
3. Flag 108 negative billing records and exclude them from gross-revenue KPIs until validated.
4. Normalize inconsistent casing in patient names and malformed hospital strings.
5. Round excessive billing precision to two decimals.
6. Document zero missingness and uniform categories as synthetic-data indicators.

## Distribution and Outlier Analysis
Age ranges from 13 to 89. Length of stay ranges from 1 to 30 days. Billing includes negative values; these are quality exceptions rather than conventional IQR outliers.

## Correlation Analysis
Numeric correlations are weak. This is consistent with independently generated synthetic fields and signals limited predictive value.

## Target Analysis
The three target classes are approximately balanced. Balance supports fair metric calculation but does not create predictive signal.

## Business Context
The dataset is useful for demonstrating data engineering, EDA, deployment patterns, and responsible model governance. It is not suitable for clinical inference or causal claims.
