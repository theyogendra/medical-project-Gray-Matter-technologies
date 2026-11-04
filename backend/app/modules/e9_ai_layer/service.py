"""
E9 · AI layer — business rules.

STARTER: a simple keyword rule stands in for the real AI model, so the whole flow
(read documents -> suggest -> show the reason) works end to end today.
Replace `suggest_type()` with the real model call; keep the two safety rules:
  1. every suggestion carries a `reason` (its source), and
  2. AI only SUGGESTS — a person accepts it in E2; we never overwrite their corrections.

Documents are read through e2_document_vault.service, never from E2's tables directly.
"""

from sqlalchemy.orm import Session

from app.modules.e2_document_vault import service as documents

from .schemas import Suggestion

# keyword in file name -> document type
KEYWORD_RULES = [
    ("blood", "Lab report"),
    ("lab", "Lab report"),
    ("mri", "Scan"),
    ("ct", "Scan"),
    ("xray", "Scan"),
    ("discharge", "Discharge summary"),
    ("prescription", "Prescription"),
]


def suggest_type(file_name: str) -> tuple[str, str] | None:
    """Return (suggested_type, reason) or None when we have no idea."""
    name = file_name.lower()
    for keyword, doc_type in KEYWORD_RULES:
        if keyword in name:
            return doc_type, f"File name contains '{keyword}'"
    return None


def suggestions_for_company(db: Session, company_id: int) -> list[Suggestion]:
    """A suggestion for every document whose type looks wrong."""
    result = []
    for doc in documents.list_documents(db, company_id):
        guess = suggest_type(doc.file_name)
        if guess and guess[0] != doc.doc_type:
            result.append(
                Suggestion(
                    document_id=doc.id,
                    file_name=doc.file_name,
                    current_type=doc.doc_type,
                    suggested_type=guess[0],
                    reason=guess[1],
                )
            )
    return result
