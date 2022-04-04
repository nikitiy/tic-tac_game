import socket
import _thread
from tkinter import *
from tkinter import messagebox as mbox
from button import changeSign


# Подключение к серверу
def connect():
    global sign
    global move

    # получение IP адреса и порта из полей
    addr = address_entry.get()
    port = port_entry.get()

    # Подключение к серверу и получение "X" или "O"
    sock.connect((addr, int(port)))
    sign = sock.recv(1).decode('utf-8')

    # move - определяет можно ли ходить. True - можно, False - нельзя
    move = True if sign == "X" else False

    # Запуск потока, который принимает и обрабатывает сообщения от серсера
    _thread.start_new_thread(get_sign, ())

    # Информирование игрока чей ход первый
    if sign == "X":
        mbox.showinfo("Info", "Вы подлючились первым, сейчас ход ваш!\nПодождитесь соперника!")
    else:
        mbox.showinfo("Info", "Вы подлючились вторым, сейчас не ваш ход!")

# Обработка кнопки настроек по умолчанию
# IP адрес localhost - 127.0.0.1
# Порт - 1018
def defSet():
    address_entry.delete(0, END)
    port_entry.delete(0, END)
    address_entry.insert(0, "127.0.0.1")
    port_entry.insert(0, "1018")

# Поток принимает и обрабатывает сообщения от сервера
# Если приходит цифра 1-9 ставится противоположный знак на эту клетку
# Если приходит "W X/O" - присваивается победа X/O
# Если приходит "N X/O" - Всем присваивается ничья
# После хода противника, переменной move присваивается True, тем самым разрешает ходить 
def get_sign():
    global game
    global move
    while True:
        try:
            data = sock.recv(3).decode('utf-8')
            if data == "R":
                game = True
                mbox.showinfo("Info", "Игра началась!")
            else:
                changeSign(data, all_buttons, "O" if sign == "X" else "X")
                data = data.split(" ")
                if data[0] == "W":
                    mbox.showinfo("Info", f"Победил: {data[1]}")
                    sock.close()
                    window.quit()
                elif data[0] == "N":
                    mbox.showinfo("Info", "Ничья!")
                    sock.close()
                    window.quit()
                move = True
        except:
            print("Игра завершена!")
            exit()

# Обработчики 1-9 кнопок
def click1(): 
    global move
    if b1.config('text')[-1] == "":
        if move and game:
            b1.configure(text=sign)
            sock.send(bytes(f'1 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click2(): 
    global move
    if b2.config('text')[-1] == "":
        if move and game:
            b2.configure(text=sign)
            sock.send(bytes(f'2 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click3(): 
    global move
    if b3.config('text')[-1] == "":
        if move and game and game:
            b3.configure(text=sign)
            sock.send(bytes(f'3 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click4(): 
    global move
    if b4.config('text')[-1] == "":
        if move and game:
            b4.configure(text=sign)
            sock.send(bytes(f'4 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click5(): 
    global move
    if b5.config('text')[-1] == "":
        if move and game:
            b5.configure(text=sign)
            sock.send(bytes(f'5 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click6(): 
    global move
    if b6.config('text')[-1] == "":
        if move and game:
            b6.configure(text=sign)
            sock.send(bytes(f'6 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click7(): 
    global move
    if b7.config('text')[-1] == "":
        if move and game:
            b7.configure(text=sign)
            sock.send(bytes(f'7 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click8(): 
    global move
    if b8.config('text')[-1] == "":
        if move and game:
            b8.configure(text=sign)
            sock.send(bytes(f'8 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")

def click9(): 
    global move
    if b9.config('text')[-1] == "":
        if move and game:
            b9.configure(text=sign)
            sock.send(bytes(f'9 {sign}', encoding='UTF-8'))
            move = False
        elif game == False:
            mbox.showwarning("warning", "Игра ещё не началась!")
        elif move == False:
            mbox.showwarning("warning", "Сейчас не ваш ход!")
    else:
        mbox.showwarning("warning", "Эта клетка занята!")


# Создание и настройка рабочего окна
window = Tk()

window.title("Крестики Нолики")
window.geometry("300x400")

Label(window, text=" IP Адресс сервера:").place(x=0, y=0)
address_entry = Entry(window, width=8)
address_entry.place(x=130, y=0)

Label(window, text=" Порт сервера:").place(x=0, y=25)
port_entry = Entry(window, width=8)
port_entry.place(x=130, y=25)

DefaultSet = Button(window, text="По умол.", command=defSet)
DefaultSet.place(x=215, y=0, width=80, height=45)

Button_Conect = Button(window, text="Подключиться", command=connect)
Button_Conect.place(x=0, y=55, width=300, height=50)

b1 = Button(window, command=click1)
b2 = Button(window, command=click2)
b3 = Button(window, command=click3)
b4 = Button(window, command=click4)
b5 = Button(window, command=click5)
b6 = Button(window, command=click6)
b7 = Button(window, command=click7)
b8 = Button(window, command=click8)
b9 = Button(window, command=click9)

b1.place(x=0, y=100, width=100, height=100)
b2.place(x=100, y=100, width=100, height=100)
b3.place(x=200, y=100, width=100, height=100)
b4.place(x=0, y=200, width=100, height=100)
b5.place(x=100, y=200, width=100, height=100)
b6.place(x=200, y=200, width=100, height=100)
b7.place(x=0, y=300, width=100, height=100)
b8.place(x=100, y=300, width=100, height=100)
b9.place(x=200, y=300, width=100, height=100)

all_buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

# По умл. ходить нельзя
game = False
move = False

# Настройка сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Запуск основного окна
window.mainloop()