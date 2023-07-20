"""
Создайте функцию-генератор.
Функция генерирует N простых чисел,
начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя»
"""


def gen_simple_nums(num: int):
    curr_num: int = 2
    while 1 < curr_num < num:
        is_prime: bool = True
        for i in range(2, curr_num // 2 + 1):
            if curr_num % i == 0:
                curr_num += 1
                is_prime = False
                break
        if is_prime:
            yield curr_num
            curr_num += 1

for number in (gen_simple_nums(50)):
    print(number, end=' ')

