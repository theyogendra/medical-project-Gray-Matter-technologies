"""
E10 · Integrations — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E10 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class Payment(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e10_payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float)  # Amount in INR
    method: Mapped[str] = mapped_column(String(200))  # Card / UPI
    status: Mapped[str] = mapped_column(String(200))  # Result from the payment gateway (test mode)
    reference: Mapped[str] = mapped_column(String(200))  # Gateway reference
