from datetime import datetime
import uuid
from app.utils.logger import get_logger

logger = get_logger("BookingAgent")


def confirm_booking(
    flights: list,
    hotels: list,
    policy: dict
) -> dict:
    """
    Booking Agent
    Inputs:
    - flights: list of flight options
    - hotels: list of hotel options
    - policy: policy decision
    """

    logger.info("Attempting booking confirmation")

    if not policy.get("approved"):
        return {
            "status": "rejected",
            "reason": "Policy not approved"
        }

    if not flights or not hotels:
        return {
            "status": "failed",
            "reason": "Missing flight or hotel data"
        }

    booking_id = f"TM-{uuid.uuid4().hex[:8].upper()}"

    return {
        "status": "confirmed",
        "booking_id": booking_id,
        "confirmed_at": datetime.utcnow().isoformat(),
        "flight": flights[0],
        "hotel": hotels[0]
    }
