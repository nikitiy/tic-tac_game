class Board:
    def __init__(self):
        self.board = [""]*9
        self.winComb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    # Проверка выигрышной комбинации
    def checkWin(self):
        for each in self.winComb:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]] and self.board[each[0]] != "":
                return self.board[each[0]]

    # Печать в консоль текущей доски
    def printBoard(self):
        print(f"\n{self.board[0]} | {self.board[1]} | {self.board[2]}\n=========\n\
{self.board[3]} | {self.board[4]} | {self.board[5]}\n=========\n\
{self.board[6]} | {self.board[7]} | {self.board[8]}\n")
