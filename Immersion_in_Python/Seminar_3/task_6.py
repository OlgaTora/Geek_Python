# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки

SPACE = 1
START = 1

data = input('Input something')
#data = 'fhgjff djfk afdjka sdgjkdff'


def convert_string(data: str):
    my_list = data.split()
    my_list.sort()
    spaces = get_max_len(my_list) + SPACE
    for i, value in enumerate(my_list, start=START):
        print(f'{i}.{value: >{spaces}}')


def get_max_len(my_list: list):
    max_len = 0
    for i in my_list:
        if max_len < len(i):
            max_len = len(i)
    return max_len


convert_string(data)

