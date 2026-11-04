"""
E7 · Patient journey — API endpoints (URLs).

All URLs start with /api/e7. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import FamilyLinkCreate, FamilyLinkRead, JourneyView

router = APIRouter(prefix="/api/e7", tags=["E7 · Patient journey"])


@router.get("/family-links", response_model=list[FamilyLinkRead])
def list_family_links(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every family link of the current company."""
    return service.list_family_links(db, company_id)


@router.post("/family-links", response_model=FamilyLinkRead, status_code=201)
def create_family_link(
    data: FamilyLinkCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a family link. Missing or wrong fields are refused with 422 automatically."""
    return service.create_family_link(db, company_id, data)


@router.get("/family-links/{family_link_id}", response_model=FamilyLinkRead)
def get_family_link(
    family_link_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)
):
    """Get one family link by id."""
    item = service.get_family_link(db, company_id, family_link_id)
    if item is None:
        raise HTTPException(status_code=404, detail="FamilyLink not found")
    return item


@router.get("/journey/{case_id}", response_model=JourneyView)
def journey(case_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """What the family sees for one case (uses E1 for the stage and E8 for consent)."""
    view = service.journey_for_case(db, company_id, case_id)
    if view is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return view
