from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name: str,
                 id_employee: int, empl_type: str,
                 age: int = 20) -> None:
        self.name = name
        self.id = id_employee
        self.age = age
        self.type = empl_type

    def get_age(self) -> int:
        return self.age

    def __repr__(self) -> str:
        return f'{self.name}, id: {self.id}, age: {self.age}'

    @abstractmethod
    def get_salary(self) -> int:
        ...
