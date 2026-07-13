"""Load the baseline pipeline and predict a single record."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import joblib
import pandas as pd
from feature_engineering import MODEL_FEATURES


def load_model(path: str | Path = "models/baseline_logistic_regression.joblib"):
    model_path = Path(path)
    if not model_path.exists(): raise FileNotFoundError(model_path)
    return joblib.load(model_path)


def predict_record(model, record: dict) -> dict:
    frame = pd.DataFrame([record])[MODEL_FEATURES]
    prediction = model.predict(frame)[0]
    probabilities = model.predict_proba(frame)[0]
    return {"prediction":str(prediction),"probabilities":dict(zip(map(str,model.classes_),map(float,probabilities)))}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--model",default="models/baseline_logistic_regression.joblib"); parser.add_argument("--record",required=True)
    args=parser.parse_args(); print(json.dumps(predict_record(load_model(args.model),json.loads(args.record)),indent=2))


if __name__ == "__main__": main()
