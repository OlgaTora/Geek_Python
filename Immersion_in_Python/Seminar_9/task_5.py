"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.

Добавивьте декоратор wraps в каждый из декораторов.
"""

from task2 import control_params
from task_3 import save_to_json
from task_4 import call_function

MAX_ATTEMPTS = 10
MIN_ATTEMPTS = 1
MAX_NUMBER = 100
MIN_NUMBER = 1


@call_function(3)
@control_params
@save_to_json
def guess_num(num: int, attempts: int) -> str:
    """Function for guess number"""
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
    print(guess_num(11, 2))
    print(f'{guess_num.__name__ = }')
    print(f'{guess_num.__doc__ = }')
