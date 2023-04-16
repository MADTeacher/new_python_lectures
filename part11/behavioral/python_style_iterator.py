from typing import Iterator


class Car:
    def __init__(self, model: str) -> None:
        self._model = model

    def get_model(self) -> str:
        return self._model


class CarIterator(Iterator):
    def __init__(self, cars: list[Car]) -> None:
        self._cars = cars
        self._index = 0

    def __next__(self) -> Car:
        if self._index >= len(self._cars):
            raise StopIteration()
        car = self._cars[self._index]
        self._index += 1
        return car


class CarList:
    def __init__(self) -> None:
        self._cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        self._cars.append(car)

    def __iter__(self) -> CarIterator:
        return CarIterator(self._cars)


if __name__ == '__main__':
    car_list = CarList()
    car_list.add_car(Car("Toyota"))
    car_list.add_car(Car("Nissan"))
    car_list.add_car(Car("Mazda"))
    car_list.add_car(Car("BMW"))
    car_list.add_car(Car("Ford"))
    car_list.add_car(Car("Honda"))

    for car in car_list:
        print(car.get_model(), end=' ')
