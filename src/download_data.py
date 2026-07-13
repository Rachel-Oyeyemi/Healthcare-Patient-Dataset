"""Download the official Kaggle dataset with a safe sample fallback."""
from __future__ import annotations
import argparse
import logging
import shutil
import subprocess
from pathlib import Path
from utils import configure_logging

LOGGER = logging.getLogger(__name__)
DATASET_ID = "prasad22/healthcare-dataset"
EXPECTED_FILENAME = "healthcare_dataset.csv"


def _download_with_kagglehub(output_dir: Path) -> Path:
    import kagglehub
    cache_dir = Path(kagglehub.dataset_download(DATASET_ID))
    candidates = list(cache_dir.glob("*.csv"))
    if not candidates:
        raise FileNotFoundError(f"No CSV found in {cache_dir}")
    destination = output_dir / EXPECTED_FILENAME
    shutil.copy2(candidates[0], destination)
    return destination


def _download_with_kaggle_cli(output_dir: Path) -> Path:
    subprocess.run(["kaggle", "datasets", "download", "-d", DATASET_ID, "-p", str(output_dir), "--unzip"], check=True)
    candidates = list(output_dir.glob("*.csv"))
    if not candidates:
        raise FileNotFoundError("Kaggle CLI completed but no CSV was found")
    destination = output_dir / EXPECTED_FILENAME
    if candidates[0] != destination:
        candidates[0].replace(destination)
    return destination


def download_dataset(output_dir: str | Path = "data/raw", allow_sample: bool = True) -> Path:
    output = Path(output_dir); output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    for method in (_download_with_kagglehub, _download_with_kaggle_cli):
        try:
            path = method(output); LOGGER.info("Dataset downloaded to %s", path); return path
        except Exception as exc:
            LOGGER.warning("%s failed: %s", method.__name__, exc); errors.append(str(exc))
    sample = Path("data/sample_data/healthcare_sample.csv")
    if allow_sample and sample.exists():
        destination = output / EXPECTED_FILENAME
        shutil.copy2(sample, destination)
        LOGGER.warning("Using bundled synthetic preview at %s", destination)
        return destination
    raise RuntimeError("Unable to download dataset: " + " | ".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="data/raw")
    parser.add_argument("--no-sample", action="store_true")
    args = parser.parse_args(); configure_logging()
    download_dataset(args.output_dir, allow_sample=not args.no_sample)


if __name__ == "__main__":
    main()
