from typing import List


# m = [[1,2],[3,4]]

# print(m)

# print(list(zip(*m))) # matrix transpose


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         zeros = []
#         row , col = len(matrix),len(matrix[0])
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     zeros.append((i,j))
#
#         for i,j in zeros:
#             matrix[i] = [0 for _ in range(col)]
#             for k in range(row):
#                 matrix[k][j] = 0
#                 # print(matrix)
#
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#
#         row0Flag = False
#         col0Flag = False
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = -1
#                     matrix[0][j] = -1
#                     if i == 0:
#                         row0Flag = True
#                     if j == 0:
#                         col0Flag = True
#
#         for i in range(1,len(matrix)):
#             if matrix[i][0]==-1:
#                 matrix[i] = [0] * len(matrix[0])
#         for j in range(1, len(matrix[0])):
#             if matrix[0][j]==-1:
#                 for i in range(len(matrix)):
#                     matrix[i][j] = 0
#
#         if row0Flag:
#             matrix[0] = [0] * len(matrix[0])
#         if col0Flag:
#             for i in range(len(matrix)):
#                 matrix[i][0] = 0




#
# m =[[1,1,1],[1,0,1],[1,1,1]]
# Solution().setZeroes(m)
# print(m)


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#
#
#
#         while len(matrix) > 0:
#             res.extend(matrix[0])
#             matrix = matrix[1:]
#             matrix = list(zip(*matrix))
#             matrix.reverse()
#
#         return res
#
# print(Solution().spiralOrder( [[1,2,3],[4,5,6],[7,8,9]]))

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         for i in range(len(matrix)):
#             for j in range(i+1,len(matrix)):
#                 matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
#
#         for i in range(len(matrix)):
#             matrix[i] = matrix[i][::-1]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            row = []
            for j in range(len(board)):
                if board[i][j] != '.':
                    row.append(board[i][j])
            if len(row) != len(set(row)):
                return False

        board = list(zip(*board))

        for i in range(len(board)):
            row = []
            for j in range(len(board)):
                if board[i][j] != '.':
                    row.append(board[i][j])
            if len(row) != len(set(row)):
                return False

        board = list(zip(*board))

        for i in range(0,len(board),3):
            for j in range(0, len(board), 3):
                b =[r[j:j+3] for r in board[i:i+3]]

                s = []
                for r in b:
                    s.extend(r)
                s = [x for x in s if x !='.']

                if len(s) != len(set(s)):
                    return False

        return True