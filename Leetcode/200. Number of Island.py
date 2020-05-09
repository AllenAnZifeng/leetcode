#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 200. Number of Island.py
@time: 2020/1/10 0:19
'''
from typing import List

sample = [["1","1","1"],
          ["0","1","0"],
          ["1","1","1"]]
class Solution:
    def expand(self,visit_map,grid_map,i,j):
        if i +1 < len(grid_map) and grid_map[i+1][j]=='1' and visit_map[i+1][j]==False:
            visit_map[i+1][j]=True
            self.expand(visit_map,grid_map,i+1,j)

        if i -1 >=0 and grid_map[i-1][j]=='1' and visit_map[i-1][j]==False:
            visit_map[i-1][j]=True
            self.expand(visit_map,grid_map,i-1,j)

        if j+1 <len(grid_map[0]) and grid_map[i][j+1]=='1'and visit_map[i][j+1]==False:
            visit_map[i][j+1]=True
            self.expand(visit_map,grid_map,i,j+1)

        if j-1 >=0 and grid_map[i][j-1]=='1'and visit_map[i][j-1]==False:
            visit_map[i][j-1]=True
            self.expand(visit_map,grid_map,i,j-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        #initialize visited 2D array
        visited=[[False for j in range(len(grid[0]))] for i in range(len(grid))]
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and visited[i][j]==False:
                    visited[i][j]=True
                    self.expand(visited,grid,i,j)
                    print(visited)
                    counter+=1
                else:
                    visited[i][j] = True
        return counter

ans=Solution()
print(ans.numIslands(sample))