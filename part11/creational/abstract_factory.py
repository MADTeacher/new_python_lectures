from abc import ABC, abstractmethod

class AbstractCar(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

class AbstractEngine(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

class SportCar(AbstractCar):
    def drive(self) -> str:
        return "Спортивный автомобиль едет быстро"

class FamilyCar(AbstractCar):
    def drive(self) -> str:
        return "Семейный автомобиль едет спокойно"

class ElectricEngine(AbstractEngine):
    def start(self) -> str:
        return "Электрический двигатель работает тихо"

class GasEngine(AbstractEngine):
    def start(self) -> str:
        return "Бензиновый двигатель работает громко"

class AbstractCarFactory(ABC):
    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def create_engine(self) -> AbstractEngine:
        pass

class SportCarFactory(AbstractCarFactory):
    def create_car(self) -> SportCar:
        return SportCar()

    def create_engine(self) -> ElectricEngine:
        return ElectricEngine()

class FamilyCarFactory(AbstractCarFactory):
    def create_car(self) -> FamilyCar:
        return FamilyCar()

    def create_engine(self) -> GasEngine:
        return GasEngine()

def client_code(factory: AbstractCarFactory) -> None:
    car = factory.create_car()
    engine = factory.create_engine()
    print(car.drive())
    print(engine.start())

if __name__ == "__main__":
    client_code(SportCarFactory())
    client_code(FamilyCarFactory())
