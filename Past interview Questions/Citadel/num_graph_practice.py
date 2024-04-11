# citadel
# A: -1  distance 1
# B: x2  distance 2
# 4,6
import heapq
from collections import deque

def bfs(start,end):
    h = [(0,start)]  # dist to node, node
    distance = {} # node: weight from node to start
    distance[start] = 0
    # visit = {start}

    while h:
        dist, node = heapq.heappop(h)
        if node == end:
            return dist


        multiplied_node = node *2
        minus_node = node - 1

        if multiplied_node not in distance or dist+2 < distance[multiplied_node]:
            distance[multiplied_node] = dist+2
            heapq.heappush(h,(dist+2,multiplied_node))

        if minus_node not in distance or dist + 1 < distance[minus_node]:
            distance[minus_node] = dist + 1
            heapq.heappush(h,(dist+1,minus_node))
        print(h)

print(bfs(4,6))


