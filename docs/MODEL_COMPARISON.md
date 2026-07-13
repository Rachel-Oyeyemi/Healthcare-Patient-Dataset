# Model Comparison

| Model | Role | Accuracy | Macro F1 | ROC-AUC OVR Macro | Interpretation |
|---|---|---:|---:|---:|---|
| Logistic Regression | Baseline | 0.323 | 0.323 | 0.483 | Transparent reference; near chance. |
| CatBoost | Advanced | 0.317 | 0.283 | 0.490 | Nonlinear comparison; no meaningful lift. |

## Why These Models
Logistic Regression is fast, interpretable, and appropriate for one-hot encoded mixed tabular data. CatBoost handles categorical variables natively and can learn nonlinear interactions.

## Selection Decision
No model should be promoted for clinical use. Logistic Regression remains the reference baseline; CatBoost is retained as a technical comparison. The lack of lift indicates limited target signal rather than insufficient model complexity.

## Evaluation Standard
Primary metric: Macro F1, because each class should receive equal importance. Secondary metrics: Accuracy, Macro Precision, Macro Recall, and multiclass one-vs-rest ROC-AUC.
