
from scarecrow_misa import PromisesLedger, drc_score

def main():
    ledger = PromisesLedger(base_dir="ledger")
    sid = ledger.start_session()
    print("Session:", sid)

    ledger.checkpoint("conversation:start")

    # Fake pillar scores
    scores = {
        "mission": 0.94,
        "humility": 0.91,
        "scaffolding": 0.90,
        "deeds": 0.92,
        "continuity": 0.93,
    }
    comp = drc_score(scores)
    ledger.record_drc(scores, composite=comp)

    ledger.checkpoint("conversation:mid")
    ok, idx = ledger.verify_chain()
    print("Chain OK:", ok, "first_bad_index:", idx)

    ledger.note("final", {"message": "closing"})
    ok, idx = ledger.verify_chain()
    print("Chain OK after final note:", ok, "first_bad_index:", idx)

    ledger.close()

if __name__ == "__main__":
    main()
