from abc import ABC, abstractmethod


class EngineInterface(ABC):
    @abstractmethod
    def start(self) -> None:
        pass


class GasolineEngine:
    def ignite(self) -> None:
        print("Запуск бензинового двигателя")


class ElectricEngine:
    def turn_on(self) -> None:
        print("Запуск электродвигателя")


class GasolineEngineAdapter(EngineInterface):
    def __init__(self, gasoline_engine: GasolineEngine) -> None:
        self._gasoline_engine = gasoline_engine

    def start(self) -> None:
        self._gasoline_engine.ignite()


class ElectricEngineAdapter(EngineInterface):
    def __init__(self, electric_engine: ElectricEngine) -> None:
        self._electric_engine = electric_engine

    def start(self) -> None:
        self._electric_engine.turn_on()


class Car:
    def __init__(self, engine: EngineInterface) -> None:
        self._engine = engine

    def start_engine(self) -> None:
        self._engine.start()


if __name__ == "__main__":
    gasoline_engine = GasolineEngine()
    electric_engine = ElectricEngine()

    gasoline_engine_adapter = GasolineEngineAdapter(gasoline_engine)
    electric_engine_adapter = ElectricEngineAdapter(electric_engine)

    car_with_gasoline_engine = Car(gasoline_engine_adapter)
    car_with_electric_engine = Car(electric_engine_adapter)

    car_with_gasoline_engine.start_engine()  # Запуск бензинового двига-теля
    car_with_electric_engine.start_engine()  # Запуск электродвигателя
