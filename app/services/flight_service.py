import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv
from app.utils.logger import get_logger

load_dotenv()
logger = get_logger("FlightService")

API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("AMADEUS_API_SECRET")
BASE_URL = "https://test.api.amadeus.com"

USE_REAL_APIS = os.getenv("USE_REAL_APIS", "false").lower() == "true"

BASE_DIR = Path(__file__).resolve().parents[2]
MOCK_DATA_PATH = BASE_DIR / "data" / "flights.json"


def _get_token():
    url = f"{BASE_URL}/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
    r = requests.post(url, data=data, timeout=20)
    r.raise_for_status()
    return r.json()["access_token"]


def _fetch_mock_flights():
    """
    ALWAYS returns a list.
    NEVER returns None.
    """
    try:
        with open(MOCK_DATA_PATH, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception as e:
        logger.error(f"Failed to load mock flights: {e}")
        return []


def fetch_flights(source: str, destination: str, date: str):
    """
    Service contract:
    - ALWAYS returns a list
    - NEVER raises to agent
    """

    if not USE_REAL_APIS:
        logger.warning("Using mock flights (feature flag disabled)")
        return _fetch_mock_flights()

    try:
        token = _get_token()
        headers = {"Authorization": f"Bearer {token}"}

        params = {
            "originLocationCode": source,
            "destinationLocationCode": destination,
            "departureDate": date,
            "adults": 1,
            "max": 5
        }

        r = requests.get(
            f"{BASE_URL}/v2/shopping/flight-offers",
            headers=headers,
            params=params,
            timeout=20
        )
        r.raise_for_status()

        results = []
        for offer in r.json().get("data", []):
            seg = offer["itineraries"][0]["segments"][0]
            results.append({
                "airline": seg["carrierCode"],
                "flight_no": seg["number"],
                "price": float(offer["price"]["total"]),
                "departure": seg["departure"]["at"],
                "arrival": seg["arrival"]["at"]
            })

        return results

    except Exception as e:
        logger.warning(f"Flight API failed, falling back to mock data: {e}")
        return _fetch_mock_flights()
