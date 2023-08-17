class ClassNotFoundException(Exception):
    """ошибка если нет такого класса"""

    def __init__(self, class_):
        self.class_ = class_

    def __str__(self):
        return f'This class {self.class_} doesnt exist'
