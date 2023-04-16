from abc import ABC, abstractmethod
from typing import TypeVar

ProductType = TypeVar("ProductType", bound="Product")

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Результат работы объекта ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Результат работы объекта ConcreteProductB"

class Creator(ABC):
    @abstractmethod
    def create_product(self) -> ProductType:
        pass

class ConcreteCreatorA(Creator):
    def create_product(self) -> ConcreteProductA:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def create_product(self) -> ConcreteProductB:
        return ConcreteProductB()

def client_code(creator: Creator) -> None:
    product = creator.create_product()
    print(product.operation())

if __name__ == "__main__":
    client_code(ConcreteCreatorA())
    client_code(ConcreteCreatorB())
