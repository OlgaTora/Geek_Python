"""
Контекст
Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
ли target в array. Такую процедуру будем называть поиском.
Задача
Реализовать императивную функцию поиска элементов на языке Python.
Реализовать декларативную функцию поиска элементов на языке Python.
"""


def search_imperative(arr: list, target: float):
    for i in arr:
        if i == target:
            return True
        return False

def search_declarative(arr: list, target: float):
    if target in arr:
        return True
    return False

if __name__ == '__main__':
    arr = [1, 2, 5, 7]
    target = 21
    print(search_imperative(arr, target))
    print(search_imperative(arr, target))