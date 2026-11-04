"""
E1 · Case management core — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E1 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class Case(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e1_cases"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(200))  # Readable case reference (E1-02 will auto-generate it)
    patient_name: Mapped[str] = mapped_column(String(200))  # Patient full name
    country: Mapped[str] = mapped_column(String(200))  # Patient's home country
    stage: Mapped[str] = mapped_column(String(200))  # Current stage (E1-07 adds the full stage list)
    owner_name: Mapped[str] = mapped_column(String(200))  # One owner per case (E1-03)
