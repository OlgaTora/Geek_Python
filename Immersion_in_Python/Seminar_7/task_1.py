"""
Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""
import random
from random import randint, uniform

START_NUM = -1000
END_NUM = 1000


def fill_file_pairs(filename: str, size: int):
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(size + 1):
            first_num: int = randint(START_NUM, END_NUM)
            second_num: float = random.uniform(START_NUM, END_NUM)
            file.writelines('|'.join(map(str, [first_num, second_num])))
            file.writelines('\n')


fill_file_pairs('task_1.txt', 50)

