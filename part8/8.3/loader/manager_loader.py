import json
from typing import Any

from models.driver import Driver
from models.employee import Employee
from loader.employee_loader import EmployeeLoader
from models.manager import Manager
from models.waiter import Waiter


class ManagerJsonLoader(EmployeeLoader):

    def load(self, path: str) -> Employee | Manager:
        with open(path) as json_file:
            employee_list: list[Employee] = []
            data = json.load(json_file)
            workers: list[dict[str, Any]] = data['employee_list']
            for it in workers:
                employee: Employee | None = None
                match it['type']:
                    case 'driver':
                        employee = Driver(
                            it['name'],
                            it['auto'],
                            it['id'],
                            it['age']
                        )
                    case 'waiter':
                        employee = Waiter(
                            it['name'],
                            it['id'],
                            it['age']
                        )
                if employee is not None:
                    employee_list.append(employee)

            return Manager(
                data['name'],
                data['id'],
                data['age'],
                employee_list
            )

    def save(self, employee: Employee, path: str) -> None:
        with open(f'{path}.json', 'w') as json_file:
            json_file.write(
                json.dumps(
                    employee,
                    default=lambda x: x.__dict__, indent=4)
            )


class ManagerTxtLoader(EmployeeLoader):

    def load(self, path: str) -> Employee | Manager:
        with open(path) as txt_file:
            employee_list: list[Employee] = []
            data = txt_file.readline().split('|')
            name = data[0]
            employee_id = int(data[1])
            age = int(data[2])
            while True:
                line = txt_file.readline()
                if not line:
                    break
                worker_data = line.split('|')
                employee: Employee | None = None
                match worker_data[0]:
                    case 'driver':
                        employee = Driver(
                            worker_data[1],
                            worker_data[2],
                            int(worker_data[3]),
                            int(worker_data[4])
                        )
                    case 'waiter':
                        employee = Waiter(
                            worker_data[1],
                            int(worker_data[2]),
                            int(worker_data[3]),
                        )
                if employee is not None:
                    employee_list.append(employee)

            return Manager(
                name,
                employee_id,
                age,
                employee_list
            )

    def save(self, employee: Employee, path: str) -> None:
        with open(f'{path}.txt', 'w') as txt_file:
            if isinstance(employee, Manager):
                data = f'{employee.name}|'
                data += f'{employee.id}|{employee.age}\n'
                txt_file.write(data)
                for it in employee.employee_list:
                    data = ''
                    if isinstance(it, Driver):
                        data = f'{it.type}|'
                        data += f'{it.name}|{it.auto}|'
                        data += f'{it.id}|{it.age}\n'
                    if isinstance(it, Waiter):
                        data = f'{it.type}|{it.name}|'
                        data += f'{it.id}|{it.age}\n'
                    txt_file.write(data)
