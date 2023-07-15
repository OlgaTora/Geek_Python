# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.
from collections import defaultdict

DUPLICATES = 2

my_list = [1, 2, 5, 8, 11, 2, 5, 5, 11, 21, 12, 18]
print(f'List = {my_list}')

# если удалять дубликаты
# for i in my_list:
#     while my_list.count(i) > 1:
#         my_list.remove(i)
# print(f'New list = {my_list}')

#если удалять все повторяющиеся
my_dict = {}
#обычный словарь
# for i in my_list:
#     my_dict.setdefault(i, 0)
#     my_dict[i] += 1
# print(my_dict)

#коллекции
my_dict = defaultdict(int)
for i in my_list:
    my_dict[i] += 1
print(my_dict)

for key, value in my_dict.items():
    if value > 1:
        for i in range(DUPLICATES):
            my_list.remove(key)

print(f'New list = {my_list}')

