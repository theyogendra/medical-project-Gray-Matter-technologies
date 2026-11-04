"""
E10 · Integrations — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E10 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Payment
from .schemas import PaymentCreate


def list_payments(db: Session, company_id: int) -> list[Payment]:
    """All payments of one company, oldest first."""
    stmt = select(Payment).where(Payment.company_id == company_id).order_by(Payment.id)
    return list(db.scalars(stmt))


def get_payment(db: Session, company_id: int, payment_id: int) -> Payment | None:
    """One payment, or None if it doesn't exist OR belongs to another company."""
    item = db.get(Payment, payment_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_payment(db: Session, company_id: int, data: PaymentCreate) -> Payment:
    """Save a new payment for this company."""
    item = Payment(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
