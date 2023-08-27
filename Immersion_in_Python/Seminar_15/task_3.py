"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответствует формату.

Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые, т.е не мая, а 5.
"""

import logging
from datetime import datetime
import argparse

DAYS_OF_WEEK = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
MONTHS = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
FORMAT = '{asctime} - {levelname} - {funcName} - {msg}'
logging.basicConfig(filename='date_modify.log', level=logging.DEBUG, encoding='utf-8',
                    style='{', format=FORMAT)
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='modify data',
                                     description='little program to modify data to format datetime',
                                     epilog='1-й четверг ноября = 2023-11-03 00:00:00')
    parser.add_argument('-d', '--day', default=1, help='count of day of week')
    parser.add_argument('-w', '--weekday', default=datetime.now().weekday(), help='week day')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='month')
    arguments = parser.parse_args()
    return modify_date(f'{arguments.day} {arguments.weekday} {arguments.month}')


def modify_date(data: str) -> datetime | None:
    try:
        day, weekday, month = data.split()
    except ValueError as e:
        logger.info(f'{e}: Invalid type of input data {data}')
        return None
    try:
        day = int(day[0])
    except ValueError as e:
        logger.info(f'{e}: Invalid number of week day {day}')

    try:
        weekday = DAYS_OF_WEEK.index(weekday[:3]) + 1
    except ValueError as e:
        logger.info(f'{e}: Invalid name of week day {weekday}')

    try:
        month = MONTHS.index(month[:3]) + 1
    except ValueError as e:
        logger.info(f'{e}: Invalid name of month {month}')

    counter = 0
    for i in range(1, 32):
        date = datetime(day=i, month=month, year=datetime.now().year)
        if date.weekday() == weekday:
            counter += 1
            if counter == day:
                return date


if __name__ == '__main__':
    print(parse())
    # print(modify_date('1-й четверг ноября'))
    # print(modify_date('3-я среда мая'))
    # print(modify_date('1-й четверг'))
    # print(modify_date('четверг апреля'))
