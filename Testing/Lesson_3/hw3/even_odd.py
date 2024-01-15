"""
Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли
переданное число четным или нечетным:
"""


def even_odd_number(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False
