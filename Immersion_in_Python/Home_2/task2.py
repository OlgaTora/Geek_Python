# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_DIV = 16
DICT_HEX = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f'}


def get_data() -> int:
    try:
        number: int = int(input('Input number: '))
    except ValueError:
        number = int(input('Its a wrong. Try again! '))
    return number


def transform(num: int, numeration: int) -> str:
    result: str = ''
    while num > 0:
        remains: str = str(num % numeration)
        if remains in DICT_HEX.keys():
            remains = DICT_HEX.get(remains)
        result = remains + result
        num //= numeration
    return result


def check_result(num: int):
    result_without_hex: str = transform(num, HEX_DIV)
    result_hex: str = hex(num)[2::]
    if result_without_hex == result_hex:
        print(f"This function is right, result is: {num} in 10 = {result_without_hex} in 16")

num = get_data()
check_result(num)

