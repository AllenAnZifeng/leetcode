#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: merge_sort.py
@time: 10/24/2018 4:22 PM
'''

a=[8,5,4,6,1,2,2,3,100,48,12]

def merge_sorted_lists(l1:list,l2:list)->list:
    l=[]
    while True:
        if l1[0]>=l2[0]:
            l.append(l2.pop(0))
        else:
            l.append(l1.pop(0))
        if len(l1)==0:
            return l+l2
        elif len(l2)==0:
            return l+l1


def merge_sort(l:list)->list:
    if len(l)<=1:
        return l
    else:
        return merge_sorted_lists(merge_sort(l[:len(l)//2]),merge_sort(l[len(l)//2:]))


b=merge_sort(a)
print(b)

