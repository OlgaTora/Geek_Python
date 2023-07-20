"""
Создайте генератор чётных чисел от нуля до 100.
Из последовательности исключите
числа, сумма цифр которых равна 8.
Решение в одну строку
"""
MIN_NUM = 0
MAX_NUM = 100
SUM_ELEM = 8


def get_sum_elements(num: int):
    summ = sum(map(int, str(num)))
    return summ

# gen = (i for i in range(MIN_NUM, MAX_NUM, 2) if (i % 10 + i // 10) != 8)
gen = (i for i in range(MIN_NUM, MAX_NUM, 2) if get_sum_elements(i) != SUM_ELEM)
print(*gen)

