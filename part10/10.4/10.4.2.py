import asyncio


async def get_name() -> str:
    await asyncio.sleep(1)
    return 'Alex'


async def my_first_coroutine() -> None:
    name = await get_name()
    print(f'Hello, {name}!')


if __name__ == "__main__":
    asyncio.run(my_first_coroutine())
# Hello, Alex!
