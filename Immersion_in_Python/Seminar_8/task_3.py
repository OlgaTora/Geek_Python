"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV
"""
import csv
import json


def save_to_csv(path_src: str, path_dst: str) -> None:
    with open(path_src, 'r', encoding='utf-8') as file_scr:
        data = json.load(file_scr)
    rows = []
    for access_level, user in data.items():
        for user_id, name in user.items():
            rows.append({'access_level': int(access_level), 'id': int(user_id), 'name': name})

    with open(path_dst, 'w', encoding='utf-8', newline='') as file_dst:
        csv_result = csv.DictWriter(file_dst, fieldnames=['access_level', 'id', 'name'], dialect='excel')
        csv_result.writeheader()
        csv_result.writerows(rows)


save_to_csv('../Seminar_13/AccessEmployes/users.json', 'task_3.csv')
