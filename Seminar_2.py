# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  - 6782 -> 23 - 0,56 -> 11

#n = input('Input float number: ')
#
#
# def to_int(n):
#     if ',' in n:
#         n = n.replace(',', '')
#     result = int(n)
#     return result
#
#
# def sum_num(n):
# #     summa = n % 10
# #     while n // 10 != 0:
# #         n = n // 10
# #         summa += n % 10
# #     return print(f'Sum is: {summa}')
# #
# # result = to_int(n)
# # sum_num(result)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Input number: '))
# my_list = [1]
# multy = 1
# for i in range(1, N):
#     multy *= (i + 1)
#     my_list.append(multy)
# print(my_list)

# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму
# в виде словаря {}

# n = int(input("Input number "))
# dict = {}
# dict = {i : round((1 + 1 / i) ** i, 2) for i in range(1, n + 1)}
# print(dict)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
#
# N = int(input('Input number '))
# my_list = [i for i in range(-abs(N), abs(N) + 1)]
# print(f'Your list is: {my_list}')


# def get_numbers(file):
#     with open(file) as file:
#         for index, line in enumerate(file):
#             if index == 0:
#                 x1 = int(line)
#             if index == 1:
#                 x2 = int(line)
#     return x1, x2
#
#
# x1, x2 = get_numbers("file.txt")
# print(f'Result is: {my_list[x1] * my_list[x2]}')

# Реализуйте алгоритм нахождения рандомного числа.
# Тут возможны разные вариации, я так понимаю, что важно саму суть понять
# from math import floor
# from time import monotonic
#
# n = monotonic()
# print(f'Random number is: {floor(n % 100) * floor(n % 10)}')

# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов * -3. *Пример: * - Для N = 5: 1, -3, 9, -27, 81

# N = int(input())
# a = 1
# for i in range(N):
#     a = a * (-3)
#     print(a, end='')

# 2. Для натурального n создать словарь индекс-значение, состоящий из
# элементов последовательности 3n + 1.
# *Пример:* - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input())
# dict = {}
#
# for i in range(1, n + 1):
#     dict[i] = i * 3 + 1
# print(dict)

# Напишите программу, в которой пользователь будет задавать две строки
# а программа - определять количество вхождений одной строки в другой.

# str_1 = input()
# str_2 = list(input().split(' '))
# count = 0
# for i in str_2:
#     if i == str_1:
#         count += 1
# print(count)
