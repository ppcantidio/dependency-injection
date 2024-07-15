import httpx

from app.domain.interfaces.gateway_interface import GatewayI


class PokemonGateway(GatewayI):
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get_pokemon(self, number: int):
        url = f"https://pokeapi.co/api/v2/pokemon/{number}"

        resp = await self.client.get(url)
        pokemon = resp.json()

        return pokemon["name"]
