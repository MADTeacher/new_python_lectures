import os

from prettytable import PrettyTable

import database.pizza_crud as crud


def create_pizza():
    print('Добавить новую пиццу')
    name = input('Введите название: ')
    price = float(input('Введите цену: '))
    description = input('Введите описание: ')
    crud.add_pizza(name, description, price)
    print('Пицца успешно добавлена!!!')


def delete_pizza():
    show_pizzas()
    pizza_id = int(input('Введите id пиццы: '))
    crud.delete_pizza(pizza_id)
    print('Пицца успешно удалена!!!')


def show_pizzas():
    table = PrettyTable(["ID", "Name", "Description", "Price"])
    pizzas = crud.get_pizzas()
    for pizza in pizzas:
        table.add_row(pizza)
    print(table)


def change_pizza_name():
    show_pizzas()
    pizza_id = int(input('Введите id пиццы: '))
    new_name = input('Введите новое название: ')
    crud.change_pizza_name(pizza_id, new_name)
    print('Пицца успешно изменена!!!')


def change_pizza_price():
    show_pizzas()
    pizza_id = int(input('Введите id пиццы: '))
    new_price = float(input('Введите новую цену: '))
    crud.change_pizza_price(pizza_id, new_price)
    print('Пицца успешно изменена!!!')


def change_pizza_description():
    show_pizzas()
    pizza_id = int(input('Введите id пиццы: '))
    new_description = input('Введите новое описание: ')
    crud.change_pizza_description(pizza_id, new_description)
    print('Пицца успешно изменена!!!')


def show_sort_pizzas_by_price():
    pizzas = crud.get_sort_pizzas_by_price()
    table = PrettyTable(["ID", "Name", "Description", "Price"])
    for pizza in pizzas:
        table.add_row(pizza)
    print(table)


def show_pizzas_by_price():
    price = float(input('Введите цену: '))
    pizzas = crud.get_pizzas_by_price(price)
    table = PrettyTable(["ID", "Name", "Description", "Price"])
    for pizza in pizzas:
        table.add_row(pizza)
    print(table)


def create_pizza_menu():
    items = [
        'Добавить новую пиццу',
        'Удалить пиццу',
        'Вывести список пицц',
        'Сортировка пицц по цене',
        'Вывести пиццы, которы >= заданной цене',
        'Изменить название пиццы',
        'Изменить стоимость пиццы',
        'Изменить описание пиццы',
        'Назад'
    ]

    while True:
        print('!!!Пиццы!!!')
        for index, item in enumerate(items):
            print(f'{index}. {item}')

        choice = int(input('Выберите пункт меню: '))
        match choice:
            case 0:
                os.system('cls')
                create_pizza()
            case 1:
                os.system('cls')
                delete_pizza()
            case 2:
                os.system('cls')
                show_pizzas()
            case 3:
                os.system('cls')
                show_sort_pizzas_by_price()
            case 4:
                os.system('cls')
                show_pizzas_by_price()
            case 5:
                os.system('cls')
                change_pizza_name()
            case 6:
                os.system('cls')
                change_pizza_price()
            case 7:
                os.system('cls')
                change_pizza_description()
            case 8:
                break
            case _:
                os.system('cls')
                print('Неверный ввод')
                continue
