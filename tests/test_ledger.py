# tests/test_ledger_min.py
from scarecrow_misa import PromisesLedger


def test_ledger_roundtrip(tmp_path):
    L = PromisesLedger(base_dir=tmp_path)
    sid = L.start_session()
    L.checkpoint("init")
    L.record_drc({"continuity": 0.9}, composite=0.9)
    ok, bad = L.verify_chain()
    assert ok and bad is None
