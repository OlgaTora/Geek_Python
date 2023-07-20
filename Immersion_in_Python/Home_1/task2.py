#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
MIN = 2
MAX = 10
ROWS = 2
SPACES = '     '


def multy_table():
    for i in range(MIN, MAX):
        for j in range(MIN, MAX//ROWS + 1):
            print_line(i, j)
        print(end='\n')
    print("\n")
    for i in range(MIN, MAX):
        for j in range(MAX//ROWS + 1, MAX):
            print_line(i, j)
        print(end='\n')


def print_line(i, j):
    if i * j < 10:
        print(f'{j} X {i} =  {i * j}', end=SPACES)
    else:
        print(f'{j} X {i} = {i * j}', end=SPACES)


multy_table()

