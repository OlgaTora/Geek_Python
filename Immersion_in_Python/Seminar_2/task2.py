# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
import math
import sys

data = [123, 'number', (1, 2, 3), math.pi, True, 'number']
for i, el in enumerate(data, start=1):
    id_elem: int = id(el)
    size: int = sys.getsizeof(el)
    hash_elem: int = hash(el)
    result: str = ''
    if type(el) == int:
        result = 'its a number'
    if isinstance(el, str):
        result = 'its a string'

    print(f'Number {i} , data {el} , id {id_elem}, size {size},'
          f' hash {hash_elem}, {result}')

