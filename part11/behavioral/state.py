from abc import ABC, abstractmethod


class CarQualityControlState(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass


class QualityControlSystem:
    def __init__(self, state: CarQualityControlState) -> None:
        self._state = state

    @property
    def state(self) -> CarQualityControlState:
        return self._state

    @state.setter
    def state(self, state: CarQualityControlState) -> None:
        self._state = state

    def handle(self) -> None:
        self._state.handle()


class InitialInspection(CarQualityControlState):
    def handle(self) -> None:
        print("Проводим первичный осмотр автомобиля.")


class AssemblyLineInspection(CarQualityControlState):
    def handle(self) -> None:
        print("Проводим осмотр автомобиля на сборочной линии.")


class PaintInspection(CarQualityControlState):
    def handle(self) -> None:
        print("Проверяем качество покраски автомобиля.")


class FinalInspection(CarQualityControlState):
    def handle(self) -> None:
        print("Проводим окончательный осмотр автомобиля перед отправ-кой клиенту.")


class QualityControlPassed(CarQualityControlState):
    def handle(self) -> None:
        print("Автомобиль успешно прошел все стадии контроля каче-ства.")


if __name__ == "__main__":
    quality_control = QualityControlSystem(InitialInspection())
    quality_control.handle()

    quality_control.state = AssemblyLineInspection()
    quality_control.handle()

    quality_control.state = PaintInspection()
    quality_control.handle()

    quality_control.state = FinalInspection()
    quality_control.handle()

    quality_control.state = QualityControlPassed()
    quality_control.handle()
