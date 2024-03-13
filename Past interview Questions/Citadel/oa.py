n = 7
edges = [[1,2],[2,3],[3,4],[3,5],[1,6],[1,7],[7,8]]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def buildTree(edges):
    if not edges:
        return None
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = TreeNode(u)
        if v not in graph:
            graph[v] = TreeNode(v)
        graph[u].children.append(graph[v])
    return graph[1]

tree = buildTree(edges)

longest = 0

def findLongestDiameter(root)->int:
    if not root:
        return 0
    res = [0]
    for i in range(len(root.children)):
        res.append(findLongestDiameter(root.children[i]))
    res.sort(reverse=True)

    global longest
    if len(res) > 1:
        longest = max(longest, res[0]+res[1])
    return res[0]+1

print(findLongestDiameter(tree))
print(longest)


n = 7
edges = [[1,2],[2,3],[3,4],[3,5],[1,6],[1,7]]

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def build_tree(n, edges):
    nodes = [Node(i) for i in range(1, n+1)]
    for edge in edges:
        parent = nodes[edge[0]-1]
        child = nodes[edge[1]-1]
        parent.children.append(child)
    return nodes[0]

root = build_tree(n, edges)

# return the diameter and the leaves on the diameter
def find_diameter(root) -> (int, [int]):
    # is leaf
    if not root.children:
        return 1, [root.val]

    # has children
    # find the diameter and leaves on the longest path
    diameters = [find_diameter(child) for child in root.children]

    if len(diameters) == 1:
        return diameters[0][0] + 1, diameters[0][1]

    diameters.sort(key=lambda x: x[0], reverse=True)

    leafs = []

    for diam, leaf in diameters:
        if diam >= diameters[1][0]:
            leafs.extend(leaf)

    return diameters[0][0] + diameters[1][0] + 1, leafs

print(find_diameter(root))



