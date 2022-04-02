from board import Board
from player import Player

b = Board()

p1 = Player("X")
p2 = Player("O")

whoMove = 0
while b.checkWin():
    
    p1.move(b) if whoMove % 2 == 0 else p2.move(b)

    whoMove += 1
    if whoMove == 9: 
        print("Ничья")
        break
