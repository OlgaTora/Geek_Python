"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle


def csv_reader(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, dialect='excel')
        lst = []
        headers = []
        for i, line in enumerate(csv_data):
            if i == 0:
                headers = line
            else:
                dct = {key: value for key, value in zip(headers, line)}
                lst.append(dct)
        print(pickle.dumps(lst))


csv_reader('task_6.csv')
