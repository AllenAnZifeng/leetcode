#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course:
@contact: anz8@mcmaster.ca
@file: knapsack.py
@time: 2020/1/4 22:44
'''

w=[2,4,5,7,9]
val=[3,5,6,8,10]
capacity=19
res=[]

def knapsack(cap:int,w_arr:list,val_arr:list,cur_val:int):
    if cap<=0 or len(val_arr)==0:
        print('cur cal',cur_val)
        res.append(cur_val)
        return
    else:
        print(w_arr)
        if cap >= w_arr[0]: # take
            knapsack(cap-w_arr[0],w_arr[1:],val_arr[1:],cur_val+val_arr[0])
        # not take even if there is enough capacity
        knapsack(cap, w_arr[1:], val_arr[1:], cur_val)

knapsack(capacity,w,val,0)
print(res)
print(max(res))