# Model Evaluation

## Design
- Stratified 80/20 train-test split
- Random seed: 42
- Patient, doctor, and hospital names excluded
- Target: `test_results`

## Logistic Regression
- Accuracy: 0.323
- Macro Precision: 0.323
- Macro Recall: 0.324
- Macro F1: 0.323
- ROC-AUC OVR Macro: 0.483

## CatBoost
- Accuracy: 0.317
- Macro Precision: 0.299
- Macro Recall: 0.308
- Macro F1: 0.283
- ROC-AUC OVR Macro: 0.490

## Interpretation
Chance-level accuracy for three equally likely classes is approximately 0.333. Both models remain close to that level. Routine admission fields do not reliably predict the synthetically assigned test-result category.

## Governance Decision
Do not use this model for diagnosis, triage, treatment, or patient communication. Production consideration would require real outcome-linked data, temporal validation, calibration, subgroup analysis, privacy controls, and clinical review.
