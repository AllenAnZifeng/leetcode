from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        g = {}
        for i in range(n):
            g[i] = []

        edges = {(a,b) for a,b in connections}
        print(edges)
        for src,dst in connections:
            g[src].append(dst)
            g[dst].append(src)
        self.changes = 0

        def dfs(node,prev):

            for nei in g[node]:
                if (nei,node) not in edges:
                    print(f'{nei=}, {node=}')
                    self.changes +=1
                if nei != prev:
                    dfs(nei,node)

        dfs(0,-1)
        return self.changes
print(Solution().minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) ) # 3



