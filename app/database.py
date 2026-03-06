from motor.motor_asyncio import AsyncIOMotorClient
from app.config import config
from app.logger import logger
import certifi

client = AsyncIOMotorClient(
    config.MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client[config.DB_NAME]
orders_collection = db[config.COLLECTION_NAME]

logger.info("MongoDB setup completed")