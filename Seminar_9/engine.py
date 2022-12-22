import tkinter as tk
from random import randint
list_field = []


def dictionary():
    lst = ['Нажми меня', 'Нажми', 'Давай сюда',
           'Я кнопка', 'Я тут', 'Тыкай сюда',
           'Харе думать', 'На-жи-май', 'Жми уже']
    fnd = lst[randint(0, 8)]
    return fnd


def create_field(m=3, n=3):
    global list_field
    list_field = [[' '] * m for i in range(n)]
    return list_field


def draw_field(coords, color):
    root = tk.Tk()
    root.configure(bg=color)
    root.geometry(coords)
    root.title("You're wellcome to the HELL")
    return root


def game_over(data):
    for i in range(3):
        for j in range(3):
            if data[i][0] == data[i][1] == data[i][2] and data[i][0] != ' ':
                return True
            elif data[0][j] == data[1][j] == data[2][j] and data[0][j] != ' ':
                return True
    if data[1][1] != ' ':
        if data[0][0] == data[1][1] == data[2][2] \
                or data[0][2] == data[1][1] == data[2][0]:
            return True
