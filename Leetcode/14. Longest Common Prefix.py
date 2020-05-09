#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 14. Longest Common Prefix.py
@time: 2020/1/23 12:55
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        strs.sort(key=len)
        print(strs)
        count=0
        if len(strs)==0:
            print('here')
            return ''
        while count<len(strs[0]):
            for i in range(len(strs)-1):
                if strs[i][count]!=strs[i+1][count]:
                    print(ans)
                    return ''.join(ans)

            ans.append(strs[0][count])
            count += 1
        return ''.join(ans)


sol=Solution()
# print(sol.longestCommonPrefix(['']))
print(sol.longestCommonPrefix(["flower","flow","flight"]))






