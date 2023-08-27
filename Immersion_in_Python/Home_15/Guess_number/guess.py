from random import randint
from exceptions import DigitsValueException, AttemptsException
from logger import logger


def get_data() -> tuple[int, int, int]:
    min_num, max_num, attempts = input('Input min, max and attempts:\n').split()
    if min_num.isdigit() and max_num.isdigit() and attempts.isdigit():
        min_num, max_num, attempts = int(min_num), int(max_num), int(attempts)
        if attempts < 1:
            logger.info(f'Input attempts < 1, {attempts}')
            raise AttemptsException(attempts)
    else:
        logger.error(f'Invalid value input {min_num}, {max_num}, {attempts}')
        raise DigitsValueException(min_num, max_num, attempts)
    return min_num, max_num, attempts


def guess_number(min_num, max_num, attempts) -> bool:
    random_num: int = randint(min_num, max_num)
    result: bool = False
    log_msg = f'Random number = {random_num}, have not guess in {attempts} attempts'
    for attempt in range(attempts):
        guess_num = int(input('Guess number: '))
        if guess_num == random_num:
            print('You are right!')
            result = True
            log_msg = f'Random number = {random_num}, guess on {attempt + 1} attempt'
            break
        else:
            print('More') if guess_num < random_num else print('Less')
    logger.info(log_msg)
    print(log_msg)
    return result


