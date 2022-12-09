from random import randint

M = 3
N = 3
game = [[' '] * M for i in range(N)]


def step_player(x, symb):
    global game
    if game[x[0]][x[1]] == ' ':
        game[x[0]][x[1]] = symb
        print('_' * 12)
        for i in range(len(game)):
            for j in range(len(game[i])):
                print(game[i][j], end=' | ')
            print()
            print('_' * 12, end='')
            print()
        return True, game
    else:
        return False


def count_step(counter):
    if counter == 5:
        return True


def play_again(answer):
    global game
    if answer == 1:
        game = [[' '] * M for i in range(N)]
        return True, game
    elif answer == 0:
        return False


def game_over():
    for i in range(M):
        for j in range(N):
            if game[i][0] == game[i][1] == game[i][2] and game[i][0] != ' ':
                return True
            elif game[0][j] == game[1][j] == game[2][j] and game[0][j] != ' ':
                return True
    if game[1][1] != ' ':
        if game[0][0] == game[1][1] == game[2][2]\
                or game[0][2] == game[1][1] == game[2][0]:
            return True


