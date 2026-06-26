def verify_transaction(tx: dict) -> dict:
    """
    Verify a transaction based on KYC and SAD–card linkage.

    Args:
        tx (dict): Transaction dictionary with keys:
            - 'kyc' (bool): Whether KYC is valid
            - 'sad_declarant' (str): Declarant name from SAD
            - 'cardholder' (str): Name on the bank card

    Returns:
        dict: Result containing 'status' and optional 'reason'.
    """
    if not tx.get("kyc"):
        return {"status": "rejected", "reason": "KYC not valid"}

    # Check if cardholder matches SAD declarant
    if tx.get("cardholder") == tx.get("sad_declarant"):
        return {"status": "approved"}
    else:
        return {"status": "rejected", "reason": "Cardholder does not match SAD declarant"}


if __name__ == "__main__":
    # Run a few sample transactions
    samples = [
        {"kyc": True, "sad_declarant": "ABC Trading Ltd", "cardholder": "ABC Trading Ltd"},
        {"kyc": True, "sad_declarant": "ABC Trading Ltd", "cardholder": "John Doe"},
        {"kyc": False, "sad_declarant": "XYZ Imports", "cardholder": "XYZ Imports"},
    ]

    for tx in samples:
        result = verify_transaction(tx)
        print(f"Transaction: {tx} -> Result: {result}")

