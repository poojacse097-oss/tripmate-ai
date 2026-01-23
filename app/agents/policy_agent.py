def evaluate_policy(pricing: dict):
    if not pricing:
        return {
            "approved": False,
            "reason": "Pricing information missing"
        }

    if not pricing.get("within_budget"):
        return {
            "approved": False,
            "reason": "Trip exceeds budget limit"
        }

    return {
        "approved": True,
        "reason": "Trip complies with all policies"
    }
