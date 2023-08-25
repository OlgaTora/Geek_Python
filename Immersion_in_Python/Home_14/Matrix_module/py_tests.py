import pytest
from Immersion_in_Python.Home_11.Matrix import Matrix


@pytest.fixture()
def new_data():
    my_matrix1 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
    my_matrix2 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 7]])
    my_matrix3 = Matrix([[1, 4, 3], [4, 8, 6], [7, 8, 9], [1, 5, 6]])
    my_matrix4 = Matrix([[1, 4, 3, 5], [4, 8, 6, 11], [7, 8, 9, 2]])
    return my_matrix1, my_matrix2, my_matrix3, my_matrix4


def test_equal(new_data):
    assert new_data[0] == new_data[1]


def test_not_equal(new_data):
    assert not new_data[0] == new_data[2]


def test_size_not_equal(new_data):
    assert not new_data[0].check_size(new_data[3])


def test_mul(new_data):
    assert new_data[0] * new_data[3] == Matrix(
        [[38, 60, 54, 55], [78, 128, 114, 120], [102, 164, 150, 141], [70, 100, 96, 74]])


def test_sum(new_data):
    assert new_data[0] + new_data[1] == Matrix(
        [[2, 8, 6], [8, 16, 12], [14, 16, 18], [2, 10, 14]])


if __name__ == '__main__':
    pytest.main(['-v'])
