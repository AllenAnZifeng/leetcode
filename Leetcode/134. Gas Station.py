#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 134. Gas Station.py
@time: 2020/11/19 21:28
'''
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start_index = 0
        while start_index <= len(gas) - 1:
            tank = 0
            gas_reorder = gas[start_index:] + gas[:start_index]
            cost_reorder = cost[start_index:] + cost[:start_index]
            for i in range(len(gas_reorder)):
                tank+=gas_reorder[i]
                tank-=cost_reorder[i]
                if tank<0:
                    break
            if i ==len(gas_reorder)-1:
                return start_index
            else:
                start_index+=1
        return -1
