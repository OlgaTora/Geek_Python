"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_data_from_dict(dct: dict, key_dict: str, default_value: int | float = None) -> int | float | None:
    result = default_value
    try:
        result = dct[key_dict]
    except KeyError as e:
        pass
    return result


if __name__ == '__main__':
    dct = {'1': 'one', '2': 'two', '3': 'three'}
    print(get_data_from_dict(dct, '1'))
    print(get_data_from_dict(dct, '4'))
