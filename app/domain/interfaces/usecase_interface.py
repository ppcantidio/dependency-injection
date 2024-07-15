from abc import ABC

from app.domain.commands import CommandABC
from app.domain.results import ResultABC


class UseCaseI(ABC):
    async def execute(self, cmd: CommandABC) -> ResultABC:
        pass
