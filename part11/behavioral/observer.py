from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, event: str) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, event: str) -> None:
        pass


class ProductionLine(Subject):
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for observer in self._observers:
            observer.update(event)

    def start_production(self) -> None:
        print("Начало производства автомобилей")
        self.notify("production_started")

    def end_production(self) -> None:
        print("Конец производства автомобилей")
        self.notify("production_ended")


class QualityControl(Observer):
    def update(self, event: str) -> None:
        if event == "production_started":
            print("Контроль качества: проверяем качество автомобилей")
        elif event == "production_ended":
            print("Контроль качества: завершаем проверку качества")


class SupplyChain(Observer):
    def update(self, event: str) -> None:
        if event == "production_started":
            print("Цепочка поставок: начинаем поставки компонентов")
        elif event == "production_ended":
            print("Цепочка поставок: завершаем поставки компонентов")


if __name__ == "__main__":
    production_line = ProductionLine()

    quality_control = QualityControl()
    supply_chain = SupplyChain()

    production_line.attach(quality_control)
    production_line.attach(supply_chain)

    production_line.start_production()
    production_line.end_production()

    production_line.detach(quality_control)
    production_line.detach(supply_chain)
