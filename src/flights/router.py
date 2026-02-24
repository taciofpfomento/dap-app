from fastapi.responses import JSONResponse
from fastapi import APIRouter

from flights.infra import create_db_pool
from flights.repository import create_repo
from flights.service import create_service

_pool = create_db_pool()
_repo= create_repo(pool=_pool)
_svc = create_service(repo=_repo)

flights_router = APIRouter()

@flights_router.get("/flights")
async def get_flight() -> JSONResponse:
  await _svc.Retrieve()

  return JSONResponse()