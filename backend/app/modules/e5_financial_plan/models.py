"""
E5 · Treatment financial plan — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E5 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class EstimateLine(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e5_estimate_lines"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)  # Case this estimate is for
    group_name: Mapped[str] = mapped_column(String(200))  # One of the 4 estimate groups
    label: Mapped[str] = mapped_column(String(200))  # What the line is for
    min_amount: Mapped[float] = mapped_column(Float)  # Minimum cost (INR)
    likely_amount: Mapped[float] = mapped_column(Float)  # Likely cost (INR)
    certainty: Mapped[str] = mapped_column(String(200))  # Certainty label
