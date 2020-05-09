#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: staircase.py
@time: 2020/1/5 13:24
'''

def staircase(n): # number of ways to go up, only 1,2,3 steps at a time
    if n<0:
        return 0
    if n ==1 or 0:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return staircase(n-1)+staircase(n-2)+staircase(n-3)
print(staircase(20))

def staircase_dp(n):
    arr=[0,1,2,4]
    for i in range(n-3):
        arr.append(arr[-1]+arr[-2]+arr[-3])
    print(arr)
    return arr[-1]

print(staircase_dp(20))

