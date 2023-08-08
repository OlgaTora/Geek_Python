from __future__ import annotations


class MatrixTransformator:
    """
    Класс, принимающий матрицу и возвращающий транспонированную
    матрицу в случае, если это возможно и None, если не возможно
    """
    @staticmethod
    def is_rectangle(matrix: list[[int]]) -> bool:
        for i in range(0, len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                return False
        return True

    def transpose_matrix(self, matrix: list[[int]]) -> list[[int]] | None:
        if self.is_rectangle(matrix):
            rows: int = (len(matrix))
            columns: int = len(matrix[0])
            new_matrix: list[[int]] = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
            return new_matrix


if __name__ == '__main__':
    my_matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 7]]
    my_matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5]]
    mt = MatrixTransformator()
    print(mt.transpose_matrix(my_matrix1))
    print(mt.transpose_matrix(my_matrix2))
