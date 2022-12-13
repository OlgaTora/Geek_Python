from user_int import input_data_complex, input_symb

result = 0


def to_complex():
    lst = input_data_complex()
    num = complex(lst[0], lst[1])
    return num


def remove_brackets(result):
    result = result.replace('(', '').replace(')', '')
    return result


def calc_complex():
    global result
    a = to_complex()
    b = to_complex()
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

