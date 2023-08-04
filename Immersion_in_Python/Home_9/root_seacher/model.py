from random import randint
import csv
from wrappers import FileName, save_to_json, search_root_from_scv
import constants as c

file_name = FileName()


@search_root_from_scv(file_name)
@save_to_json
def search_root(*args, **kwargs) -> str:
    """Нахождение корней квадратного уравнения"""
    a, b, c = map(int, args)
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


def gen_csv(file_name: str):
    """Генерация csv файла с тремя случайными числами в каждой строке.
    100-1000 строк.
    """
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        data = csv.writer(csv_file, dialect='excel')
        for _ in range(randint(c.MIN_ROWS, c.MAX_ROWS)):
            nums_list = []
            for _ in range(c.QUANTITY_IN_ROW):
                nums_list.append(str(randint(c.MIN_NUMBER, c.MAX_NUMBER)))
            data.writerow(nums_list)

