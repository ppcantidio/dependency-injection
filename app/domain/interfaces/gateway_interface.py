from abc import ABC

import httpx

from app.domain.commands import CommandABC
from app.domain.results import ResultABC


class GatewayI(ABC):
    def __init__(self, client: httpx.AsyncClient):
        self.client = client
