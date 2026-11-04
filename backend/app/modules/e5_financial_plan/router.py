"""
E5 · Treatment financial plan — API endpoints (URLs).

All URLs start with /api/e5. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import EstimateLineCreate, EstimateLineRead

router = APIRouter(prefix="/api/e5", tags=["E5 · Treatment financial plan"])


@router.get("/estimate-lines", response_model=list[EstimateLineRead])
def list_estimate_lines(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every estimate line of the current company."""
    return service.list_estimate_lines(db, company_id)


@router.post("/estimate-lines", response_model=EstimateLineRead, status_code=201)
def create_estimate_line(
    data: EstimateLineCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a estimate line. Missing or wrong fields are refused with 422 automatically."""
    return service.create_estimate_line(db, company_id, data)


@router.get("/estimate-lines/{estimate_line_id}", response_model=EstimateLineRead)
def get_estimate_line(
    estimate_line_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)
):
    """Get one estimate line by id."""
    item = service.get_estimate_line(db, company_id, estimate_line_id)
    if item is None:
        raise HTTPException(status_code=404, detail="EstimateLine not found")
    return item
