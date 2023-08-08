class CheckDate:
    """
    Класс для работы с датой в формате DD.MM.YYYY
    Возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
    Год может быть в диапазоне [1, 9999].
    Весь период действует Григорианский календарь.
    """
    MIN_DMY = 1
    MAX_YEAR = 9999
    MAX_MONTH = 12
    MAX_DAY = 31
    MONTHS_30_DAYS = (4, 6, 9, 11)
    MULTY_4 = 4
    MULTY_100 = 100
    MULTY_400 = 400
    FEBRUARY = 2

    def is_real_date(self, data: str) -> bool:
        date, month, year = map(int, data.split('.'))
        if not (self.MIN_DMY <= year <= self.MAX_YEAR and self.MIN_DMY <= month <= self.MAX_MONTH
                and self.MIN_DMY <= date <= self.MAX_DAY):
            return False
        if month in self.MONTHS_30_DAYS and date > 30:
            return False
        if month == self.FEBRUARY:
            if self.is_leap_year(year) and date > 29:
                return False
            if (not self.is_leap_year(year)) and date > 28:
                return False
        return True

    def is_leap_year(self, year: int) -> bool:
        if year % self.MULTY_4 == 0 and year % self.MULTY_100 != 0 or year % self.MULTY_400 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    check_date = CheckDate()
    print(check_date.is_real_date('10.01.2001'))
    print(check_date.is_real_date('29.02.2001'))
    print(check_date.is_real_date('29.02.2004'))
