class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
    # Делает ход и записывает символ на доске 
    def move(self, b, place):
        b.board[place-1] = self.symbol
        return self.symbol

