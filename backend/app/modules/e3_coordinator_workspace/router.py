"""
E3 · Coordinator workspace — API endpoints (URLs).

All URLs start with /api/e3. Try them at http://localhost:8000/docs
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import TodayItem

router = APIRouter(prefix="/api/e3", tags=["E3 · Coordinator workspace"])


@router.get("/today", response_model=list[TodayItem])
def today(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """The coordinator's Today view: every case with its next action."""
    return service.today_view(db, company_id)
