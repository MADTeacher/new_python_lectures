class Engine:
    def start(self) -> None:
        print("Двигатель запущен")

    def stop(self) -> None:
        print("Двигатель остановлен")


class Transmission:
    def set_drive_mode(self) -> None:
        print("Трансмиссия установлена в режим 'D'")

    def set_park_mode(self) -> None:
        print("Трансмиссия установлена в режим 'P'")


class ClimateControl:
    def set_temperature(self, temperature: float) -> None:
        print(f"Установлена температура {temperature} градусов")


class CarFacade:
    def __init__(self, engine: Engine,
                 transmission: Transmission,
                 climate_control: ClimateControl) -> None:
        self.engine = engine
        self.transmission = transmission
        self.climate_control = climate_control

    def start_car(self) -> None:
        self.engine.start()
        self.transmission.set_drive_mode()
        self.climate_control.set_temperature(20.0)

    def stop_car(self) -> None:
        self.engine.stop()
        self.transmission.set_park_mode()
        self.climate_control.set_temperature(0)


if __name__ == "__main__":
    engine = Engine()
    transmission = Transmission()
    climate_control = ClimateControl()

    car_facade = CarFacade(engine, transmission, climate_control)

    print("Запускаем автомобиль:")
    car_facade.start_car()
    print("\nОстанавливаем автомобиль:")
    car_facade.stop_car()
