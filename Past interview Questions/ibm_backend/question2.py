#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: question2.py
@time: 2021/1/13 21:25
'''

def perfectTeam(skills):
    # Write your code here
    d = {}
    for c in skills:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    values = []
    for k,v in d.items():
        values.append(v)
    if len(values)<5:
        return 0
    else:
        return (min(values))

a= [0,3,10,1,3,5,2,9,6,8]
def meanderingArray(unsorted:list):
    unsorted.sort()
    res =[]
    max_flag = True
    while unsorted:
        if max_flag:
            res.append(unsorted.pop(-1))
        else:
            res.append(unsorted.pop(0))
        max_flag = not max_flag
    return res
# print(sorted(a))
# print(meanderingArray(a))




sample = [[1,1,1,1,1],
          [1,1,0,1,1],
          [1,1,1,1,1]]
def largestArea(samples):
    # Write your code here
    matrix = [row[:] for row in samples]
    res = 0
    for r in range(1,len(samples)):
        for c in range(1,len(samples[0])):
            if matrix[r][c]>0:
                matrix[r][c] = matrix[r][c]+min(matrix[r-1][c],matrix[r][c-1],matrix[r-1][c-1])
            if matrix[r][c] > res:
                res = matrix[r][c]
    print(matrix)
    return res
print(largestArea(sample))