"""
E4 · Clinical review — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E4 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import ReviewRequest
from .schemas import ReviewRequestCreate


def list_review_requests(db: Session, company_id: int) -> list[ReviewRequest]:
    """All review requests of one company, oldest first."""
    stmt = select(ReviewRequest).where(ReviewRequest.company_id == company_id).order_by(ReviewRequest.id)
    return list(db.scalars(stmt))


def get_review_request(db: Session, company_id: int, review_request_id: int) -> ReviewRequest | None:
    """One review request, or None if it doesn't exist OR belongs to another company."""
    item = db.get(ReviewRequest, review_request_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_review_request(db: Session, company_id: int, data: ReviewRequestCreate) -> ReviewRequest:
    """Save a new review request for this company."""
    item = ReviewRequest(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
