import random

from faker import Faker

from loader.worker_loader import create_json_worker_loader
from models.manager import Manager
from models.waiter import Waiter
from models.driver import Driver
from models.employee import Employee


if __name__ == '__main__':
    worker_loader = create_json_worker_loader()

    fake = Faker()
    employee_list: list[Employee] = []
    auto_type_list = ['Lada', 'Kamaz', 'Oka']
    employee_type = [1, 2]
    for i in range(20):
        if random.choice(employee_type) == 1:
            employee_list.append(Driver(
                fake.name(),
                random.choice(auto_type_list),
                i,
                20 + i
            ))
        else:
            employee_list.append(Waiter(
                fake.name(),
                i,
                20 + i
            ))

    manager = Manager("Alex", 89, 44, employee_list)
    manager.delete_employee(18)
    manager.delete_employee(1)
    worker_loader.save_employee(manager, 'Manager_Alex')
    manager = worker_loader.load_manager('Manager_Alex.json')
    for index, it in enumerate(manager.employee_list):
        print(it, f'salary: {it.get_salary()}')
