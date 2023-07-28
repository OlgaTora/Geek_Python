"""
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 4
Имя файла и его размер должны быть в рамках переданного диапазона.

Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.

Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""
import os
import random
from string import ascii_lowercase, digits
from os import path


def create_file(extension: str, min_byte=256, max_byte=4096, min_len=6,
                max_len=30, files_quan=4) -> None:
    for i in range(files_quan):
        name = gen_name(extension, min_len, max_len)
        content = gen_content(min_byte, max_byte)
        with open(f'{name}', 'wb') as file:
            file.write(content)


def gen_name(extension: str, min_len: int, max_len: int) -> str:
    file_name = '.'.join(
            [''.join(random.choices(ascii_lowercase + digits + '_', k=random.randint(min_len, max_len))), extension])
    while path.isfile(file_name):
        #print('filename exist')
        file_name: str = '.'.join(
            [''.join(random.choices(ascii_lowercase + digits + '_', k=random.randint(min_len, max_len))), extension])
    return file_name


def gen_content(min_byte: int, max_byte: int) -> bytes:
    content = bytes(random.randint(0, 255) for _ in range(random.randint(min_byte, max_byte)))
    return content


def gen_extensions(**kwargs) -> None:
    for extension, quantity in kwargs.items():
        create_file(extension=extension, files_quan=quantity)


def check_dir(dir: str, **kwargs) -> None:
    if not path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    gen_extensions(**kwargs)


check_dir(dir='test', txt=2, csv=1, jpg=1)

