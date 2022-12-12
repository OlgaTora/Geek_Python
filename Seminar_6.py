# 	Написать программу вычисления арифметического выражения заданного строкой.
# 	Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# 	Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;
#   Реализовано для + чисел

x = 13 / 22 * 4 / (6 + 2 * 2) - 3.5 + 16 * 12 - (3 + 5 * 2)
print(f'Для проверки ответа: {x} ')

s = '13 / 22 * 4 / ( 6 + 2 * 2 ) - 3.5 + 16 * 12 - ( 3 + 5 * 2 )'
s = s.split(' ')

def arithmetic(num1, num2, num_operator):
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x / y, }
    try:
        return op[num_operator](num1, num2)
    except KeyError:
        return 'Я работаю только с +-*/'


def operation(symb, data):
    index = data.index(symb)
    data[index - 1] = arithmetic(float(data[index - 1]), float(data[index + 1]), symb)
    del (data[index + 1])
    del (data[index])


def calculation(s):
    while '*' in s or '/' in s:
        if s.count('*') > 0 and s.count('/') > 0:
            if s.index('*') < s.index('/'):
                operation('*', s)
            else:
                operation('/', s)

        else:
            if '*' in s:
                operation('*', s)
            elif '/' in s:
                operation('/', s)

    while '+' in s or '-' in s:
        if s.count('+') > 0 and s.count('-') > 0:
            if s.index('+') < s.index('-'):
                operation('+', s)

            else:
                operation('-', s)

        else:
            if '+' in s:
                operation('+', s)
            elif '-' in s:
                operation('-', s)

    return s[0]


while len(s) > 1:
    while '(' in s:
        s_part = s[s.index('(') + 1:s.index(')')]
        s = s[:s.index('(') + 1] + s[s.index(')') + 1::]
        s[s.index('(')] = calculation(s_part)
    else:
        calculation(s)

print('Ваш результат: ', end='')
print(*s)

# Задача: предложить улучшения кода(3-5задач) для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
#Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
from math import factorial
N = int(input('Input number: '))
multy = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
lst = [multy(i) for i in range(1, N +1)]
print(lst)

# 2. Напишите программу, удаляющую из текста все слова содержащие "abc"
s = 'abcsjfdk djflgabc'
result = lambda x: x.replace('abc', '')
print(result(s))


# 3. Сравнить 4 числа
my_list = [int(i) for i in input('Input: ').split(' ')]
result = lambda x: max(x)
print(result(my_list))


# 4. Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример: - A (3,6); B (2,1) -> 5,09  - A (7,-5); B (1,-1) -> 7,21
a = [float(i) for i in input('Введите координаты точки A: ').split(',')]
b = [float(i) for i in input('Введите координаты точки B: ').split(',')]
distance = 0
for i, j in zip(a, b):
  distance += (i-j)**2
print(f'Расстояние между A и B = {round(distance**.5, 2)}')

# 5. # Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# # элементов исходной последовательности.
# вариант 1
lst = [11, 23, 45, 45, 11, 11, 24]
dict = {i: lst.count(i) for i in lst}
lst_new = dict.keys()
print(*lst_new)
# # вариант 2
lst = set(lst)
print(*lst)

# 6. # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# #  - 6782 -> 23 - 0,56 -> 11

n = [i for i in input('Input number: ').split(',')]
n = list(map(int, ''.join(n)))
print(f'Sum is: {sum(n)}')

#7. # Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
lst = [11, 23, 45, 45, 11, 11, 24]
lst_new = []
for count, i in enumerate(lst):
    if count % 2 != 0:
        lst_new.append(i)

summa = sum(lst_new)
print(f'Sum is: {summa}')

