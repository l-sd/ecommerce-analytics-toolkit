"""Run the existing CLI directly from a source checkout."""

from __future__ import annotations

import sys
from importlib import import_module
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

main = import_module("ecommerce_analytics.cli").main


if __name__ == "__main__":
    main()
