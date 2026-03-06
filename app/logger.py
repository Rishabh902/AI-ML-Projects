import logging
import sys
import os

# Create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

def setup_logger():
    logger = logging.getLogger("chatbot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # ✅ Console Handler (Terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # ✅ File Handler (Log File)
    file_handler = logging.FileHandler("logs/chatbot.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Add both handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


logger = setup_logger()