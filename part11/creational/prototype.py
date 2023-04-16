from abc import ABC, abstractmethod
from copy import deepcopy

class AbstractCarPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Car(AbstractCarPrototype):
    def __init__(self, maker: str, model: str, year: int):
        self.maker = maker
        self.model = model
        self.year = year

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"{self.maker} {self.model} ({self.year})"

if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2022)
    print(car1)
    car2 = car1.clone()
    print(car2)

    print('*' * 20)
    car2.year = 2023
    print(car1)
    print(car2)
