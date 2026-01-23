from app.services.flight_service import fetch_flights
from app.utils.location_utils import get_airport_code


def search_flights(
    source: str,
    destination: str,
    date: str,
    budget: bool = False
) -> dict:
    """
    Agent responsibility:
    - Apply business rules
    - NEVER assume external data is perfect
    """

    origin_code = get_airport_code(source)
    destination_code = get_airport_code(destination)

    flights = fetch_flights(origin_code, destination_code, date)

    # 🔐 Absolute safety (enterprise rule)
    if not isinstance(flights, list):
        flights = []

    if budget:
        flights = [f for f in flights if f.get("price", 0) <= 2500]

    return {
        "route": f"{source} → {destination}",
        "date": date,
        "results": flights
    }
