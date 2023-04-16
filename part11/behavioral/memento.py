from __future__ import annotations
from typing import Optional


class CarOriginator:
    def __init__(self, speed: int, engine_temperature: float):
        self.speed = speed
        self.engine_temperature = engine_temperature

    def create_memento(self) -> CarMemento:
        return CarMemento(self.speed, self.engine_temperature)

    def restore(self, memento: CarMemento):
        self.speed = memento.speed
        self.engine_temperature = memento.engine_temperature


class CarMemento:
    def __init__(self, speed: int, engine_temperature: float):
        self._speed = speed
        self._engine_temperature = engine_temperature

    @property
    def speed(self) -> int:
        return self._speed

    @property
    def engine_temperature(self) -> float:
        return self._engine_temperature


class CarCaretaker:
    def __init__(self):
        self._mementos = []

    def save_state(self, originator: CarOriginator):
        self._mementos.append(originator.create_memento())

    def restore_state(self, originator: CarOriginator, 
                      index: Optional[int] = -1):
        memento = self._mementos.pop(index)
        originator.restore(memento)


if __name__ == "__main__":
    car = CarOriginator(80, 90.0)
    caretaker = CarCaretaker()

    # Сохраняем текущее состояние автомобиля
    caretaker.save_state(car)
    print(f"Сохранено сост-е автомобиля: скорость {car.speed},"
          f" тем-ра двигателя {car.engine_temperature}")

    # Изменяем состояние автомобиля
    car.speed = 100
    car.engine_temperature = 95.0
    print(f"Изменили сост-е автомобиля: скорость {car.speed}, "
          f"тем-ра двигателя {car.engine_temperature}")

    # Восстанавливаем сохраненное состояние автомобиля
    caretaker.restore_state(car)
    print(f"Восстановлено сост-е автомобиля: скорость {car.speed}, "
          f"тем-ра двигателя {car.engine_temperature}")
