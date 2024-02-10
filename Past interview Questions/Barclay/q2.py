"""
connections, represents connection between the satellites.
maxSatellites, represents the maximum number of satellites that can be connected to one satellite.
"""
from collections import defaultdict, deque
from typing import List

#
# def traverse(tree):
#     tree[0].visit()
#     queue = deque([tree[0]])
#     iterations = 0
#
#     while queue:
#         iterations += 1
#         # In one iteration, all nodes currently in the queue will visit one of its neighbors
#         for i in range(len(queue)):
#             current_node = queue[i]
#
#             if current_node.getChildrenLength() > 0:
#                 current_node.sortChildren()
#                 elem = current_node.children.pop(0)
#                 elem.visit()
#                 queue.append(elem)
#
#             if current_node.getChildrenLength() == 0:
#                 queue.popleft()
#     return iterations

# def traverse(graph, start_node):
#     for i in range(len(graph[start_node])):

class Node:

    def __init__(self,value):
        self.value = value
        self.children = []
        self.visited = False

    def visit(self):
        self.visited = True

    def addChild(self, child):
        self.children.append(child)

    def getChildrenLength(self):
        return len(self.children)

    def __str__(self):
        return str(f'Node:{self.value}')

    def __repr__(self):
        return self.__str__()
def maxIterations(connections:List[List], maxSatellites):

    d = {}

    for i in range(len(connections)):
        if connections[i][0] not in d:
            d[connections[i][0]] = [connections[i][1]]
        else:
            d[connections[i][0]].append(connections[i][1])
    max_node_value = 0

    for k,v in d.items():
        max_node_value = max(k,max(v))

    nodes = [ Node(i) for i in range(max_node_value + 1)]


    for k,v in d.items():
        for child in v:
            nodes[k].addChild(nodes[child])

    tree = nodes[0]













def main():
    # input for connections
    connections = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7]]

    result = maxIterations(connections, maxSatellites=3)
    print(result)


if __name__ == "__main__":
    main()