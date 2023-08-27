"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""

import logging


def div(num1: float | int, num2: float | int) -> float:
    try:
        result = num2 / num1
    except ZeroDivisionError as z:
        logging.info(z)
        result = float('inf')
    return result


logging.basicConfig(level=logging.INFO,
                    filename='division.log',
                    encoding='utf-8',
                    format="%(asctime)s - [%(levelname)s]"
                           " -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
                    datefmt='%H:%M:%S')

logger = logging.getLogger()

if __name__ == '__main__':
    div(0, 3)
    div(0, 5)
    div(1, 3)
