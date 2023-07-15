# вариант комплектации рбкзака по максимально возможной грузоподдьемности
from operator import itemgetter

my_diction = {'рюкзак': 2, 'котелок': 1, 'палатка': 7, 'байдарка': 15, 'шатер': 12, 'мангал': 2, 'спорт инвертарь': 6}
max_capacity_backpack = 20
weight = 0
capacity_backpack = 0
# print("рюкзак: ", my_diction)
# print("список вещей по максимально возможной грузоподьемности рюкзака в ", max_capacity_backpack, "кг")
# for things, value in dict(sorted(my_diction.items(), key=itemgetter(1))).items():
#     weight += my_diction[things]
#
#     if weight <= max_capacity_backpack:
#         print(things, ' = ', value)
#         capacity_backpack += my_diction[things]

print("общий вес рюкзака c вещами: ", capacity_backpack)

# 2 вариант использование всех возможных вариантов комплектации рюкзака

input('')

print("Задача 3*")

print("Все возможные варианты наполнгения рюкзака при допустимой грузоподьемности в ", max_capacity_backpack, "кг")

list_dict_value = []
list_dict_key = []
for key, value in my_diction.items():
    list_dict_key.append(key)
    list_dict_value.append(value)

def subset_sum(weights, things, target, count, partial_weights=[], partial_things=[]):
    s = sum(partial_weights)

    # check if the partial sum is equals to target
    if s <= target:
        print("список вещей(%s)\nвес вещей(%s) <= %s \n" % (partial_things, partial_weights, target))

    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(weights)):
        n = weights[i]
        remaining_weights = weights[i + 1:]
        m = things[i]
        remaining_things = things[i + 1:]
        subset_sum(remaining_weights, remaining_things, target, count + 1, partial_weights + [n], partial_things + [m])

print(subset_sum(list_dict_value, list_dict_key, max_capacity_backpack, 0))