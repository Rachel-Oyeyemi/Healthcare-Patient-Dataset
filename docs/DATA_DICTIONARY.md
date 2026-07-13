# Data Dictionary

| Column | Type | Description |
|---|---|---|
| Name | text | Synthetic patient name; excluded from modeling |
| Age | integer | Age at admission |
| Gender | category | Synthetic gender category |
| Blood Type | category | ABO/Rh blood type |
| Medical Condition | category | Primary synthetic condition |
| Date of Admission | date | Admission date |
| Doctor | text | Synthetic clinician name; excluded from modeling |
| Hospital | text | Synthetic facility name; excluded from modeling |
| Insurance Provider | category | Synthetic payer |
| Billing Amount | float | Billed amount; negatives are flagged |
| Room Number | integer | Room identifier |
| Admission Type | category | Emergency, Elective, or Urgent |
| Discharge Date | date | Discharge date |
| Medication | category | Synthetic medication |
| Test Results | target | Normal, Abnormal, or Inconclusive |

Engineered fields: `admission_id`, `length_of_stay`, `admission_month`, `admission_year`, and `is_negative_billing`.
