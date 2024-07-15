from abc import ABC
from dataclasses import dataclass
from typing import List


@dataclass
class ResultABC(ABC):
    pass


@dataclass
class GetPokemonsResult(ResultABC):
    pokemons: List[str]
    total: int
