from pydantic import BaseModel
from typing import List, Optional


class Flight(BaseModel):
    airline: str
    flight_no: str
    price: float
    departure: str
    arrival: str


class Hotel(BaseModel):
    name: str
    price_per_night: float
    rating: float
    area: str


class Pricing(BaseModel):
    flight_price: float
    hotel_price: float
    total_price: float
    budget_limit: float
    within_budget: bool


class Policy(BaseModel):
    approved: bool
    reason: str


class Booking(BaseModel):
    status: str
    booking_id: Optional[str]
    confirmed_at: Optional[str]
    flight: Optional[Flight]
    hotel: Optional[Hotel]


class Payment(BaseModel):
    status: str
    transaction_id: Optional[str]
    payment_method: Optional[str]
    amount_paid: Optional[float]
    paid_at: Optional[str]


class TripResults(BaseModel):
    flights: Optional[dict]
    hotels: Optional[dict]
    pricing: Optional[Pricing]
    policy: Optional[Policy]
    booking: Optional[Booking]
    payment: Optional[Payment]


class TripResponse(BaseModel):
    status: str
    intent_data: dict
    results: TripResults
