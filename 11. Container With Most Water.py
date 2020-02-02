#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 11. Container With Most Water.py
@time: 2020/1/23 9:54
'''
from typing import List


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         ans=0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 ans=max(ans,(j-i)*min(height[j],height[i]))
#         return ans


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        water=0
        while left < right:
            water=max(water,(right-left)*min(height[left],height[right]))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return water


sol=Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))

