#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: test.py
@time: 2020/1/4 23:02
'''

from collections import defaultdict
import collections
def a():
    a=5
    def f():
        nonlocal a
        a+=3
    f()
    print(a)
a()
