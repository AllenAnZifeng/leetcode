import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # prim, take node
        visit = set()
        g = {}
        for x, y in points:
            g[(x, y)] = {}  # {nei: dist}

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    xi, yi = points[i]
                    xj, yj = points[j]
                    dist = abs(xi - xj) + abs(yi - yj)
                    g[(xi, yi)][(xj, yj)] = dist

        x0, y0 = points[0]
        # heapq.heappush((x0,y0))
        visit.add((x0, y0))
        remainder = []  # min heap

        for node in points[1:]:
            node = tuple(node)
            d = g[node][(x0, y0)]
            heapq.heappush(remainder, [d, node])

        print(remainder)
        res = 0
        while len(visit) < len(points):
            dist, cur = heapq.heappop(remainder)
            if cur in visit:
                continue
            visit.add(cur)

            print(dist,cur)
            res += dist

            for nei, d in g[cur].items():
                if nei not in visit:
                    heapq.heappush(remainder, [d, nei])

            print((remainder))
        return res

print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))