import unittest
from Immersion_in_Python.Home_11.Matrix import Matrix


class TestMatrix(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.my_matrix1 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
        cls.my_matrix2 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
        cls.my_matrix3 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 6]])
        cls.my_matrix4 = Matrix([[1, 4, 3, 5], [4, 8, 6, 11], [7, 8, 9, 2]])

    def test_create(self):
        self.assertTrue(self.my_matrix1 == Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]]))

    def test_equal(self):
        self.assertTrue(self.my_matrix1 == self.my_matrix2)

    def test_not_equal(self):
        self.assertNotEquals(self.my_matrix1, self.my_matrix3)

    def test_size_not_equal(self):
        self.assertFalse(self.my_matrix1.check_size(self.my_matrix4))

    def test_mul(self):
        self.assertEquals(self.my_matrix1 * self.my_matrix4,
                          Matrix([[38, 60, 54, 55], [78, 128, 114, 120], [102, 164, 150, 141], [70, 100, 96, 74]]))

    def test_sum(self):
        self.assertEquals(self.my_matrix1 + self.my_matrix2,
                          Matrix([[2, 8, 6], [8, 16, 12], [14, 16, 18], [2, 10, 14]]))


if __name__ == '__main__':
    unittest.main()
