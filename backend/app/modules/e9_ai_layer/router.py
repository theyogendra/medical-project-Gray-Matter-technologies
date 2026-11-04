"""
E9 · AI layer — API endpoints (URLs).

All URLs start with /api/e9. Try them at http://localhost:8000/docs
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import Suggestion

router = APIRouter(prefix="/api/e9", tags=["E9 · AI layer"])


@router.get("/suggestions", response_model=list[Suggestion])
def suggestions(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """Document-type suggestions, each with the reason behind it."""
    return service.suggestions_for_company(db, company_id)
