from app.utils.logger import get_logger

logger = get_logger("PricingAgent")


def calculate_price(
    flights: list,
    hotels: list,
    max_budget: float = 5000
) -> dict:
    """
    Pricing agent
    Inputs:
    - flights: list of flight dicts
    - hotels: list of hotel dicts
    """

    logger.info("Calculating trip price")

    flight_price = 0
    hotel_price = 0

    # 🔐 Safety checks
    if isinstance(flights, list) and flights:
        flight_price = min(f.get("price", 0) for f in flights)

    if isinstance(hotels, list) and hotels:
        hotel_price = min(h.get("price_per_night", 0) for h in hotels)

    total_price = flight_price + hotel_price

    return {
        "flight_price": flight_price,
        "hotel_price": hotel_price,
        "total_price": total_price,
        "budget_limit": max_budget,
        "within_budget": total_price <= max_budget
    }
