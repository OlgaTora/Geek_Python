from random import randint
from exceptions import DigitsValueException, AttemptsException


def get_data() -> tuple[int, int, int]:
    min_num, max_num, attempts = input('Input min, max and attempts:\n').split()
    if min_num.isdigit() and max_num.isdigit() and attempts.isdigit():
        min_num, max_num, attempts = int(min_num), int(max_num), int(attempts)
        if attempts < 1:
            raise AttemptsException(attempts)
    else:
        raise DigitsValueException(min_num, max_num, attempts)
    return min_num, max_num, attempts


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
