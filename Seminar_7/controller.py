import logger_calc as log
from modul_rational_calc import calc_rational
from modul_complex_calc import calc_complex


def calc():
    global data
    try:
        answer = int(input('Нажмите 1, если у вас комплексные числа, нажмите 2, если рациональные '))
        if answer == 1:
            data = calc_complex()
        elif answer == 2:
            data = calc_rational()
        log.log_data(data)

    except:
        print('Ошибка')