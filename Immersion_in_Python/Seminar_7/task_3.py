"""
Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
- если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
- если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""
from typing import TextIO


def modify_files(filename_1, filename_2, filename_3):
    with open(filename_1, encoding='utf-8') as numbers, \
            open(filename_2, encoding='utf-8') as names, \
            open(filename_3, 'w', encoding='utf-8') as result:
        len_file_1 = len(numbers.readlines())
        len_file_2 = len(names.readlines())
        for _ in range(max(len_file_1, len_file_2)):
            name = readline_or_begin(names)
            nums = readline_or_begin(numbers)
            num1, num2 = nums.split('|')
            mult: float = int(num1) * float(num2)
            if mult < 0:
                result.write(name.lower() + ' ' + str(- mult) + '\n')
            else:
                result.write(name.upper() + ' ' + str(round(mult)) + '\n')


def readline_or_begin(file: TextIO) -> str:
    text = file.readline()
    if text == '':
        file.seek(0)
        text = file.readline()
    return text[:-1]


modify_files('task_1.txt', 'task_2.txt', 'task_3.txt')

