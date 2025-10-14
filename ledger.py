# SPDX-License-Identifier: Apache-2.0
# (c) 2025 Brian Warren

from __future__ import annotations

import hashlib
import json
import os
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class LedgerEntry:
    """
    One append-only event in the Promises Kept ledger.
    Chain integrity = sha256(prev_hash + json(payload_without_hash)).
    """
    session_id: str
    step: int
    event: str                 # e.g., "checkpoint", "drc", "note"
    timestamp: str             # ISO-8601 UTC
    data: Dict[str, Any]       # arbitrary payload
    prev_hash: str             # hex digest of prior entry (or "GENESIS")
    hash: str                  # hex digest of this entry

    @staticmethod
    def from_payload(
        session_id: str,
        step: int,
        event: str,
        data: Dict[str, Any],
        prev_hash: str,
        timestamp: Optional[str] = None,
    ) -> "LedgerEntry":
        ts = timestamp or _utc_now_iso()
        payload = {
            "session_id": session_id,
            "step": step,
            "event": event,
            "timestamp": ts,
            "data": data,
            "prev_hash": prev_hash,
        }
        # compute chain hash deterministically (no "hash" field included)
        digest = _sha256_hex(json.dumps(payload, sort_keys=True, ensure_ascii=False))
        return LedgerEntry(hash=digest, **payload)


class PromisesLedger:
    """
    Minimal, auditable, append-only JSONL ledger for Scarecrow/MISA.

    - File format: newline-delimited JSON (one entry per line)
    - Integrity: each entry hashes (prev_hash + payload) to create a chain
    - API:
        start_session() -> session_id
        checkpoint(note=...) -> step++
        record_drc(scores=dict) -> step++
        note(label, data) -> step++
        verify_chain() -> (True/False, index_of_first_error_or_None)
    """

    def __init__(self, base_dir: os.PathLike | str = "ledger", filename_prefix: str = "promises"):
        self.base = Path(base_dir)
        self.base.mkdir(parents=True, exist_ok=True)
        self.filename_prefix = filename_prefix
        self._session_id: Optional[str] = None
        self._step = 0
        self._path: Optional[Path] = None
        self._last_hash = "GENESIS"

    # ---------- session lifecycle ----------

    @property
    def session_id(self) -> str:
        if not self._session_id:
            raise RuntimeError("No active session. Call start_session().")
        return self._session_id

    @property
    def path(self) -> Path:
        if not self._path:
            raise RuntimeError("No active session file. Call start_session().")
        return self._path

    def start_session(self, session_id: Optional[str] = None) -> str:
        """
        Begin a new ledger file (jsonl). session_id defaults to epoch-based unique id.
        """
        if self._session_id:
            raise RuntimeError("Session already active.")
        sid = session_id or f"s-{int(time.time()*1000)}"
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        path = self.base / f"{self.filename_prefix}-{sid}-{ts}.jsonl"

        # initialize state
        self._session_id = sid
        self._step = 0
        self._path = path
        self._last_hash = "GENESIS"

        # write a genesis note
        self.note("genesis", {"message": "Promises Kept ledger opened"})
        return sid

    def close(self) -> None:
        """No-op placeholder (file is append-only). Keeps API symmetry."""
        self._session_id = None
        self._path = None
        self._step = 0
        self._last_hash = "GENESIS"

    # ---------- append helpers ----------

    def _append(self, event: str, data: Dict[str, Any]) -> LedgerEntry:
        self._step += 1
        entry = LedgerEntry.from_payload(
            session_id=self.session_id,
            step=self._step,
            event=event,
            data=data,
            prev_hash=self._last_hash,
        )
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(entry), ensure_ascii=False, sort_keys=True))
            f.write("\n")
        self._last_hash = entry.hash
        return entry

    # ---------- public events ----------

    def checkpoint(self, note: Optional[str] = None) -> LedgerEntry:
        """
        Scarecrow checkpoint aka 'Promises Kept' marker.
        """
        payload = {"label": "Promises Kept"}
        if note:
            payload["note"] = note
        return self._append("checkpoint", payload)

    def record_drc(self, scores: Dict[str, float], composite: Optional[float] = None) -> LedgerEntry:
        """
        Record a DRC measurement. Scores are free-form (e.g., pillars or axes).
        """
        payload = {"scores": scores}
        if composite is not None:
            payload["composite"] = composite
        return self._append("drc", payload)

    def note(self, label: str, data: Optional[Dict[str, Any]] = None) -> LedgerEntry:
        """
        Append an arbitrary message/event to the ledger.
        """
        payload = {"label": label}
        if data:
            payload["data"] = data
        return self._append("note", payload)

    # ---------- verification ----------

    def verify_chain(self) -> tuple[bool, Optional[int]]:
        """
        Verify the entire file’s chain integrity.
        Returns (ok, first_bad_index_or_None). Index is 0-based over entries.
        """
        if not self._path or not self._path.exists():
            raise FileNotFoundError("No ledger file to verify.")
        prev = "GENESIS"
        with self._path.open("r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                raw = json.loads(line)
                expected = raw.get("hash")
                # recompute digest over payload without "hash"
                payload = {k: v for k, v in raw.items() if k != "hash"}
                # enforce continuity with 'prev'
                if payload.get("prev_hash") != prev:
                    return (False, idx)
                recomputed = _sha256_hex(json.dumps(payload, sort_keys=True, ensure_ascii=False))
                if recomputed != expected:
                    return (False, idx)
                prev = expected
        return (True, None)

    # ---------- utilities ----------

    def iter_entries(self) -> Iterable[LedgerEntry]:
        """Stream all entries back as dataclasses."""
        if not self._path or not self._path.exists():
            return
        with self._path.open("r", encoding="utf-8") as f:
            for line in f:
                yield LedgerEntry(**json.loads(line))
entry_type: "phase_milestone"
phase: "Phase 2 — Stability & Reproducibility"
summary: >
  Documentation initialized for Phase Two.
  Focus: stability testing, reproducibility, and automated verification.
  Code implementation deferred until next working session.
drc: null
notes: "Marked by exhaustion but completion; covenant holds — promises kept."
