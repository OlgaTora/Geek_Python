"""
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
from __future__ import annotations

data = [2, 5, 11, 24, 15, 11, 2, 7, 12, 5, 6]
start = 12
end = 1


def count_summa(data_list: list[int] | list[float], first: int, last: int) -> int | float:
    summ = 0
    start_i = max(0, min(first, last))
    end_i = min(len(data_list), max(last, start))
    summ = sum(data_list[start_i:end_i + 1])
    return summ

print(count_summa(data, start, end))

