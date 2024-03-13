from collections import deque
from typing import List

#
# class Solution:
#     def movesToMakeZigzag(self, nums: List[int]) -> int:
#         evenmoves = 0
#         oddmoves = 0
#         # even case
#         for i in range(1,len(nums),2):
#             if i+1 == len(nums):
#                 if nums[i] < nums[i-1]:
#                     continue
#                 else:
#                     evenmoves += nums[i] - nums[i-1] +1
#                     continue
#             if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
#                 continue
#             else:
#                 evenmoves += nums[i] - min(nums[i-1], nums[i+1]) + 1
#         # odd
#         for i in range(0,len(nums),2):
#             print(oddmoves)
#             if i-1<0:
#                 if nums[i] >= nums[i+1]:
#                     oddmoves += nums[i] - nums[i+1] +1
#                 continue
#             if i+1 >= len(nums):
#                 if nums[i] >= nums[i-1]:
#                     oddmoves += nums[i] - nums[i-1] +1
#
#                 continue
#             if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
#                 continue
#             else:
#                 oddmoves += nums[i] -  min(nums[i-1], nums[i+1]) + 1
#
#
#
#         print(oddmoves,evenmoves)
#         return min(oddmoves,evenmoves)
#
# print(Solution().movesToMakeZigzag([6,6,1,3,7,8])) # 6


# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#         ROW = len(board)
#
#         start = 1
#         q = deque([start])
#         count = 0
#
#         def get_location(moves):
#             moves = moves - 1
#             if (moves // ROW) % 2 == 0:  # increasing
#                 r = ROW - moves // ROW - 1
#                 c = moves % ROW
#             else:
#                 r = ROW - moves // ROW - 1
#                 c = ROW - moves % ROW - 1
#             return board[r][c]
#
#         visit = set()
#         visit.add(start)
#         while q:
#             print(q)
#             for i in range(len(q)):
#                 cur = q.popleft()
#
#                 if cur == ROW ** 2:
#                     return count
#
#                 for nxt in range(cur + 1, min(cur + 6, ROW ** 2) + 1):
#                     if nxt not in visit:
#                         visit.add(nxt)
#                         ladder = get_location(nxt)
#                         if ladder != -1:
#                             if ladder not in visit:
#                                 # visit.add(ladder)
#                                 q.append(ladder)
#                         else:
#                             q.append(nxt)
#
#             count += 1
#
#         return -1
# board =[[-1,-1,-1,46,47,-1,-1,-1],
#         [51,-1,-1,63,-1,31,21,-1],
#         [-1,-1,26,-1,-1,38,-1,-1],
#         [-1,-1,11,-1,14,23,56,57],
#         [11,-1,-1,-1,49,36,-1,48],
#         [-1,-1,-1,33,56,-1,57,21],
#         [-1,-1,-1,-1,-1,-1,2,-1],
#         [-1,-1,-1,8,3,-1,6,56]]
# print(Solution().snakesAndLadders(board))

from typing import (
    List,
)

from typing import (
    List,
)

#
# class Solution:
#     """
#     @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
#     @return: an integer, the maximum enemies you can kill using one bomb
#     """
#
#     def max_killed_enemies(self, grid: List[List[str]]) -> int:
#         # write your code here
#         if len(grid) == 0:
#             return 0
#         ROW, COL = len(grid), len(grid[0])
#         n = [[0 for i in range(COL)] for j in range(ROW)]
#         s = [[0 for i in range(COL)] for j in range(ROW)]
#         w = [[0 for i in range(COL)] for j in range(ROW)]
#         e = [[0 for i in range(COL)] for j in range(ROW)]
#
#         for i in range(ROW):
#             for j in range(COL):
#                 if grid[i][j] == 'W':
#                     continue
#                 if grid[i][j] == 'E':
#                     n[i][j] += 1
#                     w[i][j] += 1
#                 if i > 0:
#                     n[i][j] += n[i - 1][j]
#                 if j > 0:
#                     w[i][j] += w[i][j - 1]
#
#         for i in range(ROW - 1, -1, -1):
#             for j in range(COL - 1, -1, -1):
#                 if grid[i][j] == 'W':
#                     continue
#                 if grid[i][j] == 'E':
#                     s[i][j] += 1
#                     e[i][j] += 1
#                 if i < ROW - 1:
#                     s[i][j] += s[i + 1][j]
#                 if j < COL - 1:
#                     e[i][j] += e[i][j + 1]
#
#         res = 0
#         for i in range(ROW):
#             for j in range(COL):
#                 if grid[i][j] == '0':
#                     res = max(res, n[i][j] + s[i][j] + e[i][j] + w[i][j])
#
#
#         return res
#
# print(Solution().max_killed_enemies([["0","E","0","0"],
#                                      ["E","0","W","E"],
#                                      ["0","E","0","0"]])) # 3


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        ROW, COL = len(board), len(board[0])

        for dx, dy in dirs:
            x, y = rMove, cMove
            count = 0
            while 0 <= x < ROW and 0 <= y < COL:
                x += dx
                y += dy
                count += 1
                print(x,y)
                if board[x][y] == '.':
                    break
                if board[x][y] == color:  # same color
                    # print('here',count, x,y)
                    if count >= 2:
                        return True
                    else:
                        break
        return False
#
# board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]
#
# print(Solution().checkMove(board,4,4,"W")) # True

# grid = [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
#
# for r in grid:
#     print(r)


# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         res = set()
#         nums1.sort()
#         nums2.sort()
#         nums3.sort()
#         nums4.sort()
#         nums4 = set(nums4)
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 for k in range(len(nums3)):
#                     search = 0 - nums1[i] - nums2[j] - nums3[k]
#                     if search in nums4:
#                         res.add((nums1[i],nums2[j],nums3[k],search))
#         print(res)
#         return len(res)
#
# print(Solution().fourSumCount([1,2],[-2,-1],[-1,2],[0,2])) # 2




class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = (1, l, r)
        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    t = max(t, (r - l + 1, l, r), key=lambda x: x[0])
                    l -= 1
                    r += 1
                    print(t)
                else:
                    break
        res = t
        print(res)
        for i in range(len(s) - 1):
            l, r = i, i + 1
            t = (0, l, r)
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    t = max(t, (r - l + 1, l, r), key=lambda x: x[0])
                    l -= 1
                    r += 1
                else:
                    break
        res = max(res, t, key=lambda x: x[0])

        return s[res[1]:res[2] + 1]

# print(Solution().longestPalindrome("babad")) # bab


arr = [4,6,76]

for i,v in enumerate(arr):
    print(i,v)
