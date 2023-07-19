# """
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
# """

nums = 123
lst = ['aa', 'bb']
my_str = 'abs'
abs = '111'
s = 'asff'


def replace_s() -> None:
    globals_list = globals()
    without_s = {}
    for key, value in globals_list.items():
        if key == 's':
            continue
        elif key.endswith('s'):
            without_s[key[:-1]] = value
            globals_list[key] = None
    for key, value in without_s.items():
        globals_list[key] = value

replace_s()
print(globals())