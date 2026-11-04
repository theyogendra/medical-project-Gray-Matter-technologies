"""
E1 · Case management core — the shapes of data going in and out of the API (Pydantic).

- CaseCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- CaseRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CaseCreate(BaseModel):
    code: str = Field(
        min_length=1,
        max_length=200,
        description="Readable case reference (E1-02 will auto-generate it)",
        examples=["IPJ-0001"],
    )
    patient_name: str = Field(
        min_length=1, max_length=200, description="Patient full name", examples=["Ahmed Musa"]
    )
    country: str = Field(
        min_length=1, max_length=200, description="Patient's home country", examples=["Nigeria"]
    )
    stage: str = Field(
        min_length=1,
        max_length=200,
        description="Current stage (E1-07 adds the full stage list)",
        examples=["Enquiry"],
    )
    owner_name: str = Field(
        min_length=1, max_length=200, description="One owner per case (E1-03)", examples=["Coordinator A"]
    )


class CaseRead(CaseCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
