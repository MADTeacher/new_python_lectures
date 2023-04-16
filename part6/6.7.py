class Employee:

    def __init__(self, name: str,
                 id_employee: int,
                 age: int = 20) -> None:
        self.name = name
        self.id = id_employee
        self.age = age

    def get_age(self) -> int:
        return self.age

    def get_salary(self) -> int:
        return (self.id + self.age) * 1000

    def __repr__(self) -> str:
        return f'{self.name}, id: {self.id}, age: {self.age}'


class Driver(Employee):

    def __init__(self, name: str,
                 auto_type: str,
                 id_employee: int,
                 age: int = 20,
                 salary_coeff: float = 0.8) -> None:
        super().__init__(name, id_employee, age)
        self.auto = auto_type
        self.salary_coeff = salary_coeff

    def get_salary(self) -> int:
        return int(super().get_salary() * self.salary_coeff)

    def __repr__(self) -> str:
        return_str = f'{self.name} is Driver, id: {self.id},'
        return_str += f' age: {self.age}, auto: {self.auto}'
        return return_str


class Waiter(Employee):

    def __init__(self, name: str,
                 id_employee: int, age: int = 20,
                 salary_coeff: int = 3) -> None:
        super().__init__(name, id_employee, age)
        self.salary_coeff = salary_coeff

    def get_salary(self) -> int:
        return super().get_salary() // self.salary_coeff

    def __repr__(self) -> str:
        return f'{self.name} is Waiter, id: ' \
               f'{self.id}, age: {self.age}'


if __name__ == '__main__':
    employee_list: list[Employee] = [
        Driver('Alex', 'Lada', 12, 45),
        Waiter('Max', 5, 19),
        Waiter('Nikita', 6, 20),
        Driver('Gleb', 'Oka', 11, 34),
    ]

    employee_type = ''
    for it in employee_list:
        if isinstance(it, Driver):
            employee_type = 'Driver'
        if isinstance(it, Waiter):
            employee_type = 'Waiter'
        print(f'{employee_type} {it.name} have salary '
              f'= {it.get_salary()}')
