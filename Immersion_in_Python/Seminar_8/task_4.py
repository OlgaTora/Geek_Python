"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции
"""
import csv
import json


def csv2son(scr_path: str, dst_path: str) -> None:
    with open(scr_path, 'r', encoding='utf-8') as scr_file:
        data_csv = csv.reader(scr_file)
        data_json = []
        for i, line in enumerate(data_csv):
            if i:
                user_data = {}
                access_level, user_id, name = line
                user_data['access_level'] = int(access_level)
                user_data['name'] = name.capitalize()
                user_data['user_id'] = f'{int(user_id):010}'
                user_data['hash'] = hash((user_id, name))
                data_json.append(user_data)
    with open(dst_path, 'w', encoding='utf-8') as dst_file:
        json.dump(data_json, dst_file, indent=2)


csv2son('task_3.csv', 'task_4.json')

