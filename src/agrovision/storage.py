import json, pathlib
from typing import List, Dict, Any

DATA_PATH = pathlib.Path("data/agrovision.json")

def load() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        DATA_PATH.write_text("[]", encoding="utf-8")
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def save(items: List[Dict[str, Any]]) -> None:
    DATA_PATH.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
