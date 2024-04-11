#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countMinimumUnreachableWarehouses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts UNWEIGHTED_INTEGER_GRAPH warehouse as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

def countMinimumUnreachableWarehouses(warehouse_nodes, warehouse_from, warehouse_to):
    # Write your code here
    res = 0

    g = {}
    for i in range(1, warehouse_nodes + 1):
        g[i] = set()

    cycle_nodes = set()

    for src, dst in zip(warehouse_from, warehouse_to):
        if dst in g[src]:
            cycle_nodes.add(dst)
            cycle_nodes.add(src)
        g[src].add(dst)
        g[dst].add(src)

    visit = set()

    def dfs(node, prev) -> bool:  # has cycle
        print('dfs', node, prev, 'visit', visit)
        cycleFlag = False
        if node in visit:
            return True

        visit.add(node)
        if node in cycle_nodes:
            cycleFlag = True

        for nei in g[node]:
            if nei != prev and dfs(nei, node):
                cycleFlag = True

        return cycleFlag

    def dfs2(node):
        print('dfs2', node)
        cycleFlag = False

        nodes_to_visit = [[node, -1]]  # stack
        while nodes_to_visit:
            cur, prev = nodes_to_visit.pop()

            if cur in visit:
                cycleFlag = True
                continue
            visit.add(cur)
            if cur in cycle_nodes:
                cycleFlag = True
            for nei in g[cur]:
                if nei != prev:
                    # visit.add(nei)
                    nodes_to_visit.append([nei, cur])

        return cycleFlag

    for i in range(1, warehouse_nodes + 1):
        if i in cycle_nodes:
            continue
        if i in visit:
            continue
        if i not in visit and dfs2(i):
            pass
        else:
            print('i:', i)
            res += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    warehouse_nodes, warehouse_edges = map(int, input().rstrip().split())

    warehouse_from = [0] * warehouse_edges
    warehouse_to = [0] * warehouse_edges

    for i in range(warehouse_edges):
        warehouse_from[i], warehouse_to[i] = map(int, input().rstrip().split())

    result = countMinimumUnreachableWarehouses(warehouse_nodes, warehouse_from, warehouse_to)

    fptr.write(str(result) + '\n')

    fptr.close()
