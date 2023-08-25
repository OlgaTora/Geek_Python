"""
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""
import json

import pytest
from Immersion_in_Python.Seminar_13.AccessEmployes.Project import Project, User
from Immersion_in_Python.Seminar_13.AccessEmployes.ExceptionBD import ExceptionBD


@pytest.fixture
def new_set() -> set[User]:
    user_set = {
        User('name1', '1', '2'),
        User('name2', '2', '6'),
        User('name3', '3', '4')
    }
    return user_set


def test_create(new_set):
    p1 = Project()
    result_test = p1.create_users(file_name='users.json')
    assert result_test == new_set


@pytest.fixture
def user_for_entrance():
    user = User('name1', '1', '0')
    return user.access_level


def test_entrance(user_for_entrance):
    p2 = Project()
    assert p2.user_enter('name1', '1') == user_for_entrance
