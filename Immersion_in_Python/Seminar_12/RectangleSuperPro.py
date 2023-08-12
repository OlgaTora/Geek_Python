"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
Добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""

from Immersion_in_Python.Seminar_11.task_3 import RectanglePro
import sys


class RectangleSuperPro(RectanglePro):
    """"Add possibility to change length and width"""
    __slots__ = ('_length', '_width')

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value: float):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Width cannot be less than 0')

    @length.setter
    def length(self, value: float):
        if value >= 0:
            self._length = value
        else:
            raise ValueError('Length cannot be less than 0')


if __name__ == '__main__':
    rect5 = RectangleSuperPro(101, 2)
    # rect5.width = -1
    # print(rect5.width)
    print(sys.getsizeof(rect5))  # dict 48
    print(sys.getsizeof(rect5))  # slots 64
