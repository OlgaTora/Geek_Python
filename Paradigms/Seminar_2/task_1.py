"""
Рассмотрим следующую задачу. Необходимо реализовать программу, которая:
Получает на вход: список li и число n
Возвращает: количество элементов в списке li равных этому заданному числу n
"""

# Structured
li = [1, 5, 3, 11, 4, 3, 6, 1]
n = 1
counter = 0
for el in li:
    if el == n:
        counter += 1


# Procedured
def count_n(n: int, li: list):
    counter = 0
    for el in li:
        if el == n:
            counter += 1
    return counter


count_n(n, li)
