from threading import Lock

class SingletonBaseClass(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class CarRegistry(metaclass=SingletonBaseClass):
    def __init__(self):
        self.cars = {}

    def add_car(self, vin: str, manufacturer: str, model: str):
        self.cars[vin] = {"manufacturer": manufacturer, "model": model}

    def get_car(self, vin: str):
        return self.cars.get(vin)


if __name__ == "__main__":
    registry1 = CarRegistry()
    registry1.add_car("1A2B3C", "Toyota", "Camry")

    registry2 = CarRegistry()
    registry2.add_car("4D5E6F", "Honda", "Civic")

    print(registry1.get_car("1A2B3C"))
    print(registry2.get_car("4D5E6F"))

    print(registry1 is registry2)  # True
