"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import os
import pickle


def find_json_save2pickle(path_src: str) -> None:
    json_files = filter(lambda file: file[-5:] == '.json', os.listdir(path_src))
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(f'{file[:-5]}.pickle', 'wb') as pickle_file:
            pickle.dump(data, pickle_file)


find_json_save2pickle('.')

