#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'classifyEdges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
from collections import deque
from typing import List


#
# def classifyEdges(g_nodes, g_from, g_to, g_weight):
#     # Write your code here
#     target = g_nodes
#     g = {i: [] for i in range(1, g_nodes + 1)}  # src: [dest, weight]
#
#     for src, dest, weight in zip(g_from, g_to, g_weight):
#         g[src].append([dest, weight])
#         g[dest].append([src, weight])
#
#     print(g)
#
#     visited = set()
#     visited.add(1)
#
#     distance = {i: float('inf') for i in range(1, g_nodes + 1)}  # distance to node 1
#     distance[1] = 0
#     q = deque([1])
#
#     while q:
#         for i in range(len(q)):
#             node = q.popleft()
#             for dest, weight in g[node]:
#                 if dest in visited:
#                     continue
#                 if distance[dest] > distance[node] + weight:
#                     distance[dest] = distance[node] + weight
#                     visited.add(dest)
#                     q.append(dest)
#
#     shortest = distance[target]
#
#     edges = set()
#
#     def dfs(node, prev, cur, s):
#         if node == target:
#             for e in cur:
#                 edges.add(e)
#
#         for dest, weight in g[node]:
#             if dest == prev:
#                 continue
#             if s + weight > shortest:
#                 continue
#             dfs(dest, node, cur + [(node, dest)], s + weight)
#
#     dfs(1, -1, [], 0)
#
#     print(edges)
#     res = ['NO' for i in range(g_edges)]
#     for i in range(g_edges):
#         start, end = g_from[i], g_to[i]
#         # print((start,end),(end,start))
#         if (start, end) in edges or (end, start) in edges:
#             res[i] = 'YES'
#
#     return res
#
# g_edges = 5
# print(classifyEdges(4, [1,2,1,3,1], [2,4,3,4,4], [1,1,1,2,2]))
import heapq
#
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         start = k
#         g = {i: [] for i in range(1, n + 1)}  # node: [nei,distance]
#         for src, nei, weight in times:
#             g[src].append([nei, weight])
#
#         distance = {i: float('inf') for i in range(1, n + 1)}
#         distance[k] = 0
#
#         visited = set()
#
#         min_heap = [[0,start]] # distance, node
#
#         res = 0
#
#         while min_heap:
#             print(f'heap: {min_heap}')
#             dist, node = heapq.heappop(min_heap)
#
#             if node in visited:
#                 continue
#             visited.add(node)
#             res = max(res,dist)
#
#             print(node, distance)
#             for nei, weight in g[node]:
#
#                 heapq.heappush(min_heap, [weight+dist,nei])
#
#
#
#         return res if len(visited)==n else -1
#
# print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1))

# class Snake:
#
#     def __init__(self):
#         self.ROW = 5
#         self.COL = 10
#         self.snake = deque([(0, 0)])
#         self.body = {(0, 0)}
#         self.pellets = set()
#
#     @staticmethod
#     def getDirection( direction):
#         if direction == "U":
#             return (-1, 0)
#         if direction == "D":
#             return (1, 0)
#         if direction == "L":
#             return (0, -1)
#         if direction == "R":
#             return (0, 1)
#
#     def move(self, direction):
#         dx,dy = self.getDirection(direction)
#         new_head = (self.snake[0][0]+dx, self.snake[0][1]+dy)
#         if new_head[0] < 0 or new_head[0] >= self.ROW or new_head[1] < 0 or new_head[1] >= self.COL:
#             print('dead')
#             return
#         if new_head in self.body:
#             print('dead')
#             return
#         if new_head in self.pellets:
#             self.pellets.remove(new_head)
#             self.snake.appendleft(new_head)
#             self.body.add(new_head)
#         else:
#             self.snake.appendleft(new_head)
#             self.body.add(new_head)
#             empty_body = self.snake.pop()
#             self.body.remove(empty_body)
#     def addFood(self, location):
#         self.pellets.add(location)
#
#     def __str__(self):
#         res = [['.' for i in range(self.COL)] for j in range(self.ROW)]
#         for body in self.snake:
#             res[body[0]][body[1]] = 's'
#         for pellet in self.pellets:
#             res[pellet[0]][pellet[1]] = 'p'
#         return '\n'.join([''.join(row) for row in res]) +'\n'
#
# s = Snake()
# s.addFood((1,1))
# s.addFood((2,2))
# s.addFood((3,3))
#
# moves = ['R','D','D','R','L','U','R','D','D','D','D']
# for move in moves:
#     s.move(move)
#     print(s)
#     print('---')


