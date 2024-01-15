"""
 Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли
переданное число в интервал (25;100)
"""

MIN_NUM = 25
MAX_NUM = 100


def number_in_interval(num: int):
    if MIN_NUM <= num <= MAX_NUM:
        return True
    else:
        return False
