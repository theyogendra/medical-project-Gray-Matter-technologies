"""
E4 · Clinical review — API endpoints (URLs).

All URLs start with /api/e4. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import ReviewRequestCreate, ReviewRequestRead

router = APIRouter(prefix="/api/e4", tags=["E4 · Clinical review"])


@router.get("/review-requests", response_model=list[ReviewRequestRead])
def list_review_requests(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every review request of the current company."""
    return service.list_review_requests(db, company_id)


@router.post("/review-requests", response_model=ReviewRequestRead, status_code=201)
def create_review_request(
    data: ReviewRequestCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a review request. Missing or wrong fields are refused with 422 automatically."""
    return service.create_review_request(db, company_id, data)


@router.get("/review-requests/{review_request_id}", response_model=ReviewRequestRead)
def get_review_request(
    review_request_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)
):
    """Get one review request by id."""
    item = service.get_review_request(db, company_id, review_request_id)
    if item is None:
        raise HTTPException(status_code=404, detail="ReviewRequest not found")
    return item
