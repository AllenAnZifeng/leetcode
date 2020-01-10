#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course:
@contact: anz8@mcmaster.ca
@file: knapsack.py
@time: 2020/1/4 22:44
'''

w=[1,2,5,6,7]
val=[1,6,18,22,28]
capacity=11
res=[]
#
#
# def knapsack(cap:int,w_arr:list,val_arr:list,cur_val:int):
#     if cap<=0 or len(val_arr)==0:
#         print('cur cal',cur_val)
#         res.append(cur_val)
#         return
#     else:
#         print(w_arr)
#         if cap >= w_arr[0]: # take
#             knapsack(cap-w_arr[0],w_arr[1:],val_arr[1:],cur_val+val_arr[0])
#         # not take even if there is enough capacity
#         knapsack(cap, w_arr[1:], val_arr[1:], cur_val)
#
# knapsack(capacity,w,val,0)
# print(res)
# print(max(res))


# def knapsack(cap:int,w_arr:list,val_arr:list,cur_val:int):
#     if cap<=0 or len(val_arr)==0:
#         # print('cur cal',cur_val)
#         # res.append(cur_val)
#         return cur_val
#     else:
#         # print(w_arr)
#         if cap < w_arr[0]: # cannot take
#             return knapsack(cap, w_arr[1:], val_arr[1:], cur_val)
#         else:
#             return max(knapsack(cap, w_arr[1:], val_arr[1:], cur_val),knapsack(cap-w_arr[0],w_arr[1:],val_arr[1:],cur_val+val_arr[0]))
#
# ans=knapsack(capacity,w,val,0)
# print(ans)

def knapsack_dp(weight_arr,val_arr,cap):
    ref_table=[[0 for i in range(cap+1)] for j in range(len(weight_arr)+1)]
    for i in range(len(weight_arr)+1):
        for j in range(cap+1):
            if i==0 or j==0:
                ref_table[i][j]=0
            else:
                if j<weight_arr[i-1]: # cannot affort current item weight --> do not take
                    ref_table[i][j]=ref_table[i-1][j]
                else:
                    ref_table[i][j]=max(ref_table[i-1][j],val_arr[i-1]+ref_table[i-1][j-weight_arr[i-1]])
    for i in ref_table:
        print(i)
    print(ref_table)
    print(ref_table[-1][-1])

knapsack_dp(w,val,capacity)

