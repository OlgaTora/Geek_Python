"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import pickle


def pickle2csv(scr_path: str, dst_path:str) -> None:
    with open(scr_path, 'rb') as pickle_file:
        pickle_data = pickle.load(pickle_file)
        headers = pickle_data[0].keys()
    with open(dst_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_data = csv.DictWriter(csv_file, fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)
        csv_data.writeheader()
        csv_data.writerows(pickle_data)


pickle2csv('task_4.pickle', 'task_6.csv')

