from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self._parts = []

    def add_part(self, part: str):
        self._parts.append(part)

    def display_parts(self) -> None:
        print(f"Автомобиль состоит из: {', '.join(self._parts)}")

class AbstractCarBuilder(ABC):
    @abstractmethod
    def build_engine(self) -> None:
        pass

    @abstractmethod
    def build_wheels(self) -> None:
        pass

    @abstractmethod
    def build_body(self) -> None:
        pass

    @abstractmethod
    def get_car(self) -> Car:
        pass

class SportCarBuilder(AbstractCarBuilder):
    def __init__(self):
        self._car = Car()

    def build_engine(self) -> None:
        self._car.add_part("Спортивный двигатель")

    def build_wheels(self) -> None:
        self._car.add_part("Низкопрофильные шины")

    def build_body(self) -> None:
        self._car.add_part("Купе")

    def get_car(self) -> Car:
        return self._car

class FamilyCarBuilder(AbstractCarBuilder):
    def __init__(self):
        self._car = Car()

    def build_engine(self) -> None:
        self._car.add_part("Экономичный двигатель")

    def build_wheels(self) -> None:
        self._car.add_part("Шины с повышенным сроком службы")

    def build_body(self) -> None:
        self._car.add_part("Универсал")

    def get_car(self) -> Car:
        return self._car

class CarDirector:
    def __init__(self, builder: AbstractCarBuilder):
        self._builder = builder

    def build_car(self) -> None:
        self._builder.build_engine()
        self._builder.build_wheels()
        self._builder.build_body()

if __name__ == "__main__":
    sport_builder = SportCarBuilder()
    director = CarDirector(sport_builder)
    director.build_car()
    sport_car = sport_builder.get_car()
    sport_car.display_parts()

    family_builder = FamilyCarBuilder()
    director = CarDirector(family_builder)
    director.build_car()
    family_car = family_builder.get_car()
    family_car.display_parts()
