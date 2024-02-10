from collections import deque
from typing import List


# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#
#
#         def f(index, cur):
#             if index == len(matchsticks):
#                 return False
#             if len(cur) > 1 and cur[-1] != cur[-2]:
#                 return False
#             if len(cur) == 3:
#                 remain = sum(matchsticks[index:])
#                 if remain == cur[-1]:
#                     return True
#                 else:
#                     return False
#
#             for i in range(index, len(matchsticks)):
#                 number = sum(matchsticks[index:i + 1])
#                 if f(i + 1, cur + [number]):
#                     return True
#
#             return False
#
#         return f(0, [])

# print(Solution().makesquare([1,1,2,2,2]))
#
# class Solution:
#     def splitString(self, s: str) -> bool:
#
#         def f(index, cur,level=0):
#             print(level*"\t",cur)
#
#             if len(cur) > 1:
#                 if cur[-1] + 1 != cur[-2]:
#                     return False
#             if index == len(s):
#                 if len(cur) > 1:
#                     return True
#                 else:
#
#                     return False
#             for i in range(index, len(s)):
#                 n = int(s[index:i + 1])
#                 if f(i + 1, cur + [n],level+1):
#                     return True
#             return False
#
#         return f(0, [])
#
#
# print(Solution().splitString('050043'))

#
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
#         bool]:
#
#         # [pre, nxt]
#         g = {}
#
#         for i in range(numCourses):
#             g[i] = set()
#
#         for pre, nxt in prerequisites:
#             g[nxt].add(pre)
#
#         def dfs(course):
#
#             for pre in g[course]:
#                 g[course] = g[course].union(dfs(pre))
#             return g[course]
#
#         for i in range(numCourses):
#             g[i].union(dfs(i))
#
#         print(g)
#         res = []
#         for pre, nxt in queries:
#             if pre in g[nxt]:
#                 res.append(True)
#             else:
#                 res.append(False)
#
#         return res
# print(Solution().checkIfPrerequisite(5,[[0,1],[1,2],[2,3],[3,4]],[[0,4],[4,0],[1,3],[3,0]]))
#
# s1 = {1,2,3}
# s2 = {3,4,5}
# s1 &= s2
# print(s1)

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        def dfs(i, j):
            if 0 <= i < ROW and 0 <= j < COL and grid[i][j] == 1:
                grid[i][j] = '*'
                q.append((i, j))
                for dx, dy in dirs:
                    dfs(i + dx, j + dy)
        flag = False
        for i in range(ROW):
            if flag:
                break
            for j in range(COL):
                if grid[i][j] != 0:
                    dfs(i, j)
                    flag = True
                    break

        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    newx, newy = x + dx, y + dy
                    if 0 <= newx < ROW and 0 <= newy < COL:
                        if grid[newx][newy] == 1:
                            return res -1
                        if grid[newx][newy] == 0:
                            grid[newx][newy] = '*'
                            q.append((newx, newy))


print(Solution().shortestBridge([[0,1],[1,0]]))


