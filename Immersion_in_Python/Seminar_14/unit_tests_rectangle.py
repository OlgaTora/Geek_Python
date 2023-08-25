"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
import unittest
from Immersion_in_Python.Seminar_11.task_3 import RectanglePro


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.rect1 = RectanglePro(5, 6)
        cls.rect2 = RectanglePro(5)
        cls.rect3 = RectanglePro(2, 5)
        cls.rect4 = RectanglePro(4, 6)
        cls.rect5 = RectanglePro(6, 5)

    def test_create(self):
        self.assertEquals(self.rect1, RectanglePro(5, 6))

    def test_get_square(self):
        self.assertEquals(self.rect1.get_square(), 30.0)

    def test_get_perimeter(self):
        self.assertEquals(self.rect1.get_perimeter(), 22.0)

    def test_equals(self):
        self.assertTrue(self.rect1, self.rect5)

    def test_not_equals(self):
        self.assertNotEquals(self.rect1, self.rect4)

    def test_le(self):
        self.assertFalse(self.rect3 >= self.rect4)

    def test_summ(self):
        self.assertEquals(self.rect3 + self.rect4, RectanglePro(7,7))


if __name__ == '__main__':
    unittest.main()
