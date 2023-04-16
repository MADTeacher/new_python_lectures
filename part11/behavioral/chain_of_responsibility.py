from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional, Any, Self


@dataclass
class Car:
    color: str | None = None
    wheels: int | None = None
    transmission: str | None = None
    engine: str | None = None


class Request:
    def __init__(self, kind: str, value: Any) -> None:
        self.kind = kind
        self.value = value


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Self) -> Self:
        pass

    @abstractmethod
    def handle(self, request: Request) -> Optional[str]:
        pass


class AbstractHandler(Handler):

    def __init__(self, handler: Optional[Handler] = None) -> None:
        self._next_handler = handler

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class EngineHandler(AbstractHandler):

    def __init__(self, handler: Optional[Handler] = None) -> None:
        super().__init__(handler)

    def handle(self, request: Request) -> Optional[str]:
        if request.kind == "engine":
            if request.value:
                return f"Проверка двигателя: двигатель установлен ({re-quest.value} л.с.)."
            else:
                return f"Проверка двигателя: двигатель отсутствует!"
        return super().handle(request)


class WheelsHandler(AbstractHandler):

    def __init__(self, handler: Optional[Handler] = None) -> None:
        super().__init__(handler)

    def handle(self, request: Request) -> Optional[str]:
        if request.kind == "wheels":
            if request.value >= 4:
                return f"Проверка колес: колеса установлены ({request.value} колеса)."
            else:
                return f"Проверка колес: не хватает колес!"
        return super().handle(request)


class TransmissionHandler(AbstractHandler):

    def __init__(self, handler: Optional[Handler] = None) -> None:
        super().__init__(handler)

    def handle(self, request: Request) -> Optional[str]:
        if request.kind == "transmission":
            if request.value:
                return f"Проверка трансмиссии: трансмиссия установлена ({re-quest.value})."
            else:
                return f"Проверка трансмиссии: трансмиссия отсутствует!"
        return super().handle(request)


class PaintHandler(AbstractHandler):

    def __init__(self, handler: Optional[Handler] = None) -> None:
        super().__init__(handler)

    def handle(self, request: Request) -> Optional[str]:
        if request.kind == "color":
            if request.value:
                return f"Проверка окраски: автомобиль окрашен ({re-quest.value})."
            else:
                return f"Проверка окраски: автомобиль не окрашен!"
        return super().handle(request)


if __name__ == "__main__":
    wheels_handler = WheelsHandler()
    engine_handler = EngineHandler(wheels_handler)
    paint_handler = PaintHandler()
    transmission_handler = TransmissionHandler(paint_handler)

    wheels_handler.set_next(transmission_handler)

    car = Car(
        color="белый",
        wheels=4,
        transmission="автоматическая",
        engine="150",
    )

    requests = [
        Request("engine", car.engine),
        Request("wheels", car.wheels),
        Request("transmission", car.transmission),
        Request("color", car.color),
    ]

    for request in requests:
        print(engine_handler.handle(request))
