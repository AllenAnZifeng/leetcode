#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 210. Course Schedule II.py
@time: 2020/1/14 12:46
'''
from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS
        d,r={},{} # r --> course: all prerequisites   d --> graph representation
        for i,j in prerequisites:
            if j not in d:
                d[j]=[i]
            else:
                d[j].append(i)
            if i not in r:
                r[i]=[j]
            else:
                r[i].append(j)
        # print('d',d)
        print('r',r)

        queue = [i for i in range(numCourses) if i not in r]
        # queue initializes with courses without any prerequisite
        # print(queue)

        res=[]
        while len(queue)!=0:
            node=queue.pop(0)
            res.append(node)
            for i in r:
                if node in r[i]:
                    r[i].remove(node)
                    if len(r[i])==0:
                        queue.append(i)
            empty_key = [k for k in r if len(r[k])==0]
            for k in empty_key:
                r.pop(k)
        if len(r)!=0:
            return []
        else:
            return res

a=Solution()
ans=a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(ans)

#topological ordering
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         d={}
#         for i,j in prerequisites:
#             if j not in d:
#                 d[j]=[i]
#             else:
#                 d[j].append(i)
#         print(d)
#         visited = [False]*numCourses
#         stack = []
#         path=[]
#         flag=False
#         def dfs(node: int):
#             visited[node]=True
#             path.append(node)
#             if node not in d: # not a prerequisite for any other course
#                 stack.append(node)
#                 path.remove(node)
#                 return
#             for n in d[node]:
#                 if n in path:
#                     nonlocal flag
#                     flag=True
#                     return
#                 if visited[n]==False:
#                     dfs(n)
#             stack.append(node)
#             path.remove(node)
#
#         for i in range(numCourses):
#             if visited[i]==False:
#                 dfs(i)
#         print('stack',stack)
#         print('visited',visited)
#         print(flag)
#         return stack[::-1] if flag==False else []
#
# a=Solution()
# # ans=a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
# ans=a.findOrder(2,[[0,1],[1,0]])
# print(ans)