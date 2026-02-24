
from typing import Protocol
from asyncpg.pool import Pool


class Repo(Protocol):
  def Retrieve(self) -> None:
    pass
  
class _Repository(Repo):
    def __init__(self, db_pool: Pool) -> None:
      self.db_pool = db_pool

    async def Retrieve(self) -> None:
      async with self.db_pool as pool:
        async with pool.acquire() as conn:
          result = await conn.fetch('SELECT * FROM bookings.flights WHERE flight_id = $1', 1)
          print(result)

def create_repo(pool: Pool) -> Repo:
    return _Repository(db_pool=pool)