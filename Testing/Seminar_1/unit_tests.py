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
        self.assertRaises(ArithmeticError, self.calculator.calculation, 1, 0, '/')

    def test_divide_by_zero_check_message(self):
        with self.assertRaises(ArithmeticError) as e:
            self.calculator.calculation(100, 0, '/')
            self.assertEqual(str(e.exception), 'Division by zero is not possible')

    def test_bad_operator(self):
        with self.assertRaises(ValueError) as e:
            self.calculator.calculation(100, 0, ';')
            self.assertEqual(str(e.exception), 'Unexpected value operator')

    #   проверка функции подсчета скидки с вводом целых чисел
    def test_calculate_discount(self):
        self.assertEqual(self.calculator.calculate_discount(100, 10), 90.0)

    # проверка ожидаемого исключения при вводе скидки более 100%
    def test_calculate_bad_discount(self):
        self.assertRaises(ArithmeticError, self.calculator.calculate_discount, 100, 101)

    def test_calculate_bad_discount_check_msg(self):
        with self.assertRaises(ArithmeticError) as e:
            self.calculator.calculate_discount(100, 101)
            self.assertEqual(str(e.exception), 'Discount should be from 0 to 100 percents')

    # проверка ожидаемого исключения при вводе суммы меньше 0
    def test_calculate_discount_bad_amount(self):
        self.assertRaises(ArithmeticError, self.calculator.calculate_discount, -100, 10)

    def test_calculate_discount_bad_amount_check_msg(self):
        with self.assertRaises(ArithmeticError) as e:
            self.calculator.calculate_discount(-100, 10)
            self.assertEqual(str(e.exception), 'Amount should be more than zero')

    # проверка ожидаемого исключения при вводе не целых чисел
    def test_calculate_discount_bad_inputs(self):
        self.assertRaises(TypeError, self.calculator.calculate_discount, -100, '1')

    def test_calculate_discount_bad_inputs_check_msg(self):
        with self.assertRaises(TypeError) as e:
            self.calculator.calculate_discount(-100, '1')
            self.assertEqual(str(e.exception), 'You should input only integers')

    # Используйте параметризованные тесты для проверки работы этих операций на различных входных данных
    #и убедитесь, что результаты верны.

#     private final Calc calculator = new Calc();
#
#     @ParameterizedTest
#     @CsvSource({"1, 2, 3", "0, 0, 0", "-1, 1, 0", "10, -5, 5"})
#     void testAdd(int a, int b, int expected) {
#         int result = calculator.add(a, b);
#         assertEquals(expected, result);
#     }
#     @ParameterizedTest
#     @CsvSource({"1, 2, -1", "0, 0, 0", "-1, 1, -2", "10, -5, 15"})
#     void testSubtract(int a, int b, int expected) {
#         int res = calculator.subtract(a,b);
#         assertEquals(expected, res);
#     }
#
#     @ParameterizedTest
#     @CsvSource({"1, 2, 2", "0, 0, 0", "-1, 1, -1", "10, -5, -50"})
#     void multiply(int a, int b, int expected) {
#         int res = calculator.multiply(a,b);
#         assertEquals(expected, res);
#     }
#
#     @ParameterizedTest
#     @CsvSource({"1, 2, 0.5", "-1, 1, -1", "10, -5, -2"})
#     void divide(int a, int b, double expected) {
#         double res = calculator.divide(a,b);
#         assertEquals(expected, res, 0.001);
#     }
#
#     @Test
#     void whatExceptoinWillBeThrown(){
#         assertThrows(IllegalArgumentException.class, () -> calculator.divide(1,0));
#     }
#
#     @ParameterizedTest
#     @CsvSource({"1, 0", "-1, 0", "10, 0"})
#     void manyExceptions(int a, int b){
#         assertThrows(IllegalArgumentException.class, () -> calculator.divide(a,b));
#     }
#
#
# }
if __name__ == '__main__':
    unittest.main()
