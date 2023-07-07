# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 10


def guess_num():
    attempt = 1
    hidden_num = randint(LOWER_LIMIT, UPPER_LIMIT)
    while attempt <= ATTEMPTS:
        num = int(input("Input your choice: "))
        if num == hidden_num:
            print(f"You're right, hidden number is {num}")
            break
        elif num < 0 or num >= 1000:
            print("You've to guess from 0 to 1000")
        else:
            if num > hidden_num:
                print(f"Input number {num} is more then hidden number")
            else:
                print(f"Input number {num} is less then hidden number")
        attempt += 1

guess_num()

