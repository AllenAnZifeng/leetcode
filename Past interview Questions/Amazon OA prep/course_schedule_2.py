from typing import List



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites)==0:
            return [i for i in range(numCourses-1,-1,-1)]

        adj_list = [[False for __ in range(numCourses)] for _ in range(numCourses)]
        for i,j in prerequisites:
            adj_list[j][i]=True

        visited = [0 for _ in range(numCourses)]
        stack=[]

        def dfs(i):
            if visited[i] ==1: # visited
                return True
            if visited[i]==-1:
                return False

            visited[i]=-1
            for j in range(numCourses):
                if adj_list[i][j]:

                    if not dfs(j):
                        return False

            visited[i]=1
            stack.append(i)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return stack[::-1]



















s = Solution().findOrder()