from scarecrow_misa.ledger import PromisesLedger
from pathlib import Path
import tempfile, json

def test_chain_integrity(tmp_path: Path):
    p = tmp_path / "ledger.json"
    L = PromisesLedger(p)
    L.append("event_a", {"x": 1})
    L.append("event_b", {"y": 2})
    assert L.verify()