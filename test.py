#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: test.py
@time: 2020/1/4 23:02
'''

# print(['a']+['b'])
from typing import List

a=[1,2,3]
b=[3,4,5]
c= [6,7,8]
d=[a,b,c]
print(list(zip(*d)))

l=[1,2,3,4,5,6,7]
print(l[:2]+l[3:])


