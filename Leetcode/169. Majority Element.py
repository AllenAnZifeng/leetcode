#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 169. Majority Element.py
@time: 2020/11/19 14:42
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1

        for k,v in d.items():
            if v > len(nums)//2:
                return k
