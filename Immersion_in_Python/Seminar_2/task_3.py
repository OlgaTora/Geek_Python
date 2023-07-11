#  Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BIN = 2
OCT = 8


def get_data() -> tuple[int, int]:
    promt: str = input('Input number and numeration: ')
    num, numeration = promt.split()
    while not num.isdigit() or int(numeration) not in (BIN, OCT):
        promt = input('Its a wrong. Try again! ')
        num, numeration = promt.split()
    return int(num), int(numeration)


def transform(num: int, numeration: int) -> str:
    result: str = ''
    while num > 0:
        result = str(num % numeration) + result
        num //= numeration
    return result


num, numeration = get_data()
print(f'result is: {transform(num, numeration)}')
print(oct(num)[2::])
print(bin(num)[2::])
