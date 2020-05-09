#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 16. 3Sum Closest.py
@time: 2020/2/2 13:03
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance = float("inf")
        ans= 0
        for i in range(len(nums)):

            left,right=i+1,len(nums)-1

            while left<right:
                total = sum([nums[i], nums[left], nums[right]])
                if total ==target:
                    return total
                elif total < target:
                    if target-total<distance:
                        distance = target-total
                        ans = total
                    left+=1
                else:
                    if total-target<distance:
                        distance = total - target
                        ans = total
                    right-=1

        return ans

print(Solution().threeSumClosest([1,2,5,10,11],12))