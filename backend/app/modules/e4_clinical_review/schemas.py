"""
E4 · Clinical review — the shapes of data going in and out of the API (Pydantic).

- ReviewRequestCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- ReviewRequestRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ReviewRequestCreate(BaseModel):
    case_id: int = Field(ge=1, description="Case sent for review", examples=[1])
    doctor_name: str = Field(
        min_length=1, max_length=200, description="Doctor receiving the link", examples=["Dr. Rao"]
    )
    status: str = Field(
        min_length=1, max_length=200, description="Sent / Opened / Answered", examples=["Sent"]
    )
    expires_at: str = Field(
        min_length=1,
        max_length=200,
        description="Link expiry date, YYYY-MM-DD (E4-01)",
        examples=["2026-11-10"],
    )


class ReviewRequestRead(ReviewRequestCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
