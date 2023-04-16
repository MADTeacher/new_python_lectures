from typing import Callable, Any


def sum_list(data: list[int]) -> int:
    return sum(data) + 1


def splitter(string: str, symbol: str) -> list[str]:
    return string.split(symbol)


def create_person(name: str, 
                  age: int, 
                  is_married: bool) -> dict[str, Any]:
    return {'name': name,
            'age': age,
            'is_married': False
            }


def pow_n(n: int) -> Callable[[int], int]:
    def action(x: int) -> int:
        return x ** n
    return action
