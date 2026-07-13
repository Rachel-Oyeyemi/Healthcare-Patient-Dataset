# Healthcare Patient Dataset — Executive Presentation

---

## 1. Overview
ML + visualization portfolio project using synthetic hospital-admission data.

---

## 2. Business Problem
Can routine admission attributes classify Test Results—and is the evidence strong enough to justify deployment?

---

## 3. Dataset
55,500 rows, 15 columns, zero missing values, 534 exact duplicates, and 108 negative billing records. The data is synthetic.

---

## 4. Exploratory Analysis
Uniform categories, weak numeric relationships, duplicate rows, negative billing amounts, and text-quality issues.

---

## 5. Modeling
Baseline: multinomial Logistic Regression. Advanced: CatBoost. Identifiers are excluded to reduce memorization and leakage.

---

## 6. Results
Logistic Regression accuracy 0.323; CatBoost accuracy 0.317; chance level is approximately 0.333.

---

## 7. Insights
Additional model complexity did not create meaningful predictive signal.

---

## 8. Recommendations
Use the project for analytics learning and governance demonstration. Do not use it for clinical decisions.

---

## 9. Future Work
Acquire governed real-world data; define a time-bounded outcome; add temporal validation, calibration, fairness review, and monitoring.

---

## 10. Conclusion
Responsible data science includes recognizing when a model should not be deployed.
