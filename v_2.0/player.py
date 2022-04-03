class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def move(self, b, place):
        b.board[place-1] = self.symbol
        return self.symbol

