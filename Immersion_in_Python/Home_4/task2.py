"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def get_dict_kwargs(**kwargs):
    kwargs_dict = {}
    for key, value in kwargs.items():
        try:
            kwargs_dict[value] = key
        except TypeError:
            kwargs_dict[str(value)] = key
    return kwargs


print(get_dict_kwargs(arg1='a', arg2=2))
print(get_dict_kwargs(arg1=1, arg2=[1, 2, 3]))
print(get_dict_kwargs(arg1='Hola-coca-cola', arg2='1234', arg3=1234, arg4=['1', '2', '3']))


# для возврата хэша
# a = [1, 2]
# print(a.__hash__)

