# Решите квадратное уравнение 5x2-10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.


def find_root(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("No roots")
    else:
        print((- b - d ** 0.5) / 2 * a)
        print((- b + d ** 0.5) / 2 * a)

#find_root(5, -10, -400)


# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.

def find_summa(n, e):
    x = 0
    summ = 0
    while x < n:
        if x % e != 0 and x % 2 == 0:
            summ += x
        x += 1
    print(summ)


#find_summa(10, 3)

# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

GREGORIAN = 1582
LEAP = "{} year is leap"
NO_LEAP = "{} year is not leap"
NO_GREGORIAN = "{} year is before Gregorian"
MULTY_4 = 4
MULTY_100 = 100
MULTY_400 = 400


def leap_year(year):
    res = ""
    if year >= GREGORIAN:
        if year % MULTY_4 == 0 and year % MULTY_100 != 0 or year % MULTY_400 == 0:
            res = LEAP.format(year)
        else:
            res = NO_LEAP.format(year)
    else:
        res = NO_GREGORIAN.format(year)
    print(res)


#leap_year(int(input("Input year: ")))

# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN = 1
MAX = 999
DECIMAL_DIV = 10
HUNDRED_DIV = 100


def play_with_num():
    num = 0
    res = 0
    type_num = ''
    while not (MIN < num < MAX):
        num = int(input('Input number: '))

    if num // HUNDRED_DIV > 0:
        type_num = 'three-digit'
        res = str(num)
        res = int(res[::-1])
    elif num // DECIMAL_DIV > 0:
        type_num = 'two-digit'
        res = (num % DECIMAL_DIV) * (num // DECIMAL_DIV)
    else:
        type_num = 'one-digit'
        res = num ** 2
    print(f'Your number is {type_num}. Result is: {res}')

play_with_num()

