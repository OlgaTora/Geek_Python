"""
Расчет корреляции Пирсона в функциональной парадигме
coef = cov_x_y / std_x * std_y 
std - стандартное отклонение
cov - ковариация
"""
import statistics
import numpy as np


def get_coef_pirson(array_1: list, array_2: list):
    std_1 = np.sqrt(sum(map(np.square, map(lambda x: x - statistics.mean(array_1), array_1))) / (len(array_1) - 1))
    std_2 = np.sqrt(sum(map(np.square, map(lambda x: x - statistics.mean(array_2), array_2))) / (len(array_2) - 1))
    cov = sum(map(lambda x, y: (x - statistics.mean(array_1)) * (y - statistics.mean(array_2)), array_1, array_2)) / (
                len(array_1) - 1)
    pirson = round(cov / (std_1 * std_2), 2)
    return f'Pirson = {pirson}'


if __name__ == '__main__':
    array_1 = [1, 2, 3, 4, 5]
    array_2 = [1, -3, 5, -7, 9]
    print(get_coef_pirson(array_1, array_2))
