from threading import Thread
from queue import Queue


class Pizzeria:
    def __init__(self) -> None:
        self.order_queue: Queue[str|None] = Queue()

    def take_order(self, order: str) -> None:
        self.order_queue.put(order)
        print(f"Принята заказ: {order}")

    def cook_pizza(self) -> None:
        while True:
            order = self.order_queue.get()
            if order is None:
                break

            print(f"Повар начинает готовить пиццу {order}")
            self.order_queue.task_done()


def serve_clients(pizzeria: Pizzeria, orders: list[str]) -> None:
    threads = []

    for order in orders:
        t = Thread(target=pizzeria.take_order, args=(order,))
        threads.append(t)
        t.start()

    cook_thread = Thread(target=pizzeria.cook_pizza)
    cook_thread.start()

    for t in threads:
        t.join()

    pizzeria.order_queue.join()
    pizzeria.order_queue.put(None)
    cook_thread.join()


if __name__ == '__main__':
    orders = [
        "Маргарита",
        "Пепперони",
        "Гавайская",
        "Сицилийская",
    ]
    pizzeria = Pizzeria()
    serve_clients(pizzeria, orders)
