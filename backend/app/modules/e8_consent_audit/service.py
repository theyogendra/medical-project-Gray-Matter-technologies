"""
E8 · Consent and audit — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E8 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Consent
from .schemas import ConsentCreate


def list_consents(db: Session, company_id: int) -> list[Consent]:
    """All consents of one company, oldest first."""
    stmt = select(Consent).where(Consent.company_id == company_id).order_by(Consent.id)
    return list(db.scalars(stmt))


def get_consent(db: Session, company_id: int, consent_id: int) -> Consent | None:
    """One consent, or None if it doesn't exist OR belongs to another company."""
    item = db.get(Consent, consent_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_consent(db: Session, company_id: int, data: ConsentCreate) -> Consent:
    """Save a new consent for this company."""
    item = Consent(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def has_consent(db: Session, company_id: int, case_id: int) -> bool:
    """
    True if this case has at least one granted (not revoked) consent.
    Other modules (E4 doctor links, E7 family view) MUST call this before sharing anything.
    """
    stmt = select(Consent).where(
        Consent.company_id == company_id,
        Consent.case_id == case_id,
        Consent.granted.is_(True),
    )
    return db.scalars(stmt).first() is not None
