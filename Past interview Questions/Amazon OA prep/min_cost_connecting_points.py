from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        f = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        adj_matrix = [[0 for _ in range(len(points))] for __ in range(len(points))]

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                adj_matrix[i][j] = f(points[i], points[j])
                adj_matrix[j][i] = f(points[i], points[j])

        for r in adj_matrix:
            if r==[0]*len(adj_matrix[0]):
                return 0


        # for r in adj_matrix:
        #     print(r)

        visited_index=[]

        border =[] #distance,index


        visited_index.append(0)
        border.extend([[adj_matrix[0][i],i] for i in range(len(adj_matrix[0])) if adj_matrix[0][i]!=0])
        heapq.heapify(border)
        # for x in ([[adj_matrix[0][i],i] for i in range(len(adj_matrix[0])) if adj_matrix[0][i]!=0]):
        #     heapq.heappush(border,x)
        # print(border)

        ans=0

        count=1
        while len(border)!=0:
            # print(border)
            # p = min(border,key=lambda x:x[0])
            p=heapq.heappop(border)
            distance,index=p[0],p[1]
            if index in visited_index:
                pass
            else:
                count+=1

                visited_index.append(index)
                ans+=distance
                # border.extend([[adj_matrix[index][i],i] for i in range(len(adj_matrix[0])) if adj_matrix[index][i]!=0])
                # heapq.heapify(border)
                if count>= len(points):
                    return ans
                for x in [[adj_matrix[index][i],i] for i in range(len(adj_matrix[0])) if adj_matrix[index][i]!=0]:
                    heapq.heappush(border,x)

        if len(visited_index)!=len(points):
            return 0
        else:
            return ans


print(Solution().minCostConnectPoints(
[[0,0],[1,1],[1,0],[-1,1]]))



