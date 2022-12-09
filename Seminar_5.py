# 	Напишите программу, удаляющую из текста все слова содержащие "abc"
# s = [i for i in input().split(' ')]
# for i in s:
#     if 'abc' in i:
#         i = i.replace('abc', '')
#         print(i, end=' ')
# abcsjfdk djflgabc

# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Игра против интеллектуального бота
#
# from game_conf_engine import candy_quantity, take_from, game_over, seach_residue, bot, whose_move
#
# user_number = whose_move()
# quantity = total_quantity = 0
# print(f'Господа! У нас в игре {candy_quantity()} конфет!')
# print(10 * '- ')
#
#
# while True:
#     print(f'В игру вступает игрок {user_number} !!!')
#     if user_number == 1:
#         quantity = int(input(f'Барабанная дробь! Игрок {user_number} "ЧЕЛОВЕК" берет конфеты: '))
#     else:
#         print(f'Барабанная дробь! Игрок {user_number} "БОТ" берет конфеты: ', end='')
#         quantity = bot()
#         print(quantity)
#
#     step_success = take_from(quantity)
#
#     if step_success:
#         user_number = 2 if user_number == 1 else 1
#         total_quantity += quantity
#         print(f'Осталось конфеток на кону {seach_residue(total_quantity)}')
#         print(10 * '- ')
#     else:
#         print('Вы совершате ошибку! Вы можете взять от 1 до 28 конфет')
#
#     if game_over():
#         break
#
# print(f'Респект игрок номер {user_number}, вы выиграли!')

# крестики нолики
# Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих фигуры по вертикали,
# горизонтали или диагонали, выигрывает. Первый ход делает игрок, ставящий крестики.
# Обычно по завершении партии выигравшая сторона зачёркивает чертой свои три знака (нолика или крестика), составляющих сплошной ряд.

# from engine_xo import game_over, step_player, count_step, play_again
#
# user_number = 'КРЕСТИК'
# symb = 'X'
# counter = 0
#
# while True:
#
#     print(f'В игру вступает мастер {user_number} ')
#     print('-*' * 15)
#
#     step = [(int(i) - 1) for i in input(f'Введите координаты хода за {user_number}: ').split(' ')]
#     try:
#         step_success = step_player(step, symb)
#         print('-*' * 15)
#     except IndexError:
#         print(f'Разуй глаза, {user_number}, размер поля: 3 х 3')
#         print('-*' * 15)
#         continue
#
#     if step_success:
#         user_number = 'НОЛИК' if user_number == 'КРЕСТИК' else 'КРЕСТИК'
#         symb = '0' if symb == 'X' else 'X'
#         counter += 1
#
#     else:
#         print('УПППС! Клетка уже занята!')
#
#     if count_step(counter):
#         print(f'Крепитесь, у вас НИЧЬЯ!')
#         answer = int(input('Играем еще? 1 - да, 0 - нет'))
#         play = play_again(answer)
#         if play:
#             continue
#         else:
#             break
#
#     if game_over():
#         user_number = 'НОЛИК' if user_number == 'КРЕСТИК' else 'КРЕСТИК'
#         print(f'Выиграл {user_number}')
#         print('-*' * 15)
#         answer = int(input('Играем еще? 1 - да, 0 - нет: '))
#         play = play_again(answer)
#         if play:
#             continue
#         else:
#             break

# 	Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# 	входные и выходные данные хранятся в отдельных текстовых файлах
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# 5a29v4s3D3d2F4g2O3i2a

# with open('seminar_5_2.txt') as file:
#     s = list(''.join(file.read()))
#
#
# def encoder(s):
#     new_s = ''
#     count = 1
#     fnd = s[0]
#     for i in range(1, len(s)):
#         if fnd == s[i]:
#             count += 1
#             if i == len(s) - 1:
#                 new_s += str(count) + s[i - 1]
#         else:
#             new_s += str(count) + s[i - 1]
#             fnd = s[i]
#             count = 1
#     return new_s
#
# new_s = encoder(s)
# print(new_s)
#
#
# def decoder(new_s):
#     new_s = list(''.join(new_s))
#     s = ''
#     num = ''
#     for i in new_s:
#         if i.isdigit():
#
#             num += str(i)
#         else:
#             s += (int(num) * i)
#             num = ''
#     return s
#
# print(decoder(new_s))
# with open('file_seminar_5_3.txt', 'w') as file:
#     file.write(str(s))

# в строке не хватает одного числа, его надо добавить
#
# with open('file_seminar_5.txt') as file:
#     s = list(map(int, file.read().split(' ')))
#
# for i in range(len(s) - 1):
#     if s[i + 1] - s[i] > 1:
#         fnd = s[i] + 1
#         print(fnd)
#         s.insert(i + 1, fnd)
# s = ' '.join(list(map(str, s)))
# print(s)
#
# with open('file_seminar_5.txt', 'w') as file:
#     file.write(s)


# Найти НОК и НОД
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Комм: Простые числа делятся на себя и 1

# n, m  = map(int, input("Input two numbers: ").split(' '))
# if n == 0:
#     print('Try another number!')
# elif m == 0:
#     print('Try another number!')
#
#
# def seach_dif(number):
#     dif = 2
#     lst = [0] * number
#     while dif < number:
#         if number % dif == 0:
#             number //= dif
#             lst.append(dif)
#         dif += 1
#
#     lst = set(lst)
#     lst.remove(0)
#     return lst
#
# lst_n = seach_dif(n)
# lst_m = seach_dif(m)
# nok_search = lst_n.intersection(lst_m)
# nok = 1
# for i in nok_search:
#     nok *= i
#
# nod = n * m // nok
# print(f'НОД = {nod} НОК = {nok}')
