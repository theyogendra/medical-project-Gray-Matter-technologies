"""
E7 · Patient journey — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E7 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class FamilyLink(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e7_family_links"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)  # Case the family can follow
    contact_name: Mapped[str] = mapped_column(String(200))  # Family member's name
    phone: Mapped[str] = mapped_column(String(200))  # Where the one-time code goes
    active: Mapped[bool] = mapped_column(Boolean)  # False after 'stop sharing'
