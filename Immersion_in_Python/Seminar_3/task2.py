# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте, если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях


def convert_data():
    data: str = input('Input something:\n')
    new_data = ''
    if data.count('.') == 1 and data.replace('.', '').replace('-', '').isdecimal():
        new_data = float(data)
    elif data[0] == '-' and data.replace('-', '').isdecimal():
        new_data = int(data[1::])
    elif data.isdecimal():
        new_data = int(data)
    else:
        if one_letter_lower(data):
            new_data = data.lower()
        else:
            new_data = data.upper()
    return data, new_data


def one_letter_lower(my_str: str) -> bool:
    counter = 0
    for i in my_str:
        if i.isupper():
            counter += 1
    return True if counter == 1 else False


data, new_data = convert_data()
print(f'Data = {data}, type = {type(data)}')
print(f'New data = {new_data}, type = {type(new_data)}')

# для теста
# data = '123'
# data = '-123'
# data = '1.23'
# data = '-1.23'
# data = 'ghFb hgjA ghD'
# data = 'bvbHbnn bnnb1'

