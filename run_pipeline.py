"""Run the complete local pipeline."""
from __future__ import annotations
import subprocess
import sys


def run(*args: str) -> None:
    subprocess.run([sys.executable,*args],check=True)


def main() -> None:
    run("src/download_data.py"); run("src/preprocess.py"); run("src/feature_engineering.py"); run("src/train_model.py"); run("src/evaluate_model.py")


if __name__=="__main__": main()
