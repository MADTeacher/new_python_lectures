from abc import ABC, abstractmethod


class Car:
    def __init__(self, name: str, parts: dict[str, str]) -> None:
        self.name = name
        self.parts = parts

    def __str__(self) -> str:
        return f"Автомобиль: {self.name}, детали: {self.parts}"


class AssemblyStrategy(ABC):
    @abstractmethod
    def assemble_car(self, name: str, parts: dict[str, str]) -> Car:
        pass


class BasicAssemblyStrategy(AssemblyStrategy):
    def assemble_car(self, name: str, parts: dict[str, str]) -> Car:
        car = Car(name, parts)
        print(f"Автомобиль {name} собран с помощью базовой стратегии сборки.")
        return car


class AdvancedAssemblyStrategy(AssemblyStrategy):
    def assemble_car(self, name: str, parts: dict[str, str]) -> Car:
        car = Car(name, parts)
        print(
            f"Автомобиль {name} собран с помощью расширенной стра-тегии сборки.")
        return car


class CarAssemblyLine:
    def __init__(self, assembly_strategy: AssemblyStrategy) -> None:
        self.assembly_strategy = assembly_strategy

    def set_assembly_strategy(self, assembly_strategy: AssemblyStrategy) -> None:
        self.assembly_strategy = assembly_strategy

    def assemble_car(self, name: str, parts: dict[str, str]) -> Car:
        return self.assembly_strategy.assemble_car(name, parts)


if __name__ == "__main__":
    parts = {
        "кузов": "купе",
        "двигатель": "V8",
        "трансмиссия": "автоматическая",
    }

    assembly_line = CarAssemblyLine(BasicAssemblyStrategy())
    car1 = assembly_line.assemble_car("Tesla Model S", parts)
    print(car1)

    assembly_line.set_assembly_strategy(AdvancedAssemblyStrategy())
    car2 = assembly_line.assemble_car("Tesla Model X", parts)
    print(car2)
