from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator.orchestrator import orchestrate
from app.models.trip_models import TripResponse

app = FastAPI(title="TripMate AI")

class TripRequest(BaseModel):
    query: str

@app.post("/plan-trip", response_model=TripResponse)
def plan_trip(request: TripRequest):
    return orchestrate(request.query)
