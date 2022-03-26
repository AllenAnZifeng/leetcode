#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 136. Single Number.py
@time: 2020/11/19 14:14
'''

from typing import List


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         if len(nums)==1:
#             return nums[0]
#         else:
#             index = 0
#             while index<len(nums):
#                 if index!=len(nums)-1 and nums[index]==nums[index+1]:
#                     index+=2
#                 else:
#                     return nums[index]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d.pop(nums[i],None)
        print(d)
        return list(d.keys())[0]

print(Solution().singleNumber([2,2,1]))