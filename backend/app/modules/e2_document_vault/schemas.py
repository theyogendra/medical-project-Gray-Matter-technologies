"""
E2 · Document vault — the shapes of data going in and out of the API (Pydantic).

- DocumentCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- DocumentRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class DocumentCreate(BaseModel):
    case_id: int = Field(ge=1, description="Which case this document belongs to", examples=[1])
    file_name: str = Field(
        min_length=1, max_length=200, description="Original file name", examples=["blood_report.pdf"]
    )
    doc_type: str = Field(
        min_length=1, max_length=200, description="Document type (E2-02)", examples=["Lab report"]
    )
    doc_date: str = Field(
        min_length=1,
        max_length=200,
        description="Date on the document, YYYY-MM-DD (E2-03)",
        examples=["2026-10-01"],
    )


class DocumentRead(DocumentCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
