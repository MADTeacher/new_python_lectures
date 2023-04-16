from abc import ABC, abstractmethod


class CarAssemblyLine(ABC):
    def assemble_car(self) -> None:
        self.assemble_engine()
        self.assemble_body()
        self.install_safety_systems()
        self.add_additional_equipment()

    @abstractmethod
    def assemble_engine(self) -> None:
        pass

    @abstractmethod
    def assemble_body(self) -> None:
        pass

    @abstractmethod
    def install_safety_systems(self) -> None:
        pass

    def add_additional_equipment(self) -> None:
        print("Установка дополнительного оборудования")


class GasolineCarAssemblyLine(CarAssemblyLine):
    def assemble_engine(self) -> None:
        print("Сборка бензинового двигателя")

    def assemble_body(self) -> None:
        print("Сборка кузова для бензиновой машины")

    def install_safety_systems(self) -> None:
        print("Установка систем безопасности для бензиновой машины")


class ElectricCarAssemblyLine(CarAssemblyLine):
    def assemble_engine(self) -> None:
        print("Сборка электродвигателя")

    def assemble_body(self) -> None:
        print("Сборка кузова для электрической машины")

    def install_safety_systems(self) -> None:
        print("Установка систем безопасности для электрической машины")


class AutonomousCarAssemblyLine(ElectricCarAssemblyLine):
    def install_safety_systems(self) -> None:
        super().install_safety_systems()
        print("Установка системы автономного вождения")

    def add_additional_equipment(self) -> None:
        print("Установка дополнительных аккумуляторов для автономной машины")


if __name__ == "__main__":
    gasoline_car_assembly = GasolineCarAssemblyLine()
    electric_car_assembly = ElectricCarAssemblyLine()
    autonomous_car_assembly = AutonomousCarAssemblyLine()

    print("Сборка бензиновой машины:")
    gasoline_car_assembly.assemble_car()

    print("\nСборка электрической машины:")
    electric_car_assembly.assemble_car()

    print("\nСборка автономной машины:")
    autonomous_car_assembly.assemble_car()
