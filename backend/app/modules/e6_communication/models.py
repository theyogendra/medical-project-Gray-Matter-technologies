"""
E6 · Communication timeline — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E6 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class Message(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e6_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)  # Case this message belongs to
    channel: Mapped[str] = mapped_column(String(200))  # In-app / Email / WhatsApp
    visibility: Mapped[str] = mapped_column(String(200))  # Patient-visible / Internal-only / Clinical
    body: Mapped[str] = mapped_column(String(200))  # Message text
