# Healthcare Patient Dataset — ML + Visualization

[![CI](https://github.com/Rachel-Oyeyemi/Healthcare-Patient-Dataset/actions/workflows/ci.yml/badge.svg)](https://github.com/Rachel-Oyeyemi/Healthcare-Patient-Dataset/actions)

A recruiter-ready portfolio project demonstrating data engineering, exploratory analysis, multiclass machine learning, model governance, visualization, Streamlit deployment, and executive communication.

> **Responsible-use notice:** The Kaggle dataset is synthetic and Faker-generated. This repository is for education and portfolio demonstration only. It must not be used for diagnosis, treatment, triage, or patient-level decisions.

## Project Overview
This project analyzes synthetic hospital-admission records and tests whether routine admission attributes can classify **Test Results** as **Normal**, **Abnormal**, or **Inconclusive**. It compares a transparent Logistic Regression baseline with CatBoost.

## Business Problem
Healthcare teams need trustworthy data pipelines and evidence-based model gates. The central question is not only “Which model scores highest?” but also “Does this dataset contain enough valid signal to justify prediction?”

## Dataset Source
- Kaggle: `prasad22/healthcare-dataset`
- Official profile: **55,500 rows × 15 columns**
- Target: **Test Results** (3 classes)
- Missing values: **0**
- Exact duplicates: **534**
- Negative billing records: **108**
- Source license: **CC0-1.0**

The full Kaggle CSV is not committed. `src/download_data.py` downloads it through KaggleHub or the Kaggle CLI. A compact, clearly labeled synthetic preview is included so the project remains runnable. Published benchmark artifacts were generated on a larger deterministic representative sample using the same schema.

## Repository Structure
```text
├── app/                    # Streamlit application
├── data/raw/               # Official Kaggle download location
├── data/processed/         # Generated clean/model-ready data
├── data/sample_data/       # Bundled synthetic preview
├── docs/                   # Charter, EDA, evaluation, recommendations, career materials
├── models/                 # Baseline and advanced model artifacts
├── notebooks/              # Four end-to-end notebooks
├── presentation/           # 10-slide deck, notes, and PowerPoint generator
├── reports/                # Machine-readable metrics
├── src/                    # Production-style pipeline modules
├── tests/                  # Unit tests
├── visuals/                # EDA and model charts
├── run_pipeline.py
└── requirements.txt
```

## Methodology
1. Acquire the official file or use the bundled preview.
2. Validate the required 15-column schema.
3. Remove exact duplicates, normalize text, parse dates, and flag negative billing.
4. Engineer length of stay, admission month/year, and billing-quality features.
5. Compare Logistic Regression with CatBoost.
6. Evaluate Accuracy, Macro Precision/Recall/F1, multiclass ROC-AUC, and confusion matrices.
7. Communicate results through Streamlit, technical reports, and an executive deck.

## Results — Representative Benchmark
| Model | Accuracy | Macro F1 | ROC-AUC OVR Macro |
|---|---:|---:|---:|
| Logistic Regression | 0.323 | 0.323 | 0.483 |
| CatBoost | 0.317 | 0.283 | 0.490 |

Chance-level accuracy for three balanced classes is approximately **0.333**. The absence of lift is the key governance result: this synthetic target contains little reliable predictive signal.

## How to Run
```bash
git clone https://github.com/Rachel-Oyeyemi/Healthcare-Patient-Dataset.git
cd Healthcare-Patient-Dataset
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python run_pipeline.py
streamlit run app/app.py
```

Download the official Kaggle data after authenticating KaggleHub or the Kaggle CLI:
```bash
python src/download_data.py --no-sample
python run_pipeline.py
```

Generate the executive PowerPoint:
```bash
python presentation/create_presentation.py
```

Run tests:
```bash
pytest -q
```

## Documentation
- [Project Charter](docs/PROJECT_CHARTER.md)
- [EDA Report](docs/EDA_REPORT.md)
- [Model Comparison](docs/MODEL_COMPARISON.md)
- [Model Evaluation](docs/MODEL_EVALUATION.md)
- [Business Recommendations](docs/BUSINESS_RECOMMENDATIONS.md)
- [Data Dictionary](docs/DATA_DICTIONARY.md)
- [Resume, LinkedIn & Interview Materials](docs/RESUME_LINKEDIN_INTERVIEW.md)
- [10-slide Executive Deck](presentation/Healthcare_Patient_Dataset_Executive_Presentation.md)

## Business Impact
- Prevents invalid clinical performance claims from synthetic data
- Establishes reusable data-quality and model-evaluation controls
- Flags negative billing records before financial reporting
- Demonstrates a scientifically correct **do not deploy** decision

## Author
**Rachel Oyeyemi** — Data Analytics & AI Portfolio
