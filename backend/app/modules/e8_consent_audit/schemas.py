"""
E8 · Consent and audit — the shapes of data going in and out of the API (Pydantic).

- ConsentCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- ConsentRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ConsentCreate(BaseModel):
    case_id: int = Field(ge=1, description="Case the consent is for", examples=[1])
    scope: str = Field(
        min_length=1,
        max_length=200,
        description="Exactly what the patient agreed to",
        examples=["Share reports with Dr. Rao"],
    )
    granted: bool = Field(description="False once revoked", examples=[True])


class ConsentRead(ConsentCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
