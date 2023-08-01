import os


def get_dir_size(dir_path: str) -> int:
    size = 0
    for dir_paths, dirs, files in os.walk(dir_path):
        for file in files:
            file_dir = os.path.join(dir_paths, file)
            size += os.path.getsize(file_dir)
        return size

