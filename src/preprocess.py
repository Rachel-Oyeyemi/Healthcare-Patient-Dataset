"""Clean and validate raw healthcare admission records."""
from __future__ import annotations
import argparse
import logging
import re
from pathlib import Path
import pandas as pd
from utils import configure_logging, ensure_parent

LOGGER = logging.getLogger(__name__)
REQUIRED_COLUMNS = {"Name","Age","Gender","Blood Type","Medical Condition","Date of Admission","Doctor","Hospital","Insurance Provider","Billing Amount","Room Number","Admission Type","Discharge Date","Medication","Test Results"}


def snake_case(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def validate_schema(data: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")


def preprocess_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    validate_schema(data)
    clean = data.copy(); clean.columns = [snake_case(c) for c in clean.columns]
    for column in ("date_of_admission", "discharge_date"):
        clean[column] = pd.to_datetime(clean[column], errors="coerce")
    if clean[["date_of_admission", "discharge_date"]].isna().any().any():
        raise ValueError("Invalid admission or discharge dates detected")
    before = len(clean); clean = clean.drop_duplicates().reset_index(drop=True)
    LOGGER.info("Removed %d exact duplicates", before - len(clean))
    clean["name"] = clean["name"].astype(str).str.strip().str.title()
    clean["doctor"] = clean["doctor"].astype(str).str.replace(r"^Dr\.\s*", "", regex=True).str.strip().str.title()
    clean["hospital"] = clean["hospital"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip(" ,").str.title()
    clean["billing_amount"] = pd.to_numeric(clean["billing_amount"], errors="coerce").round(2)
    clean["age"] = pd.to_numeric(clean["age"], errors="coerce").astype("Int64")
    clean["room_number"] = pd.to_numeric(clean["room_number"], errors="coerce").astype("Int64")
    clean["is_negative_billing"] = (clean["billing_amount"] < 0).astype(int)
    clean["length_of_stay"] = (clean["discharge_date"] - clean["date_of_admission"]).dt.days
    if (clean["length_of_stay"] < 0).any():
        raise ValueError("Discharge date precedes admission date")
    clean.insert(0, "admission_id", [f"ADM-{i+1:06d}" for i in range(len(clean))])
    return clean


def preprocess_file(input_path: str | Path, output_path: str | Path) -> Path:
    source = Path(input_path)
    if not source.exists(): raise FileNotFoundError(source)
    cleaned = preprocess_dataframe(pd.read_csv(source))
    output = ensure_parent(output_path); cleaned.to_csv(output, index=False)
    LOGGER.info("Saved %d cleaned rows to %s", len(cleaned), output); return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/raw/healthcare_dataset.csv")
    parser.add_argument("--output", default="data/processed/healthcare_clean.csv")
    args = parser.parse_args(); configure_logging(); preprocess_file(args.input, args.output)


if __name__ == "__main__": main()
