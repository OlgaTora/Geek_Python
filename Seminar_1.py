# # -*- coding: utf-8 -*-
# Seminar_1_Geek

# Напишите программу, которая принимает на вход цифру, обозначающую день недели
# и проверяет, является ли этот день выходным.
# Пример: - 6 -> да  - 7 -> да  - 1 -> нет

# day = int(input("Input number of Day of Week - "))
# if 0 > day or day > 7:
#     print('Wrong day')
# elif 5 < day < 8:
#     print('yes')
# else:
#     print('no')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# не (X или Y или Z) = не X  и не Y и не Z) для всех значений предикат

# for X in range(0, 2):
#     for Y in range(0, 2):
#         for Z in range(0 ,2):
#             if not (X or Y or Z) == (not X and not Y and not Z):
#                 print(f'TRUE X = {X}, Y = {Y}, Z = {Z}')

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример: - x=34; y=-30 -> 4   - x=2; y=4-> 1  - x=-34; y=-30 -> 3

# x = int(input("Input X - "))
# y = int(input("Input Y - "))
#
# if x == 0 or y == 0:
#     print('Wrong coordinates')
# elif x > 0:
#     if y > 0:
#         print('1')
#     else:
#         print('4')
# else:
#     if y > 0:
#         print('2')
#     else:
#         print('3')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
# num = int(input('Input '))
# if 4 < num < 1:
#     print('Wrong number')
# elif num == 1:
#     print('x > 0 and y > 0')
# elif num == 2:
#     print('x < 0 and y > 0')
# elif num == 3:
#     print('x < 0 and y < 0')
# else:
#     print('x > 0 and y < 0')

# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
# Пример: - A (3,6); B (2,1) -> 5,09  - A (7,-5); B (1,-1) -> 7,21

# x1 = int(input("Input X1 - "))
# y1 = int(input("Input Y1 - "))
#
# x2 = int(input("Input X2 - "))
# y2 = int(input("Input Y2 - "))
#
# distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)
# print(f'Distance is: {distance}')

# Сравнить 4 числа
# my_list = []
# a = int(input('input A: '))
# my_list.append(a)
# b = int(input('input B: '))
# my_list.append(b)
# c = int(input('input C: '))
# my_list.append(c)
# d = int(input('input D: '))
# my_list.append(d)
# maximum = my_list[0]
# for i in range(1, len(my_list)):
#     if my_list[i] > maximum:
#         maximum = my_list[i]
# print(maximum)


# Вводится число и выводятся числа от - числа до числа

# n = int(input('Input n: '))
# for i in range(-abs(n), abs(n) + 1):
#     print(i, end=' ')

#Вернуть первое число дробной части (можно делать и через строку - число после точки)
# n = float(input('Input n: '))
# first = int(n * 10 % 10)
#
# print(f'Первое число после дроби: {first}')

# кратно ли число 10, 5,  или 15 и не кратно 30

# num = int(input("Input number: "))
# if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
#     print('YES')
# else:
#     print('NO')


# Напишите программу для вычисления и вывода суммы квадратов элементов списка numbers.
# Примечание. Попробуйте решить задачу двумя способами: с помощью функции reduce(), и с помощью функций map() и sum().
# Напишите программу для вычисления и вывода суммы квадратов двузначных чисел, которые делятся на 77 без остатка.
# Примечание 1. При решении задачи используйте функции filter(), map() и sum().
# Примечание 2. На 77 должно делиться исходное двузначное число, а не его квадрат.
# Примечание 3. Не забывайте про отрицательные двузначные числа.
#
# my_array = [-11, -15, 77, -77]
#
#
# def map(function, items):
#     result = []
#     for item in items:
#         new_item = function(item)
#         result.append(new_item)
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def dif_77(x):
#     return x % 77 == 0
#
#
# def squares(x):
#     return x**2
#
# res1 = sum(map(squares, filter(dif_77, my_array)))
# print(res1)
#
#
# def add(x, y):
#     return x**2 + y**2
#
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in filter(dif_77, items):
#         acc = operation(acc, item)
#     print(acc)
#     return acc
#
# res = reduce(add, my_array, 0)
# print(res)

#Напишите функцию func_apply(), принимающую на вход функцию и список значений и
# возвращающую список, в котором каждое значение будет результатом применения переданной функции к переданному списку.
#Примечание 1. Приведенный ниже код, при условии, что функция func_apply() написана правильно

# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def func_apply(function, items):
#     result = []
#     for item in items:
#         new_item = function(item)
#         result.append(new_item)
#     return result
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
# print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
# print(func_apply(str, [1, 2, 3, 4, 5, 6]))

# Требовалось написать программу, которая:
# преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
# фильтрует список words  и оставляет только палиндромы длиной более 4 символов;
# находит произведение чисел из списка numbers.
# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num, 1), floats))
# filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

#Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce()
#выводит в алфавитном порядке список primary городов с населением более 12 млн человек, в формате:
#Cities: Beijing, Buenos Aires, ...
#Примечание 1. использование встроенных функций filter(), map(), sorted() и reduce()
#Примечание 2. Ставить запятую в конце вывода не нужно.

from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]
cities = sorted(list(filter(lambda name: name[1] > 15000000, data)))
print(cities)

#Напишите функцию func, используя синтаксис анонимных функций, которая
# принимает целочисленный аргумент и возвращает значение True, если он делится без остатка
# на 19 или на 13 и False в противном случае.

#func = lambda x: x % 19 == 0 or x % 13 == 0
# def func(x):
#     return x % 19 == 0 or x % 13 == 0

#Напишите функцию func, используя синтаксис анонимных функций, которая принимает
# строковый аргумент и возвращает значение True, если переданный аргумент начинается
# и заканчивается на английскую букву a (регистр буквы неважен) и False в противном случае.

#func = lambda s.lower(): s.endswith('a') & s.startswith('a')
# def func(s):
#     s = s.lower()
#     return s.endswith('a') & s.startswith('a')


#Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, которая
# принимает строковый аргумент и возвращает значение True, если переданный аргумент
# является неотрицательным числом (целым или вещественным) и False в противном случае.

# is_non_negative_num = lambda x: list(x == x.isdigit and x > 0)
#
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))
#

# False
# True
# False
# False
# True
# False
# False
# True

#Примечание 2. Неотрицательные числа — это положительные числа и число нуль.



#Напишите программу, которая с помощью встроенных функций filter() и sorted()
# выводит слова из списка words, имеющие длину ровно 6 символов. Слова следует вывести в
# алфавитном порядке на одной строке, разделив символом пробела.

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday',
#          'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday',
#          'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate',
#          'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide',
#          'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
# print(*sorted(list(filter(lambda s: len(s) == 6, words))))


#Напишите программу, которая с помощью встроенных функций map() и filter() удаляет
# из списка numbers все нечетные элементы, большие 47, а все четные элементы нацело делит на два
# (целочисленное деление – //).
# Полученные числа следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок.

numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81,
           66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72,
           32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39
    , 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
print(list(filter(lambda num: num > 47 if num % 2 == 1 else map(lambda num: num // 2, numbers), numbers)))


