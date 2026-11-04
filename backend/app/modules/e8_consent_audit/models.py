"""
E8 · Consent and audit — database tables.

One class = one table. One attribute = one column.
This starter table is an EXAMPLE: change the columns to match your approved data plan
(sheet task "Plan the E8 data"), and add more tables below as your tasks need them.
"""

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimestampMixin
from app.core.tenancy import TenantMixin


class Consent(TenantMixin, TimestampMixin, Base):
    # Table names start with the module code so modules never clash.
    __tablename__ = "e8_consents"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(Integer)  # Case the consent is for
    scope: Mapped[str] = mapped_column(String(200))  # Exactly what the patient agreed to
    granted: Mapped[bool] = mapped_column(Boolean)  # False once revoked
