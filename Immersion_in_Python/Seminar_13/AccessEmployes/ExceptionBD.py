"""
Создайте класс с базовым исключением и дочерние классы-
исключения: ○ошибка уровня, ○ошибка доступа.
"""


class ExceptionBD(Exception):
    pass


class LevelException(ExceptionBD):
    def __init__(self, name: str, user_id: str, access_level: str):
        self.access_level = access_level
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f'User {self.name} with id {self.user_id} cannot have level {self.access_level}'


class AccessException(ExceptionBD):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'This user {self.name} is not exist'
