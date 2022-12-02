# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

my_list = []
summa = 0
for i in range(0, 5):
    my_list.append(random.randint(0, 25))
    if i % 2 != 0:
        summa += my_list[i]

print(f'List is: {my_list}')
print(f'Sum is: {summa}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]


my_list = [random.randint(0, 8) for i in range(0, 5)]
multy_list = []
print(f'List is: {my_list}')

if len(my_list) % 2 != 0:
    my_list.insert(len(my_list) // 2 + 1, my_list[len(my_list) // 2])
    print(f'New List is: {my_list}')

for i in range(0, len(my_list) // 2):
    multy_list.append(my_list[i] * my_list[len(my_list) - 1 - i])

print(f'Result is: {multy_list}')


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [round(random.uniform(0, 8), 2) for i in range(0, 5)]
largest = 0
smallest = 1
for i in my_list:
    i = i % 1
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i

print(f'Random list is: {my_list}')
print(f'The difference between min and max is: {(largest - smallest)}')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: - 45 -> 101101  3 -> 11 - 2 -> 10


try:
    n = int(input('Input number: '))
    s = ''
    if n < 0:
          n = n * -1
    elif n == 0:
          print(f'Your number in binary system is: {n}')
    while n > 0:
        if n % 2 == 0:
            s = '0' + s
        else:
            s = '1' + s
        n //= 2
    print(f'Your number in binary system is: {s}')


except:
    print("You've to input number")

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

try:
    n = int(input('Input number: '))
    my_list = [0] * (n - 1) + [1, 0, 1] + [0] * (n - 1)

    for i in range(n + 1, len(my_list)):
        my_list[i] = my_list[i - 1] + my_list[i - 2]
    for j in range(n - 2, -1, -1):
        my_list[j] = (abs(my_list[j + 1]) + abs(my_list[j + 2]))
        if j % 2 == 0:
            my_list[j] = - my_list[j]

    print(f'Negative Fibonacci list is: {my_list}')

except:
    print("You've to input number")

# Реализовать алгоритм перемешивания списка.
import time

def rand_num(minim =0, maxim=10):
    num = int((time.time() % 1) * (maxim - minim) + minim)
    return num

lst = [2, 3, 7, 11, 54]
#random.shuffle(lst)

for i in range(len(lst)):
    j = rand_num(0, len(lst) - 1)
    tmp = lst[i]
    lst[i], lst[j] = lst[j], lst[i]

print(lst)

# Определить, присутствует ли в заданном списке строк, некоторое число
lst = ['sdgdsg', '11dfgfdgd', '12dfbdb', 'dfhh']
num = 2

for i in lst:
    if i.count(str(num)):
        print(True)
        break

# номер второго вхождения строки в списке
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: [], ищем: "123", ответ: -1

lst = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
fnd = 'qwe'
counter = 0
index = - 1
for i in range(0, len(lst) - 1):
    if lst[i] == fnd:
        counter += 1
    if counter == 2:
      index = i
      break
print(index)
