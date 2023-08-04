"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
from typing import Callable


def get_data(num: int, attempts: int) -> Callable[[], None]:
    def guess_num():
        for i in range(1, attempts + 1):
            print(f'Attempt = {i}')
            guess_number = int(input('Guess num\n'))
            if guess_number == num:
                print('You are right')
                break
            print('More') if guess_number > num else print('Less')

    return guess_num


if __name__ == '__main__':
    closure = get_data(5, 2)
    print(closure())

