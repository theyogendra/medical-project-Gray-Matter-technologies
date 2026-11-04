"""
E2 · Document vault — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E2 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class Document(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e2_documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)  # Which case this document belongs to
    file_name: Mapped[str] = mapped_column(String(200))  # Original file name
    doc_type: Mapped[str] = mapped_column(String(200))  # Document type (E2-02)
    doc_date: Mapped[str] = mapped_column(String(200))  # Date on the document, YYYY-MM-DD (E2-03)
