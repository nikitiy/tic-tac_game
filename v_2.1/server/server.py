import socket
from board import Board
from player import Player

# Порт сокета!
port = 1018

# Создание 2-х объектов игроков и доски
p1 = Player("X")
p2 = Player("O")
players = [p1, p2]
board = Board()

# Настройка сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))

sock.listen(2)
print("Ожидание подключения...\n")

# Подключение 2-х клиентов и присвоение первому "X" и второму "O"
clients = []
for i in range(2):
    conn, addr = sock.accept()
    print("Connect: ", addr)
    conn.send(bytes("O", encoding='utf-8')) if i else conn.send(bytes("X", encoding='utf-8'))
    clients.append(conn)
print("\nВсе игроки подключены!")

# Отправка клиентам о готовности игры
clients[0].send(bytes("R", encoding="UTF-8"))
clients[1].send(bytes("R", encoding="UTF-8"))

# Основной цикл игры
# Принимает сообщение от одного клиента с координатой и знаком игрока
# Делает ход через игрока 
# Отправляет другому клиенту координату
counter = 0
while True:
    buff = clients[counter%2].recv(3)
    arr = buff.decode("utf-8").split(" ")
    players[counter%2].move(board, int(arr[0]))
    clients[not(counter%2)].send(bytes(arr[0], encoding="UTF-8"))
    counter += 1
    board.printBoard()

    # проверка на выигрышную комбинацию
    if board.checkWin():
        clients[0].send(bytes(f"W {board.checkWin()}", encoding='utf-8'))
        clients[0].close()
        clients[1].send(bytes(f"W {board.checkWin()}", encoding='utf-8'))
        clients[1].close()  
        sock.close()
        break
    
    # проверка на ничью
    if counter == 9:
        clients[0].send(bytes("N", encoding='utf-8'))
        clients[0].close()
        clients[1].send(bytes("N", encoding='utf-8'))
        clients[1].close()  
        sock.close()
        break
    
