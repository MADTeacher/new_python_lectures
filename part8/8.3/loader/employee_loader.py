from abc import ABC, abstractmethod

from models.employee import Employee


class EmployeeLoader(ABC):

    @abstractmethod
    def load(self, path: str) -> Employee:
        ...

    @abstractmethod
    def save(self, employee: Employee, path: str) -> None:
        ...
