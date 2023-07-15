# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь, где ключ — тип элемента,
# значение — список элементов данного тип


my_tuple = (2, 5, 8.11, 11.11, True, 3, (2, 11, 13), 'aaa', 5, 'bbb', 14,)
my_dict = {}

# for i in my_tuple:
#     if type(i) in my_dict.keys():
#         my_dict[type(i)].append(i)
#     else:
#         my_dict[type(i)] = [i]

for i in my_tuple:
    my_dict.setdefault(type(i), []).append(i)

print(my_dict)
