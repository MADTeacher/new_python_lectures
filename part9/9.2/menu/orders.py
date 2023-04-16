import os

from prettytable import PrettyTable

import database.orders_crud as crud
from menu.pizza import show_pizzas


def create_orders():
    name = input("Введите имя заказчика: ")
    phone = input("Введите телефон заказчика: ")
    address = input("Введите адрес заказчика: ")
    order_id = crud.add_order(name, phone, address)
    print('Добавьте пиццу в заказ')
    while True:
        show_pizzas()
        pizza_id = int(input("Выберете номер пиццы: "))
        quantity = int(input("Введите количество пиццы: "))
        crud.add_order_item(pizza_id, order_id, quantity)
        print('Пицца добавлена в заказ. Желаете продолжить? (y/n)')
        if input().lower() == 'y':
            continue
        else:
            break
    print('Заказ сформирован!!!')


def change_orders_status():
    show_orders()
    order_id = int(input('Введите ID заказа: '))
    crud.set_completed_order(order_id)
    print('Заказ выполнен')


def show_current_orders():
    orders = crud.get_current_orders()
    table = PrettyTable(["Order ID", "Is Completed", "Name", "Phone", "Address"])
    for order in orders:
        table.add_row(order)
    print(table)


def show_completed_orders():
    orders = crud.get_completed_orders()
    table = PrettyTable(["Order ID", "Is Completed", "Name", "Phone", "Address"])
    for order in orders:
        table.add_row(order)
    print(table)


def show_order_info():
    show_orders()
    order_id = int(input('Введите ID заказа: '))
    orders = crud.get_orders_with_pizzas(order_id)
    table = PrettyTable(
        [
            "Order ID",
            "is_completed",
            "Customer Name",
            "Phone",
            "Address",
            "Pizza",
            "Quantity",
        ]
    )
    for order in orders:
        table.add_row(order)
    print(table)


def show_orders() -> None:
    orders = crud.get_orders()
    table = PrettyTable(["Order ID", "Is Completed", "Name", "Phone", "Address"])
    for order in orders:
        table.add_row(order)
    print(table)


def create_orders_menu() -> None:
    items = [
        'Добавить заказ',
        'Изменить статус заказа',
        'Показать тещие заказы',
        'Показать подробности заказа',
        'Показать выполненные заказы',
        'Назад'
    ]
    
    while True:
        print('!!!Меню заказов!!!')
        for index, item in enumerate(items):
            print(f'{index}. {item}')
        
        choice = int(input('Выберите пункт меню: '))
        match choice:
            case 0:
                os.system('cls')
                create_orders()
            case 1:
                os.system('cls')
                change_orders_status()
            case 2:
                os.system('cls')
                show_current_orders()
            case 3:
                os.system('cls')
                show_order_info()
            case 4:
                os.system('cls')
                show_completed_orders()
            case 5:
                break
            case _:
                os.system('cls')
                print('Неверный ввод')
                continue
