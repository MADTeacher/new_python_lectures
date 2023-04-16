import json

from models.driver import Driver
from models.employee import Employee
from loader.employee_loader import EmployeeLoader


class DriverJsonLoader(EmployeeLoader):

    def load(self, path: str) -> Employee | Driver:
        with open(path) as json_file:
            data = json.load(json_file)
            return Driver(
                data['name'],
                data['auto'],
                data['id'],
                data['age']
            )

    def save(self, employee: Employee, path: str) -> None:
        with open(f'{path}.json', 'w') as json_file:
            json_file.write(
                json.dumps(
                    employee,
                    default=lambda x: x.__dict__, indent=4)
            )


class DriverTxtLoader(EmployeeLoader):

    def load(self, path: str) -> Employee | Driver:
        with open(path) as txt_file:
            data = txt_file.readline().split('|')
            return Driver(
                data[0],
                data[1],
                int(data[2]),
                int(data[3])
            )

    def save(self, employee: Employee, path: str) -> None:
        with open(f'{path}.txt', 'w') as txt_file:
            if isinstance(employee, Driver):
                data = f'{employee.name}|{employee.auto}|'
                data += f'{employee.id}|{employee.age}'
                txt_file.write(data)