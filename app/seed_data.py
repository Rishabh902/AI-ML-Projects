# seed_data.py
import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import orders_collection

async def seed():
    await orders_collection.insert_many([
        {
            "order_id": "2345679836",
            "customer_name": "Rishabh",
            "status": "Shipped"
        },
        {
            "order_id": "9876543210",
            "customer_name": "Amit",
            "status": "Delivered"
        }
    ])
    print("Data seeded successfully!")

asyncio.run(seed())