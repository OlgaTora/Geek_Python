import csv
import json
import os
from functools import wraps
from typing import Callable

from FileName import FileName


def search_root_from_scv(file: FileName) -> Callable:
    """ Декоратор, запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла.
    """

    def search_roots(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file.file_name, 'r', encoding='utf-8') as csv_file:
                numbers_list = csv.reader(csv_file, dialect='excel')
                for i in numbers_list:
                    a, b, c = i
                    result = func(a, b, c, *args, *kwargs)
            return result

        return wrapper

    return search_roots


def save_to_json(func: Callable) -> Callable:
    """ Декоратор, сохраняющий переданные параметры и результаты работы
    функции в json файл.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        data = []
        data_dct = {'args': args, **kwargs}
        if os.path.exists(file_name):
            print('path')
            with open(file_name, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        result = func(*args, **kwargs)
        data_dct['result'] = result
        data.append(data_dct)

        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
        return result

    return wrapper
