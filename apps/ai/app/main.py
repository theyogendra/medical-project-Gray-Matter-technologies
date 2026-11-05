from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Medical AI Service", version="1.0.0")


class HealthResponse(BaseModel):
    status: str
    service: str
    environment: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="medical-ai-service",
        environment="development",
    )


@app.get("/")
def root() -> dict:
    return {"message": "Medical AI service is ready."}
