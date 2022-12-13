from fractions import Fraction
from user_int import input_data_rational, input_symb

result = 0


def to_rational():
    lst = input_data_rational()
    num = Fraction(lst[0], lst[1])
    return num


def remove_brackets(result):
    result = result.replace('(', '').replace(')', '')
    return result


def calc_rational():
    global result
    a = to_rational()
    b = to_rational()
    symb = input_symb()
    if symb == '+':
        result = f'{a} + {b} = {a + b}'
    elif symb == '-':
        result = f'{a} - {b} = {a - b}'
    elif symb == '*':
        result = f'{a} * {b} = {a * b}'
    elif symb == '/':
        result = f'{a} / {b} = {a / b}'
    result = remove_brackets(result)
    return result
