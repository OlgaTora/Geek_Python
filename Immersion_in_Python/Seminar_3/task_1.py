# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.


my_list = [1, 2, 5, 8, 11, 2, 5, 12, 18]
new_list = []


# длинное
def get_new_list(list_1, list_2) -> list:
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(f'List = {my_list}')
print(f'New list = {get_new_list(my_list, new_list)}')

#короткое

new_list = list(set(my_list))
print(f'New list = {get_new_list(my_list, new_list)}')

