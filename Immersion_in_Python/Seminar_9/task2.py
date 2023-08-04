"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from random import randint
from typing import Callable
from functools import wraps

MAX_ATTEMPTS = 10
MIN_ATTEMPTS = 1
MAX_NUMBER = 100
MIN_NUMBER = 1


def control_params(func: Callable) -> Callable[[int, int], None]:
    @wraps(func)
    def wrapper(num: int, attempts: int, *args, **kwargs):
        if not MAX_NUMBER >= num >= MIN_NUMBER or not MAX_ATTEMPTS >= attempts >= MIN_ATTEMPTS:
            print('Random!')
            num = randint(MIN_NUMBER, MAX_NUMBER)
            attempts = randint(MIN_ATTEMPTS, MAX_ATTEMPTS)
        return func(num, attempts, *args, **kwargs)

    return wrapper


@control_params
def guess_num(num: int, attempts: int) -> str:
    result: str = ''
    for i in range(1, attempts + 1):
        print(f'Attempt = {i}')
        guess_number = int(input('Guess num\n'))
        if guess_number == num:
            result = 'You are right'
            return result
        print('More') if guess_number > num else print('Less')
    result = 'You cant guess number!'
    return result


if __name__ == '__main__':
    print(guess_num(911, 31))
