"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
"""


class User:
    MIN_LEVEL = 1
    MAX_LEVEL = 7

    def __init__(self, name: str, user_id: str, access_level: str):
        self.user_id = user_id
        self.name = name
        if int(access_level) >= self.MIN_LEVEL or int(access_level) <= self.MAX_LEVEL:
            self.access_level = access_level
        else:
            raise ValueError('Access level from 1 to 7')

    def __str__(self):
        return (f'User name {self.name}, '
                f'id {self.user_id}, '
                f'access level is {self.access_level}')

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))
