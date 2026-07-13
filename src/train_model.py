"""Train baseline Logistic Regression and advanced CatBoost models."""
from __future__ import annotations
import argparse
import json
import logging
from pathlib import Path
import joblib
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from feature_engineering import MODEL_FEATURES, TARGET
from utils import configure_logging, ensure_parent, save_json

LOGGER = logging.getLogger(__name__)
NUMERIC = ["age","billing_amount","room_number","length_of_stay","admission_month","admission_year","is_negative_billing"]
CATEGORICAL = [c for c in MODEL_FEATURES if c not in NUMERIC]


def split_data(frame: pd.DataFrame):
    return train_test_split(frame[MODEL_FEATURES], frame[TARGET], test_size=.2, random_state=42, stratify=frame[TARGET])


def train_baseline(X: pd.DataFrame, y: pd.Series) -> Pipeline:
    prep = ColumnTransformer([("num", StandardScaler(), NUMERIC),("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=True), CATEGORICAL)])
    model = LogisticRegression(max_iter=1500, class_weight="balanced", random_state=42)
    return Pipeline([("preprocessor", prep),("model", model)]).fit(X, y)


def train_catboost(X: pd.DataFrame, y: pd.Series) -> CatBoostClassifier:
    model = CatBoostClassifier(iterations=250, depth=6, learning_rate=.08, loss_function="MultiClass", random_seed=42, verbose=False, allow_writing_files=False)
    return model.fit(X, y, cat_features=CATEGORICAL)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/processed/model_features.csv")
    parser.add_argument("--models-dir", default="models")
    args = parser.parse_args(); configure_logging()
    frame = pd.read_csv(args.input); X_train, X_test, y_train, y_test = split_data(frame)
    models = Path(args.models_dir); models.mkdir(parents=True, exist_ok=True)
    baseline = train_baseline(X_train, y_train); joblib.dump(baseline, models/"baseline_logistic_regression.joblib")
    advanced = train_catboost(X_train, y_train); advanced.save_model(models/"advanced_catboost.cbm")
    joblib.dump({"X_test":X_test,"y_test":y_test}, models/"evaluation_split.joblib")
    save_json({"target":TARGET,"features":MODEL_FEATURES,"categorical_features":CATEGORICAL,"random_seed":42}, models/"model_metadata.json")
    LOGGER.info("Saved trained models to %s", models)


if __name__ == "__main__": main()
