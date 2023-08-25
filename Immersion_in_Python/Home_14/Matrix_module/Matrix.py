class Matrix:
    """Class matrix for print, add, multiply and compare matrices."""

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        if not self.is_filled():
            raise TypeError('The rows lengths have to be same')

    def is_filled(self) -> bool:
        """Function check is matrix filled completely
        >>> my_matrix1 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
        >>> my_matrix1.is_filled()
        True
        """
        for i in range(len(self.matrix) - 1):
            if len(self.matrix[i]) != len(self.matrix[i + 1]):
                return False
        return True

    def compatibility(self, other) -> bool:
        """Function to compare size of two matrices for multiply"""
        if self.columns == other.rows:
            return True
        else:
            return False

    def check_size(self, other) -> bool:
        """
        >>> my_matrix1 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
        >>> my_matrix3 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 6]])
        >>> my_matrix1.check_size(my_matrix3)
        True
        """
        if self.rows == other.rows and self.columns == other.columns:
            return True
        else:
            return False

    def __eq__(self, other):
        """Function for compare two matrices"""
        if self.check_size(other):
            for i in range(self.rows):
                for j in range(self.columns):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        else:
            return False

    def __add__(self, other):
        """Function for add two matrices"""
        summ_result = [[0] * self.columns for _ in range(other.rows)]
        if self.check_size(other):
            for i in range(self.rows):
                for j in range(self.columns):
                    summ_result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(summ_result)
        else:
            raise ValueError('Matrix has different size')

    def __mul__(self, other):
        """Function for multiply two matrices"""
        mul_result = [[0] * self.rows for _ in range(other.columns)]
        if self.compatibility(other):
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        mul_result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(mul_result)
        else:
            raise ValueError('Matrix has different size')

    def __str__(self) -> str:
        """Function for show information about object to user"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __repr__(self):
        """Function to show information to developer"""
        return f'{self.rows= }, {self.columns= }, {self.matrix = }'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
