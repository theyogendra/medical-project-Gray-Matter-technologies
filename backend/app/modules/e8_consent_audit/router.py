"""
E8 · Consent and audit — API endpoints (URLs).

All URLs start with /api/e8. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import ConsentCreate, ConsentRead

router = APIRouter(prefix="/api/e8", tags=["E8 · Consent and audit"])


@router.get("/consents", response_model=list[ConsentRead])
def list_consents(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every consent of the current company."""
    return service.list_consents(db, company_id)


@router.post("/consents", response_model=ConsentRead, status_code=201)
def create_consent(
    data: ConsentCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a consent. Missing or wrong fields are refused with 422 automatically."""
    return service.create_consent(db, company_id, data)


@router.get("/consents/{consent_id}", response_model=ConsentRead)
def get_consent(consent_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """Get one consent by id."""
    item = service.get_consent(db, company_id, consent_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Consent not found")
    return item
