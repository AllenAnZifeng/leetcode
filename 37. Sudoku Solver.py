#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 37. Sudoku Solver.py
@time: 2020/2/9 14:08
'''
from typing import List


import time
start= time.time()
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        candidate_board={}
        row,col=9,9

        def isValidSudoku(board: List[List[str]], r, c) -> bool:
            def row(board, r, c):
                row_stuff = [_ for _ in board[r] if _ != '.']
                return len(row_stuff) == len(set(row_stuff))
            def col(board, r, c):
                # col_stuff = [row[c] for row in board if row[c] != '.']
                col_stuff = [_ for _ in list(zip(*board))[c] if _ != '.']
                return len(col_stuff) == len(set(col_stuff))
            def block(board, r, c):
                row = r // 3 * 3
                col = c // 3 * 3
                b = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            if board[i][j] not in b:
                                b.add(board[i][j])
                            else:
                                return False
                return True
            return row(board, r, c) and col(board, r, c) and block(board, r, c)

        def candidate(board,r,c):
            # print(r,c)
            def currentRow(board,r,c):
                # print(set([_ for _ in board[r] if _ !='.']))
                return set([_ for _ in board[r] if _ !='.'])
            def currentCol(board,r,c):
                # print(set([_ for _ in list(zip(*board))[c] if _ !='.']))
                return set([_ for _ in list(zip(*board))[c] if _ !='.'])
            def currentBlock(board,r,c):
                row,col=r//3*3,c//3*3
                # print(set([board[i][j] for i in range(row,row+3) for j in range(col,col+3) if board[i][j] !='.']))
                return set([board[i][j] for i in range(row,row+3) for j in range(col,col+3) if board[i][j] !='.'])
            s=set('123456789')
            # print(s-(currentRow(board,r,c)|currentCol(board,r,c)|currentBlock(board,r,c)))
            return s-(currentRow(board,r,c)|currentCol(board,r,c)|currentBlock(board,r,c))

        for i in range(row):
            for j in range(col):
                if board[i][j]=='.':
                    candidate_board[(i,j)] = candidate(board,i,j)
        candidate_board = sorted(candidate_board.items(),key=lambda x:len(x[1]))
        # print(candidate_board)
        self.flag= False
        def fill(board,index):
            if index >= len(candidate_board):
                self.flag =True
                return
            r,c= candidate_board[index][0][0],candidate_board[index][0][1]
            for num in candidate_board[index][1]:
                board[r][c]=str(num)
                if isValidSudoku(board,r,c):
                    fill(board,index+1)
                    if self.flag: return
            # after trying all numbers, set grid back to initial
            board[r][c]='.'

        fill(board,0)



board=[
       [".",".","9","7","4","8",".",".","."],
       ["7",".",".",".",".",".",".",".","."],
       [".","2",".","1",".","9",".",".","."],
       [".",".","7",".",".",".","2","4","."],
       [".","6","4",".","1",".","5","9","."],
       [".","9","8",".",".",".","3",".","."],
       [".",".",".","8",".","3",".","2","."],
       [".",".",".",".",".",".",".",".","6"],
       [".",".",".","2","7","5","9",".","."]
       ]

# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]

Solution().solveSudoku(board)
end=time.time()
for r in board:
    print(r)
print(end-start)