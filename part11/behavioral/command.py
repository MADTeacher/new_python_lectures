from abc import ABC, abstractmethod
from typing import Optional


class Car:
    def __init__(self) -> None:
        self._state = "не работает"

    def set_state(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class RepairCommand(Command):
    def __init__(self, car: Car) -> None:
        self._car = car
        self._previous_state: Optional[str] = None

    def execute(self) -> None:
        self._previous_state = self._car.get_state()
        self._car.set_state("ремонт")

    def undo(self) -> None:
        if self._previous_state is not None:
            self._car.set_state(self._previous_state)


class MaintenanceCommand(Command):
    def __init__(self, car: Car) -> None:
        self._car = car
        self._previous_state: Optional[str] = None

    def execute(self) -> None:
        self._previous_state = self._car.get_state()
        self._car.set_state("обслуживание")

    def undo(self) -> None:
        if self._previous_state is not None:
            self._car.set_state(self._previous_state)


class CarService:
    def __init__(self) -> None:
        self._history: list[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo_last_command(self) -> None:
        if self._history:
            last_command = self._history.pop()
            last_command.undo()


if __name__ == "__main__":
    car = Car()
    service = CarService()

    repair_command = RepairCommand(car)
    service.execute_command(repair_command)
    print(car.get_state())  # ремонт

    maintenance_command = MaintenanceCommand(car)
    service.execute_command(maintenance_command)
    print(car.get_state())  # обслуживание

    service.undo_last_command()
    print(car.get_state())  # ремонт

    service.undo_last_command()
    print(car.get_state())  # не работает
