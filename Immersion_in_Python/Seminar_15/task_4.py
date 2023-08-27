"""
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога,
- название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""
import argparse
import logging
from collections import namedtuple
from pathlib import Path

File = namedtuple('File', ['name', 'extension', 'is_dir', 'parent_dir'])

FORMAT = '{asctime} - {levelname} - {funcName} - {msg}'
logging.basicConfig(filename='files_info.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    style='{',
                    format=FORMAT)
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(prog='files info',
                                     description='little program to save information about files in directory')
    parser.add_argument('-d',
                        '--directory',
                        help='directory',
                        type=Path)
    arguments = parser.parse_args()
    return get_dir_info(arguments.directory)


def get_dir_info(path: Path):
    for obj in path.iterdir():
        file = File(obj.stem if obj.is_file() else obj.name,
                    obj.suffix, obj.is_dir(), obj.parent)
        logger.info(file)
        if file.is_dir:
            get_dir_info(Path(file.parent_dir)/file.name)


if __name__ == '__main__':
    get_dir_info(Path('/home/olgatorres/PycharmProjects/Geek_Python/Immersion_in_Python/Home_7'))
