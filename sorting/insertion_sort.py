#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: insertion_sort.py
@time: 2020/1/8 19:51
'''

a=[8,5,4,6,1,2,2,3,100,48,12]

def insertion_sort(arr:list):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]

            else:
                break
        print(arr)
    return arr
print(insertion_sort(a))



