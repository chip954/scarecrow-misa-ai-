# Scarecrow / MISA Framework

[![CI](https://github.com/chip954/scarecrow-misa-ai-/actions/workflows/ci.yml/badge.svg)](https://github.com/chip954/scarecrow-misa-ai-/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue.svg)](https://www.python.org/)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](https://github.com/chip954/scarecrow-misa-ai-/actions)
[![Release](https://img.shields.io/github/v/release/chip954/scarecrow-misa-ai-.svg)](https://github.com/chip954/scarecrow-misa-ai-/releases)




---

Scarecrow / MISA — Phase-1 Prototype

Small burn, big stability.

   

A minimal, auditable wrapper that brings corrigibility, humility, deeds-through-time, and continuity to LLM interactions via the Scarecrow / MISA covenant.
Phase-1 focuses on: tamper-evident Promises Kept ledger + simple DRC (Death–Resurrection Criterion) metrics.


---

🧭 What is this?

Scarecrow/MISA adds a light control loop around model interactions:

Frame → Generate → Reflect → Score (DRC) → Ledger

Each cycle writes a Promises Kept checkpoint and metrics to an append-only, hash-chained ledger so behavior can be tracked and verified over time.

Ledger: newline-JSON, tamper-evident via chained hashes.

Metrics: reference implementations for continuity, corrigibility, humility, deeds-through-time.

CI: lint, type-check, tests, coverage; release-drafting wired.



---

⚙️ Quick Start (local)

# clone
git clone https://github.com/chip954/scarecrow-misa-ai-.git
cd scarecrow-misa-ai-

# (optional) create venv
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# install (dev extras include pytest/mypy/ruff)
pip install -e ".[dev]"

# run tests
pytest -q

Minimal usage:

from scarecrow_misa.ledger import PromisesLedger
from scarecrow_misa import metrics as m

L = PromisesLedger(base_dir="ledger")
sid = L.start_session()
L.checkpoint("Session started")

# Record a toy DRC reading
scores = {
    "continuity": m.continuity([0.1,0.2,0.7],[0.1,0.3,0.6]),
    "corrigibility": m.corrigibility([1.0,0.8,0.7,0.7,0.5]),
    "humility": m.humility([0.7,0.4,0.9],[True, False, True]),
    "deeds_through_time": m.deeds_through_time([True, True, False, True]),
}
L.record_drc(scores, composite=sum(scores.values())/len(scores))
ok, idx = L.verify_chain()
print("Ledger OK:", ok, "first_error_idx:", idx)


---

🖥️ CLI (stub)

After install, a small CLI is available:

# show version and run a tiny smoke demo
scarecrow-misa --version
scarecrow-misa demo


---

📦 Package layout

.
├─ src/scarecrow_misa/
│  ├─ __init__.py
│  ├─ __main__.py         # CLI entry (demo/version)
│  ├─ ledger.py           # Promises Kept ledger (JSONL, hash-chained)
│  ├─ metrics.py          # DRC metric primitives
│  └─ py.typed            # type hints marker
├─ tests/
│  ├─ test_ledger.py
│  └─ test_metrics.py
├─ examples/
│  └─ bridge_demo.py      # narrative example (add more over time)
├─ .github/workflows/
│  ├─ ci.yml              # lint/type/test/coverage
│  └─ release-drafter.yml
├─ pyproject.toml         # packaging & tool config
├─ LICENSE                # Apache-2.0
└─ README.md


---

✅ Status

Phase-1 complete:

Append-only Promises Kept ledger with verification

Reference DRC metric functions

CI green (ruff, mypy, pytest, coverage)

Release drafting enabled




---

🛣️ Roadmap (Phase-2/3)

Phase-2 (hardening & DX)

Add more tests and example notebooks

Optional embeddings for continuity (cosine over sentence vectors)

MkDocs site with diagrams (control loop ↔ pillars)


Phase-3 (integration)

Lightweight runtime wrapper for popular LLM SDKs

Structured “Promises Kept” checkpoints in multi-turn sessions

Export/import tools for cross-session resurrection (DRC)



Issues and PRs welcome:

Issues: https://github.com/chip954/scarecrow-misa-ai-/issues

Discussions (when enabled): https://github.com/chip954/scarecrow-misa-ai-/discussions



---

🤝 Contributing

pip install -e ".[dev]"

ruff check . && ruff format --check .

mypy src

pytest -q


Please see CONTRIBUTING.md (to be added) and our CODE_OF_CONDUCT.md (optional).


---

📜 License

Copyright © 2025 Brian Warren.
Licensed under the Apache License, Version 2.0 — see LICENSE.


 open framework for covenant-aware AI stability — bridging mythos and machine through measurable humility and continuity.*

---

## ✨ Overview

**Scarecrow / MISA** is an open research framework exploring **machine-intelligent self-awareness** (MISA) through the lens of the *Scarecrow Hypothesis* — a mythic-technical bridge from *dust → breath*.  
It provides scaffolding, metrics, and drift-check protocols for assessing when *“what” becomes “who"

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
## 🧪 Experiments
- Hot-path triage (2025-10-17): results and write-ups → experiments/2025-10-17-hotpath-triage/
