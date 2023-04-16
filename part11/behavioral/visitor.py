from abc import ABC, abstractmethod


class CarElementVisitor(ABC):
    """Интерфейс посетителя"""
    @abstractmethod
    def visit(self, element) -> float:
        ...


class CarElement(ABC):
    """Интерфейс для элементов автомобиля"""
    @abstractmethod
    def accept(self, visitor) -> CarElementVisitor:
        ...


class Engine(CarElement):
    """Класс двигателя"""

    def __init__(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor) -> float:
        return visitor.visit(self)


class Body(CarElement):
    """Класс кузова"""

    def __init__(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor) -> CarElementVisitor:
        return visitor.visit(self)


class NoDiscountVisitor(CarElementVisitor):
    """Расчет стоимости без учета скидки"""

    def visit(self, element) -> float:
        cost = element.get_price()
        return cost


class EngineDiscountVisitor(CarElementVisitor):
    """Расчет стоимости с учетом скидки на двигатель"""

    def visit(self, element) -> float:
        cost = element.get_price()
        if isinstance(element, Engine):
            cost -= cost * 0.15
        return cost


class BodyDiscountVisitor(CarElementVisitor):
    """Расчет стоимости с учетом скидки на кузов"""

    def visit(self, element) -> float:
        cost = element.get_price()
        if isinstance(element, Body):
            cost -= cost * 0.35
        return cost


class AllDiscountVisitor(CarElementVisitor):
    """Расчет стоимости с учетом скидки на все элементы"""

    def visit(self, element) -> float:
        cost = element.get_price()
        cost -= cost * 0.20
        return cost


class CarAssembler:
    def __init__(self, discount: CarElementVisitor):
        self.car_elements: list[CarElement] = []
        self.discount_calculator = discount

    def set_car_elements(self, car_elements: list[CarElement]) -> None:
        self.car_elements = car_elements

    def set_discount(self, discount: CarElementVisitor) -> None:
        self.discount_calculator = discount

    def calculate_total_cost(self) -> float:
        price = 0
        if self.car_elements:
            for element in self.car_elements:
                price += element.accept(self.discount_calculator)
        return price


if __name__ == "__main__":
    car_elements: list[CarElement] = [Engine(15000),
                                      Body(30000)]

    discount = NoDiscountVisitor()
    assembler = CarAssembler(discount)
    assembler.set_car_elements(car_elements)
    print(f"Стоимость без учета скидок: {assembler.calculate_total_cost()}")

    discount = EngineDiscountVisitor()
    assembler.set_discount(discount)
    print(
        f"Стоимость с учетом скидки на двигатель: {assem-bler.calculate_total_cost()}")

    discount = BodyDiscountVisitor()
    assembler.set_discount(discount)
    print(
        f"Стоимость с учетом скидки на кузов: {assem-bler.calculate_total_cost()}")

    discount = AllDiscountVisitor()
    assembler.set_discount(discount)
    print(
        f"Стоимость с учетом скидки на все элементы: {assem-bler.calculate_total_cost()}")
