import os
from utils import create_file_list, count_files, check_rename_possibility, is_file_exist

DIR = 'C:\\Users\\вяаы\\PycharmProjects\\GEEK\\Immersion_in_Python\\Home_7\\make_files\\test\\text'


def rename_files(num_quantity: int, ext_old: str, ext_new: str,
                 symb_range: list[int], new_name: str = None):
    files = create_file_list(DIR)
    file_names, counter = count_files(files, ext_old)
    if check_rename_possibility(file_names, num_quantity, symb_range, counter):
        for i in range(counter):
            file = file_names[i]
            counter_name: str = str(i)
            while len(counter_name) < num_quantity - 1:
                counter_name = '0' + counter_name
            new_file = f'{file[symb_range[0]:symb_range[1]]}{new_name}{counter_name}.{ext_new}'
            os.chdir(DIR)
            is_file_exist(file, new_file)

