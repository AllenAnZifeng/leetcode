#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: plates.py
@time: 2020/4/7 17:52
'''

# brute force
# def take(n,items): # remaining items to take
#
#     if n==1:
#         return max(list(zip(*items))[0])
#     scores = []
#     for i in range(len(items)):
#         copy= [r[:] for r in items]
#         plate_to_take = copy[i].pop(0)
#         if copy[i] ==[]:
#             copy.pop(i)
#         scores.append(plate_to_take+take(n-1,copy))
#     return max(scores)
#

def p(matrix):
    for row in matrix:
        for c in row:
            print(str(c).center(5),end='')
        print()

def dptake(n,items):
    partialSum = [] # partialSum[i][x] --> the sum of x plates from i th stack
    for i in range(len(items)):
        stack = [0]
        for j in range(len(items[0])):
            stack.append(sum(items[i][:j+1]))
        partialSum.append(stack)
    # p(partialSum)

    dp = [[0 for j in range(n+1)] for i in range(len(items))]
    for i in range(n+1):
        if i <len(items[0]):
            dp[0][i] = partialSum[0][i]
        else:
            dp[0][i]=partialSum[0][-1]

    for i in range(1,len(items)):
        for j in range(1,n+1):
            for x in range(min(j+1,len(items[0])+1)):
                dp[i][j] = max(dp[i][j],partialSum[i][x]+dp[i-1][j-x])


                # p(dp)
    return dp[-1][-1]


def dp_save_space(n,items):
    partialSum = []  # partialSum[i][x] --> the sum of x plates from i th stack
    for i in range(len(items)):
        stack = [0]
        for j in range(len(items[0])):
            stack.append(sum(items[i][:j + 1]))
        partialSum.append(stack)
    # p(partialSum)

    dp = [0 for j in range(n + 1)]
    for i in range(n + 1):
        if i < len(items[0]):
            dp[i] = partialSum[0][i]
        else:
            dp[i] = partialSum[0][-1]

    for i in range(1, len(items)):
        ndp = [0 for j in range(n + 1)]
        for j in range(1, n + 1):
            for x in range(min(j + 1, len(items[0]) + 1)):
                ndp[j] = max(ndp[j], partialSum[i][x] + dp[j - x])
        dp=ndp
        # p(dp)
    return dp[-1]

s1='''2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10

'''

s='''1
2 1 2
10 
80 

'''



if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        numStacks, _, total = [int(s) for s in input().split()]
        beautyLists=[]
        for j in range(numStacks):
            beautyLists.append([int(s) for s in input().split()])
        # print(beautyLists)
        print('Case #%d: %d'%(i+1,dp_save_space(total,beautyLists)))

