from typing import Protocol

from flights.repository import Repo
from functools import cache

class Svc(Protocol):
    async def Retrieve(self, id: int) -> dict:
        ...

class _Service(Svc):
    repo: Repo

    def __init__(self, repo: Repo) -> None:
        self.repo = repo

    async def Retrieve(self, id: int) -> dict:        
        return await self.repo.Retrieve(id)

@cache
def create_service(repo: Repo) -> Svc:
    return _Service(repo=repo)