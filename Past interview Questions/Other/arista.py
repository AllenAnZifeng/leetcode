from typing import List
from collections import deque
# a = 4
#
# print(bin(a))
# print(bin(a>>1))

d = {0:[1,2],1:[3,4],2:[4],3:[],4:[]}

# 1,2 is the preque for 0
def bfs(arr:dict):
    q = deque()

    indegress = {node:len(prereqs) for node,prereqs in arr.items()}
    res = []
    g = {}
    for node in arr.keys():
        g[node] = []

    for node, prereqs in arr.items():
        for prereq in prereqs:
            g[prereq].append(node)

    for n,degree in indegress.items():
        if degree == 0:
            q.append(n)


    while q:
        for i in range(len(q)):
            item = q.popleft()
            res.append(item)

            for course in g[item]:
                indegress[course] -=1
                if indegress[course] == 0:
                    q.append(course)

   
    if len(res) != len(arr.keys()):
        return []

    return res
print(bfs(d))

#
# output  = []
# def dfs(node):
#
#     for n in d[node]:
#         if n not in output:
#             dfs(n)
#     output.append(node)
#
# print(dfs(0))
#
# print(output)




#
# def topo_dfs(arr):
#     res = []
#     cur = []
#     def dfs(node):
#         if node in cur:
#             return False
#         if node in res:
#             return True
#         cur.append(node)
#         for pre in arr[node]:
#             if dfs(pre) == False:
#                 return False
#         cur.remove(node)
#         res.append(node)
#
#     for n in arr.keys():
#         if dfs(n) == False:
#             return []
#     return res
# print(topo_dfs(d))

# def topo_sort(arr):
#
#     res = []
#     q = deque()
#     g = {}
#
#     for k in d.keys():
#         g[k] = []
#
#     for k,v in d.items():
#         for n in v:
#             g[n].append(k)
#
#
#     # print(g)
#
#     indegrees = {k:len(v) for k,v in arr.items()}
#
#
#     for k,v in indegrees.items():
#         if v ==0:
#             q.append(k)
#
#     while q:
#
#         item = q.popleft()
#         for n in g[item]:
#             indegrees[n] -=1
#             if indegrees[n] == 0:
#                 q.append(n)
#         res.append(item)
#
#     if len(res) != len(indegrees):
#         return []
#     else:
#         return res


# print(topo_sort(d))

#
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#
#         d = {}
#
#         def edit_distance(w1, w2) -> int:
#
#             if (w1, w2) in d:
#                 return d[(w1, w2)]
#
#             if w1 == w2:
#                 d[(w1, w2)] = 0
#                 return 0
#
#             if len(w2) == 0:
#                 d[(w1, w2)] = len(w1)
#                 return len(w1)
#
#             if len(w1) == 0:
#                 d[(w1, w2)] = len(w2)
#                 return len(w2)
#
#             if w1[0] == w2[0]:
#                 # match, delete, insert
#                 match = edit_distance(w1[1:], w2[1:])
#                 d[(w1, w2)] = match
#                 return match
#             else:
#                 # replace , delete, insert
#                 replace = edit_distance(w1[1:], w2[1:]) + 1
#                 delete = edit_distance(w1[1:], w2) + 1
#                 insert = edit_distance(w1, w2[1:]) + 1
#                 ans = min(replace, delete, insert)
#                 d[(w1, w2)] = ans
#                 return ans
#
#         return edit_distance(word1, word2)
#
#
# print(Solution().minDistance('intention','execution'))


#
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#
#         d = {}
#
#         def edit_distance(w1, w2) -> int:
#
#             if (w1, w2) in d:
#                 return d[(w1, w2)]
#
#             if w1 == w2:
#                 d[(w1, w2)] = 0
#                 return 0
#
#             if len(w2) == 0:
#                 d[(w1, w2)] = len(w1)
#                 return len(w1)
#
#             if len(w1) == 0:
#                 d[(w1, w2)] = len(w2)
#                 return len(w2)
#
#             if w1[0] == w2[0]:
#                 # match, delete, insert
#                 match = edit_distance(w1[1:], w2[1:])
#                 d[(w1, w2)] = match
#                 return match
#             else:
#                 # replace , delete, insert
#                 replace = edit_distance(w1[1:], w2[1:]) + 1
#                 delete = edit_distance(w1[1:], w2) + 1
#                 insert = edit_distance(w1, w2[1:]) + 1
#                 ans = min(replace, delete, insert)
#                 d[(w1, w2)] = ans
#                 return ans
#
#         return edit_distance(word1, word2)
#
#
# print(Solution().minDistance('intention','execution'))

