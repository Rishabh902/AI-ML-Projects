import json
import os
import re
from app.model_loader import model, vectorizer
from app.database import orders_collection
from app.config import config
from app.logger import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTENTS_PATH = os.path.join(BASE_DIR, "data", "intents.json")

with open(INTENTS_PATH) as f:
    intents = json.load(f)


def predict_intent(text):
    logger.info(f"Predicting intent for: {text}")

    if model is None or vectorizer is None:
        logger.error("Model or Vectorizer not loaded")
        return None, 0

    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    confidence = 1.0
    if hasattr(model, "predict_proba"):
        try:
            confidence = max(model.predict_proba(X)[0])
        except Exception as e:
            logger.warning(f"predict_proba failed: {e}")
            confidence = 1.0

    logger.info(f"Predicted tag: {prediction}, Confidence: {confidence}")

    return prediction, confidence


def get_response(tag):
    logger.info(f"Fetching response for tag: {tag}")

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            response = intent["responses"][0]
            logger.info(f"Response selected: {response}")
            return response

    logger.warning("Tag not found, returning default response")
    return config.DEFAULT_RESPONSE


async def chatbot_reply(message):
    logger.info(f"Incoming message: {message}")

    message = message.lower().strip()

    # Rule-based order check
    if "order" in message:
        logger.info("Order keyword detected")
        return "Please provide your order ID."

    # If user sends 10-digit number → treat as order ID
    if message.isdigit() and len(message) == 10:
        logger.info("Order ID detected, checking database")
        return await check_order_status(message)

    # ML-based prediction
    tag, confidence = predict_intent(message)

    if tag is None:
        logger.error("Model not loaded properly")
        return "Model not loaded properly."

    if confidence < config.CONFIDENCE_THRESHOLD:
        logger.warning(f"Low confidence: {confidence}")
        return config.DEFAULT_RESPONSE

    return get_response(tag)


async def check_order_status(order_id: str):
    try:
        logger.info(f"Searching for order ID: {order_id}")

        order = await orders_collection.find_one({"order_id": order_id})

        logger.info(f"Database result: {order}")

        if order:
            response = f"Order {order_id} is {order['status']} for {order['customer_name']}."
            logger.info(f"Order found response: {response}")
            return response
        else:
            logger.warning("Order not found in database")
            return "Order not found."

    except Exception as e:
        logger.error(f"Database error: {e}", exc_info=True)
        return "Database error."