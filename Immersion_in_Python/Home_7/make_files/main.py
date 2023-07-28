from model_rename import rename_files
from model_create import create_files_diff_ext

if __name__ == '__main__':
    create_files_diff_ext(dir='test', txt=12, aaa=1, doc=1, jpeg=1, wmw=1)
    button: int = int(input('Do you want to rename files?\n'
                            'press 1 - I want\n'
                            'press 2 - exit\n'))
    if button == 1:
        rename_files(3, 'txt', 'doc', [2, 4], 'new_name')

