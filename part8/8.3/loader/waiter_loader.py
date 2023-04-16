import json

from loader.employee_loader import EmployeeLoader
from models.employee import Employee
from models.waiter import Waiter


class WaiterJsonLoader(EmployeeLoader):

    def load(self, path: str) -> Employee | Waiter:
        with open(path) as json_file:
            data = json.load(json_file)
            return Waiter(
                data['name'],
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


class WaiterTxtLoader(EmployeeLoader):

    def load(self, path: str) -> Employee | Waiter:
        with open(path) as txt_file:
            data = txt_file.readline().split('|')
            return Waiter(
                data[0],
                int(data[1]),
                int(data[2])
            )

    def save(self, employee: Employee, path: str) -> None:
        with open(f'{path}.txt', 'w') as txt_file:
            if isinstance(employee, Waiter):
                data = f'{employee.name}|'
                data += f'{employee.id}|{employee.age}'
                txt_file.write(data)


if __name__ == '__main__':
    waiter_json_loader = WaiterJsonLoader()
    waiter_txt_loader = WaiterTxtLoader()

    waiter1 = Waiter('Иван', 1, 20)
    waiter2 = Waiter('Пётр', 2, 30)

    waiter_json_loader.save(waiter1, f'{waiter1.name}')
    waiter_txt_loader.save(waiter2, f'{waiter2.name}')

    load_waiter1 = waiter_json_loader.load(f'{waiter1.name}.json')
    print(f'load_waiter1: {load_waiter1}')
    load_waiter2 = waiter_txt_loader.load(f'{waiter2.name}.txt')
    print(f'load_waiter2: {load_waiter2}')