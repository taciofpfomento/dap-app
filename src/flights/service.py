from typing import Protocol

from flights.repository import Repo
from functools import cache

class Svc(Protocol):
    async def Retrieve(self) -> None:
        ...

class _Service(Svc):
    repo: Repo

    def __init__(self, repo: Repo) -> None:
        self.repo = repo

    async def Retrieve(self) -> None:        
        await self.repo.Retrieve()

@cache
def create_service(repo: Repo) -> Svc:
    return _Service(repo=repo)