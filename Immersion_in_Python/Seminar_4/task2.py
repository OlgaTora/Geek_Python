""""✔ Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def get_data() -> str:
    data = input('Input something:\n')
    return data


def convert_to_unocode(input_data: str) -> list[int]:
    data_set = set([ord(i) for i in input_data])
    data_set = sorted(list(data_set), reverse=True)
    return data_set


data = get_data()
print(convert_to_unocode(data))

