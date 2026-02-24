from fastapi.responses import JSONResponse
from fastapi import APIRouter

from flights.infra import create_db_pool
from flights.repository import create_repo
from flights.service import create_service

flights_router = APIRouter()

@flights_router.get("/flights")
async def get_flight() -> JSONResponse:
  pool = create_db_pool()
  svc = create_service(repo=create_repo(pool=pool))

  await svc.Retrieve()

  return JSONResponse()