import os

from prettytable import PrettyTable

import database.employee_crud as crud


def create_employee():
    name = input('Введите имя: ')
    position = input('Введите должность: ')
    employee_id = crud.add_employee(name, position)
    start_time = input('Введите время начала работы (HH:MM): ')
    end_time = input('Введите время окончания работы (HH:MM): ')
    crud.add_shift(employee_id, start_time, end_time)
    print('Сотрудник успешно добавлен!!!')


def show_employees():
    employees = crud.get_employees_with_shifts()
    table = PrettyTable(["Employee ID", "Name", "Position", "Start Time", "End Time"])
    for employee in employees:
        table.add_row(employee)
    print(table)


def delete_employee():
    employees = crud.get_employees()
    table = PrettyTable(["Employee ID", "Name", "Position"])
    for employee in employees:
        table.add_row(employee)
    print(table)
    employee_id = int(input('Введите ID сотрудника, которого хотите удалить: '))
    crud.delete_employee(employee_id)
    crud.delete_shift(employee_id)
    print('Сотрудник успешно удален!!!')


def create_employee_menu():
    items = [
        'Добавить нового сотрудника',
        'Удалить сотрудника',
        'Вывести список сотрудников',
        'Назад',
    ]

    while True:
        print('!!!Сотрудники!!!')
        for index, item in enumerate(items):
            print(f'{index}. {item}')
        
        choice = int(input('Выберите пункт меню: '))
        match choice:
            case 0:
                os.system('cls')
                create_employee()
            case 1:
                os.system('cls')
                delete_employee()
            case 2:
                os.system('cls')
                show_employees()
            case 3:
                break
            case _:
                os.system('cls')
                print('Неверный ввод')
                continue
