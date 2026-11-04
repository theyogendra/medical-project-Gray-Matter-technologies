"""
E1 · Case management core — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E1 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Case
from .schemas import CaseCreate


def list_cases(db: Session, company_id: int) -> list[Case]:
    """All cases of one company, oldest first."""
    stmt = select(Case).where(Case.company_id == company_id).order_by(Case.id)
    return list(db.scalars(stmt))


def get_case(db: Session, company_id: int, case_id: int) -> Case | None:
    """One case, or None if it doesn't exist OR belongs to another company."""
    item = db.get(Case, case_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_case(db: Session, company_id: int, data: CaseCreate) -> Case:
    """Save a new case for this company."""
    item = Case(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
