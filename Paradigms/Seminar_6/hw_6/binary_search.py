"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.
"""


def binary_search(arr: list, num: int):
    if len(arr) == 0:
        raise ValueError('Array is empty')
    if len(arr) == 1:
        if num == arr[0]:
            return 0
        else:
            return -1
    left: int = 0
    right: int = len(arr) - 1
    while left <= right:
        middle_id: int = (left + right) // 2
        middle_value = arr[middle_id]
        if middle_value < num:
            left = middle_id + 1
        elif middle_value > num:
            right = middle_id - 1
        else:
            return middle_id
    return -1


if __name__ == '__main__':
    arr_1 = [2, 4, 8, 11, 25, 123, 1015, 1021]
    arr_2 = [25]
    arr_3 = []
    num = 25
    print(binary_search(arr_1, num))
    print(binary_search(arr_2, num))
    print(binary_search(arr_3, num))
