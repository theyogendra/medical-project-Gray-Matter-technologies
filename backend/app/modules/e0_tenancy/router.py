"""
E0 · Tenancy and onboarding — API endpoints (URLs).

All URLs start with /api/e0. Try them at http://localhost:8000/docs
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import CompanyCreate, CompanyRead

router = APIRouter(prefix="/api/e0", tags=["E0 · Tenancy and onboarding"])


@router.get("/companies", response_model=list[CompanyRead])
def list_companies(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """
    A user may only ever see their OWN company, so this list has at most one item.
    (It is a list so every module's starter screen works the same way.)
    """
    company = service.get_company(db, company_id)
    return [company] if company else []


@router.get("/companies/me", response_model=CompanyRead)
def my_company(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """The current user's company."""
    company = service.get_company(db, company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.post("/companies", response_model=CompanyRead, status_code=201)
def sign_up_company(data: CompanyCreate, db: Session = Depends(get_db)):
    """Sign-up: create a new company. E0-01 adds the first user and email verification."""
    return service.create_company(db, data)
