#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 36. Valid Sudoku.py
@time: 2020/2/7 23:16
'''
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=9,9
        col_sets = [set() for _ in range(col)]
        block_sets =[set() for _ in range(col)]
        for r in range(row):
            row_set=set()
            for c in range(col):
                if board[r][c] =='.': continue
                if board[r][c] in row_set or board[r][c] in col_sets[c] or board[r][c] in block_sets[(r//3)*3+c//3]:
                    # print(board[r][c],r,c)
                    # print(row_set)
                    # print(col_sets)
                    # print(block_sets,block_sets[c//3])
                    return False
                else:
                    row_set.add(board[r][c])
                    col_sets[c].add(board[r][c])
                    block_sets[(r//3)*3+c//3].add(board[r][c])

        return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(board))
print(*board)