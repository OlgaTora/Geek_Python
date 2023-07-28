from utils import gen_name, gen_content, check_dir, check_extension, change_dir


def create_file(extension: str, min_byte=256, max_byte=4096, min_len=6,
                max_len=30, files_quan=4) -> None:
    for i in range(files_quan):
        name = gen_name(extension, min_len, max_len)
        content = gen_content(min_byte, max_byte)
        with open(f'{name}', 'wb') as file:
            file.write(content)


def create_files_diff_ext(dir: str, **kwargs) -> None:
    check_dir(dir)
    for extension, quantity in kwargs.items():
        check_extension(extension)
        create_file(extension=extension, files_quan=quantity)
        change_dir(dir)

