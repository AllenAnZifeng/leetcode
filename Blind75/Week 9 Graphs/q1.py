from typing import List

# initialize a 2D array of values
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def dfs(matrix):
  # Check for an empty matrix/graph.
  if not matrix:
    return []

  rows, cols = len(matrix), len(matrix[0])
  visited = set()
  directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
  stack = [(0,0)]

  while stack:
    i, j = stack.pop()
    if (i, j) in visited:
      continue
    print(matrix[i][j])
    visited.add((i, j))
    # Traverse neighbors.
    for direction in directions:
      next_i, next_j = i + direction[0], j + direction[1]
      if 0 <= next_i < rows and 0 <= next_j < cols:
        # Add in question-specific checks, where relevant.
        stack.append((next_i, next_j))
  # def traverse(i, j):
  #   if (i, j) in visited:
  #     return
  #   print(matrix[i][j])
  #   visited.add((i, j))
  #   # Traverse neighbors.
  #   for direction in directions:
  #     next_i, next_j = i + direction[0], j + direction[1]
  #     if 0 <= next_i < rows and 0 <= next_j < cols:
  #       # Add in question-specific checks, where relevant.
  #       traverse(next_i, next_j)
  #
  # for i in range(rows):
  #   for j in range(cols):
  #     traverse(i, j)

# dfs(matrix)



from collections import deque


def bfs(matrix):
    # Check for an empty matrix/graph.
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    queue = deque([(0, 0)])
    while queue:
        curr_i, curr_j = queue.popleft()
        if (curr_i, curr_j) not in visited:
            visited.add((curr_i, curr_j))
            print(matrix[curr_i][curr_j])
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in question-specific checks, where relevant.
                    queue.append((next_i, next_j))
# bfs(matrix)


from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        visited = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        islands = {} # id:size
        idx = 2
        res = 0

        def traverse(i, j):
            if (i, j) in visited:
                return 0

            visited.add((i, j))
            grid[i][j] = idx
            size = 1
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if 0 <= nx < ROW and 0 <= ny < COL and (nx, ny) not in visited and grid[nx][ny] == 1:
                    size += traverse(nx, ny)
            return size

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = traverse(i, j)
                    islands[idx] = size
                    idx += 1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    size = 1
                    neis = set()
                    for dx, dy in dirs:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < ROW and 0 <= ny < COL and grid[nx][ny]>=2:
                            neis.add(grid[nx][ny])
                    size += sum([islands[nei] for nei in neis])
                    res = max(res,size)



        return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))

