# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

data = 'k: exit'
data = data.split(':')
print(data[1][1::])

#
# HEX_DIV = 16
#
#
# def get_data() -> tuple[int, int]:
#     promt: str = input('Input number and numeration: ')
#     num, numeration = promt.split()
#     while not num.isdigit():
#         promt = input('Its a wrong. Try again! ')
#         num, numeration = promt.split()
#     return int(num), int(numeration)
#
#
# def transform(num: int, numeration: int) -> str:
#     result: str = ''
#     while num > 0:
#         result = str(num % numeration) + result
#         num //= numeration
#     return result
#
#
# num, numeration = get_data()
# print(f'result is: {transform(num, numeration)}')
# print(oct(num)[2::])
# print(bin(num)[2::])
