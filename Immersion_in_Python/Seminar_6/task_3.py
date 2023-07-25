"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""
__all__ = ['get_data', 'is_real_date']
MIN_Y_M_D = 1
MAX_YEAR = 9999
MAX_MONTH = 1
MAX_DAY = 31
MONTHS_30_DAYS = (4, 6, 9, 11)
MULTY_4 = 4
MULTY_100 = 100
MULTY_400 = 400
FEBRUARY = 2


def get_data() -> tuple[int, int, int]:
    while True:
        try:
            data = input("Input date in format DD.MM.YYYY:\n").split('.')
            if len(data) < 3:
                print('Error, date in format  DD.MM.YYYY')
            else:
                date, month, year = data
                if len(date) == 2 and len(month) == 2 and len(year) == 4:
                    date, month, year = map(int, data)
                    return date, month, year
        except ValueError:
            print('Not characters please')


def is_real_date(date: int, month: int, year: int) -> bool:
    if not MIN_Y_M_D <= year <= MAX_YEAR and MIN_Y_M_D <= month <= MAX_MONTH and MIN_Y_M_D <= date <= MAX_DAY:
        return False
    if month in MONTHS_30_DAYS and date > 30:
        return False
    if month == FEBRUARY:
        if is_leap_year(year) and date > 29:
            return False
        if (not is_leap_year(year)) and date > 28:
            return False
    return True


def is_leap_year(year: int) -> bool:
    if year % MULTY_4 == 0 and year % MULTY_100 != 0 or year % MULTY_400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    date, month, year = get_data()
    print(is_real_date(date, month, year))
