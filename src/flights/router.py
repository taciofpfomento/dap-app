from fastapi import APIRouter
from fastapi.responses import JSONResponse

from flights.infra import create_db_pool
from flights.repository import create_repo
from flights.service import create_service

flights_router = APIRouter()

@flights_router.get("/flights/{id}")
async def get_flight(id: int) -> JSONResponse:
  _pool = await create_db_pool()
  _repo= create_repo(pool=_pool)
  _svc = create_service(repo=_repo)

  return await _svc.Retrieve(id)