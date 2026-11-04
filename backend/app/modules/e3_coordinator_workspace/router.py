"""
E3 · Coordinator workspace — API endpoints (URLs).

Every URL starts with /api/e3. Add endpoints to `router` below; they appear
at http://localhost:8000/docs. Keep each endpoint thin: read the request,
call service.py, return the result.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api/e3", tags=["E3 · Coordinator workspace"])
