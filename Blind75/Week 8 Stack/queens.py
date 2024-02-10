# from typing import List
#
#
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         # positive diagonal
#         cols = []
#         positiveDiagonal = [] # r+c
#         negativeDiagonal = [] # r-c
#
#         res = []
#         def place(row:int):
#             if row == n:
#                 board = []
#                 r = '.' * n
#                 for i in range(n):
#                     board.append(r[:cols[i]]+'Q'+r[cols[i]+1:])
#
#                 res.append(board)
#
#                 return
#
#             for c in range(n):
#                 if c not in cols and (row-c) not in negativeDiagonal and (row+c) not in positiveDiagonal:
#                     cols.append(c)
#                     negativeDiagonal.append((row-c))
#                     positiveDiagonal.append(row+c)
#                     place(row+1)
#
#                     cols.pop()
#                     negativeDiagonal.pop()
#                     positiveDiagonal.pop()
#         place(0)
#
#         return res
#
#
#
#
# from collections import deque
# from typing import List
#
#
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#
#         res = 0
#
#         row, col = len(grid), len(grid[0])
#
#         visited = [[False for _ in range(col)] for __ in range(row)]
#
#         def bfs(i, j):
#             fresh = []
#             rot = deque()
#             q = deque()
#             visited[i][j] = True
#             q.append([i, j])
#
#             dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#             while q:
#                 r, c = q.popleft()
#                 if grid[r][c] == 1:
#                     fresh.append([r, c])
#                 elif grid[r][c] == 2:
#                     rot.append([r, c])
#
#                 new_rcs = [(r + dir[0], c + dir[1]) for dir in dirs]
#                 for new_r, new_c in new_rcs:
#                     if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] != 0 and not visited[new_r][
#                         new_c]:
#                         q.append([new_r, new_c])
#                         visited[new_r][new_c] = True
#
#             if len(fresh) ==0:
#                 return  0
#             if len(rot) == 0:
#                 return -1
#
#             count = 0
#
#             while len(fresh) != 0:
#
#                 new_rot = deque()
#
#                 while rot:
#
#                     rot_r, rot_c = rot.popleft()
#                     to_rot = [[rot_r + dir[0], rot_c + dir[1]] for dir in dirs]
#
#                     for to_be_rotted in to_rot:
#                         if to_be_rotted in fresh:
#                             fresh.remove(to_be_rotted)
#                             new_rot.append(to_be_rotted)
#                 rot = new_rot
#                 count += 1
#
#             return count
#
#         for i in range(row):
#             for j in range(col):
#                 if visited[i][j]:
#                     continue
#
#                 if grid[i][j] != 0:
#                     ans = bfs(i, j)
#                     if ans == -1:
#                         return -1
#                     else:
#                         res = max(res, ans)
#
#         return res
#
# grid = [[0,2]]
# print(Solution().orangesRotting(grid))
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])

        rots = deque()
        time = 0
        fresh = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rots.append([i, j])

        if fresh == 0:
            return 0

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while rots:
            new_rot = []

            for r, c in rots:

                to_rot = [[r + dr, c + dc] for dr, dc in dirs]

                for new_r, new_c in to_rot:
                    if new_r in range(ROW) and new_c in range(COL) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        new_rot.append([new_r, new_c])
            rots = new_rot

            time += 1

        if fresh == 0:
            return time
        else:
            return -1

# grid = [[2,1,1],[1,1,0],[0,1,1]]
# print(Solution().orangesRotting(grid))

# s1 = {1}
# s2 = set(s1)
#
# s2.add(2)
# print(s1)
# print(s2)
# print(s1==s2)

