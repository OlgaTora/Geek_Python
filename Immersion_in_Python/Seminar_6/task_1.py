"""
Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

Улучшаем:
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""


from random import randint
from sys import argv

__all__ = ['get_data', 'guess_number']


def get_data() -> tuple[int, int, int]:
    min_num, max_num, attemps = map(int, input('Input min, max and attempts:\n').split())
    return min_num, max_num, attemps


def guess_number(min_num: int, max_num: int, attempts: int):
    random_num: int = randint(min_num, max_num)
    result: bool = False
    for attempt in range(attempts):
        guess_num = int(input('Guess number: '))
        if guess_num == random_num:
            print('You are right!')
            result = True
            break
        else:
            print('More') if guess_num < random_num else print('Less')
    return result


if __name__ == '__main__':
    #запуск в консоли
    #min_num, max_num, attemps = get_data()
    # print(f'result: {guess_number(min_num, max_num, attemps)}')

    #запуск в терминале
    name, *param = argv
    result = guess_number(*(int(i) for i in param))
    print(f'result: {result}')

