"""
E4 · Clinical review — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E4 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class ReviewRequest(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e4_review_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)  # Case sent for review
    doctor_name: Mapped[str] = mapped_column(String(200))  # Doctor receiving the link
    status: Mapped[str] = mapped_column(String(200))  # Sent / Opened / Answered
    expires_at: Mapped[str] = mapped_column(String(200))  # Link expiry date, YYYY-MM-DD (E4-01)
