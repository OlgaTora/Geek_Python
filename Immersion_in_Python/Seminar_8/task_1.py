"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""


import json


def save_to_json(dir_src: str, dir_dst: str) -> None:
    with open(dir_src, 'r', encoding='utf-8') as file_scr:
        dict_src = {}
        for line in file_scr:
            name, num = line.split(' ')
            dict_src[name.capitalize()] = float(num)
    with open(dir_dst, 'w', encoding='utf-8') as file_dst:
        json.dump(dict_src, file_dst, ensure_ascii=False, indent=2)


save_to_json('C:\\Users\\вяаы\\PycharmProjects\\GEEK\\Immersion_in_Python\\Seminar_7\\task_3.txt', 'task_1.json')

