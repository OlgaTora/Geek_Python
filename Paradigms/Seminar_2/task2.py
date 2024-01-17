"""
След матрицы: структурный
● Контекст
След матрицы - это сумма чисел на её главной диагонали. След определён только для квадратных матриц
(количество столбцов = количеству строк).
● Задача
Реализовать чисто структурную реализацию вычисления следа для любой матрицы NxN.
"""
# Structured
matrix = [1, 5, 2], [4, 6, 3], [6, 3, 1]
steps = len(matrix[0])
trace = sum([matrix[i][i] for i in range(steps)])
print(trace)


# Procedured
def count_trace(matrix):
    steps = len(matrix[0])
    trace = sum([matrix[i][i] for i in range(steps)])
    print(trace)


matrix = [1, 5, 2], [4, 6, 3], [6, 3, 1]
count_trace(matrix)
