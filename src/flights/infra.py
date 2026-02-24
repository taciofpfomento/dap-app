from functools import cache
from asyncpg.pool import Pool, create_pool

from settings import get_settings

@cache
def create_db_pool() -> Pool:
    return create_pool(
        dsn=get_settings().flight_db_dsn
    )