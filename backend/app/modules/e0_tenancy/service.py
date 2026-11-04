"""
E0 · Tenancy and onboarding — business rules.

A "company" is one medical-travel business using IPJ-OS (a tenant).
Everything else in the product belongs to exactly one company.
Other modules call get_company() — never query the companies table directly.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Company
from .schemas import CompanyCreate


def get_company(db: Session, company_id: int) -> Company | None:
    """The company with this id, or None."""
    return db.get(Company, company_id)


def create_company(db: Session, data: CompanyCreate) -> Company:
    """Sign-up step: create a new company (E0-01 will add the first user + email check)."""
    company = Company(**data.model_dump())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def ensure_demo_company(db: Session) -> Company:
    """
    Make sure company #1 exists so everyone can try the app before login is built.
    Called once when the server starts (see app/main.py).
    """
    first = db.scalars(select(Company).order_by(Company.id).limit(1)).first()
    if first is not None:
        return first
    return create_company(db, CompanyCreate(name="Demo Company", plan="Free"))
