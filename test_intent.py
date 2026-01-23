# test_intent.py

from app.agents.intent_agent import extract_intent

query = "Book a ticket for tomorrow from Bangalore to Chennai and find budget hotels"
print(extract_intent(query))
