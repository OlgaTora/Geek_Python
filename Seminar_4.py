import math
from random import randint, uniform

# Вычислить число p c заданной точностью d
# Пример: # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = random.uniform(10**-1, 10**-10)
# Костыльное решение
d = 0.00001

counter = 2
while d < 1:
    d *= 10
    counter += 1

s = str(math.pi)
print(s[:2] + s[2:counter])

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Комм: Простые числа делятся на себя и 1

n = int(input("Input number: "))
if n == 0:
    print('Try another number!')


def eratosfen():
    lst = [i for i in range(0, n + 1)]
    dif = 2

    while dif < n:
        if lst[dif] != 0:
            i = dif * 2
            while i < n:
                lst[i] = 0
                i += dif
        dif += 1

    lst = set(lst)
    lst.remove(0)
    return lst

lst = eratosfen()
result = []

for k in lst:
    if n % k == 0 and k not in result:
        result.append(k)
        n = n // k
print(result)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

lst = [11, 23, 45, 45, 11, 11, 24]
lst_new = [] * len(lst)
for i in lst:
    if i not in lst_new:
        lst_new.append(i)
print(*lst_new)


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: # - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#*Доп задание: значения коэффициентов от -100 до 100
#
max_v = 99
min_v = 0
s = ''
#
# #реализация случайных коэф со случайным знаком
def simbol():
    if randint(1, 3) == 1:
        simb = '+'
    else:
        simb = '-'
    return simb

def coef(min_value, max_value):
    r_coef = randint(min_value, max_value)
    if r_coef > 1:
        r_coef = simbol() + ' ' + str(r_coef)
    elif r_coef == 1:
        r_coef = simbol()
    return r_coef

k = int(input('Input your number: '))

for i in range(k, -1, -1):
    coeff = coef(min_v, max_v)
    if coeff != 0:
        if i > 1:
            s += f'{coeff} X^{i} '
            if s[0] == '+':
                s = s[2:]
        elif i == 1:
            s += f'{coeff} X '
        else:
            s += f'{coeff}'
    else:
        print('')

s += ' = 0'
print(s)

with open('file_seminar_4_1', 'w') as file:
    file.write(s)

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Создадим один новый и возьмем уже имеющийся файл
#*Доп задание: для разного размера уравнения - реализован вариант одинаковой размерности

with open('file_seminar_4_2', 'w') as file_2:
    file_2.write('9 X^4 - 5 X^3 + 32 X^2 + 12 X - 87 = 0')


def get_data(file):
    with open(file) as file:
        return file.read()

s1 = get_data('file_seminar_4_1')
s2 = get_data('file_seminar_4_2')

# понять какая строка большей степени (для разных степеней)
#print(s1[s1.find('^') + 1])
#print(s2[s2.find('^') + 1]

# ищем коэф наибольший для сложения
coef = int(s1[s1.find('^') + 1])

s1 = s1.split(' ')
s2 = s2.split(' ')
# для проверки на печать
print(s1, s2, sep='\n')

s = ''

while coef > 0:
    for i in range(1, len(s1) - 2):
        if 'X' in s1[i]:

            # если оба знака одинаковые
            if s1[i - 2] == s2[i - 2]:
                if s1[i - 2] == '+':
                    s += ' +'
                else:
                    s += ' -'
                s += ' ' + str(int(s1[i - 1]) + int(s2[i - 1]))

            # если первое число больше второго
            elif int(s1[i - 1]) > int(s2[i - 1]):
                if s1[i - 2] == '-':
                    s += ' -'
                elif s2[i - 2] == '-':
                    s += ' +'
                s += ' ' + str(int(s1[i - 1]) - int(s2[i - 1]))

            # если второе число больше первого
            elif int(s2[i - 1]) > int(s1[i - 1]):
                if s2[i - 2] == '-':
                    s += ' -'
                elif s1[i - 2] == '-':
                    s += ' +'
                s += ' ' + str(int(s2[i - 1]) - int(s1[i - 1]))
            s += ' ' + s1[i]
            coef -= 1

if s1[-4] == s2[-4]:
    if s1[-4] == '+':
        s += ' +'
    else:
        s += ' -'
    s += ' ' + str(int(s1[-3]) + int(s2[-3]))
else:
    if int(s1[-3]) > int(s2[-3]):
        if s1[-4] == '-':
            s += ' -'
        else:
            s += ' +'
    elif int(s2[-3]) > int(s1[-3]):
        if s2[-4] == '-':
            s += ' -'
        else:
            s += ' +'
    s += ' ' + str(abs(int(s2[-3]) - int(s1[-3])))

# уберем лишний знак вначале
if s[1] in '+-' and s1[0] != '-' and s2[0] != '-':
    s = s[2:]

s += ' = 0'
print(s)

with open('file_seminar_4_3', 'w') as file:
    file.write(s)

# Строка содержит набор чисел. Показать большее и меньшее число

s = '7345dfdf863sdfg25fdkjgkfhga7345875fg78'
lst = [i for i in s if i in '0123456789']
print(max(lst), min(lst))
#
# # Если данные с пробелом
s = '1 2 3 4 5 2 8 1'
lst = [float(i) for i in s.split()]
print(max(lst), min(lst))

#Найти корни квадратного уравнения Ax² + Bx + C = 0
#математикой или используя дополнительные библиотеки*
#
a, b, c = int(input('Input coef a: ')), int(input('Input coef b: ')), int(input('Input coef c: '))
disc = b ** 2 - 4 * a * c
if disc < 0:
    print('No roots')
elif disc == 0:
    print(f'root is: {- b / (2 * a)}')
else:
    print(f'root is: {(- b + disc ** 0.5) / (2 * a)} and {(- b - disc ** 0.5) / (2 * a)}')

s = '9 X^2 + 32 X + 12'
lst = [i for i in s.split() if i.isdigit()]

print(lst)

