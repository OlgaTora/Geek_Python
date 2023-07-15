# Три друга взяли вещи в поход. Сформируйте  словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей, кроме одного и его имя
# ✔ Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

FRIEND = 3
trip_pack = {'friend 1': ('backpack', 'water', 'stew', 'boots', 'tent', 'umbrella',),
             'friend 2': ('backpack', 'water', 'stew', 'map',),
             'friend 3': ('backpack', 'water', 'stew', 'boots', 'map',),
             }

all_things_all_friends = list(trip_pack.values())


def all_friend_have_thing(all_things_all_friends: list):
    result = set(all_things_all_friends[0])  # вещи первого друга
    for one_friend_things in range(1, FRIEND):
        result &= set(all_things_all_friends[one_friend_things])
    return result


def one_friend_have(trip_pack: dict) -> list:
    friends = trip_pack.keys()
    result_list = []
    for friend in friends:
        result = set(trip_pack.get(friend))
        other_things = set()
        for i in friends:
            if i != friend:
                other_things |= set(trip_pack.get(i))
        result -= other_things
        if result:
            result_list.append(", ".join(result))
    return result_list


def friend_not_have_thing(pack_dict: dict, all_have: set):
    friends = trip_pack.keys()
    result_list = []
    for friend in friends:
        other_things = set()
        for i in friends:
            if i != friend:
                if not other_things:
                    other_things = set(trip_pack.get(i))
                else:
                    other_things &= set(trip_pack.get(i))
        result = other_things - all_have
        if result:
            result_list.append(friend)
    return result_list


all_have = all_friend_have_thing(all_things_all_friends)
unique = one_friend_have(trip_pack)
who_not_have = friend_not_have_thing(trip_pack, all_have)

print(f'All friends have this things: {", ".join(all_have)}')
print(f'One friend have this thing: {", ".join(unique)}')
print(f'Friend who dont have thing that have other friends: {", ".join(who_not_have)}')

