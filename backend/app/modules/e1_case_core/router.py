"""
E1 · Case management core — API endpoints (URLs).

All URLs start with /api/e1. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import CaseCreate, CaseRead

router = APIRouter(prefix="/api/e1", tags=["E1 · Case management core"])


@router.get("/cases", response_model=list[CaseRead])
def list_cases(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every case of the current company."""
    return service.list_cases(db, company_id)


@router.post("/cases", response_model=CaseRead, status_code=201)
def create_case(
    data: CaseCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a case. Missing or wrong fields are refused with 422 automatically."""
    return service.create_case(db, company_id, data)


@router.get("/cases/{case_id}", response_model=CaseRead)
def get_case(case_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """Get one case by id."""
    item = service.get_case(db, company_id, case_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return item
