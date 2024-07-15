import asyncio
import time

from app.domain.commands import GetPokemonsCmd
from app.domain.services.bootstrap import bootstrap_usecase

start_time = time.time()

cmd = GetPokemonsCmd(quantity=100)


async def main():
    result = await bootstrap_usecase(cmd)
    print(result)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
