"""
E10 · Integrations — the shapes of data going in and out of the API (Pydantic).

- PaymentCreate: what the app SENDS to create one. Pydantic checks it automatically and
  answers 422 with a clear message if a field is missing or wrong.
- PaymentRead:   what the API SENDS BACK. It adds id, company_id and created_at,
  which users must never be able to set themselves.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PaymentCreate(BaseModel):
    amount: float = Field(ge=0, description="Amount in INR", examples=[4999.0])
    method: str = Field(min_length=1, max_length=200, description="Card / UPI", examples=["UPI"])
    status: str = Field(
        min_length=1,
        max_length=200,
        description="Result from the payment gateway (test mode)",
        examples=["Test-success"],
    )
    reference: str = Field(
        min_length=1, max_length=200, description="Gateway reference", examples=["TEST-0001"]
    )


class PaymentRead(PaymentCreate):
    model_config = ConfigDict(from_attributes=True)  # lets us return database objects directly

    id: int
    company_id: int
    created_at: datetime
