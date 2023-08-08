"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь
"""
import math

PI = math.pi


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def get_length(self) -> float:
        return 2 * PI * self.radius

    def get_square(self) -> float:
        return 2 * PI * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(10)
    print(f'{circle.get_length() = }')
    print(f'{circle.get_square() = }')
