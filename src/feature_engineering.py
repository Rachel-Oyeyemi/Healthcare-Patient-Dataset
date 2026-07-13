"""Create leakage-conscious model features."""
from __future__ import annotations
import argparse
import logging
import pandas as pd
from utils import configure_logging, ensure_parent

LOGGER = logging.getLogger(__name__)
TARGET = "test_results"
MODEL_FEATURES = ["age","gender","blood_type","medical_condition","insurance_provider","billing_amount","room_number","admission_type","medication","length_of_stay","admission_month","admission_year","is_negative_billing"]


def engineer_features(data: pd.DataFrame) -> pd.DataFrame:
    frame = data.copy()
    frame["date_of_admission"] = pd.to_datetime(frame["date_of_admission"], errors="raise")
    frame["discharge_date"] = pd.to_datetime(frame["discharge_date"], errors="raise")
    if "length_of_stay" not in frame:
        frame["length_of_stay"] = (frame["discharge_date"] - frame["date_of_admission"]).dt.days
    frame["admission_month"] = frame["date_of_admission"].dt.month
    frame["admission_year"] = frame["date_of_admission"].dt.year
    if "is_negative_billing" not in frame:
        frame["is_negative_billing"] = (frame["billing_amount"] < 0).astype(int)
    missing = set(MODEL_FEATURES + [TARGET]).difference(frame.columns)
    if missing: raise ValueError(f"Missing model columns: {sorted(missing)}")
    return frame[MODEL_FEATURES + [TARGET]].copy()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/processed/healthcare_clean.csv")
    parser.add_argument("--output", default="data/processed/model_features.csv")
    args = parser.parse_args(); configure_logging()
    features = engineer_features(pd.read_csv(args.input))
    output = ensure_parent(args.output); features.to_csv(output, index=False); LOGGER.info("Saved %s", output)


if __name__ == "__main__": main()
