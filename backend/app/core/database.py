"""
Database connection, shared by all modules.

- `Base`            every table class inherits from it
- `TimestampMixin`  adds a `created_at` column
- `get_db`          gives each API request its own database session
"""

from collections.abc import Iterator
from datetime import datetime, timezone

from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from app.core.config import DATABASE_URL

# SQLite needs this flag when used from a web server; PostgreSQL does not.
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=_connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Base(DeclarativeBase):
    """Parent class of every table in every module."""


class TimestampMixin:
    """Add to a table to get a `created_at` column filled in automatically."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )


def get_db() -> Iterator[Session]:
    """FastAPI dependency: one session per request, always closed afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables() -> None:
    """
    Create any missing tables (development only).

    Later we switch to migrations (Alembic) so table changes are versioned in git.
    """
    Base.metadata.create_all(bind=engine)
