import tkinter as tk
from tkinter import messagebox
from engine import create_field, draw_field, game_over, dictionary
from constants import SIZE

symb = 'X'
count = 0
list_field = create_field()


def title():
    title_field = draw_field('500x170', 'black')
    lbl = tk.Label(
        title_field,
        text='Крестики - нолики',
        font=('Terminator Cyr 4', 25),
        fg='yellow', bg='black',
        anchor=tk.W
    )
    lbl.grid(column=1, row=0)
    btn = tk.Button(
        title_field,
        text='Нажми, если хочешь\n повеселиться!',
        bg='black', fg='red',
        relief=tk.RAISED,
        justify=tk.CENTER,
        font=('Terminator Cyr 4', 25),
        command=title_field.destroy,
    )
    btn.grid(column=1, row=5)
    title_field.mainloop()


def clicked(row, col):
    global symb, count
    if list_field[row][col] == ' ':
        list_field[row][col] = symb
        label = tk.Label(
            text=symb,
            font=('mono', 120, 'bold'),
            bg='green')
        label.grid(row=row, column=col, sticky='nsew')
        count += 1
        if game_over(list_field):
            messagebox.showinfo('Срочное СООБЩЕНИЕ', f'Выиграл мастер игры {symb}')
            res = messagebox.showerror('Срочное СООБЩЕНИЕ', 'Нажмите, чтобы завершить игру!')
            if res:
                quit()
        elif count == 9:
            messagebox.showinfo('Срочное СООБЩЕНИЕ', f'Господа, у вас ничья!')
            res = messagebox.showerror('Срочное СООБЩЕНИЕ', 'Нажмите, чтобы завершить игру!')
            if res:
                quit()
        symb = '0' if symb == 'X' else 'X'


def play():
    field = draw_field('800x800', 'gray')
    for i in range(SIZE):
        field.columnconfigure(i, weight=1, minsize=75)
        field.rowconfigure(i, weight=1, minsize=50)
        for j in range(SIZE):
            frame = tk.Frame(
                master=field,
                relief=tk.RAISED,
                borderwidth=1,
            )
            frame.grid(row=i, column=j, padx=6, pady=6)

            button = tk.Button(
                master=frame,
                text=dictionary(),
                width=10, height=5,
                font=('Verdana', 20, 'bold'),
                bg='yellow',
                command=lambda row=i, col=j: clicked(row, col)
            )
            button.grid(row=i, column=j, sticky='nsew')
    field.mainloop()
