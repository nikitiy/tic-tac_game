class Board:
    def __init__(self):
        self.board = [""]*9
        self._winComb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def checkWin(self, window, message):
        for each in self._winComb:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]] and self.board[each[0]] != "":
                message.showinfo("Информация", f"Выиграл игрок - {self.board[each[0]]}")
                window.quit()
                exit()
