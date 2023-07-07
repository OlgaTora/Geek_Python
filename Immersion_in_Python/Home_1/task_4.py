# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

COMPOSITE = "This number {} is composite"
PRIME = "This number {} is prime"
MIN_LIMIT = 0
MAX_LIMIT = 100000


def check_number(num):
    count_div = 0
    if num < MIN_LIMIT or num > MAX_LIMIT:
        print("You can't use this number in this program")
    elif num == 0 or num == 1:
        print(f"{num} is not prime and is not composite")
    else:
        for i in range(2, num):
            if num % i == 0:
                count_div += 1
                break
        print(COMPOSITE.format(num) if count_div > 0 else PRIME.format(num))


check_number(int(input("Input number > 0 and < 100000: ")))

