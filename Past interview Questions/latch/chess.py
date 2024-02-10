from typing import List

class Position:
    def __init__(self,x:int,y:int): # 0,0 is bottom left  0-7
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
class Board:
    def __init__(self):
        self.board = [['' for _ in range(8)] for __ in range(8)]
        self.player = 'white'
        self.whitePieces = {'Rook':2,'Knight':2,'Bishop':2,'Queen':1,'King':1,'Pawn':8}
        self.blackPieces = {'Rook':2,'Knight':2,'Bishop':2,'Queen':1,'King':1,'Pawn':8}

    def __str__(self):
        res = ''
        for row in self.board:
            temp = []
            for x in row:
                if x == '':
                    temp.append('   ')
                else:
                    temp.append(str(x))
            res += '|'.join(temp) + '\n'
        return res

    def getStats(self):
        print(f'White: {self.whitePieces}')
        print(f'Black: {self.blackPieces}')

    def initiliazeBoard(self):
        self.board[0][0] = Rook('black',Position(0,0),self)
        self.board[3][0] = Rook('white',Position(7,0),self)
    def flipPlayer(self):
        if self.player == 'white':
            self.player = 'black'
        else:
            self.player = 'white'

    def moveP1toP2(self,p1:Position,p2:Position):
        toRemove = self.board[p2.x][p2.y]
        if toRemove != '': # type: Piece

            if isinstance(toRemove,Piece) and toRemove.color == 'white':
                self.whitePieces[toRemove.name] -= 1
            elif isinstance(toRemove,Piece) and toRemove.color == 'black':
                self.blackPieces[toRemove.name] -= 1

        self.board[p2.x][p2.y] = self.board[p1.x][p1.y]
        self.board[p1.x][p1.y] = ''

    def checkEnd(self):
        pass




class Piece:
    def __init__(self,color:str,position:Position,board:Board):
        self.color = color
        self.position = position
        self.name = ''
        self.board = board

    def move(self,target:Position)->bool:
        if target in self.getMoves():
            self.board.moveP1toP2(self.position,target)
            self.position = target
            return True
        else:
            return False
    def getMoves(self)->List[Position]:
        pass

class Rook(Piece):
    def __init__(self,color,position,board):
        super().__init__(color,position,board)
        self.name = 'Rook'

    def __str__(self):
        return self.color[0] + '车'

    def getMoves(self):
        moves = [] # type: List[Position]
        for i in range(self.position.x+1,8):
            if self.board.board[i][self.position.y] == '':
                moves.append(Position(i,self.position.y))
            else:
                piece = self.board.board[i][self.position.y]
                if isinstance(piece,Piece) and piece.color != self.color:
                    moves.append(Position(i,self.position.y))
                break

        for i in range(self.position.x-1,-1,-1):
            if self.board.board[i][self.position.y] == '':
                moves.append(Position(i,self.position.y))
            else:
                piece = self.board.board[i][self.position.y]
                if isinstance(piece,Piece) and piece.color != self.color:
                    moves.append(Position(i,self.position.y))
                break

        for j in range(self.position.y+1,8):
            if self.board.board[self.position.x][j] == '':
                moves.append(Position(self.position.x,j))
            else:
                piece = self.board.board[self.position.x][j]
                if isinstance(piece,Piece) and piece.color != self.color:
                    moves.append(Position(self.position.x,j))
                break
        for j in range(self.position.y-1,-1,-1):
            if self.board.board[self.position.x][j] == '':
                moves.append(Position(self.position.x,j))
            else:
                piece = self.board.board[self.position.x][j]
                if isinstance(piece,Piece) and piece.color != self.color:
                    moves.append(Position(self.position.x,j))
                break
        return moves

b = Board()
b.initiliazeBoard()
print(b)
b.getStats()
res = b.board[0][0].move(Position(7,0))
print(res)
print(b)
b.getStats()