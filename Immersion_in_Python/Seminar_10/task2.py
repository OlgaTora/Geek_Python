"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle(object):

    def __init__(self, length: float, width: float = None):
        self._length = float(length)
        if width is not None:
            self._width = float(width)
        else:
            self._width = length

    def get_square(self) -> float:
        return self._length * self._width

    def get_perimeter(self) -> float:
        return 2 * (self._length + self._width)


if __name__ == '__main__':
    rectangle1 = Rectangle(5, 6)
    print(f'{rectangle1.get_square() = }')
    print(f'{rectangle1.get_perimeter() = }')
    rectangle2 = Rectangle(5)
    print(f'{rectangle2.get_square() = }')
    print(f'{rectangle2.get_perimeter() = }')
