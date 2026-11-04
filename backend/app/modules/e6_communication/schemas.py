"""
E6 · Communication timeline — the shapes of data going in and out of the API (Pydantic).

- MessageCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- MessageRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MessageCreate(BaseModel):
    case_id: int = Field(ge=1, description="Case this message belongs to", examples=[1])
    channel: str = Field(
        min_length=1, max_length=200, description="In-app / Email / WhatsApp", examples=["WhatsApp"]
    )
    visibility: str = Field(
        min_length=1,
        max_length=200,
        description="Patient-visible / Internal-only / Clinical",
        examples=["Internal-only"],
    )
    body: str = Field(
        min_length=1,
        max_length=200,
        description="Message text",
        examples=["Called the family, reports coming tomorrow"],
    )


class MessageRead(MessageCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
