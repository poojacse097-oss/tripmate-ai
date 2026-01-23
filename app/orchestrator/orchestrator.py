from app.agents.intent_agent import extract_intent
from app.agents.flight_agent import search_flights
from app.agents.hotel_agent import search_hotels
from app.agents.pricing_agent import calculate_price
from app.agents.policy_agent import evaluate_policy
from app.agents.booking_agent import confirm_booking
from app.agents.payment_agent import process_payment
from app.utils.logger import get_logger

logger = get_logger("Orchestrator")


def orchestrate(user_query: str) -> dict:
    logger.info("Received user query")

    # 1️⃣ Extract intent
    intent_data = extract_intent(user_query)
    logger.info(f"Detected intent: {intent_data.get('intent')}")

    if "error" in intent_data:
        return {
            "status": "failed",
            "reason": intent_data["error"]
        }

    entities = intent_data.get("entities", {})
    response = {
        "status": "success",
        "intent_data": intent_data,
        "results": {}
    }

    # 2️⃣ Flight search
    response["results"]["flights"] = search_flights(
        source=entities.get("source"),
        destination=entities.get("destination"),
        date=entities.get("date"),
        budget=True
    )

    # 3️⃣ Hotel search
    if "hotel" in entities.get("preferences", ""):
        response["results"]["hotels"] = search_hotels(
            city=entities.get("destination"),
            date=entities.get("date"),
            budget=True
        )

    # 4️⃣ Pricing
    response["results"]["pricing"] = calculate_price(
        flights=response["results"]["flights"]["results"],
        hotels=response["results"]["hotels"]["results"]
    )

    # 5️⃣ Policy check
    response["results"]["policy"] = evaluate_policy(
        response["results"]["pricing"]
    )

    # 6️⃣ Booking
    response["results"]["booking"] = confirm_booking(
    flights=response["results"]["flights"]["results"],
    hotels=response["results"]["hotels"]["results"],
    policy=response["results"]["policy"]

    )

    # 7️⃣ Payment
    response["results"]["payment"] = process_payment(
        response["results"]["pricing"]["total_price"]
    )

    logger.info("Trip orchestration completed successfully")
    return response
