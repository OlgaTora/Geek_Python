"""Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки
"""


def get_data() -> str:
    data = input('Input something:\n')
    return data


def print_data(data: str):
    data_list = sorted(data.split())
    max_len = len(max(data_list, key=lambda x: len(x)))
    for num, word in enumerate(data_list, start=1):
        print(f'{num}. {word:>{max_len}}')


data = get_data()
print_data(data)

