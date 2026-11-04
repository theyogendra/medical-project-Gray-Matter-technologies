"""
E0 · Tenancy and onboarding — the shapes of data going in and out of the API (Pydantic).

- CompanyCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- CompanyRead:   what the API SENDS BACK. It adds id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CompanyCreate(BaseModel):
    name: str = Field(
        min_length=1, max_length=200, description="Company display name", examples=["Sunrise Medical Travel"]
    )
    plan: str = Field(
        min_length=1, max_length=200, description="Free / Practice / Desk (E0-02)", examples=["Free"]
    )


class CompanyRead(CompanyCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    created_at: datetime
