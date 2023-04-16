import asyncio
from asyncio import Future
from typing import Any

# Словарь с информацией о заказах на пиццу
orders = {}

async def handle_order(
        order_id: int,
        pizza: str,
        quantity: int, future: Future) -> None:
    # Асинхронная операция обработки заказа
    await asyncio.sleep(5)

    # Сохраняем информацию о заказе
    orders[order_id] = {"pizza": pizza, "quantity": quantity}

    # Устанавливаем результат заказа в объект Future
    result = (order_id, orders[order_id])
    future.set_result(result)


async def make_order(order_id: int, pizza: str, quantity: int):
    # Создаем объект Future для получения результата заказа
    order_result = Future()

    # Отправляем заказ на обработку
    asyncio.create_task(handle_order(order_id, pizza, quantity, order_result))

    # Ожидаем результатов заказа
    while not order_result.done():
        print('Ожидаем результата заказа...')
        await asyncio.sleep(1)
    

async def main():
    # Создаем несколько заказов
    order1 = asyncio.create_task(make_order(1, "Маргарита", 2))
    order2 = asyncio.create_task(make_order(2, "Четыре сыра", 1))

    # Ожидаем завершения обработки заказов
    await asyncio.gather(order1, order2)

    # Вывод результатов заказов
    print(orders)


if __name__ == '__main__':
    asyncio.run(main())
