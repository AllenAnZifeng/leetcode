#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: print_heap.py
@time: 2020/1/9 22:07
'''
import math

a=[8,5,4,6,1,2,3,100,48,12]
def print_heap(arr:list):
    # counter=1
    # while len(arr)!=0:
    #     print(arr[:counter])
    #     arr=arr[counter:]
    #     counter*=2

    for level in range(int(math.log(len(arr),2))+1):
        for _ in range(2**level):
            if len(arr)!=0:
                print(arr.pop(0),end=' ')
            else:
                break
        print()


print_heap(a)