"""
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
 Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def get_data() -> str:
    data = input('Input two numbers:\n')
    return data


def get_dict_unicode(input_data: str) -> dict[str: int]:
    numbers = {}
    input_data = list(map(int, input_data.split()))
    max_num = max(input_data)
    min_num = min(input_data)
    for i in range(min_num, max_num + 1):
        numbers[chr(i)] = i

    return numbers

data = get_data()
print(get_dict_unicode(data))
