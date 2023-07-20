"""
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
Для вывода результата используйте «принт»
без перехода на новую строку.
"""

MIN = 2
MAX = 10
ROWS = 2
SPACES = 2
COLUMNS = int((MAX - MIN) / ROWS)

gen = (f'\t{k:>{SPACES}} X {j:>{SPACES}} =  {k * j:>{SPACES}}\t' if k != i + COLUMNS - 1 else
       f'{k:>{SPACES}} X {j:>{SPACES}} =  {k * j:>{SPACES}}\n' if j != MAX - 1 else
       f'{k:>{SPACES}} X {j:>{SPACES}} =  {k * j:>{SPACES}}\n\n'
       for i in range(MIN, MAX, COLUMNS) for j in range(MIN, MAX) for k in range(i, i + COLUMNS))

print(*gen, end=' ')

