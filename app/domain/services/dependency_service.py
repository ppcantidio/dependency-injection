import inspect
from typing import Any, Optional, Type

import httpx

from app.domain.interfaces.gateway_interface import GatewayI
from app.domain.interfaces.usecase_interface import UseCaseI
from app.infra.gateways.pokemon_gateway import PokemonGateway


class DependencyService:
    @staticmethod
    def get_dependencies(module: Type[UseCaseI]) -> dict:
        deps = {}
        params = inspect.signature(module).parameters
        for name, dependency in DEPENDENCIES.items():
            if name in params:
                deps[name] = dependency
        return deps

    @staticmethod
    def inject_dependencies(
        module: Type[UseCaseI],
        deps: Optional[Type[Any]] = None,
        client: Optional[httpx.AsyncClient] = None,
    ) -> Any:
        if deps is None:
            deps = DependencyService.get_dependencies(module)

        for name, dependency in deps.items():
            if issubclass(dependency, GatewayI):
                if client is None:
                    raise ValueError("Client is required for gateway dependencies")
                deps[name] = dependency(client)

        return module(**deps)


DEPENDENCIES = dict(
    pokemon_gateway=PokemonGateway,
)
