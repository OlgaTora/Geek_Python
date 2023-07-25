import random

QUEENS_QUANT = 8
COUNTER_RESULTS = 2


def play_queens(queens: list) -> bool:
    for i in range(QUEENS_QUANT):
        for j in range(i + 1, QUEENS_QUANT):
            if queens[i][0] == queens[j][0] \
                    or queens[i][1] == queens[j][1] \
                    or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def gen_random_queens() -> list:
    queens = []
    counter = 0
    while counter < QUEENS_QUANT:
        coord = (random.randint(1, QUEENS_QUANT + 1), random.randint(1, QUEENS_QUANT + 1))
        if coord not in queens:
            queens.append(coord)
            counter += 1
    return queens


def search_queens() -> list:
    counter = 0
    result = []
    while counter < COUNTER_RESULTS:
        queens = gen_random_queens()
        if play_queens(queens):
            result.append(queens)
            counter += 1
    return result

