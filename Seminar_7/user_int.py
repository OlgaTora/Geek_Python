

a1 = 0
a2 = 0
c1 = 0
c2 = 0
data = 0


def input_data_complex():
    global c1, c2
    c1 = int(input('Введите первый коэффициент: '))
    c2 = int(input('Введите второй коэффициент: '))
    return c1, c2


def input_data_rational():
    global a1, a2
    a1 = int(input('Введите числитель: '))
    a2 = int(input('Введите знаменатель: '))
    return a1, a2


def input_symb():
    try:
        symb = input('Введите символ арифметической операции: ')
        if symb in '+-*/':
            return symb
    except:
        print('Ошибка при введении символа!')


