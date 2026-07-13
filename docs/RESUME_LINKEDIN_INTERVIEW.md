# Resume, LinkedIn, and Interview Materials

## Resume Bullet Points
- Built an end-to-end Python ML pipeline for a 55,500-row synthetic healthcare dataset, including schema validation, duplicate removal, date feature engineering, model persistence, and automated evaluation.
- Compared Logistic Regression and CatBoost for three-class prediction using Accuracy, Macro Precision/Recall/F1, ROC-AUC, and confusion matrices; identified near-chance performance and documented a responsible no-deployment decision.
- Developed a multi-page Streamlit application, executive deck, reproducible notebooks, CI tests, and business recommendations covering billing anomalies, data governance, and model risk.

## LinkedIn Project Description
Built a production-style Healthcare Patient Analytics project using Python, scikit-learn, CatBoost, Streamlit, and GitHub Actions. The project profiles 55,500 synthetic admission records, detects duplicates and negative billing values, engineers utilization and calendar features, compares baseline and advanced multiclass models, and presents findings through an interactive app and executive deck. The key result was responsible model governance: performance remained close to chance, so the model should not be used for clinical decisions.

## Interview Talking Points
- Synthetic data is useful for engineering practice but dangerous for performance claims.
- Macro F1 gives equal weight to all three classes.
- High-cardinality names were excluded to reduce memorization.
- Negative billing values were flagged rather than silently deleted.
- Model complexity cannot manufacture absent signal.

## Common Questions and Sample Answers
### Why Test Results?
The dataset creator frames it as a multiclass target. I used it to demonstrate the workflow while testing whether it actually contained learnable signal.

### Why did CatBoost not outperform Logistic Regression?
Many fields appear independently generated. When predictors and target have little relationship, complexity fits noise rather than generalizable signal.

### What was the most important quality issue?
Negative billing values can distort revenue KPIs. I retained them, added a flag, and recommended validation before financial aggregation.

### Would you deploy the model?
No. The data is synthetic and performance is near chance. Deployment would require governed real outcomes, temporal validation, calibration, subgroup analysis, clinical review, and privacy controls.
