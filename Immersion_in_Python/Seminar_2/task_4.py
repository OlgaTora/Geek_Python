# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import decimal
import math


ACCURACY = 42
DIAMETER = 1000
PI: decimal.Decimal = decimal.Decimal(math.pi)
decimal.getcontext().prec = ACCURACY


def get_data() -> decimal.Decimal:
    try:
        d: int = int(input('Input diameter less than 1000: '))
    except ValueError:
        print('That was no valid number!')
    return decimal.Decimal(d)


def calc(d) -> tuple[decimal.Decimal, decimal.Decimal]:
    square: decimal.Decimal = d / 2 ** 2 * PI
    length: decimal.Decimal = d * PI
    return square, length

d = get_data()
if d > 1000:
    print('Its wrong diameter!')
else:
    square, length = calc(d)
    print(f'square: {square}, length: {length}')
