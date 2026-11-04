"""
E6 · Communication timeline — API endpoints (URLs).

All URLs start with /api/e6. Try them at http://localhost:8000/docs
An endpoint should only: read the request -> call service.py -> return the result.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.tenancy import get_company_id

from . import service
from .schemas import MessageCreate, MessageRead

router = APIRouter(prefix="/api/e6", tags=["E6 · Communication timeline"])


@router.get("/messages", response_model=list[MessageRead])
def list_messages(db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """List every message of the current company."""
    return service.list_messages(db, company_id)


@router.post("/messages", response_model=MessageRead, status_code=201)
def create_message(
    data: MessageCreate,
    db: Session = Depends(get_db),
    company_id: int = Depends(get_company_id),
):
    """Create a message. Missing or wrong fields are refused with 422 automatically."""
    return service.create_message(db, company_id, data)


@router.get("/messages/{message_id}", response_model=MessageRead)
def get_message(message_id: int, db: Session = Depends(get_db), company_id: int = Depends(get_company_id)):
    """Get one message by id."""
    item = service.get_message(db, company_id, message_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return item
