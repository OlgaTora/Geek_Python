"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться
"""
import json
import os.path

MIN_LEVEL = 1
MAX_LEVEL = 7


def save_to_json(file: str) -> None:
    set_id = set()
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as src_file:
            data = json.load(src_file)
            for user in data.values():
                set_id.update(user.keys())
    else:
        data = {str(access_level): {} for access_level in range(MIN_LEVEL, MAX_LEVEL + 1)}

    while True:
        name = input('Input name: ')
        if not name:
            break
        id = input('Input id: ')
        access_level = input('Input access_level: ')
        if id in set_id:
            continue
        set_id.update(id)
        data[access_level][id] = name
        with open(file, 'w', encoding='utf-8') as dst_file:
            json.dump(data, dst_file, indent=1, ensure_ascii=False)


save_to_json('task_2.json')

