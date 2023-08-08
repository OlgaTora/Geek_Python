"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from task_3 import Person, Gender
import random


class Employee(Person):
    __magic_num: int = 7
    min_id = 100_000
    max_id = 1_000_000

    def __init__(self, name: str, surname: str, age: int, gender: Gender, nationality: str,
                 id_employee: int):
        super().__init__(name, surname, age, gender, nationality)
        if self.min_id <= id_employee < self.max_id:
            self.id_employee = id_employee
        else:
            self.id_employee = int(random.randrange(self.min_id, self.max_id))

    def get_id(self):
        return self.id_employee

    def get_level(self):
        access_level: int = sum(int(i) for i in str(self.id_employee)) % self.__magic_num
        return access_level


if __name__ == '__main__':
    employee1 = Employee('Ivan', 'Ivanov', 22, Gender.male, 'spanish', 777_777)
    print(f'{employee1.get_id() = }')
    print(f'{employee1.get_level() = }')
    employee2 = Employee('Ivan', 'Ivanov', 22, Gender.male, 'spanish', 777_777)
    print(f'{hash(employee1) = }')
    print(f'{hash(employee2) = }')
