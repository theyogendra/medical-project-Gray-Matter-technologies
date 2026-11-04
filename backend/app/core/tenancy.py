"""
Company separation ("tenancy") — the most important rule in IPJ-OS:
one company must NEVER see another company's data.

How every module follows it:
1. Tables holding company data inherit `TenantMixin` -> they get a `company_id` column.
2. Endpoints ask for `company_id: int = Depends(get_company_id)`.
3. Service functions filter every query by that company_id.
"""

from fastapi import Header
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column


class TenantMixin:
    """Add to every table that stores a company's data."""

    company_id: Mapped[int] = mapped_column(Integer, index=True)


def get_company_id(x_company_id: int = Header(default=1, ge=1)) -> int:
    """
    Which company is making this request?

    TEMPORARY: read from the `X-Company-Id` header (default 1) so everyone can build
    before login exists. E0 (sign-up and login) will replace the body of this function
    with "the company of the logged-in user". Because every module calls this one
    function, that change happens in exactly one place.
    """
    return x_company_id
