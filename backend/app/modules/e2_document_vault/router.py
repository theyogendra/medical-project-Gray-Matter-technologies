"""
E2 · Document vault — API endpoints (URLs).

All URLs start with /api/e2. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import DocumentCreate, DocumentRead

router = APIRouter(prefix="/api/e2", tags=["E2 · Document vault"])


@router.get("/documents", response_model=list[DocumentRead])
def list_documents(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every document of the current company."""
    return service.list_documents(db, company_id)


@router.post("/documents", response_model=DocumentRead, status_code=201)
def create_document(
    data: DocumentCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a document. Missing or wrong fields are refused with 422 automatically."""
    return service.create_document(db, company_id, data)


@router.get("/documents/{document_id}", response_model=DocumentRead)
def get_document(document_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """Get one document by id."""
    item = service.get_document(db, company_id, document_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return item
