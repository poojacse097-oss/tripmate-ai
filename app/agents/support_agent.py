from datetime import datetime

def handle_support(action: str, booking: dict):
    if not booking or booking.get("status") != "confirmed":
        return {
            "status": "failed",
            "reason": "No confirmed booking found"
        }

    if action == "cancel":
        return {
            "status": "cancelled",
            "booking_id": booking.get("booking_id"),
            "cancelled_at": datetime.utcnow().isoformat(),
            "refund_status": "Initiated"
        }

    if action == "help":
        return {
            "status": "ticket_created",
            "booking_id": booking.get("booking_id"),
            "message": "Support team will contact you shortly"
        }

    return {
        "status": "failed",
        "reason": "Unsupported support action"
    }
