from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name: str,
                 id_employee: int,
                 age: int) -> None:
        self.__name = name
        self.__id = id_employee
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def increment_age(self) -> None:
        self.__age += 1

    @property
    def id_employee(self) -> int:
        return self.__id

    @abstractmethod
    def get_salary(self) -> int:
        ...

    def __repr__(self) -> str:
        return f'{self.__name}, id: {self.__id}, age: {self.__age}'
