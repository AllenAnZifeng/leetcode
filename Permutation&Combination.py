#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Permutation&Combination.py
@time: 2020/4/5 0:07
'''


l=[1,2,3,4,5]
a=[2,3]

def combination(n, l) -> list:
    if n == 1:
        return [[x] for x in l]
    combo = []
    for i in range(len(l)):
        combo.extend([[l[i]]+item for item in combination(n-1,l[i+1:])])
    return combo


def permutation(n,l)-> list:
    if n == 1:
        return [[x] for x in l]
    combo = []
    for i in range(len(l)):
        combo.extend([[l[i]]+item for item in permutation(n-1,l[:i]+l[i+1:])])
    return combo


print(combination(2, [1]))
# print(len(combination(3, l)))
# print(permutation(2,l))
# print(len(permutation(2,l)))