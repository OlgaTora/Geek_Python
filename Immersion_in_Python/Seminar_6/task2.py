"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
"""
__all__ = ['show_result_storage', 'storage_puzzle', 'guess_puzzle', 'result_storage']
_results_storage = {}


def guess_puzzle(puzzle, answers, attemps):
    print(f'My puzzle: {puzzle}')
    attemps_counter = 1
    while attemps > 0:
        guess_answ: str = input('Guess\n')
        if guess_answ in answers:
            return attemps_counter
        attemps_counter += 1
        attemps -= 1
    return 0


def storage_puzzle(attempts: int = 3):
    puzzles = {'puzzle_1': ['1', '2'],
               'puzzle_2': ['2', '3'],
               'puzzle_3': ['4', '5'],
               'puzzle_4': ['6', '7']
               }
    for puzzle, answer in puzzles.items():
        result: int = guess_puzzle(puzzle, answer, attempts)
        result_storage(puzzle, result)
        print(f'Result is: {result}')


def result_storage(puzzle: str, attempt: int):
    _results_storage.update({puzzle: attempt})


def show_result_storage():
    print('Statistics:\n')
    output = '\n'.join(
        f'{puzzle} have guess in {attempt} attempt' if attempt > 0 else f'{puzzle} havent guess'
        for puzzle, attempt in _results_storage.items())
    print(output)


if __name__ == '__main__':
    # задача 1
    # result: int = guess_puzzle('puzzle', ['1', '2'], 3)
    # print(f'Result is: {result}')
    # задача 2
    storage_puzzle()
    # задача 3
    show_result_storage()

