from typing import Self


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __lt__(self, other: Self) -> bool:
        return (self.width * self.height) < (other.width * other.height)

    def __le__(self, other: Self) -> bool:
        return (self.width * self.height) <= (other.width * other.height)

    def __eq__(self, other: Self) -> bool:
        return (self.width * self.height) == (other.width * other.height)

    def __ne__(self, other: Self) -> bool:
        return (self.width * self.height) != (other.width * other.height)

    def __gt__(self, other: Self) -> bool:
        return (self.width * self.height) > (other.width * other.height)

    def __ge__(self, other: Self) -> bool:
        return (self.width * self.height) >= (other.width * other.height)

    def __str__(self):
        return "Rectangle({}, {})".format(self.width, self.height)


if __name__ == "__main__":
    rect1 = Rectangle(2, 3)
    rect2 = Rectangle(4, 5)
    rect3 = Rectangle(1, 6)

    print(rect1 < rect2)  # True
    print(rect2 <= rect3)  # False
    print(rect1 == rect3)  # True
    print(rect2 != rect3)  # True
    print(rect3 > rect1)  # False
    print(rect2 >= rect1)  # True
