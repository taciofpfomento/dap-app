from functools import cache
from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from health.router import health_router
from flights.router import flights_router
from settings import get_settings

_app = FastAPI()

def _load_routers() -> None:
    _app.include_router(health_router)
    _app.include_router(flights_router)

def main() -> None:
   _load_routers()
   uvicorn.run(_app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()