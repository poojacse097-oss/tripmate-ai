CITY_TO_AIRPORT = {
    "bangalore": "BLR",
    "chennai": "MAA",
    "hyderabad": "HYD",
    "delhi": "DEL",
    "mumbai": "BOM"
}

def get_airport_code(city: str) -> str:
    if not city:
        return None

    return CITY_TO_AIRPORT.get(city.lower(), city[:3].upper())
