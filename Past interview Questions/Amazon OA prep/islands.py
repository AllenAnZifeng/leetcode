
from typing import List

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
def numIslands( grid: List[List[str]]) -> int:
    def expand(i, j):
        # print('expanding',i,j)
        # p(visited)

        # if grid[i][j] == "0":
        #     return
        if i + 1 < len(grid) and visited[i+1][j]==False and grid[i+1][j]=="1":
            visited[i+1][j] = True
            expand(i + 1, j)
        if i - 1 >= 0 and visited[i-1][j]==False and grid[i-1][j]=="1":
            visited[i-1][j] = True
            expand(i - 1, j)
        if j + 1 < len(grid[0]) and visited[i][j+1]==False and grid[i][j+1]=="1":
            visited[i][j+1] = True
            expand(i, j + 1)
        if j - 1 >= 0 and visited[i][j-1]==False and grid[i][j-1]=="1":
            visited[i][j-1] = True
            expand(i, j - 1)

    def p(v):
        for x in v:
            print(x)

    visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]

    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # p(visited)
            # print(i,j)
            if visited[i][j] == False and grid[i][j]=="1":

                # p(visited)
                visited[i][j] = True
                # p(visited)
                # print('before',i,j)

                expand(i,j)

                count+=1
    return count




print(numIslands(grid))