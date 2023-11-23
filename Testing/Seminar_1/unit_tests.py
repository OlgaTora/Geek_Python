import unittest

from Testing.Seminar_1.Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.message = 'Ошибка в методе'

    def tearDown(self):
        self.calculator = None

    # Проверка базового функционала с целыми числами:
    def test_add(self):
        self.assertEqual(self.calculator.calculation(2, 6, '+'), 8, msg=self.message)

    def test_subtract(self):
        self.assertEqual(self.calculator.calculation(2, 2, '-'), 0, msg=self.message)

    def test_multiply(self):
        self.assertEqual(self.calculator.calculation(2, 7, '*'), 14, msg=self.message)

    def test_divide(self):
        self.assertEqual(self.calculator.calculation(100, 50, '/'), 2, msg=self.message)

    def test_divide_by_zero(self):
        with self.assertRaises(ArithmeticError) as e:
            self.calculator.calculation(100, 0, '/')
            self.assertEqual(str(e.exception), 'Division by zero is not possible')

    def test_bad_operator(self):
        with self.assertRaises(ValueError) as e:
            self.calculator.calculation(100, 0, ';')
            self.assertEqual(str(e.exception), 'Unexpected value operator')

    def test_calculate_discount(self):
        self.assertEqual(self.calculator.calculate_discount(100, 10), 90.0)

    def test_calculate_bad_discount(self):
        with self.assertRaises(ValueError) as e:
            self.assertEqual(self.calculator.calculate_discount(100, 101), 90.0)
            self.assertEqual(str(e.exception), 'Discount should be from 0 to 100 percents')

    def test_calculate_discount_bad_amount(self):
        with self.assertRaises(ValueError) as e:
            self.assertEqual(self.calculator.calculate_discount(-100, 10), 90.0)
            self.assertEqual(str(e.exception), 'Amount should be more than zero')


if __name__ == '__main__':
    unittest.main()
