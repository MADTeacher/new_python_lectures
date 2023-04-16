from abc import ABC, abstractmethod
from typing import Iterator


class CarCollection(ABC):
    @abstractmethod
    def iterator(self) -> Iterator:
        pass


class Car:
    def __init__(self, model: str) -> None:
        self._model = model

    def get_model(self) -> str:
        return self._model


class CarList(CarCollection):
    def __init__(self) -> None:
        self._cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        self._cars.append(car)

    def iterator(self) -> Iterator:
        return iter(self._cars)


if __name__ == '__main__':
    car_list = CarList()
    car_list.add_car(Car("Toyota"))
    car_list.add_car(Car("Nissan"))
    car_list.add_car(Car("Mazda"))
    car_list.add_car(Car("BMW"))
    car_list.add_car(Car("Ford"))
    car_list.add_car(Car("Honda"))

    for car in car_list.iterator():
        print(car.get_model())
