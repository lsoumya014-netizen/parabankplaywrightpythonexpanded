from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "testdata" / "test_data.json"


def load_test_data() -> dict[str, Any]:
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)
