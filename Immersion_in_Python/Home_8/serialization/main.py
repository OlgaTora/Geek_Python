"""
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
"""
from model import walk_dir
from save import save2json, save2pickle, save2csv
CURR_DIR = 'C:\\Users\\вяаы\\PycharmProjects\\GEEK\\Immersion_in_Python'


if __name__ == '__main__':
    result = walk_dir(CURR_DIR)
    save2json(result, 'walk_dir.json')
    save2pickle(result, 'walk_dir.pickle')
    save2csv(result, 'walk_dir.csv')

