"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_number():
    while True:
        prompt = input('Input float or integer number:\n')
        try:
            result = int(prompt)
            break
        except ValueError as e:
            print(f'{prompt} not possible to modify to integer')
        try:
            result = float(prompt)
            break
        except ValueError as e:
            print(f'{prompt} not possible to modify to float')
    return result


if __name__ == '__main__':
    print(f'result is {get_number()}')
