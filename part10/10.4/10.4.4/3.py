import asyncio
from asyncio import Future, Queue


class Pizza:
    def __init__(self, name: str, cooking_time: float):
        self.name = name
        self.cooking_time = cooking_time

    def __str__(self):
        return self.name


async def cook_pizza(pizza: Pizza) -> str:
    await asyncio.sleep(pizza.cooking_time)
    return f"Пицца '{pizza}' готова!"


async def handle_order(order: list[Pizza], queue: Queue) -> None:
    for pizza in order:
        future = Future()
        await queue.put((pizza, future))
        result = await future
        print(result)


async def process_orders(queue: Queue) -> None:
    while True:
        pizza, future = await queue.get()
        print(f"Начинаем готовить пиццу '{pizza}'")
        result = await cook_pizza(pizza)
        future.set_result(result)
        queue.task_done()


async def main():
    margherita = Pizza("Маргарита", 5)
    pepperoni = Pizza("Пепперони", 7)
    hawaiian = Pizza("Гавайская", 6)

    order: list[Pizza] = [margherita, pepperoni, hawaiian]

    queue = Queue()
    order_handling_task = asyncio.create_task(handle_order(order, queue))

    processing_task = asyncio.create_task(process_orders(queue))

    await order_handling_task
    await queue.join()
    processing_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
