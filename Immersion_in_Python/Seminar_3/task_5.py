# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы

my_list = [1, 2, 5, 8, 11, 2, 5, 12, 18]
index_list = []

# for i in range(len(my_list)):
#     if my_list[i] % 2 != 0:
#         index_list.append(i + 1)

for i, value in enumerate(my_list, start=1):
    if value % 2 != 0:
        index_list.append(i)

print(f'Index list = {index_list}')

