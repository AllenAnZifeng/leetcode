from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[False for __ in range(numCourses)] for _ in range(numCourses)]
        for i,j in prerequisites:
            adj_list[j][i] = True

        visited = [0 for _ in range(numCourses)]
        for r in adj_list:
            print(r)

        def dfs(i:int)->bool:
            if visited[i]==1:
                return True
            if visited[i]==-1:
                return False

            visited[i]=-1
            for j in range(numCourses):
                if adj_list[i][j]:
                    if not dfs(j):
                        return False

            visited[i]=1

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True






s=Solution().canFinish(
5,
[[1,4],[2,4],[3,1],[3,2]])
print(s)