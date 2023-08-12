"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""

from Immersion_in_Python.Seminar_11.task_3 import RectanglePro


class Descr:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.name, value)
        else:
            raise ValueError('Its not possible value less or equals zero')


class RectangleDescriptors(RectanglePro):
    length = Descr()
    width = Descr()


if __name__ == '__main__':
    rect5 = RectangleDescriptors(101, 2)
    #rect5.width = -1
