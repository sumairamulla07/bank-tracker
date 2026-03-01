from fastapi import FastAPI
from pydantic import BaseModel
from sms_parser import parse_sms
from categorizer import categorize_merchant
from datetime import datetime

app = FastAPI()

class SMSRequest(BaseModel):
    sms_text: str

@app.get("/")
def home():
    return {"message": "Bank Tracker is alive! 🎉"}

@app.post("/sms")
def process_sms(request: SMSRequest):
    try:
        from database import transactions_collection
        parsed = parse_sms(request.sms_text)
        category = categorize_merchant(parsed["merchant"])

        transaction = {
            "merchant": parsed["merchant"],
            "upi_id": parsed["upi_id"],
            "amount": parsed["amount"],
            "type": parsed["type"],
            "category": category,
            "raw_sms": request.sms_text,
            "date": datetime.now().isoformat()
        }

        result = transactions_collection.insert_one(transaction)
        transaction["_id"] = str(result.inserted_id)
        return {"message": "Transaction saved!", "transaction": transaction}
    except Exception as e:
        return {"error": str(e)}

@app.get("/transactions")
def get_transactions():
    try:
        from database import transactions_collection
        transactions = list(transactions_collection.find())
        for t in transactions:
            t["_id"] = str(t["_id"])
        return transactions
    except Exception as e:
        return {"error": str(e)}

@app.get("/summary")
def get_summary():
    try:
        from database import transactions_collection
        transactions = list(transactions_collection.find({"type": "debit"}))
        summary = {}
        for t in transactions:
            cat = t.get("category", "Other")
            summary[cat] = summary.get(cat, 0) + (t.get("amount") or 0)
        return summary
    except Exception as e:
        return {"error": str(e)}

@app.put("/transactions/{id}")
def update_category(id: str, category: str):
    try:
        from database import transactions_collection
        from bson import ObjectId
        transactions_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"category": category}}
        )
        return {"message": "Category updated!"}
    except Exception as e:
        return {"error": str(e)}
