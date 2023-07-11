from aiogram.dispatcher.filters.state import StatesGroup, State
from fractions import Fraction


class UserInputRat(StatesGroup):
    first_rat_num = State()
    symbol = State()
    second_rat_num = State()


class UserInputComp(StatesGroup):
    first_comp_num = State()
    symbol = State()
    second_comp_num = State()


def get_data(file):
    with open(file) as file:
        return file.read()


def to_rational(num):
    num = num.split('/')
    num = Fraction(int(num[0]), int(num[1]))
    return float(num)


def to_complex(num):
    num = num[:-1]
    num = num.split('+')
    num = complex(int(num[0]), int(num[1]))
    return num


def calc(first_num, second_num, symb):
    res = 0
    if symb == '+':
        res = first_num + second_num
    elif symb == '-':
        res = first_num - second_num
    elif symb == '*':
        res = first_num * second_num
    elif symb == '/':
        res = first_num / second_num
    return res


def is_valid_rational(message):
    try:
        to_rational(message)
        return True
    except:
        return False


def is_valid_complex(message):
    try:
        if message[-1] != 'j':
            return False
        else:
            to_complex(message)
            return True
    except:
        return False


def check_complex_res(res):
    res = str(res).replace('(', '').replace(')', '')
    if res[res.find('j') - 1] == '0':
        res = res[:-3]
    return res

