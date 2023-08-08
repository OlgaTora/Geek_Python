import os
import json

CURR_DIR = 'C:\\Users\\вяаы\\PycharmProjects\\GEEK\\Immersion_in_Python'


class SerializatorJSON:
    """
    Класс, который получает на вход директорию и рекурсивно
    обходит её и все вложенные директории. Результаты обхода сохраняет в json.
    Для дочерних объектов указывает родительскую директорию.
    Для каждого объекта указывает файл это или директория.
    Сохраняет размер файлов и директорий в байтах.
    """

    def __init__(self, dir_src: str):
        self.dir_src = dir_src

    def walk_dir(self) -> list[{}]:
        result = []
        for dir_paths, dirs, files in os.walk(self.dir_src):
            for directory in dirs:
                dir_path = os.path.join(dir_paths, directory)
                result.append(
                    {'name': directory,
                     'parent_dir': dir_paths,
                     'type': 'directory',
                     'size': self.get_dir_size(dir_path)})
            for file in files:
                file_path = os.path.join(dir_paths, file)
                result.append(
                    {'name': file,
                     'parent_dir': dir_paths,
                     'type': 'file',
                     'size': os.path.getsize(file_path)
                     })
        return result

    @staticmethod
    def get_dir_size(dir_path) -> int:
        size = 0
        for dir_paths, dirs, files in os.walk(dir_path):
            for file in files:
                file_dir = os.path.join(dir_paths, file)
                size += os.path.getsize(file_dir)
            return size

    def save2json(self, path_dst: str) -> None:
        lst_src = self.walk_dir()
        with open(path_dst, 'w', encoding='utf-8') as file_dst:
            json.dump(lst_src, file_dst, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    serial = SerializatorJSON(CURR_DIR)
    serial.save2json('walk_dir.json')
