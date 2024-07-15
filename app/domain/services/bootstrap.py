from typing import Any

import httpx

from app.domain.commands import CommandABC, GetPokemonsCmd
from app.domain.interfaces.gateway_interface import GatewayI
from app.domain.services.dependency_service import DependencyService
from app.domain.usecases.get_pokemons import GetPokemons


async def bootstrap_usecase(cmd: CommandABC) -> Any:
    usecase = USECASES[type(cmd)]
    deps = DependencyService.get_dependencies(usecase)

    has_gateway_as_a_dependency = any(
        issubclass(dep, GatewayI) for dep in deps.values()
    )
    if has_gateway_as_a_dependency:
        async with httpx.AsyncClient() as client:
            usecase_instance = DependencyService.inject_dependencies(
                usecase, deps, client
            )
            return await usecase_instance.execute(cmd)

    usecase_instance = DependencyService.inject_dependencies(usecase)
    return usecase_instance.execute(cmd)


USECASES = {GetPokemonsCmd: GetPokemons}
