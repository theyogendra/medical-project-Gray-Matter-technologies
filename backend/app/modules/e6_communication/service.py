"""
E6 · Communication timeline — business rules.

Keep endpoints (router.py) thin: they only call functions from this file.
Other modules may call these functions too — that is the ONLY way another module
should read or change E6 data (never by querying our tables directly).

Every function takes `company_id` and filters by it: one company never sees another's data.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Message
from .schemas import MessageCreate


def list_messages(db: Session, company_id: int) -> list[Message]:
    """All messages of one company, oldest first."""
    stmt = select(Message).where(Message.company_id == company_id).order_by(Message.id)
    return list(db.scalars(stmt))


def get_message(db: Session, company_id: int, message_id: int) -> Message | None:
    """One message, or None if it doesn't exist OR belongs to another company."""
    item = db.get(Message, message_id)
    if item is None or item.company_id != company_id:
        return None
    return item


def create_message(db: Session, company_id: int, data: MessageCreate) -> Message:
    """Save a new message for this company."""
    item = Message(company_id=company_id, **data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
