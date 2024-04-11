edges = [(1, 2), (2, 3), (3, 4), (3, 6), (5, 6), (2, 5)]
# edges = [(1, 2), (2, 3), (3, 4)]
# edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (6, 7), (6, 8), (6, 9), (7, 8), (7, 9), (8, 9)]
k = 2


def findSubgraph(n,edges,k):
    g = {}
    visit = set()
    for i in range(1,n+1):
        g[i] = []
    for u,v in edges:
        g[u].append(v)
        g[v].append(u)

    res = set()
    def dfs(node):
        print('now node:',node)
        if node in visit:
            return True
        visit.add(node)
        count = 0
        for nei in g[node]:
            if dfs(nei):
                count+=1
        print(f'{node=}, {count=}')
        if count>=k:
            res.add(node)
            return True
        else:
            return False

    dfs(1)
    print(res)


findSubgraph(9,edges,k)


