"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания периметра.
При этом должен создаваться новый экземпляр
прямоугольника.
При вычитании не допускайте отрицательных значений.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

from Immersion_in_Python.Seminar_10.task2 import Rectangle


class RectanglePro(Rectangle):
    """
    Добавлена возможность сложения и вычитания периметра,
    сравнение прямоугольников по площади."""

    def __add__(self, other: Rectangle):
        """Функция сложение"""
        summ: float = self.get_perimeter() + self.get_perimeter()
        width = self._width + self._length
        length = summ / 2 - width
        return RectanglePro(length, width)

    def __sub__(self, other):
        """Функция вычитание"""
        if self.get_perimeter() < other.get_perimeter():
            self, other = other, self
        sub: float = self.get_perimeter() - other.get_perimeter()
        width = abs(self._width - self._length)
        length = sub / 2 - width
        return RectanglePro(length, width)

    def __eq__(self, other):
        """Функция сравнения на равенство"""
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """Функция сравнения больше"""
        return self.get_square() > other.get_square()

    def __le__(self, other):
        """Функция сравнения меньше или равно"""
        return self.get_square() <= other.get_square()

    def __str__(self):
        '''Функция вывода информации для пользователя'''
        return f'This is rectangle with width={self._width} and length={self._length}'


if __name__ == '__main__':
    rect1 = RectanglePro(2, 5)
    print(rect1)
    rect2 = RectanglePro(4, 6)
    result1 = rect1 + rect2
    print(result1)
    print(result1.get_perimeter())
    result2 = rect1 - rect2
    print(result2.get_perimeter())
    print(rect1.get_square())
    print(rect2.get_square())
    print(rect1 >= rect2)
