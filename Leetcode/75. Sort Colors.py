#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 75. Sort Colors.py
@time: 2020/10/30 16:37
'''
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        index = 0
        while counter <len(nums):
            if nums[index] ==0:
                nums.pop(index)
                nums.insert(0,0)
                index+=1
            elif nums[index] ==2:
                nums.pop(index)
                nums.insert(len(nums)-1, 2)
            elif nums[index] ==1:
                index+=1

            counter+=1


