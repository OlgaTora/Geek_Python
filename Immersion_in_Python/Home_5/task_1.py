"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

absolute_path = 'C:\PycharmProjects\GEEK\Immersion_in_Python\Home_3\cats.txt'


def path_to_tuple(path: str) -> tuple[str, str, str]:
    file_path = '\\'.join(absolute_path.split('\\')[:-1])
    file_name, file_extension = absolute_path.split('\\')[-1].split('.')
    return file_path, file_name, file_extension


print(path_to_tuple(absolute_path))
# print(type(path_to_tuple(absolute_path)))

