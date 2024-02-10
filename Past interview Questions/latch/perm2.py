from typing import List


# arr = [1,2,3,4,5]
#
# res = []
# path = []
# def combo(i):
#     if len(path) == 3:
#         res.append(path[:])
#         return
#
#     if i == len(arr):
#         return
#
#     path.append(arr[i])
#     combo(i+1)
#     path.pop()
#     combo(i + 1)
#
# combo(0)
# print(res)
#



# check if two intervals overlap

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#
#         res = []
#
#         d = {}
#
#         for n in nums:
#             if n not in d:
#                 d[n] =1
#             else:
#                 d[n] +=1
#
#         def dfs(cur):
#             if len(cur) == len(nums):
#                 res.append(cur[:])
#                 return
#             for n in d.keys():
#                 if d[n]!=0:
#                     d[n]-=1
#                     cur.append(n)
#                     dfs(cur[:])
#                     cur.pop()
#                     d[n]+=1
#
#         dfs([])
#         return res
#
# print(Solution().permute([1,1,2]))


class State:
    def __init__(self,board,player):
        self.board = board
        self.player = player

    def flipPlayer(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
    def __hash__(self):
        t = tuple(tuple(row) for row in self.board)
        return hash((t,self.player))

    def __eq__(self, other:'State'):
        if self.player == other.player and self.board == other.board:
            return True
        else:
            return False
    def __str__(self):
        res = ''
        for row in self.board:
            res += '.'.join(row) + '\n'
        res += f'Next Player {self.player}'
        return res
    def checkValid(self):
        for r in range(3):
            if self.board[r][0] != '' and self.board[r][0] == self.board[r][1] == self.board[r][2]:
                return True

        for c in range(3):
            if self.board[0][c] != '' and self.board[0][c] == self.board[1][c] == self.board[2][c]:
                return True

        if self.board[0][0] != '' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True

        if self.board[0][2] != '' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True

        # check full
        for row in self.board:
            if '' in row:
                return False
        return True

    def copy(self):
        board = [row[:] for row in self.board]
        return State(board,self.player)



class Simulation:

    def __init__(self):
        self.games = set()
        self.count = 0

    def getBoard(self):
        return [['' for _ in range(3)] for __ in range(3)]
    def getState(self):
        return State(self.getBoard(),'X')
    def play(self,i,j,state:State):

        if state.board[i][j] != '':
            return




        state.board[i][j] = state.player
        state.flipPlayer()

        if state.checkValid():
            self.games.add(state)
            self.count +=1
            print(self.count)
            return

        for r in range(3):
            for c in range(3):
                self.play(r,c,state.copy())


    def main(self):
        for r in range(3):
            for c in range(3):
                self.play(r,c,self.getState())


a = [None]
print(a)