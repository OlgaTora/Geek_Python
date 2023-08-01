import os
from utils import get_dir_size


def walk_dir(dir_src: str) -> list[{}]:
    result = []
    for dir_paths, dirs, files in os.walk(dir_src):
        for directory in dirs:
            dir_path = os.path.join(dir_paths, directory)
            result.append(
                {'name': directory,
                 'parent_dir': dir_paths,
                 'type': 'directory',
                 'size': get_dir_size(dir_path)})
        for file in files:
            file_path = os.path.join(dir_paths, file)
            result.append(
                {'name': file,
                 'parent_dir': dir_paths,
                 'type': 'file',
                 'size': os.path.getsize(file_path)
                 })
    return result

