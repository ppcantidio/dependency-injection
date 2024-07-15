import asyncio

from app.domain.commands import GetPokemonsCmd
from app.domain.interfaces.usecase_interface import UseCaseI
from app.domain.results import GetPokemonsResult
from app.infra.gateways.pokemon_gateway import PokemonGateway


class GetPokemons(UseCaseI):
    def __init__(self, pokemon_gateway: PokemonGateway):
        self.pokemon_gateway = pokemon_gateway

    async def execute(self, cmd: GetPokemonsCmd) -> GetPokemonsResult:
        coroutines = [
            self.pokemon_gateway.get_pokemon(i + 1) for i in range(cmd.quantity)
        ]
        pokemons = await asyncio.gather(*coroutines)
        result = GetPokemonsResult(pokemons=pokemons, total=len(pokemons))
        return result
