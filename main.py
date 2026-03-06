from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.chatbot_engine import chatbot_reply
from app.database import client
from app.logger import logger

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class Message(BaseModel):
    message: str


@app.on_event("startup")
async def startup_event():
    try:
        await client.admin.command("ping")
        logger.info("MongoDB Connected Successfully!")
    except Exception as e:
        logger.error(f"MongoDB Connection Failed: {e}")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    logger.info("Home page accessed")
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(msg: Message):
    try:
        logger.info(f"Message received: {msg.message}")

        reply = await chatbot_reply(msg.message)

        logger.info(f"Reply generated: {reply}")

        return {"response": reply}

    except Exception as e:
        logger.error(f"Full crash: {e}", exc_info=True)
        return {"response": "Backend crashed."}