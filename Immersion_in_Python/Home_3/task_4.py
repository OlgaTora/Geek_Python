# ✔ Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.


BACKPACK_CAPACITY = 20
backpack = {'water': 10, 'stew': 15, 'tent': 30, 'umbrella': 2, 'boots': 5, 'juice': 12,
            'socks': 3, 'fire': 1, 'dog': 16}


def get_full_backpack(backpack: dict, weight_backpack: float) -> list:
    full_backpack = []
    for thing, weight in backpack.items():
        if weight <= weight_backpack:
            full_backpack.append(thing)
            weight_backpack -= weight
    return full_backpack

print(get_full_backpack(backpack, BACKPACK_CAPACITY))

