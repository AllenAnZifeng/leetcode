
n = 7
edges = [[1,2],[2,3],[3,4],[3,5],[4,9],[9,10],[5,11],[11,12]]

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
longest_path_leaves = []

def findLongestPathToLeaf(root)->(int, [int]):
    # is leaf
    if not root.children:
        return 0, [root.val]

    res = []

    for child in root.children:
        res.append(findLongestPathToLeaf(child))
    res.sort(reverse=True)

    leaves = []
    for length, leaf in res:
        if length == res[0][0]:
            leaves.extend(leaf)

    global longest, longest_path_leaves
    if len(res) > 1:
        leaves_all = []
        for length, leaf in res:
            if length >= min(res[0][0], res[1][0]):
                leaves_all.extend(leaf)

        current_longest = res[0][0] + 2 + res[1][0]
        if current_longest > longest:
            longest = current_longest
            longest_path_leaves = leaves_all
        elif current_longest == longest:
            longest_path_leaves.extend(leaves_all)
    else:
        if res[0][0] + 1 > longest:
            longest = res[0][0] + 1
            longest_path_leaves = leaves + [root.val]
        elif res[0][0] + 1 == longest:
            longest_path_leaves.extend(leaves + [root.val])

    return res[0][0] + 1, leaves

print(findLongestPathToLeaf(tree))
print(longest, longest_path_leaves)