"""
В классе Calculator создайте метод calculateDiscount,
который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
Не забудьте написать тесты для проверки этого поведения.
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
        if isinstance(amount, int) and isinstance(discount, int):
            if amount < 0:
                raise ArithmeticError('Amount should be more than zero')
            if not 0 <= discount <= 100:
                raise ArithmeticError('Discount should be from 0 to 100 percents')
            return amount * (1 - discount / 100)
        else:
            raise TypeError('You should input only integers')
