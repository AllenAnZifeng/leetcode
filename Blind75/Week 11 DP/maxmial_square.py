from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        ROW, COL = len(matrix), len(matrix[0])

        cache = {}

        def f(r, c):  # return sqaure length
            IF (r, c) in cache:
                return cache[(r, c)]

            IF matrix[r][c] == 0:
                cache[(r, c)] = 0
                return cache[(r, c)]

            bot, right, botright = 0, 0, 0
            IF r + 1 < ROW:
                bot = f(r + 1, c)
            IF c + 1 < COL:
                right = f(r, c + 1)
            IF r + 1 < ROW and c + 1 < COL:
                botright = f(r + 1, c + 1)

            cache[(r, c)] = min(bot, right, botright) + 1
            return cache[(r, c)]

        f(0, 0)

        length = max(cache.values())
        print(cache)
        return length ** 2

print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 4
