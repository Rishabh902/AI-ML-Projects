import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = "chatbot_db"
    COLLECTION_NAME = "orders"
    CONFIDENCE_THRESHOLD = 0.40
    DEFAULT_RESPONSE = "Sorry, I didn't understand that clearly. Can you rephrase?"

config = Config()