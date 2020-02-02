#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: shell_sort.py
@time: 2020/1/8 16:57
'''
a=[8,5,4,6,1,2,2,3,100,48,12]

def shell_sort(arr:list):
    h=1
    while h< len(arr)/3:
        h=3*h+1

    while h>=1:
        for i in range(h,len(arr)):
            for j in range(i,h-1,-h):
                if arr[j]<arr[j-h]:
                    arr[j-h],arr[j]=arr[j],arr[j-h]
        print(arr)
        h=(h-1)//3

    return arr

print(shell_sort(a))


    