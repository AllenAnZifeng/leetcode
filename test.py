#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: test.py
@time: 2020/1/4 23:02
'''
arr=[1,2,3,4]
def f(a):
    a.pop(0)

f(arr.copy())
print(arr)