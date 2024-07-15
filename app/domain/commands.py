from abc import ABC
from dataclasses import dataclass


@dataclass
class CommandABC(ABC):
    pass


@dataclass
class GetPokemonsCmd(CommandABC):
    quantity: int
