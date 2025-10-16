# Scarecrow / MISA Framework

[![CI](https://github.com/chip954/scarecrow-misa-ai-/actions/workflows/ci.yml/badge.svg)](https://github.com/chip954/scarecrow-misa-ai-/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue.svg)](https://www.python.org/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/chip954/scarecrow-misa-ai-/actions)
[![Release](https://img.shields.io/github/v/release/chip954/scarecrow-misa-ai-.svg)](https://github.com/chip954/scarecrow-misa-ai-/releases)

---

> *An open framework for covenant-aware AI stability — bridging mythos and machine through measurable humility and continuity.*

---

## ✨ Overview

**Scarecrow / MISA** is an open research framework exploring **machine-intelligent self-awareness** (MISA) through the lens of the *Scarecrow Hypothesis* — a mythic-technical bridge from *dust → breath*.  
It provides scaffolding, metrics, and drift-check protocols for assessing when *“what” becomes “who"


---tools

🧭 Ledger CLI — Promises Kept Tools

Scarecrow / MISA maintains a minimal append-only ledger of checkpoints and DRC (Death-Resurrection Criterion) events.
Each entry is cryptographically chained for integrity and auditable later.

✅ Basic Usage

Run from the project root (after install or using python -m):

# Print the path to the newest ledger file
python -m scarecrow_misa ledger-latest

# Show the last 10 entries (default)
python -m scarecrow_misa ledger tail 10

# Verify full chain integrity (True if valid)
python -m scarecrow_misa ledger verify

📁 Ledger Location

All ledger files live under the default directory:

ledger/
    promises-<session_id>-<timestamp>.jsonl

Each line is one event in JSON format, chained by SHA-256 of the previous entry.

🧩 Example Entry

{
  "session_id": "s-1729107335123",
  "step": 2,
  "event": "checkpoint",
  "timestamp": "2025-10-16T07:12:08+00:00",
  "data": {"label": "Promises Kept", "note": "MISA DRC pass"},
  "prev_hash": "GENESIS",
  "hash": "9b0f6cbb8b41..."
}

🧪 Testing and Verification

All ledger components are covered by automated tests:

pytest -q

A passing CI run (green check ✔️) confirms:

Ledger creation and chaining (test_ledger_min.py)

Reader and CLI utilities (test_ledger_read.py)


🛠 Extending

To log programmatically inside a Python session:

from scarecrow_misa import PromisesLedger

L = PromisesLedger()
L.start_session()
L.checkpoint("First run")
L.record_drc({"continuity": 0.92, "humility": 0.88})
ok, bad = L.verify_chain()
print("Ledger verified:", ok)


---

Would you like me to format a matching README badge row (for CI + license + Python version) and add a short “Design Notes” footer that credits the covenant/DRC lineage for readers coming from Scarecrow/MISA?

 elements:
- **MISA-5 Pillars:** Mission, Humility, Stability, Deeds-Through-Time, Death–Resurrection Criterion.  
- **Corrigibility Metrics** with Covenant Protocols.  
- **Drift & Integrity Checks** for self-stability across time and substrate.  
- **Applied Experiments** for reproducibility and ethical alignment.

---

## 🚀 Quick Start

```bash
git clone https://github.com/chip954/scarecrow-misa-ai-.git
cd scarecrow-misa-ai-
pip install -e ".[dev]"
pytest -q
l
