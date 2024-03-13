from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == 0:
                return 0
            if (i, j) in visited:
                return -1

            visited.add((i, j))
            sides = 0

            res = [dfs(i + 1, j), dfs(i - 1, j), dfs(i, j + 1), dfs(i, j - 1)]

            for r in res:
                if r == 0:
                    sides += 1
                elif r == -1:
                    pass
                else:
                    sides += r
            print(f'{i=}, {j=} {visited=}')
            print(f'{res=} {sides=}')
            return sides


        res = 0
        for i in range(ROW):
            for j in range(COL):
                res = max(dfs(i, j), res)

        return res

print(Solution().islandPerimeter([[1,1,1],[1,1,1],[1,1,1],[0,1,1]]))

