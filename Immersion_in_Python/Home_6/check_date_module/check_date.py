"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

import constants as c


def get_data() -> tuple[int, int, int]:
    while True:
        try:
            data = input("Input date in format DD.MM.YYYY:\n").split('.')
            if len(data) < 3:
                print('Error, date in format  DD.MM.YYYY')
            else:
                date, month, year = data
                if len(date) == c.LEN_DD_AND_MM and len(month) == c.LEN_DD_AND_MM and len(year) == c.LEN_YEAR:
                    date, month, year = map(int, data)
                    return date, month, year
        except ValueError:
            print('Not characters please')


def is_real_date(date: int, month: int, year: int) -> bool:
    if not (c.MIN_Y_M_D <= year <= c.MAX_YEAR and c.MIN_Y_M_D <= month <= c.MAX_MONTH
            and c.MIN_Y_M_D <= date <= c.MAX_DAY):
        return False
    if month in c.MONTHS_30_DAYS and date > 30:
        return False
    if month == c.FEBRUARY:
        if is_leap_year(year) and date > 29:
            return False
        if (not is_leap_year(year)) and date > 28:
            return False
    return True


def is_leap_year(year: int) -> bool:
    if year % c.MULTY_4 == 0 and year % c.MULTY_100 != 0 or year % c.MULTY_400 == 0:
        return True
    else:
        return False

