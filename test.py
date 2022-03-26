#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: test.py
@time: 2020/1/4 23:02
'''


# add(1,2,3)(4,5)(6)(7)


# class add:
#     def __call__(self, *args):
#         return add(self.val, *args)
#
#     def __init__(self, *args):
#         self.val = sum(args)
#
#     def value(self):
#         return self.val
#
#     # def __str__(self):
#     #     return str(self.val)
#
#
# print(add(1, 2, 3)(4, 5))

import cmath

s=0.3654j
# Gp=0.039/(5*s+1)
# Gv=1/(0.033*s+1)
# Gs=1/(0.25*s+1)

# total = Gp*Gv*Gs
n=3
Gloop = 1/(5*s+1)**n
Ku=1/abs(Gloop)
Kc=Ku/2
print('Ku',Ku)
print('Kc',Kc)


