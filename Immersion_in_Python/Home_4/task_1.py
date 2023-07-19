"""
Напишите функцию для транспонирования матрицы
"""
from __future__ import annotations

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 7]]


def is_rectangle(matrix: list[[int]]) -> bool:
    for i in range(0, len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            return False
    return True


def transpose_matrix(matrix: list[[int]]) -> list[[int]] | None:
    if is_rectangle(matrix):
        rows: int = (len(matrix))
        columns: int = len(matrix[0])
        new_matrix: list[[int]] = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
        return new_matrix


result = transpose_matrix(my_matrix)
print(f'New matrix:\n{result}') if result else print('Matrix is not rectangle')
