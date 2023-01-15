# Задача 3. Создайте программу для игры в "Крестики-нолики".


import random
from tkinter import *

form = Tk()
form.title('Игра крестики-нолики')

game_run = True
field = []
cross_count = 0


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'skyblue'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            bot_move()
            check_win('O')


def check_win(smb):
    for n in range(3):
        check(field[n][0], field[n][1], field[n][2], smb)
        check(field[0][n], field[1][n], field[2][n], smb)
    check(field[0][0], field[1][1], field[2][2], smb)
    check(field[2][0], field[1][1], field[0][2], smb)


def check(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'lightgreen'
        global game_run
        game_run = False


def win(a1, a2, a3, smb):
    result = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        result = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        result = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        result = True
    return result


def bot_move():
    for n in range(3):
        if win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if win(field[2][0], field[1][1], field[0][2], 'O'):
        return

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(text=' ', width=6, height=3,
                        font=('Arial', 18, 'bold'),
                        background='skyblue',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(text='Начать заново', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

form.mainloop()
