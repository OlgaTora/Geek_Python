"""
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import json
from User import User


def create_users(file_name) -> set[User]:
    with open(file_name, 'r', encoding='utf-8') as file:
        users_dict = json.load(file)
        users_set = set()
        for level, user in users_dict.items():
            for key, value in user.items():
                users_set.add(User(value, key, level))
    return users_set


create_users('users.json')
