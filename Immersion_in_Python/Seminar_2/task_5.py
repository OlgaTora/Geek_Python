# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.


a, b, c = map(int, input('Input coefficients: ').split())


def find_root(a: int, b: int, c: int) -> str:
    result: str = ''
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = (- b - d ** 0.5) / 2 * a
        x_2 = (- b + d ** 0.5) / 2 * a
        result = f'Two roots: x1 = {x_1} x2 = {x_2}'
    elif d == 0:
        x_1 = - b / (2 * a)
        result = f'One roots: x = {x_1}'
    else:
        d = complex(d, 0)
        x_1 = (- b - d ** 0.5) / 2 * a
        x_2 = (- b + d ** 0.5) / 2 * a
        result = f'Two complex roots: x1 = {x_1} x2 = {x_2}'
    return result


print(find_root(a, b, c))
