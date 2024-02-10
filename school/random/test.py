#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: perm2.py
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

# import cmath
#
# s=0.3654j
# # Gp=0.039/(5*s+1)
# # Gv=1/(0.033*s+1)
# # Gs=1/(0.25*s+1)
#
# # total = Gp*Gv*Gs
# n=3
# Gloop = 1/(5*s+1)**n
# Ku=1/abs(Gloop)
# Kc=Ku/2
# print('Ku',Ku)
# print('Kc',Kc)


# def g(a):
#
#     for i in range(3):
#         yield i+a
#     return "hello"
#
# a= g(2)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print([x for x in g()])

from typing import List

def f(requests:List[int],stock_length:int,left_over:List[int])->int: # return
    if len(requests) ==0:
        print([stock_length-x for x in left_over])
        return 0

    left_over.sort()
    used_left_over_flag = False
    new_left_over = left_over[::]
    for i in range(len(new_left_over)):
        if new_left_over[i]>=requests[0]:
            new_left_over[i] -= requests[0]
            used_left_over_flag = True
            break
    new_piece_left_over=left_over[::]
    new_piece_left_over.append(stock_length-requests[0])
    if used_left_over_flag:
        return min(f(requests[1:],stock_length,new_left_over),f(requests[1:],stock_length,new_piece_left_over)+1)
    else:
        return f(requests[1:],stock_length,new_piece_left_over)+1

# print(f([4,3,4,1,7,8],10,[]))
# print(f([6,3,2,2,6,3,2,2,6,3,2,2],10,[]))
