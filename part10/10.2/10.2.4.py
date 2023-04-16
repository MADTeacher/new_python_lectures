import time
from concurrent.futures import ThreadPoolExecutor

def prepare_pizza(order: str) -> str:
    """
    Функция, которая имитирует приготовление пиццы
    """
    print(f"Готовлю пиццу для заказа {order}")
    time.sleep(5)
    print(f"Пицца для заказа {order} готова")
    return order

def pack_pizza(order: str) -> str:
    """
    Функция, которая имитирует упаковку пиццы
    """
    print(f"Упаковываю пиццу для заказа {order}")
    time.sleep(3)
    print(f"Пицца для заказа {order} упакована")
    return order

def deliver_pizza(order: str) -> str:
    """
    Функция, которая имитирует доставку пиццы
    """
    print(f"Доставляю пиццу для заказа {order}")
    time.sleep(2)
    print(f"Пицца для заказа {order} доставлена")
    return order

def process_order(order: str) -> None:
    """
    Функция, которая обрабатывает заказ на пиццу
    """
    print(f"Начинаю обработку заказа {order}")
    prepare_pizza(order)
    pack_pizza(order)
    deliver_pizza(order)
    print(f"Заказ {order} обработан")

if __name__ == "__main__":
    orders = ["1", "2", "3", "4", "5"]
    with ThreadPoolExecutor(max_workers=3) as executor:
        for order in orders:
            executor.submit(process_order, order)
