"""
Таблица умножения
● Условие
На вход подается число n.
● Задача
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
"""


def multiplication_table(num: int):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            res = i * j
            print(f'{i}*{j}={res}')
        print('____')


if __name__ == '__main__':
    number: int = 5
    multiplication_table(number)
