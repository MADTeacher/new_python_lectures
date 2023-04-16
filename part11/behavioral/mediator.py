from abc import ABC, abstractmethod
from typing import Optional


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Optional["Colleague"], event: str) -> None:
        pass


class Colleague(ABC):
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

    def notify_mediator(self, event: str) -> None:
        self._mediator.notify(self, event)


class CarMediator(Mediator):
    def __init__(self) -> None:
        self._engine = Engine(self)
        self._transmission = Transmission(self)
        self._cooling_system = CoolingSystem(self)
        self._speed_sensor = SpeedSensor(self)
        self._cruise_control_enabled = False

    def notify(self, sender: Optional[Colleague], event: str) -> None:
        if event == "cruise_control_enabled":
            self._cruise_control_enabled = True
            self._engine.set_cruise_speed()
            self._transmission.set_cruise_mode()
            self._cooling_system.start_cooling()
        elif event == "cruise_control_disabled":
            self._cruise_control_enabled = False
            self._engine.reset_cruise_speed()
            self._transmission.reset_cruise_mode()
            self._cooling_system.stop_cooling()
        elif event == "speed_changed" and self._cruise_control_enabled:
            current_speed = self._speed_sensor.get_speed()
            self._engine.adjust_speed(current_speed)


class Engine(Colleague):
    def set_cruise_speed(self) -> None:
        print("Установлена скорость круиз-контроля")

    def reset_cruise_speed(self) -> None:
        print("Скорость круиз-контроля сброшена")

    def adjust_speed(self, current_speed: int) -> None:
        print(f"Скорость двигателя скорректирована: {current_speed}")


class Transmission(Colleague):
    def set_cruise_mode(self) -> None:
        print("Трансмиссия переключена в режим круиз-контроля")

    def reset_cruise_mode(self) -> None:
        print("Трансмиссия вышла из режима круиз-контроля")


class CoolingSystem(Colleague):
    def start_cooling(self) -> None:
        print("Система охлаждения включена")

    def stop_cooling(self) -> None:
        print("Система охлаждения выключена")


class SpeedSensor(Colleague):
    def __init__(self, mediator: Mediator) -> None:
        super().__init__(mediator)
        self._speed = 0

    def change_speed(self, new_speed: int) -> None:
        self._speed = new_speed
        self.notify_mediator("speed_changed")

    def get_speed(self) -> int:
        return self._speed


if __name__ == "__main__":
    car_mediator = CarMediator()
    speed_sensor = car_mediator._speed_sensor
    # Включаем круиз-контроль
    car_mediator.notify(None, "cruise_control_enabled")

    # Изменяем скорость и проверяем регулирование двигателем
    speed_sensor.change_speed(80)
    speed_sensor.change_speed(85)

    # Отключаем круиз-контроль
    car_mediator.notify(None, "cruise_control_disabled")
