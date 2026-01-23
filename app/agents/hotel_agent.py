from app.services.hotel_service import fetch_hotels


def search_hotels(city: str, date: str, budget: bool = False) -> dict:
    """
    Business logic for hotel search.
    Data is fetched via service layer.
    """

    hotels = fetch_hotels(city, date)

    # Apply business rule (budget filter)
    if budget:
        hotels = [h for h in hotels if h["price_per_night"] <= 2000]

    return {
        "city": city,
        "date": date,
        "results": hotels
    }
