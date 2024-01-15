"""
Для разогрева на первое домашнее задание будет каноническая задача сортировки списка.
Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном/декларативном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки
"""


def sort_array_imperative(arr: list):
    for i in range(0, len(arr) - 1):
        biggest = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[biggest]:
                biggest = j
        arr[i], arr[biggest] = arr[biggest], arr[i]
    return arr


def sort_array_declarative(arr: list):
    return sorted(arr, reverse=True)


if __name__ == '__main__':
    arr = [1, 5, 7, 3, 5, 9, 11, -1, 0, 0, -2, -4, 13]
    print(sort_array_imperative(arr))
    print(sort_array_declarative(arr))
