from fastapi.responses import JSONResponse
from fastapi import APIRouter

health_router = APIRouter()

@health_router.get("/health")
def health() -> JSONResponse:
  return JSONResponse()