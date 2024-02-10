class Board:
    def __init__(self):
        self.board = [['' for i in range(3)] for j in range(3)]
        self.player = 'X'

        self.backtrack = [] # (board,player)
        self.endSates = set()

        self.count = 0


    def __str__(self):
        return f'{self.board[0]}\n{self.board[1]}\n{self.board[2]}\n{self.player}'

    def flipPlayer(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def checkEnd(self):
        # row
        for r in range(3):
            if self.board[r][0] != '' and self.board[r][0] == self.board[r][1] == self.board[r][2]:

                return True

        # col
        for c in range(3):
            if self.board[0][c] != '' and self.board[0][c] == self.board[1][c] == self.board[2][c]:

                return True

        # diag
        if self.board[0][0] != '' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != '' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        for row in self.board:
            if '' in row:
                return False
        print('board full')
        return True

    def getBoardState(self):
        boardTuple = tuple(tuple(self.board[i][j] for i in range(3)) for j in range(3))
        return (boardTuple,self.player)

    def recoverState(self,state):
        self.board = [[state[0][i][j] for j in range(3)] for i in range(3)]
        self.player = state[1]
    def start(self,i,j): # assume X goes first
        if self.board[i][j]!='':
            return


        state = self.getBoardState()
        self.backtrack.append(state)

        self.board[i][j] =self.player
        self.flipPlayer()

        if self.checkEnd():
            self.endSates.add(self.getBoardState())
            self.count +=1
            self.recoverState(self.backtrack.pop())
            return


        for r in range(3):
            for c in range(3):
                self.start(r,c)

        self.recoverState(self.backtrack.pop())

    def main(self):
        for r in range(3):
            for c in range(3):
                self.start(r, c)



b = Board()
# b.start(0,0)
# print(b.count)
b.main()
print(b.count)
print(len(b.endSates))






