from typing import Self


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Self:
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: int | float) -> Self:
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other: int | float) -> Self:
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    
    print(v1 + v2)  # Vector(4, 6)
    print(v2 - v1)  # Vector(2, 2)
    print(v1 * 2)   # Vector(2, 4)
    print(2 * v1)   # Vector(2, 4)
    print(v2 / 2)   # Vector(1.5, 2.0)
