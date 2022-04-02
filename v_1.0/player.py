class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def move(self, b):
        place = int(input(f"Куда поставить {self.symbol}? ")) - 1
        while True:
            try:
                # Проверка на занятость клетки
                while b.board[place] == "X" or b.board[place] == "O": place = int(input("Это место уже занято, подумайте лучше!: ")) - 1

                b.board[place] = self.symbol
                b.printBoard()
                break
            # Исключение на случай, если клетка была не найдена 
            except:
                place = int(input("Такой клетки не существует, подумайте лучше!: "))
