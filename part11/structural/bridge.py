from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self) -> str:
        pass


class GasEngine(Engine):
    def start(self) -> str:
        return "Бензиновый двигатель запущен"


class ElectricEngine(Engine):
    def start(self) -> str:
        return "Электродвигатель запущен"


class ControlSystem(ABC):
    @abstractmethod
    def control(self) -> str:
        pass


class ManualControlSystem(ControlSystem):
    def control(self) -> str:
        return "Ручная система управления"


class AutomaticControlSystem(ControlSystem):
    def control(self) -> str:
        return "Автоматическая система управления"


class Car(ABC):
    def __init__(self, engine: Engine, control_system: ControlSystem) -> None:
        self._engine = engine
        self._control_system = control_system

    @abstractmethod
    def drive(self) -> None:
        pass


class Sedan(Car):
    def drive(self) -> None:
        print(
            f"Седан: {self._engine.start()}, {self._control_system.control()}")


class SUV(Car):
    def drive(self) -> None:
        print(
            f"Внедорожник:{self._engine.start()},{self._control_system.control()}")


if __name__ == "__main__":
    gas_engine = GasEngine()
    electric_engine = ElectricEngine()
    manual_control_system = ManualControlSystem()
    automatic_control_system = AutomaticControlSystem()

    sedan = Sedan(gas_engine, manual_control_system)
    suv = SUV(electric_engine, automatic_control_system)

    sedan.drive()
    suv.drive()
