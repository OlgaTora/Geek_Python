import os
from os import path
from random import choices, randint
from string import ascii_lowercase, digits

_dirs = {
    'text': ['txt', 'doc', 'rtf'],
    'video': ['mp4', 'wmw', 'mpeg'],
    'images': ['bmp', 'jpeg', 'png']
}


def gen_name(extension: str, min_len: int, max_len: int) -> str:
    file_name = '.'.join(
        [''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len))), extension])
    while path.isfile(file_name):
        file_name: str = '.'.join(
            [''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len, max_len))), extension])
    return file_name


def gen_content(min_byte: int, max_byte: int) -> bytes:
    content = bytes(randint(0, 255) for _ in range(randint(min_byte, max_byte)))
    return content


def create_file_list(dir: str) -> list[str]:
    file_names = []
    for dir_path, dir_name, file_name in os.walk(dir):
        file_names.extend(file_name)
    return file_names


def check_dir(dir: str) -> None:
    if not path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)


def check_extension(extension: str) -> None:
    for dir_name, extension_name in _dirs.items():
        if extension in extension_name:
            check_dir(dir_name)


def change_dir(dir: str) -> None:
    curr_dir = os.getcwd().split("\\")[-1]
    if curr_dir != dir:
        os.chdir('..')


def count_files(files_list: list[str], ext: str) -> tuple[list[str], int]:
    counter: int = 0
    files_with_ext = []
    for file in files_list:
        if file.split('.')[1] == ext:
            files_with_ext.append(file)
            counter += 1
    return files_with_ext, counter


def compare_quantities(counter: int, num_quantity: int) -> bool:
    quantity: int = int('1' + '0' * num_quantity)
    if counter > quantity:
        return False
    return True


def check_file_length(files_list: list[str], symb_range: list[int]) -> bool:
    for file in files_list:
        if len(file) < symb_range[1]:
            return False
    return True


def check_rename_possibility(files_list: list[str], num_quantity: int,
                             symb_range: list[int], counter: int) -> bool:
    if not compare_quantities(counter, num_quantity):
        print('Files quantity is more than index')
        return False
    if not check_file_length(files_list, symb_range):
        print('You have file with length less than symbols range')
        return False
    return True


def is_file_exist(file: str, new_file: str) -> None:
    if not os.path.isfile(new_file):
        os.rename(file, new_file)
    else:
        print(f'Cant rename this file {file}, {new_file} is exist')

