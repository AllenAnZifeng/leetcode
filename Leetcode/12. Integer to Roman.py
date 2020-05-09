#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 12. Integer to Roman.py
@time: 2020/2/2 13:49
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        d={1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
        s=''
        arr=[]
        for n in d.keys():
            arr.append([num//n,n])
            num=num%n
        # print(arr)
        for i in range(len(arr)):
            if arr[i][0]==4:
                arr[i-1][0]+=1
                if arr[i-1][1]!=1000:
                    arr[i-1]=[1,arr[i-1][0]*arr[i-1][1]]

                arr[i][0]=1
                arr[i],arr[i-1]=arr[i-1],arr[i]
        # print(arr)
        for i in range(len(arr)):
            s+=arr[i][0]*d[arr[i][1]]
        return s
print(Solution().intToRoman(58))

