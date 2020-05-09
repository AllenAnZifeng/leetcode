#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: binary_search.py
@time: 10/24/2018 4:33 PM
'''

# a=[1,3,4,5,6,8,9,10,14] #missing 2,7,11,12,13

a=[1,2,3,4,5,6]
def binary_search(l:list,target:int):
    low=0
    high=len(l)-1
    while low<=high:
        mid = int((low + high) / 2)
        if l[mid]==target:
            return mid
        elif l[mid]<target:
            low=mid+1
        elif l[mid]>target:
            high=mid-1
    return -1

v=binary_search(a,6)
print(v)
# for i in range(len(a)):
#     print(a[i],i)