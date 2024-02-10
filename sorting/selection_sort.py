#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: perm2.py
@time: 2020/1/8 16:45
'''

a=[8,5,4,6,1,2,2,3,100,48,12]

def selection_sort(arr:list):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

print(selection_sort(a))


