"""Shared project utilities."""
from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import Any


def configure_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(level=level, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")


def ensure_parent(path: str | Path) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    return output


def save_json(payload: dict[str, Any], path: str | Path) -> None:
    ensure_parent(path).write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
