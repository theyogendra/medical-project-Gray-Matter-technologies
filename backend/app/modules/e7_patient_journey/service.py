"""
E7 · Patient journey — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E7 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.e1_case_core import service as cases
from app.modules.e8_consent_audit import service as consent

from .models import FamilyLink
from .schemas import FamilyLinkCreate, JourneyView


def list_family_links(db: Session, company_id: int) -> list[FamilyLink]:
    """All family links of one company, oldest first."""
    stmt = select(FamilyLink).where(FamilyLink.company_id == company_id).order_by(FamilyLink.id)
    return list(db.scalars(stmt))


def get_family_link(db: Session, company_id: int, family_link_id: int) -> FamilyLink | None:
    """One family link, or None if it doesn't exist OR belongs to another company."""
    item = db.get(FamilyLink, family_link_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_family_link(db: Session, company_id: int, data: FamilyLinkCreate) -> FamilyLink:
    """Save a new family link for this company."""
    item = FamilyLink(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


# ---------------------------------------------------------------------------
# Family journey view — shows how E7 USES E1 (cases) and E8 (consent)
# through their service functions.
# ---------------------------------------------------------------------------
PLAIN_STAGE = {
    "Enquiry": "We have your enquiry and are collecting reports",
    "Medical Review": "Doctors are reviewing the reports",
    "Estimate": "Your treatment cost estimate is being prepared",
    "Travel": "We are arranging your travel",
}


def journey_for_case(db: Session, company_id: int, case_id: int) -> JourneyView | None:
    """The family's view of one case, or None if the case doesn't exist for this company."""
    case = cases.get_case(db, company_id, case_id)
    if case is None:
        return None
    return JourneyView(
        case_code=case.code,
        stage_plain=PLAIN_STAGE.get(case.stage, "Your case is in progress"),
        sharing_allowed=consent.has_consent(db, company_id, case_id),
    )
