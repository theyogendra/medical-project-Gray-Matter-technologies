"""
E0 · Tenancy and onboarding — API endpoints (URLs).

Every URL starts with /api/e0. Add endpoints to `router` below; they appear
at http://localhost:8000/docs. Keep each endpoint thin: read the request,
call service.py, return the result.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/e0", tags=["E0 · Tenancy and onboarding"])
