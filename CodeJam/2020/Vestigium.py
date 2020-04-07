#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Vestigium.py
@time: 2020/4/3 22:21
'''



def trace(m): #matrix 2d array
    t=0
    for i in range(len(m)):
       t+=m[i][i]
    return t #int

def checkrow(m):

    repeat =0
    for row in m:
        if len(set(row))!=len(row):
            repeat+=1
    return repeat

def checkcol(m):
    repeat =0
    m = list(zip(*m))
    for col in m:
        if len(set(col))!=len(col):
            repeat+=1

    return repeat

if __name__ == '__main__':
    number_of_matrix =int(input())
    matrixDict = {}
    for id in range(1,number_of_matrix+1):
        size = int(input())
        temp = []
        for j in range(size):
            row=input()
            row=list(map(int,row.split()))
            temp.append(row)
        matrixDict[id]=temp
    for k,v in matrixDict.items():
        print("Case #%d: %d %d %d"%(k,trace(v),checkrow(v),checkcol(v)))
