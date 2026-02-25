
from typing import Protocol
from asyncpg.pool import Pool
from functools import cache


class Repo(Protocol):
  def Retrieve(self, id: int) -> dict:
    pass
  
class _Repository(Repo):
    db_pool: Pool
    
    def __init__(self, db_pool: Pool) -> None:
      self.db_pool = db_pool

    async def Retrieve(self, id: int) -> dict:
      result = {}
      async with self.db_pool as pool:
        async with pool.acquire() as conn:
            records = await conn.fetch("""SELECT * FROM bookings.flights WHERE flight_id = $1""", id)

      if len(records) == 0:
         return {}
      
      result = dict(records[0])

      return result

@cache
def create_repo(pool: Pool) -> Repo:
    return _Repository(db_pool=pool)