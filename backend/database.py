from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import certifi

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(
    MONGO_URL,
    server_api=ServerApi('1'),
    tlsCAFile=certifi.where(),
    connectTimeoutMS=5000,
    socketTimeoutMS=5000,
    serverSelectionTimeoutMS=5000
)

db = client["bank_tracker"]
transactions_collection = db["transactions"]

print("✅ MongoDB client created!")