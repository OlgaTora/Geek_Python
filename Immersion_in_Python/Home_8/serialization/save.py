import json
import pickle
import csv


def save2json(lst_src: list[{}], path_dst: str) -> None:
    with open(path_dst, 'w', encoding='utf-8') as file_dst:
        json.dump(lst_src, file_dst, ensure_ascii=False, indent=1)


def save2csv(lst_src: list[{}], path_dst: str) -> None:
    field_names = lst_src[0].keys()
    with open(path_dst, 'w', encoding='utf-8', newline='') as file_dst:
        csv_result = csv.DictWriter(file_dst, fieldnames=field_names, dialect='excel')
        csv_result.writeheader()
        csv_result.writerows(lst_src)


def save2pickle(lst_src: list[{}], path_dst: str) -> None:
    with open(path_dst, 'wb') as pickle_file:
        pickle.dump(lst_src, pickle_file)

