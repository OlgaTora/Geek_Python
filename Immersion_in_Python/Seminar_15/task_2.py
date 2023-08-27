"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.

Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
- уровень логирования,
- дату события,
- имя функции (не декоратора),
- аргументы вызова,
- результат.
"""

import logging
from typing import Callable


FORMAT = '{asctime} - {levelname} - {msg}'
logging.basicConfig(level=logging.DEBUG,
                    filename='division_deco.log',
                    encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def deco_log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_data = {'args': args, **kwargs}
        log_msg = f'{func.__name__}: {log_data} - result={result}'
        logger.info(log_msg)
        return result

    return wrapper


@deco_log
def div(num1: float | int, num2: float | int) -> float:
    try:
        result = num2 / num1
    except ZeroDivisionError:
        result = float('inf')
    return result


if __name__ == '__main__':
    div(0, 3)
    div(0, 5)
    div(1, 3)
