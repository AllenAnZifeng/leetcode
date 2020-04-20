#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: workout.py
@time: 2020/4/7 18:54
'''


def peak(m):
    count =0
    for i in range(1,len(m)-1):
        if m[i]>m[i-1] and m[i]>m[i+1]:
            count+=1
    return count


if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        numMountain= int(input())
        mountains=[]
        mountains.extend([int(s) for s in input().split()])
        # print(mountains)
        print('Case #%d: %d'%(i+1,peak(mountains)))