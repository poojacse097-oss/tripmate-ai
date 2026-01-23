import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"

def extract_intent(user_text: str) -> dict:
    prompt = f"""
Extract intent and entities in STRICT JSON only.
Keys: intent, source, destination, date, preferences.

Text: {user_text}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an intent extraction engine. Output ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)
    except Exception:
        return {"error": "Invalid JSON", "raw": text}
