"""
Создайте функцию генератор чисел Фибоначчи
"""
# 1 1 2 3 5 8 13 21


def gen_fibonacci(num: int):
    fib1 = 1
    fib2 = 1
    for i in range(1, num + 1):
        if i == 1 or i == 2:
            fib = 1
        else:
            fib = fib1 + fib2
        yield fib
        fib2 = fib1
        fib1 = fib


for i, number in enumerate(gen_fibonacci(7), start=1):
    print(f'fib {i} = {number:>2}', end='\n')

