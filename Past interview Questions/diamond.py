#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: diamond.py
@time: 9/24/2018 12:07 PM
'''

import math

def diamond(num:int):
    for i in range(1,2*num):
        print(" "*int(math.fabs(num-i))+"*"*((num-int(math.fabs(num-i)))*2-1))

diamond(3)



