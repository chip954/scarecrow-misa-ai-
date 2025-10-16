# tests/test_ledger_min.py
from scarecrow_misa import PromisesLedger


def test_ledger_roundtrip(tmp_path):
    L = PromisesLedger(base_dir=tmp_path)
    sid = L.start_session()
    L.checkpoint("init")
    L.record_drc({"continuity": 0.9}, composite=0.9)
    ok, bad = L.verify_chain()
    assert ok and bad is None
from pathlib import Path
from scarecrow_misa.ledger import PromisesLedger
from scarecrow_misa.ledger_read import latest_ledger, tail

def test_latest_and_tail(tmp_path: Path):
    # make a ledger and write a couple entries
    led_dir = tmp_path / "ledger"
    L = PromisesLedger(base_dir=led_dir)
    L.start_session("t1")
    L.checkpoint("first")
    L.record_drc({"continuity": 0.9})
    ok, bad = L.verify_chain()
    assert ok and bad is None

    # reader sees it
    p = latest_ledger(led_dir)
    assert p is not None and p.exists()
    last = tail(p, n=2)
    assert len(last) == 2
