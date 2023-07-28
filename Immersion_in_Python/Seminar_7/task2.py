"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""
import random

vowels = 'euioa'
COUNT_NAMES = 10
MIN_SYMB = 4
MAX_SYMB = 7
MIN_VOWEL = 2


def get_nicknames(filename):
    with open(filename, 'a', encoding='utf_8') as file:
        for name in range(COUNT_NAMES):
            name: str = ''
            for _ in range(random.randint(MIN_SYMB, MAX_SYMB)):
                name += chr(random.randint(97, 122))
            while not check_vowels(name):
                name = name.replace(name[random.randrange(len(name))], random.choice(vowels))
            name = name.capitalize()
            file.writelines(name)
            file.writelines('\n')


def check_vowels(name: str) -> bool:
    vowels_counter = 0
    for letter in name:
        if letter in vowels:
            vowels_counter += 1
    return True if vowels_counter >= 2 else False

get_nicknames('task_2.txt')

