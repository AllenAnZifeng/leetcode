#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 39. Combination Sum.py
@time: 2020/2/10 15:26
'''
from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[] #type: List[List]
        candidates.sort()
        def dfs(candidates,target,temp:list,idx):
            if target ==0:
                self.ans.append(temp[:])

            for i in range(idx,len(candidates)):
                x=candidates[i]
                if target-x<0:
                    return
                else:
                    #target-x>0:
                    # t=temp[:]
                    # t.append(
                    dfs(candidates,target-x,temp+[x],i)

        dfs(candidates,target,[],0)
        # self.ans = set([tuple(l) for l in self.ans]) #remove duplicate
        # print(self.ans)
        # self.ans = [list(s) for s in self.ans]
        # print(self.ans)
        return self.ans
Solution().combinationSum([2,3,6,7],7)







