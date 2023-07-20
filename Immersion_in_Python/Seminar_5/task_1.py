"""
Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
второе и третье число являются ключами.
первое число является значением для первого ключа.
четвертое и все возможные последующие числа
хранятся в кортеже как значения второго ключа.
"""
from __future__ import annotations


def get_dict_from_input() -> dict[int: int | tuple]:
    value_1, key_1, key_2, *value_2 = map(int, input().split('/'))
    dct = {key_1: value_1, key_2: tuple(value_2)}
    return dct


print(get_dict_from_input())
