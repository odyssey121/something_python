class Color:
    WHITE = 0
    BLACK = 1
    EMPTY = ' .'

class AbsChess:
    def __init__(self,color):
        self.color = color

    def __repr__(self):
        return self.IMG[self.color]

class Empty:
    def __init__(self):
        self.color = Color.EMPTY

    def __repr__(self):
        return self.color

class Pawn(AbsChess):
    IMG = ('♙', '♟')

    def get_move(self, board, y , x):
        move = []
        if self.color == Color.WHITE and y < 7 and board.get_color(y+1,x) == Color.EMPTY:
            move.append([y+1,x])
        return move
        

class King(AbsChess):
    IMG = ('♔', '♚')

class Board:
    def __init__(self):
        self.board = [ [Empty()] * 8 for i in range(8) ]
        self.board[2][1] = Pawn(Color.WHITE)
        self.board[6][1] = King(Color.BLACK)

    def get_color(self, y, x):
        return self.board[y][x].color
    def get_move(self, y, x):
        return self.board[y][x].get_move(self, y, x)

    def __repr__(self):
        rep = ''
        for i in range(8):
            rep += ' '.join(map(str,(self.board[i])))+ '\n'
        return rep



print(Board().get_move(2,1))

