# verifier.py

def verify_transaction(tx: dict) -> dict:
    """
    Verify a transaction based on KYC and AML flags.

    Args:
        tx (dict): Transaction dictionary with 'kyc' and 'aml' boolean keys.

    Returns:
        dict: Result containing 'status' and optional 'fine'.
    """
    if tx.get("kyc") and tx.get("aml"):
        return {"status": "approved", "fine": 0}
    elif tx.get("kyc") and not tx.get("aml"):
        return {"status": "approved", "fine": 200}
    else:
        return {"status": "rejected"}


if __name__ == "__main__":
    # Run a few sample transactions
    samples = [
        {"kyc": True, "aml": True},
        {"kyc": True, "aml": False},
        {"kyc": False, "aml": True},
        {"kyc": False, "aml": False},
    ]

    for tx in samples:
        result = verify_transaction(tx)
        print(f"Transaction: {tx} -> Result: {result}")
