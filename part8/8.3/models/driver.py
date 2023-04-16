from models.employee import Employee


class Driver(Employee):

    def __init__(self, name: str,
                 auto_type: str,
                 id_employee: int,
                 age: int = 20) -> None:
        super().__init__(name, id_employee, 'driver', age)
        self.auto = auto_type

    def get_salary(self) -> int:
        return (self.id + self.age) * 2

    def __repr__(self) -> str:
        return_str = f'{self.name} is Driver, id: {self.id},'
        return_str += f' age: {self.age}, auto: {self.auto}'
        return return_str
