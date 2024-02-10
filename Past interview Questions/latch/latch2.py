class State:
    def __init__(self, board, player):
        self.board = board
        self.player = player


    def __eq__(self, other):
        return self.board == other.board and self.player == other.player

    def __hash__(self):
        t = tuple([tuple(row[:]) for row in self.board])
        return hash((t, self.player))

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

        # check board full
        for row in self.board:
            if '' in row:
                return False
        # print('board full')
        return True

    def copy(self):
        return State([row[:] for row in self.board], self.player)

class Simulate:
    def __init__(self):
        self.endSates = set()
        self.count = 0
    def getNewBoard(self):
        return [['' for i in range(3)] for j in range(3)]

    def start(self, i, j, state):  # assume X goes first
        if state.board[i][j] != '':
            return

        state.board[i][j] = state.player
        state.flipPlayer()

        if state.checkEnd():
            self.endSates.add(state.copy())
            self.count += 1
            print(len(self.endSates))
            return



        for r in range(3):
            for c in range(3):
                self.start(r, c, state.copy())


    def main(self):
        for r in range(3):
            for c in range(3):
                s1 = State(self.getNewBoard(), 'X')
                self.start(r, c, s1.copy())
                # s2 = State(self.getNewBoard(), 'O')
                # self.start(r, c, s2.copy())




obj = Simulate()
obj.main()
print(len(obj.endSates))
print(obj.count)



# b = [['X', 'O', 'O'],
#      ['O', 'X', 'X'],
#      ['X', 'O', 'O']]
#
# s = State(b, 'X')
# print(s.checkEnd())