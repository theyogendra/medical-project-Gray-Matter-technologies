"""
E2 · Document vault — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E2 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Document
from .schemas import DocumentCreate


def list_documents(db: Session, company_id: int) -> list[Document]:
    """All documents of one company, oldest first."""
    stmt = select(Document).where(Document.company_id == company_id).order_by(Document.id)
    return list(db.scalars(stmt))


def get_document(db: Session, company_id: int, document_id: int) -> Document | None:
    """One document, or None if it doesn't exist OR belongs to another company."""
    item = db.get(Document, document_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_document(db: Session, company_id: int, data: DocumentCreate) -> Document:
    """Save a new document for this company."""
    item = Document(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
