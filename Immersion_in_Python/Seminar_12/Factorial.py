"""
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
import json
from collections import deque


class Factorial:
    """ Class-function for calculate factorial"""

    def __init__(self, count: int):
        self._history = deque(maxlen=count)

    def __call__(self, number: int):
        mult: int = 1
        for i in range(2, number + 1):
            mult *= i
        self._history.append({number: mult})
        return mult

    def show_history(self):
        return self._history

    def __enter__(self):
        """Function for open context manager"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Function for write data to json"""
        data = {}
        while self._history:
            data.update(self._history.popleft())
        with open('factioral_history.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)


if __name__ == '__main__':
    factorial = Factorial(4)
    with factorial as f:
        print(f(10))
        print(f(15))
        print(f(5))
        print(f.show_history())
