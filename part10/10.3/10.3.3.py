from multiprocessing import Process, Queue
import time

def cook_pizza(queue: Queue) -> None:
    pizza_names = ["Маргарита", "Пепперони", "Гавайская", "Четыре се-зона"]
    for pizza in pizza_names:
        print(f"Начинаю готовить пиццу {pizza}...")
        time.sleep(5)  # Имитация времени готовки пиццы
        print(f"Пицца {pizza} готова!")
        queue.put(pizza)

def deliver_pizza(queue: Queue) -> None:
    while True:
        pizza = queue.get()
        if pizza is None:
            break
        print(f"Начинаю доставлять пиццу {pizza}...")
        time.sleep(3)  # Имитация времени доставки пиццы
        print(f"Пицца {pizza} доставлена!")

if __name__ == "__main__":
    pizza_queue = Queue()

    cook_process = Process(target=cook_pizza, args=(pizza_queue,))
    delivery_process = Process(target=deliver_pizza, args=(pizza_queue,))

    cook_process.start()
    delivery_process.start()

    cook_process.join()

    # Отправляем специальный сигнал остановки процессу доставки
    pizza_queue.put(None)
    delivery_process.join()
