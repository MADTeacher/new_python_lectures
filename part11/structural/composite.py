from abc import ABC, abstractmethod
from typing import List


class AutoCompanyUnit(ABC):
    @abstractmethod
    def get_profit(self) -> int:
        pass


class Showroom(AutoCompanyUnit):
    def __init__(self, profit: int) -> None:
        self._profit = profit

    def get_profit(self) -> int:
        return self._profit


class Office(AutoCompanyUnit):
    def __init__(self) -> None:
        self._children: List[AutoCompanyUnit] = []

    def add(self, unit: AutoCompanyUnit) -> None:
        self._children.append(unit)

    def remove(self, unit: AutoCompanyUnit) -> None:
        self._children.remove(unit)

    def get_profit(self) -> int:
        total_profit = 0
        for child in self._children:
            total_profit += child.get_profit()
        return total_profit


if __name__ == "__main__":
    head_office = Office()
    regional_office1 = Office()
    regional_office2 = Office()

    showroom1 = Showroom(200000)
    showroom2 = Showroom(250000)
    showroom3 = Showroom(300000)
    showroom4 = Showroom(400000)

    regional_office1.add(showroom1)
    regional_office1.add(showroom2)
    regional_office2.add(showroom3)
    regional_office2.add(showroom4)

    head_office.add(regional_office1)
    head_office.add(regional_office2)

    print(f"Головной офис получает: {head_office.get_profit()} рублей")
