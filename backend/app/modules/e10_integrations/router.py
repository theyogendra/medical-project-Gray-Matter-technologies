"""
E10 · Integrations — API endpoints (URLs).

All URLs start with /api/e10. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import PaymentCreate, PaymentRead

router = APIRouter(prefix="/api/e10", tags=["E10 · Integrations"])


@router.get("/payments", response_model=list[PaymentRead])
def list_payments(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every payment of the current company."""
    return service.list_payments(db, company_id)


@router.post("/payments", response_model=PaymentRead, status_code=201)
def create_payment(
    data: PaymentCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a payment. Missing or wrong fields are refused with 422 automatically."""
    return service.create_payment(db, company_id, data)


@router.get("/payments/{payment_id}", response_model=PaymentRead)
def get_payment(payment_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """Get one payment by id."""
    item = service.get_payment(db, company_id, payment_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return item
