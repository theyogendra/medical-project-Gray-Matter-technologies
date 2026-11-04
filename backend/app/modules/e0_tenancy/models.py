"""
E0 · Tenancy and onboarding — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E0 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin


# Company is the tenant itself, so it has no company_id column.
class Company(TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e0_companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))  # Company display name
    plan: Mapped[str] = mapped_column(String(200))  # Free / Practice / Desk (E0-02)
