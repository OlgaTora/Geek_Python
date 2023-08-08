"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""
from enum import Enum


class Gender(Enum):
    male = 'male'
    female = 'female'


class Person:
    def __init__(self, name: str, surname: str, age: int, gender: Gender, nationality: str):
        self.gender = gender
        self.nationality = nationality
        self._age = age
        self.name = name
        self.surname = surname

    def birthday(self):
        self._age += 1
        return self._age

    def full_name(self):
        return ' '.join([self.name, self.surname])

    def get_age(self):
        return self._age


if __name__ == '__main__':
    p1 = Person('Ivan', 'Ivanov', 22, Gender.male, 'spanish')
    print(p1.full_name())
    print(p1.get_age())
    p1.birthday()
    print(p1.get_age())
    p1._age = 1
    print(p1.get_age())
