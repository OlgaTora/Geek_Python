# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


my_list = [1, 2, 5, 8, 11, 2, 5, 5, 11, 21, 12, 18]
duples = []
print(f'List = {my_list}')

for i in my_list:
    if my_list.count(i) > 1 and i not in duples:
        duples.append(i)
print(f'Duplicates list = {duples}')
