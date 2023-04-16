from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class CarDecorator(Car):
    def __init__(self, car: Car) -> None:
        self._car = car


class BasicCar(Car):
    def cost(self) -> int:
        return 1000000

    def description(self) -> str:
        return "Базовый автомобиль"


class AirConditioning(CarDecorator):
    def cost(self) -> int:
        return self._car.cost() + 20000

    def description(self) -> str:
        return self._car.description() + ", кондиционер"


class SafetySystem(CarDecorator):
    def cost(self) -> int:
        return self._car.cost() + 30000

    def description(self) -> str:
        return self._car.description() + ", система безопасности"


class NavigationSystem(CarDecorator):
    def cost(self) -> int:
        return self._car.cost() + 25000

    def description(self) -> str:
        return self._car.description() + ", система навигации"


if __name__ == "__main__":
    car = BasicCar()
    print(car.description())
    print(f"Стоимость: {car.cost()}")

    car_with_ac = AirConditioning(car)
    print(car_with_ac.description())
    print(f"Стоимость: {car_with_ac.cost()}")

    car_with_safety = SafetySystem(car_with_ac)
    print(car_with_safety.description())
    print(f"Стоимость: {car_with_safety.cost()}")

    car_with_all = NavigationSystem(car_with_safety)
    print(car_with_all.description())
    print(f"Стоимость: {car_with_all.cost()}")
