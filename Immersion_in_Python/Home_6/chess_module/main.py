"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

Релизованы 2 варианта:
1. с кортежами координат внутри списка
2. со списками по х и у

Вариант со списками работает в несколько раз быстрее
"""
from play_chess_light_v import search_queens_v2, play_queens_v2
from play_chess import search_queens, play_queens

if __name__ == '__main__':
    #for test
    # queens = [(4, 1), (4, 2), (8, 3), (5, 4), (7, 5), (1, 6), (3, 7), (6, 8)] #x1 = x2
    # print(play_queens(queens))
    # queens = [(4, 1), (2, 1), (8, 3), (5, 4), (7, 5), (1, 6), (3, 7), (6, 8)] #y1 = y2
    # print(play_queens(queens))
    # queens = [(1, 1), (2, 2), (8, 3), (5, 4), (7, 5), (1, 6), (3, 7), (6, 8)] #diagonal
    # print(play_queens(queens))
    # queens = [(2, 6), (7, 7), (3, 9), (4, 1), (8, 2), (1, 8), (9, 4), (6, 5)]
    # print(play_queens(queens))

# v1
    # result = search_queens_v2()
    # for i in result:
    #     print(i)

#v2
    result_v2 = search_queens_v2()
    for key, value in result_v2.items():
        print(key, value)

