from tkinter import *
from tkinter import messagebox as mbox
from board import Board
from player import Player

board = Board()

p1 = Player("X")
p2 = Player("O")

def click1(): 
    if b1.config('text')[-1] in "XO" and b1.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b1.configure(text=f"{p1.move(board, 1) if whoMove % 2 == 0 else p2.move(board, 1)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click2(): 
    if b2.config('text')[-1] in "XO" and b2.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b2.configure(text=f"{p1.move(board, 2) if whoMove % 2 == 0 else p2.move(board, 2)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click3(): 
    if b3.config('text')[-1] in "XO" and b3.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b3.configure(text=f"{p1.move(board, 3) if whoMove % 2 == 0 else p2.move(board, 3)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click4(): 
    if b4.config('text')[-1] in "XO" and b4.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b4.configure(text=f"{p1.move(board, 4) if whoMove % 2 == 0 else p2.move(board, 4)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click5(): 
    if b5.config('text')[-1] in "XO" and b5.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b5.configure(text=f"{p1.move(board, 5) if whoMove % 2 == 0 else p2.move(board, 5)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click6(): 
    if b6.config('text')[-1] in "XO" and b6.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b6.configure(text=f"{p1.move(board, 6) if whoMove % 2 == 0 else p2.move(board, 6)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click7(): 
    if b7.config('text')[-1] in "XO" and b7.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b7.configure(text=f"{p1.move(board, 7) if whoMove % 2 == 0 else p2.move(board, 7)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click8(): 
    if b8.config('text')[-1] in "XO" and b8.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b8.configure(text=f"{p1.move(board, 8) if whoMove % 2 == 0 else p2.move(board, 8)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()

def click9(): 
    if b9.config('text')[-1] in "XO" and b9.config('text')[-1] != "":
        mbox.showwarning("Предупреждение", "Клетка занята!")
        return 
    global whoMove
    b9.configure(text=f"{p1.move(board, 9) if whoMove % 2 == 0 else p2.move(board, 9)}")
    board.checkWin(window, mbox)
    whoMove += 1
    if whoMove == 9:
        mbox.showinfo("Информация", "Ничья!")
        window.quit()


window = Tk()

window.title("Крестики Нолики")
window.geometry("300x300")

whoMove = 0

b1 = Button(window, command=click1)
b2 = Button(window, command=click2)
b3 = Button(window, command=click3)
b4 = Button(window, command=click4)
b5 = Button(window, command=click5)
b6 = Button(window, command=click6)
b7 = Button(window, command=click7)
b8 = Button(window, command=click8)
b9 = Button(window, command=click9)

b1.place(x=0, y=0, width=100, height=100)
b2.place(x=100, y=0, width=100, height=100)
b3.place(x=200, y=0, width=100, height=100)
b4.place(x=0, y=100, width=100, height=100)
b5.place(x=100, y=100, width=100, height=100)
b6.place(x=200, y=100, width=100, height=100)
b7.place(x=0, y=200, width=100, height=100)
b8.place(x=100, y=200, width=100, height=100)
b9.place(x=200, y=200, width=100, height=100)

window.mainloop()
