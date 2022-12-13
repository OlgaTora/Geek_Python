a1 = 0
a2 = 0
b1 = 0
b2 = 0
c1 = 0
c2 = 0
d1 = 0
d2 = 0


def input_data_complex():
    global c1, c2, d1, d2
    c1 = int(input('Введите первый коэффициент для А: '))
    c2 = int(input('Введите второй коэффициент для А: '))
    d1 = int(input('Введите первый коэффициент для B: '))
    d2 = int(input('Введите второй коэффициент для B: '))
    return a1, a2, b1, b2

def input_data_rational():
    global a1, b1, a2, b2
    a1 = int(input('Введите числитель А: '))
    a2 = int(input('Введите знаменатель А: '))
    b1 = int(input('Введите числитель B: '))
    b2 = int(input('Введите знаменатель B: '))
    return a1, a2, b1, b2


def input_symb():
    try:
        symb = input('Введите символ арифметической операции: ')
        if symb in '+-*/':
            return symb
    except:
        print('Ошибка при введении символа!')


def choice_calc():
    try:
        answer = input('Нажмите 1, если у вас комплексные числа, нажмите 2, если рациональные')
        if answer == 1:
            input_data_complex()
        elif answer == 2:
            input_data_rational()
    except:
        print('Нажмите 1, если у вас комплексные числа, нажмите 2, если рациональные')

def print_result():
    pass