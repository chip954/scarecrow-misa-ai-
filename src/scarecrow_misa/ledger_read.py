# SPDX-License-Identifier: Apache-2.0
# (c) 2025 Brian Warren

from __future__ import annotations

from pathlib import Path
from typing import Iterator, Dict, Any, Optional
import json
import time


def _ledger_files(base_dir: str | Path = "ledger") -> list[Path]:
    base = Path(base_dir)
    if not base.exists():
        return []
    return sorted(base.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)


def latest_ledger(base_dir: str | Path = "ledger") -> Optional[Path]:
    files = _ledger_files(base_dir)
    return files[-1] if files else None


def iter_entries(path: Path) -> Iterator[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def tail(path: Path, n: int = 10) -> list[Dict[str, Any]]:
    buf: list[Dict[str, Any]] = []
    for rec in iter_entries(path):
        buf.append(rec)
        if len(buf) > n:
            buf.pop(0)
    return buf


def pretty_entry(rec: Dict[str, Any]) -> str:
    t = rec.get("timestamp", "?")
    k = rec.get("event", rec.get("kind", "?"))
    step = rec.get("step", "?")
    sid = rec.get("session_id", "?")
    return f"[{t}] sid={sid} step={step} event={k} -> {json.dumps(rec.get('data') or rec, ensure_ascii=False)}"


def pretty_print_tail(path: Path, n: int = 10) -> str:
    lines = [pretty_entry(r) for r in tail(path, n=n)]
    return "\n".join(lines)
