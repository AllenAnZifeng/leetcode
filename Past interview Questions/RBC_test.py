#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: RBC_test.py
@time: 2020/1/19 15:35
'''
from math import fabs
def kDifference(arr, k):
    # Write your code here

    count=0
    arr=set(arr)
    for i in arr:
        if i+k in arr:
            count+=1

    # print(count)
    return count

kDifference([1,3,5],2)
