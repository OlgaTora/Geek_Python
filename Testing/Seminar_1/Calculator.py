"""Задание 1. ** В классе Calculator создайте метод calculateDiscount,
 который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
 Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
 Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
  Не забудьте написать тесты для проверки этого поведения.

*Задание 2. (необязательное) *
Мы хотим улучшить функциональность нашего интернет-магазина. Ваша задача - добавить два новых метода в класс Shop:
Метод sortProductsByPrice(), который сортирует список продуктов по стоимости. Метод getMostExpensiveProduct(),
 который возвращает самый дорогой продукт. Напишите тесты, чтобы проверить, что магазин хранит верный список
  продуктов (правильное количество продуктов, верное содержимое корзины).
Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
Напишите тесты для проверки корректности работы метода sortProductsByPrice (проверьте правильность сортировки).
Используйте класс Product для создания экземпляров продуктов и класс Shop для написания методов сортировки и тестов.
"""


class Calculator:
    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: str):
        result: int

        match operator:
            case '+':
                result: int = first_operand + second_operand
            case '-':
                result: int = first_operand - second_operand
            case '*':
                result: int = first_operand * second_operand
            case '/':
                if second_operand != 0:
                    result: float = first_operand / second_operand
                else:
                    raise ArithmeticError('Division by zero is not possible')
            case _:
                raise ValueError('Unexpected value operator: ' + operator)

        return result

    @staticmethod
    def calculate_discount(amount: int, discount: int) -> float:
        if amount < 0:
            raise ValueError('Amount should be more than zero')
        if not 0 <= discount <= 100:
            raise ValueError('Discount should be from 0 to 100 percents')
        return amount * (1 - discount / 100)

c = Calculator()
res = c.calculate_discount(100, 10)
print(res)