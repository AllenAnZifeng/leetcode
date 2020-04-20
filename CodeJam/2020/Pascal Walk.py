#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Pascal Walk.py
@time: 2020/4/10 22:44
'''


import math
# print(math.factorial(5))
#
#
#
# def generate_path(n):
#     path = [1,1]
#     row = int(math.log(n,2))
#     print(row)
#     if n>= 2**row + (n-1)*2-1:
#         print()
#
# generate_path(18)

# if __name__ == '__main__':
#     cases = int(input())
#     for i in range(cases):
#         n=int(input())
#         path(n)
#

def print_path(final_row):
    row = 1
    while row <= final_row:
        if row % 2 == 1:
            for col in range(1,row+1):
                print(row,col)
        else:
            for col in range(row,0, -1):
                print(row,col)
        row+=1

for i in range(int(input())):
    target = int(input())
    row = int(math.log2(target))
    print_path(row)
