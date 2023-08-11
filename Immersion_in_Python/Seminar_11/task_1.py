"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
"""
import time


class MyStr(str):
    """
    В классе доступны все возможности str,
    и дополнительно хранятся имя автора строки и время создания
    """

    def __new__(cls, data: str, creator: str):
        print('Function NEW called')
        instance = super().__new__(cls, data)
        instance.creator = creator
        instance.time_added = time.time()
        return instance

    def __str__(self):
        '''Функция вывода информации для пользователя'''
        return f'{super().__str__()} created by {self.creator} at {self.time_added}'


example1 = MyStr('text', 'teacher')
print(example1)
print(MyStr.__doc__)
