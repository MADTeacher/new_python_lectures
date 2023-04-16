from models.employee import Employee


class Waiter(Employee):

    def __init__(self, name: str,
                 id_employee: int, age: int = 20) -> None:
        super().__init__(name, id_employee, 'waiter', age)

    def get_salary(self) -> int:
        return self.id + self.age

    def __repr__(self) -> str:
        return f'{self.name} is Waiter, id: {self.id}, age: {self.age}'
