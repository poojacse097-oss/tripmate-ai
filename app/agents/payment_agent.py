from datetime import datetime
import uuid
from app.utils.logger import get_logger

logger = get_logger("PaymentAgent")


def process_payment(
    amount: float,
    method: str = "UPI"
) -> dict:
    """
    Payment Agent
    Inputs:
    - amount: total amount to be paid
    - method: payment method (default UPI)
    """

    logger.info(f"Processing payment of amount: {amount}")

    if amount <= 0:
        return {
            "status": "failed",
            "reason": "Invalid payment amount"
        }

    transaction_id = f"PAY-{uuid.uuid4().hex[:10].upper()}"

    return {
        "status": "success",
        "transaction_id": transaction_id,
        "payment_method": method,
        "amount_paid": amount,
        "paid_at": datetime.utcnow().isoformat()
    }
