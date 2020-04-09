#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Allocation.py
@time: 2020/4/7 17:42
'''

cases = int(input())
for i in range(cases):
    _, budget = [int(s) for s in input().split()]
    priceList = [int(s) for s in input().split()]
    priceList.sort()
    count = 0
    for p in priceList:
        if budget - p >= 0:
            count += 1
            budget = budget - p
        else:
            break
    print("Case #%d: %d"%(i+1,count))