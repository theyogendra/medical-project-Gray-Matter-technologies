"""
E2 · Document vault — API endpoints (URLs).

Every URL starts with /api/e2. Add endpoints to `router` below; they appear
at http://localhost:8000/docs. Keep each endpoint thin: read the request,
call service.py, return the result.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/e2", tags=["E2 · Document vault"])
