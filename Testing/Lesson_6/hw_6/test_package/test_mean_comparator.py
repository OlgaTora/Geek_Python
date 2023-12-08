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


def test_compare_mean():
    first_list = [1, -1, 0]
    second_list = [2, 2, 22]
    mean_comparator = MeanComparator(first_list, second_list)
    assert mean_comparator.compare_mean() == 'Второй список имеет большее среднее значение'
