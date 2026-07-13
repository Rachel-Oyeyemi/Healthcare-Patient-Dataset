# Project Charter

## Business Problem
Determine whether routine synthetic admission attributes can classify the three-category `Test Results` field while establishing a defensible data-quality and model-governance workflow.

## Objectives
1. Build a reproducible ingestion and validation pipeline.
2. Profile missingness, duplicates, outliers, target balance, and text quality.
3. Compare an interpretable baseline with an advanced categorical model.
4. Publish an interactive application and executive-ready documentation.
5. Make a deployment recommendation based on evidence rather than model complexity.

## Stakeholders
- Data and analytics leaders
- Hospital operations and revenue-cycle teams
- Machine-learning engineers and model-risk reviewers
- Portfolio reviewers, recruiters, and hiring managers

## Success Metrics
- Required schema validated and pipeline reproducible
- All data-quality exceptions documented
- Accuracy, Macro Precision, Macro Recall, Macro F1, ROC-AUC, and confusion matrices produced
- Streamlit application and executive deck runnable
- Deployment decision explicitly documented

## Expected Business Impact
Reusable controls can prevent duplicate admissions, malformed reference data, and negative billing records from contaminating analytics. The model-governance result demonstrates when a predictive system should not be deployed.

## Technical Architecture
Kaggle/KaggleHub → raw CSV → schema validation → cleaning → feature engineering → train/test split → Logistic Regression/CatBoost → metrics and artifacts → Streamlit and documentation.

## End-to-End Workflow
Acquire → validate → profile → clean → engineer → train → evaluate → communicate → govern.

## Constraints and Risks
The data is synthetic, contains no real clinical causality, and cannot establish safety or efficacy. Patient, doctor, and hospital names are excluded from modeling to reduce memorization and leakage risk.
