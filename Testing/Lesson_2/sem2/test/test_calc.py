import unittest
from parameterized import parameterized

from Testing.Lesson_2.sem2.calc import Calc

"""
Используйте параметризованные тесты для проверки работы этих операций на 
различных входных данных и убедитесь, что результаты верны.
"""


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def tearDown(self):
        self.calc = None

    @parameterized.expand([('test_1', 1, 2, 3), ('test_2', 0, 0, 0), ('test_3', -1, 1, 0), ('test_4', 10, -5, 5)])
    def test_add(self, test_name, in_1, in_2, expected):
        assert self.calc.add(in_1, in_2) == expected

    @parameterized.expand([('test_1', 1, 2, -1), ('test_2', 0, 0, 0), ('test_3', -1, 1, -2), ('test_4', 10, -5, 15)])
    def test_subtract(self, test_name, in_1, in_2, expected):
        assert self.calc.subtract(in_1, in_2) == expected

    @parameterized.expand([('test_1', 1, 2, 2), ('test_2', 0, 0, 0), ('test_3', -1, 1, -1), ('test_4', 10, -5, -50)])
    def test_multiply(self, test_name, in_1, in_2, expected):
        assert self.calc.multiply(in_1, in_2) == expected

    @parameterized.expand([('test_1', 1, 2, 0.5), ('test_3', -1, 1, -1), ('test_4', 10, -5, -2)])
    def test_divide(self, test_name, in_1, in_2, expected):
        assert self.calc.divide(in_1, in_2) == expected

    def test_what_exception_will_be_thrown(self):
        self.assertRaises(ValueError, lambda: self.calc.divide(1, 0))

    @parameterized.expand([('test_1', 1, 0), ('test_2', -1, 0), ('test_3', 10, 0)])
    def test_divide_many_exceptions(self, test_name, in_1, in_2):
        with self.subTest(test_name=test_name):
            with self.assertRaises(ValueError):
            #Здесь вызывается код, который должен вызвать исключение
                result = self.calc.divide(in_1, in_2)


if __name__ == '__main__':
    unittest.main()
