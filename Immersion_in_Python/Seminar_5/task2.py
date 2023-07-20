"""
Самостоятельно сохраните в переменной строку текста.
Создайте из строки словарь, где ключ — буква, а значение — код буквы.
Напишите преобразование в одну строку.

Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили.
Сохраните его итераторатор.
Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

COUNT= 5
data = 'The origin of the English word cat'


def from_data_to_dict(data: str) -> dict[str:int]:
    dct = {i: ord(i) for i in data}
    return dct


def print_with_iter(dct: dict[str:int]):
    iter_dict = iter(dct.items())
    for _ in range(COUNT):
        print(next(iter_dict))


result_dct = from_data_to_dict(data)
print_with_iter(result_dct)

