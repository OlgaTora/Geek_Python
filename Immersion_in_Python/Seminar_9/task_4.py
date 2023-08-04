"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
from typing import Callable
from functools import wraps


def call_function(calls: int) -> Callable:
    result = []

    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(calls):
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@call_function(5)
def get_sum(*args):
    return sum(args)


if __name__ == '__main__':
    print(get_sum(1, 2, 3))
