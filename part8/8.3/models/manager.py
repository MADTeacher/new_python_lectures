from models.employee import Employee


class Manager(Employee):

    def __init__(self, name: str,
                 id_employee: int, age: int,
                 employee_list: list[Employee]) -> None:
        super().__init__(name, id_employee, 'manager', age)
        self.employee_list: list[Employee] = employee_list

    def get_salary(self) -> int:
        return (self.id + self.age) * 4

    def __repr__(self) -> str:
        return f'{self.name} is Manager, id: {self.id}, age: {self.age}'

    def delete_employee(self, employee_id: int) -> None:
        del_employee: Employee | None = None
        for it in self.employee_list:
            if it.id == employee_id:
                del_employee = it
                break
        if del_employee is not None:
            self.employee_list.remove(del_employee)
