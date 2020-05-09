#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 7. Reverse Integer.py
@time: 2020/1/23 1:37
'''
from functools import reduce

#
# class Solution:
#     def reverse(self, x: int) -> int:
#         if x==0 or x > 2**31-1 or x< -2**31:
#             return 0
#         sign=1
#         if x<0:
#             sign=-1
#         x=abs(x)
#         digits=[]
#         while x>0:
#             digits.append(x%10)
#             x=x//10
#         res=sign*reduce(lambda x,y:x*10+y,digits)
#         return res if res <= 2**31-1 and res >= -2**31 else 0

class Solution(object):
    def reverse(self, x):
        s = (x > 0) - (x < 0) # determine sign, True - False = 1
        r = int(str(x*s)[::-1]) # x*s --> abs
        return s*r * (r < 2**31)

s=Solution()
print(s.reverse(12345))