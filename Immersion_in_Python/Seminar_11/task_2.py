"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-
архивов
list-архивы также являются свойствами экземпляра
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    """Singleton. Хранит число и строку в списках."""
    _instance = None

    def __init__(cls, text: str, number: float):
        print("INIT")
        cls.number = number
        cls.text = text

    def __new__(cls, *args, **kwargs):
        print('NEW')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_nums = []
            cls._instance.archive_str = []
        else:
            cls._instance.archive_nums.append(cls._instance.number)
            cls._instance.archive_str.append(cls._instance.text)

        return cls._instance

    def __repr__(cls):
        '''Функция вывода информации для разработчика'''
        return f'number: {cls.number}, text: {cls.text}'

    def __str__(cls):
        '''Функция вывода информации для пользователя'''
        return (f'Number: {cls.archive_nums}\n'
                f'String archive: {cls.archive_str}'
                f'Current number: {cls.number}\n'
                f'Current text: {cls.text}')


example1 = Archive('text1', 1)
example2 = Archive('text2', 2)
example3 = Archive('text3', 3)

print(Archive.__doc__)
print(example1)
print(f'{example1 = }')
