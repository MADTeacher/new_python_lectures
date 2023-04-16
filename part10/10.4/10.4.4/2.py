import asyncio
from asyncio import Future

class Pizza:
    def __init__(self, name: str, cooking_time: float):
        self.name = name
        self.cooking_time = cooking_time

    def __str__(self):
        return self.name

async def cook_pizza(pizza: Pizza) -> str:
    await asyncio.sleep(pizza.cooking_time)
    return f"Пицца '{pizza}' готова!"

async def handle_order(order: list[Pizza]) -> list[Future]:
    pizza_futures: list[Future] = []
    for pizza in order:
        future: asyncio.Future = asyncio.ensure_future(cook_pizza(pizza))
        pizza_futures.append(future)
    return pizza_futures

async def main():
    margherita = Pizza("Маргарита", 5)
    pepperoni = Pizza("Пепперони", 7)
    hawaiian = Pizza("Гавайская", 6)

    order: list[Pizza] = [margherita, pepperoni, hawaiian]

    pizza_futures = await handle_order(order)

    for future in pizza_futures:
        print(await future)

if __name__ == "__main__":
    asyncio.run(main())
