import json
from pathlib import Path
from app.utils.logger import get_logger
logger = get_logger("HotelService")


DATA_PATH = Path("data/hotels.json")

def fetch_hotels(city: str, date: str):
    with open(DATA_PATH, "r") as f:
        return json.load(f)
    logger.info("Fetching hotels")
logger.warning("Hotel API failed, using mock data")

