"""
Напишите программу, которая выводит
на экран числа от 1 до 100.
При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
Вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
*Превратите решение в генераторное выражение.
"""

MIN_NUM = 1
MAX_NUM = 100
MULTIPLE_1 = 3
MULTIPLE_2 = 5

PRINT_MULT_1 = 'Fizz'
PRINT_MULT_2 = 'Buzz'
PRINT_MULT_1_2 = 'FizzBuzz'

for i in range(MIN_NUM, MAX_NUM):
    if i % (MULTIPLE_1 * MULTIPLE_2) == 0:
        i = PRINT_MULT_1_2
    elif i % MULTIPLE_1 == 0:
        i = PRINT_MULT_1
    elif i % MULTIPLE_2 == 0:
        i = PRINT_MULT_2
    # print(i, end=' ')

gen = (PRINT_MULT_1_2 if i % (MULTIPLE_1 * MULTIPLE_2) == 0 else PRINT_MULT_1
if i % MULTIPLE_1 == 0 else PRINT_MULT_2 if i % MULTIPLE_2 == 0 else i for i in range(MIN_NUM, MAX_NUM))
print(*gen)

