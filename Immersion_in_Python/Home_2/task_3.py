# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions as fr


def get_data() -> tuple[str, str]:
    data: str = input('Input two rational numbers with symbol / ')
    a, b = data.split()
    return a, b


def split_rational(num: str) -> tuple[int, int]:
    first_num, second_num = map(int, num.split('/'))
    return first_num, second_num


def join_rational(first_num: int, second_num: int) -> str:
    result: str = "/".join([str(first_num), str(second_num)])
    return result


def get_lcm(first_num: int, second_num: int) -> int:
    if first_num > second_num:
        larger = first_num
    else:
        larger = second_num
    while True:
        if larger % first_num == 0 and larger % second_num == 0:
            lcm = larger
            break
        larger += 1
    return lcm


def get_gcd(first_num: int, second_num: int) -> int:
    if second_num == 0:
        return first_num
    return get_gcd(second_num, first_num % second_num)


def reduce_fraction(first_num, second_num):
    gcd = get_gcd(first_num, second_num)
    first_num_res = first_num // gcd
    second_num_res = second_num // gcd
    return first_num_res, second_num_res


def calc_summ(first_num_a: int, second_num_a: int, first_num_b: int,
              second_num_b: int) -> str:
    lcm: int = get_lcm(second_num_a, second_num_b)
    first_num_c: int = int(first_num_a * lcm / second_num_a + first_num_b * lcm / second_num_b)
    second_num_c: int = lcm
    first_num_c, second_num_c = reduce_fraction(first_num_c, second_num_c)
    result: str = join_rational(first_num_c, second_num_c)
    return result


def calc_multy(first_num_a: int, second_num_a: int, first_num_b: int,
               second_num_b: int) -> str:
    first_num_c: int = first_num_a * first_num_b
    second_num_c: int = second_num_a * second_num_b
    first_num_c, second_num_c = reduce_fraction(first_num_c, second_num_c)
    result: str = join_rational(int(first_num_c), int(second_num_c))
    return result


def check_module_fractions(first_num_a: int, second_num_a: int, first_num_b: int,
                           second_num_b: int) -> tuple[fr.Fraction, fr.Fraction]:
    f_first = fr.Fraction(first_num_a, second_num_a)
    f_second = fr.Fraction(first_num_b, second_num_b)
    summ: fr.Fraction = f_first + f_second
    multy: fr.Fraction = f_first * f_second
    return summ, multy


try:
    a, b = get_data()
    first_num_a, second_num_a = split_rational(a)
    first_num_b, second_num_b = split_rational(b)
    multy: str = calc_multy(first_num_a, second_num_a, first_num_b, second_num_b)
    summ: str = calc_summ(first_num_a, second_num_a, first_num_b, second_num_b)
    summ_f, multy_f = check_module_fractions(first_num_a, second_num_a, first_num_b, second_num_b)

    print(f'Summa of {a} and {b} = {summ}')
    print(f'Using modul fraction. Summa of {a} and {b} = {summ_f}')
    print('------------------------------------------------------')
    print(f'Multy of {a} and {b} = {multy}')
    print(f'Using modul fraction. Multy of {a} and {b} = {multy_f}')
except ValueError:
    print('Error! You have to input two rational numbers with symbol / ')
except ZeroDivisionError:
    print('Error! Its not possible divide by zero')
