import pytest

from Testing.Lesson_6.hw_6.mean_comparator import MeanComparator


@pytest.mark.parametrize('any_list, expected', [([1, 2, 3], 2), ([-1, 1], 0), ([1], 1)])
def test_get_mean(any_list, expected):
    assert MeanComparator.get_mean(any_list) == expected


def test_get_mean_with_exception_empty_list():
    any_list = []
    with pytest.raises(ValueError) as e:
        MeanComparator.get_mean(any_list)
    assert str(e.value) == "Список не должен быть пустым"


def test_get_mean_with_exception_type_error():
    any_list = [1 , '1']
    with pytest.raises(TypeError) as e:
        MeanComparator.get_mean(any_list)
    assert str(e.value) == 'Список должен состоять из цифр'


@pytest.mark.parametrize('first_list, second_list, expected',
                         [([1, -1, 0], [2, 2, 22], 'Второй список имеет большее среднее значение'),
                          ([1, 1111, 0], [2, 2, 22], 'Первый список имеет большее среднее значение'),
                          ([1, 3], [2, 2, 2], 'Средние значения равны')])
def test_compare_mean(first_list, second_list, expected):
    mean_comparator = MeanComparator(first_list, second_list)
    assert mean_comparator.compare_mean() == expected
