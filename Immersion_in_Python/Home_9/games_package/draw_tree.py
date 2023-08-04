"""
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
"""

STAR = '*'
SPACE = ' '


def draw_fir_tree(rows):
    spaces = rows - 1
    stars = 1
    if rows < 2:
        print("This tree is impossible")
    else:
        for i in range(rows):
            print(SPACE * spaces + STAR * stars + SPACE * spaces)
            stars += 2
            spaces -= 1


draw_fir_tree(int(input('Input rows for Christmas tree: ')))
