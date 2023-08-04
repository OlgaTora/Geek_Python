import random

QUEENS_QUANT = 8
COUNTER_RESULTS = 4


def play_queens_v2(x: list[int], y: list[int]) -> bool:
    for i in range(QUEENS_QUANT):
        for j in range(i + 1, QUEENS_QUANT):
            if x[i] == x[j] or y[i] == y[j] \
                    or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def gen_random_queens_v2(x: list[int], y: list[int]) -> tuple[list, list]:
    random.shuffle(x)
    random.shuffle(y)
    return x, y


def search_queens_v2() -> dict:
    counter = 0
    result = {}
    x = list(range(1, QUEENS_QUANT + 1))
    y = list(range(1, QUEENS_QUANT + 1))
    while counter < COUNTER_RESULTS:
        x_curr, y_curr = gen_random_queens_v2(x, y)
        if play_queens_v2(x_curr, y_curr):
            counter += 1
            result[f'x {counter}'] = tuple(x_curr)
            result[f'y {counter}'] = tuple(y_curr)
    return result

