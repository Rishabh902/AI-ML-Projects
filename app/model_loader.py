import pickle
import os
from app.logger import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "chatbot_model.pkl") # we have join the path and search models 
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

try:
    logger.info("ML model is loading...") # this is logger from logs , we can see all action from this 
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)

    logger.info("Model and vectorizer loaded successfully")

except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise e