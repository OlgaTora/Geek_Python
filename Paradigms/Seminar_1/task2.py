"""
Условие
На вход подается: список целых чисел arr
● Задача
Реализовать функцию, которая возвращает три числа:
○ Долю позитивных чисел
○ Долю нулей
○ Долю отрицательных чисел
"""


def search_part_imperative(arr: list):
    zero, negative, positive = 0, 0, 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i == 0:
            zero += 1
        else:
            negative += 1
    return f'Posivite = {round(positive / len(arr), 2)},\n' \
           f'negative = {round(negative / len(arr), 2)},\n' \
           f'zero = {round(zero / len(arr), 2)}'


def search_part_declrative(arr: list):
    zero = len(list(filter(lambda x: x == 0, arr)))
    negative = len(list(filter(lambda x: x < 0, arr)))
    positive = len(list(filter(lambda x: x > 0, arr)))
    counts = [zero, negative, positive]
    return list(map(lambda count: round(count / len(arr), 2), counts))


if __name__ == '__main__':
    arr = [1, 2, 5, 0, 0, 0, 11, 12, -11, -2, 11, 0, -3]
    print(search_part_imperative(arr))
    print(search_part_declrative(arr))
