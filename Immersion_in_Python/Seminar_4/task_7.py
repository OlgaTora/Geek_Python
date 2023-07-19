"""
 Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""
from __future__ import annotations

companies_balance = {'abc': [1000, 200, -400, -300],
                     'kuku': [500, -1000, -10, 2000, -200],
                     'ruku': [10, -20, 300, 1000, 400, -100],
                     }


def is_profitable(companies_info: dict[str: list[int | float]]) -> bool:
    # for value in companies_info.values():
    #     if sum(value) < 0:
    #         return False
    # return True
    return all(map(lambda x: sum(x) > 0, companies_info.values()))


print(is_profitable(companies_balance))

