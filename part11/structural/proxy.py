from abc import ABC, abstractmethod


class CarAccess(ABC):
    @abstractmethod
    def open_door(self, door_number: int) -> str:
        pass


class Car(CarAccess):
    def open_door(self, door_number: int) -> str:
        return f"Дверь номер {door_number} открыта."


class CarProxy(CarAccess):
    def __init__(self, car: Car, access_code: str) -> None:
        self.car = car
        self.access_code = access_code

    def open_door(self, door_number: int) -> str:
        if self.access_code == "SECRET":
            return self.car.open_door(door_number)
        return "Доступ запрещен."


if __name__ == "__main__":
    car = Car()
    car_proxy = CarProxy(car, "SECRET")

    print(car_proxy.open_door(1))  # Дверь номер 1 открыта.
    print(car_proxy.open_door(2))  # Дверь номер 2 открыта.

    car_proxy_wrong_access = CarProxy(car, "WRONG")
    print(car_proxy_wrong_access.open_door(1))  # Доступ запрещен.
