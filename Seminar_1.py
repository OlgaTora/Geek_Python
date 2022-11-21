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

