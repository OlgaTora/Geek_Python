# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions as fr


def get_data() -> tuple[int, int]:
    data: str = input('Input two rational numbers with symbol / ')
    if data.count('/') < 2:
        print('Invalid data')
    a, b = data.split()
    return a, b


def split_rational(num: str) -> tuple[int, int]:
    first_num, second_num = map(int, num.split('/'))
    return first_num, second_num


def join_rational(first_num: int, second_num: int) -> str:
    result: str = "/".join([str(first_num), str(second_num)])
    return result


def calc_lcm(first_num: int, second_num:int):
    lcm: int = 1
    if first_num > second_num:
        greater = first_num
    else:
        greater = second_num
    while True:
        if greater % first_num == 0 and greater % second_num == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def calc_summ(first_num_a: int, second_num_a: int, first_num_b: int, second_num_b: int) -> str:
    lcm: int = calc_lcm(second_num_a, second_num_b)
    first_num_c: int = int(first_num_a * lcm / second_num_a + first_num_b * lcm / second_num_b)
    second_num_c: int = lcm
    result = join_rational(first_num_c, second_num_c)
    return result


def calc_multy(first_num_a: int, second_num_a: int, first_num_b: int, second_num_b: int) -> str:
    first_num_c: int = first_num_a * first_num_b
    second_num_c: int = second_num_a * second_num_b
    result: str = join_rational(first_num_c, second_num_c)
    return result


def check_module_fractions(first_num_a: str, second_num_a: str, first_num_b: str, second_num_b: str)\
        -> tuple[fr.Fraction, fr.Fraction]:
    f_first = fr.Fraction(first_num_a, second_num_a)
    f_second = fr.Fraction(first_num_b, second_num_b)
    summ = f_first + f_second
    multy = f_first * f_second
    return summ, multy


a, b  = get_data()
first_num_a, second_num_a = split_rational(a)
first_num_b, second_num_b = split_rational(b)
multy: str = calc_multy(a, b)
summ: str = calc_summ(a, b)
summ_f, multy_f = check_module_fractions(a, b)
print(f'Summa of {a} and {b} = {summ}')
print(f' Use modul fraction. Summa of {a} and {b} = {summ_f}')
print(f'Multy of {a} and {b} = {multy}')
print(f' Use modul fraction. Multy of {a} and {b} = {multy_f}')

# СОКРАТИТЬ ЕЩЕ