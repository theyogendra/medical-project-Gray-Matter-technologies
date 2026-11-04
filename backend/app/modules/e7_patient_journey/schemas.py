"""
E7 · Patient journey — the shapes of data going in and out of the API (Pydantic).

- FamilyLinkCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- FamilyLinkRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class FamilyLinkCreate(BaseModel):
    case_id: int = Field(ge=1, description="Case the family can follow", examples=[1])
    contact_name: str = Field(
        min_length=1, max_length=200, description="Family member's name", examples=["Fatima Musa"]
    )
    phone: str = Field(
        min_length=1,
        max_length=200,
        description="Where the one-time code goes",
        examples=["+234 800 000 0000"],
    )
    active: bool = Field(description="False after 'stop sharing'", examples=[True])


class FamilyLinkRead(FamilyLinkCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime


class JourneyView(BaseModel):
    """What the family sees: plain words only, no internal notes."""

    case_code: str
    stage_plain: str = Field(description="Stage in plain language for the family")
    sharing_allowed: bool = Field(description="False if the patient has not given / has revoked consent")
