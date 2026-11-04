"""
E5 · Treatment financial plan — the shapes of data going in and out of the API (Pydantic).

- EstimateLineCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- EstimateLineRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EstimateLineCreate(BaseModel):
    case_id: int = Field(ge=1, description="Case this estimate is for", examples=[1])
    group_name: str = Field(
        min_length=1, max_length=200, description="One of the 4 estimate groups", examples=["Hospital"]
    )
    label: str = Field(
        min_length=1, max_length=200, description="What the line is for", examples=["Surgery package"]
    )
    min_amount: float = Field(ge=0, description="Minimum cost (INR)", examples=[250000.0])
    likely_amount: float = Field(ge=0, description="Likely cost (INR)", examples=[300000.0])
    certainty: str = Field(min_length=1, max_length=200, description="Certainty label", examples=["Likely"])


class EstimateLineRead(EstimateLineCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
