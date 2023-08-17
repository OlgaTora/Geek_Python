import json
from typing import Set
from User import User
from ExceptionBD import AccessException, LevelException


class Project:
    FILE_NAME = 'users.json'

    def __init__(self):
        self.admin = None
        self.users_set = self.create_users()

    def create_users(self) -> Set[User]:
        """Function for load list of user into the set"""
        with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
            users_dict = json.load(file)
        users_set = set()
        for level, user in users_dict.items():
            for key, value in user.items():
                users_set.add(User(value, key, level))
        return users_set

    def user_enter(self, name: str, user_id: str):
        """Function for enter"""
        test_user = User(name, user_id, '0')
        if test_user in self.users_set:
            for user in self.users_set:
                if test_user == user:
                    self.admin = user
            return f'Your level  is {self.admin.access_level}'
        else:
            raise AccessException(name)

    def add_new_user(self, name: str, user_id: str, access_level: str):
        """Function for add new user"""
        if int(access_level) > int(self.admin.access_level):
            raise LevelException(name, user_id, access_level)
        new_user = User(name, user_id, access_level)
        self.users_set.add(new_user)

    def save_users(self):
        """Function for save users to json file"""
        data = {str(access_level): {} for access_level in range(User.MIN_LEVEL, User.MAX_LEVEL+ 1)}
        for user in self.users_set:
            for key in data.keys():
                if user.access_level == key:
                    data[key][user.user_id] = user.name
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
