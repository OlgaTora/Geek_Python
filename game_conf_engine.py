from random import randint

MAX_CANDY = 29
CANDY = 100
total = 0
residue = 0


def whose_move():
    who = randint(1, 2)
    if who == 1:
        return 1
    else:
        return 2


def candy_quantity():
    global total
    total = CANDY
    return total


def take_from(quantity):
    if 0 < quantity < MAX_CANDY:
        return True
    else:
        return False


def seach_residue(total_quantity):
    global residue
    residue = total - total_quantity
    return residue


def bot():
    if residue % (MAX_CANDY + 1) == 0:
        bot_quantity = randint(1, 29)
    else:
        bot_quantity = residue % (MAX_CANDY + 1)
    return bot_quantity


def game_over():
    return residue < MAX_CANDY

