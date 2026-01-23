from datetime import datetime, timedelta

def normalize_date(date_str: str) -> str:
    if not date_str:
        return None

    if date_str.lower() == "tomorrow":
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    return date_str
