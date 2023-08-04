"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""
from typing import Callable, Any
import json
import os
from functools import wraps


def save_to_json(func: Callable) -> Callable[[tuple, dict], Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        data = []

        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        result = func(*args, **kwargs)
        data_dct = {'args': args, **kwargs, 'result': result}
        data.append(data_dct)

        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
        return result
    return wrapper


@save_to_json
def get_summ(*args, **kwargs) -> int:
    return sum(args)


@save_to_json
def concat_str(*args, **kwargs) -> str:
    return ''.join(args)


if __name__ == '__main__':
    get_summ(1, 2, x=5, y=6)
    concat_str('a', 'e', 'b', x='world', y='hello')

