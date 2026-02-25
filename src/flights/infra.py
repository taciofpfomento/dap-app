from functools import cache
from asyncpg.pool import Pool, create_pool

from settings import get_settings

async def create_db_pool() -> Pool:
    dsn=get_settings().flight_db_dsn
    return create_pool(dsn=dsn)