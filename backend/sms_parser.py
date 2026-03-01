import re

def parse_sms(sms_text):
    result = {
        "amount": None,
        "merchant": None,
        "type": None,  # "debit" or "credit"
        "upi_id": None
    }

    # Find amount (looks for Rs, INR, or ₹ followed by numbers)
    amount_match = re.search(r'(?:Rs\.?|INR|₹)\s*(\d+(?:\.\d{1,2})?)', sms_text, re.IGNORECASE)
    if amount_match:
        result["amount"] = float(amount_match.group(1))

    # Find UPI ID (looks like something@something)
    upi_match = re.search(r'[\w.\-]+@[\w]+', sms_text)
    if upi_match:
        result["upi_id"] = upi_match.group()
        # Extract merchant name from UPI ID (part before @)
        result["merchant"] = upi_match.group().split("@")[0].lower()

    # Figure out if money went out or came in
    debit_words = ["debited", "deducted", "paid", "sent", "payment of"]
    credit_words = ["credited", "received", "added"]

    sms_lower = sms_text.lower()
    if any(word in sms_lower for word in debit_words):
        result["type"] = "debit"
    elif any(word in sms_lower for word in credit_words):
        result["type"] = "credit"

    return result