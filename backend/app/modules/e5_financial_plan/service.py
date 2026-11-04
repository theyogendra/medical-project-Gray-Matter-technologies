"""
E5 · Treatment financial plan — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E5 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import EstimateLine
from .schemas import EstimateLineCreate


def list_estimate_lines(db: Session, company_id: int) -> list[EstimateLine]:
    """All estimate lines of one company, oldest first."""
    stmt = select(EstimateLine).where(EstimateLine.company_id == company_id).order_by(EstimateLine.id)
    return list(db.scalars(stmt))


def get_estimate_line(db: Session, company_id: int, estimate_line_id: int) -> EstimateLine | None:
    """One estimate line, or None if it doesn't exist OR belongs to another company."""
    item = db.get(EstimateLine, estimate_line_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_estimate_line(db: Session, company_id: int, data: EstimateLineCreate) -> EstimateLine:
    """Save a new estimate line for this company."""
    item = EstimateLine(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
