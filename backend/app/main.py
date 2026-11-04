"""
IPJ-OS backend — entry point.

Run from the backend/ folder:
    uvicorn app.main:app --reload
then open http://localhost:8000/docs to see and try every endpoint.

This file only plugs the modules together. Each module's code lives in app/modules/<module>/.
Adding a new module router here is a change to shared code, so the lead reviews it.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import ALLOWED_ORIGINS
from app.core.database import SessionLocal, create_tables
from app.modules.e0_tenancy import service as tenancy_service
from app.modules.e0_tenancy.router import router as e0_router
from app.modules.e1_case_core.router import router as e1_router
from app.modules.e2_document_vault.router import router as e2_router
from app.modules.e3_coordinator_workspace.router import router as e3_router
from app.modules.e4_clinical_review.router import router as e4_router
from app.modules.e5_financial_plan.router import router as e5_router
from app.modules.e6_communication.router import router as e6_router
from app.modules.e7_patient_journey.router import router as e7_router
from app.modules.e8_consent_audit.router import router as e8_router
from app.modules.e9_ai_layer.router import router as e9_router
from app.modules.e10_integrations.router import router as e10_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once when the server starts.
    create_tables()
    with SessionLocal() as db:
        tenancy_service.ensure_demo_company(db)  # company #1, used until login exists
    yield


app = FastAPI(title="IPJ-OS API", version="0.1.0", lifespan=lifespan)

# Lets the Flutter web app (a different port) call this API in development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in (
    e0_router,
    e1_router,
    e2_router,
    e3_router,
    e4_router,
    e5_router,
    e6_router,
    e7_router,
    e8_router,
    e9_router,
    e10_router,
):
    app.include_router(router)


@app.get("/api/health", tags=["System"])
def health() -> dict:
    """Quick check that the server is up."""
    return {"ok": True}
