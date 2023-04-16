import os

from menu.employee import create_employee_menu
from menu.orders import create_orders_menu
from menu.pizza import create_pizza_menu


def create_main_menu() -> None:
    items = [
        'Сотрудники',
        'Заказы',
        'Асортимент пицц',
        'Выход'
    ]

    while True:
        print('!!!Главное меню!!!')
        for index, item in enumerate(items):
            print(f'{index}. {item}')

        choice = int(input('Выберите пункт меню: '))
        match choice:
            case 0:
                os.system('cls')
                create_employee_menu()
            case 1:
                os.system('cls')
                create_orders_menu()
            case 2:
                os.system('cls')
                create_pizza_menu()
            case 3:
                break
            case _:
                print('Неверный ввод')
                continue
        os.system('cls')
