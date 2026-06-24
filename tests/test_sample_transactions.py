from verifier import verify_transaction

def test_full_compliance():
    tx = {"kyc": True, "aml": True}
    assert verify_transaction(tx) == {"status": "approved", "fine": 0}

def test_partial_compliance_with_fine():
    tx = {"kyc": True, "aml": False}
    assert verify_transaction(tx) == {"status": "approved", "fine": 200}

def test_rejection():
    tx = {"kyc": False, "aml": True}
    assert verify_transaction(tx) == {"status": "rejected"}
