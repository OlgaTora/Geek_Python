import pytest
from Immersion_in_Python.Seminar_14.str_modify.main import string_modify


def test1_method():
    assert string_modify('it was long thought') == 'it was long thought', 'Error'


def test2_method():
    assert string_modify('It was Long thought') == 'it was long thought'


def test3_method():
    assert string_modify('it was, long thought!') == 'it was long thought'


def test4_method():
    assert string_modify('it was long thought да дорогая') == 'it was long thought  '


def test5_method():
    assert string_modify('It was Long thought, да дорогая?') == 'it was long thought  '


if __name__ == '__main__':
    pytest.main(['-v'])
