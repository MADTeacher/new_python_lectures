from abc import ABC, abstractmethod
from enum import Enum

class ProductType(Enum):
    A = "A"
    B = "B"

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

def product_factory(product_type: ProductType) -> Product:
    if product_type == ProductType.A:
        return ConcreteProductA()
    elif product_type == ProductType.B:
        return ConcreteProductB()
    else:
        raise ValueError(f"Неизвестный тип продукта: {product_type}")

def client_code(product_type: ProductType) -> None:
    product = product_factory(product_type)
    print(product.operation())

if __name__ == "__main__":
    client_code(ProductType.A)
    client_code(ProductType.B)
