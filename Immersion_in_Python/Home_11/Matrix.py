class Matrix:
    """Class matrix for print, add, multiply and compare matrices."""

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        if not self.is_filled():
            raise TypeError('The rows lengths have to be same')

    def is_filled(self) -> bool:
        """Function check is matrix filled completely"""
        for i in range(len(self.matrix) - 1):
            if len(self.matrix[i]) != len(self.matrix[i + 1]):
                return False
        return True

    def check_size(self, other) -> bool:
        """Function to compare size of two matrices"""
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
        result = [[0] * self.columns for _ in range(self.rows)]
        if self.check_size(other):
            for i in range(self.rows):
                for j in range(self.columns):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        else:
            raise ValueError('Matrix has different size')

    def __str__(self) -> str:
        """Function for show information about object to user"""
        return '\n'.join([str(row) for row in my_matrix_1])

    def __repr__(self):
        """Function to show information to developer"""
        return (f"' '.join[{self.rows= }, {self.columns= }, {self.matrix = }]")



if __name__ == '__main__':
    my_matrix1 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
    my_matrix2 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
    my_matrix3 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 6]])

    my_matrix_1 = [[1, 2, 3], [4, 5, 66], [7, 8, 9], [111, 5, 7]]
    # my_matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5]]
    #print(my_matrix1)

    #result = '\n'.join([' '.join(map(str, row)) for row in my_matrix_1])


    #print
    print(my_matrix1)
    print(my_matrix1.__repr__())

    # compare
    print(my_matrix1 == my_matrix2)
    print(my_matrix1 == my_matrix3)

    # add
    print(f'result of add:\n{my_matrix1 + my_matrix2}')
