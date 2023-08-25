import unittest
from Immersion_in_Python.Seminar_14.str_modify.main import string_modify


class TestStringModifier(unittest.TestCase):
    def test_method1(self):
        self.assertEqual(string_modify('it was long thought'), 'it was long thought')

    def test_method2(self):
        self.assertEqual(string_modify('It was Long thought'), 'it was long thought')

    def test_method3(self):
        self.assertEqual(string_modify('it was, long thought!'), 'it was long thought')

    def test_method4(self):
        self.assertEqual(string_modify('it was long thought да дорогая'), 'it was long thought  ')

    def test_method5(self):
        self.assertEqual(string_modify('It was Long thought, да дорогая?'), 'it was long thought  ')


if __name__ == '__main__':
    unittest.main()
