#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 887. Super Egg Drop.py
@time: 2020/4/6 22:02
'''

#
# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         if k==1:
#             return n
#         if n==1: # 1 floor, 1 check
#             return 1
#         if n==0: # no floor, 0 check
#             return 0
#
#
#         number_of_drops=[]
#         for i in range(1,n+1):
#             number_of_drops.append(1+max(self.superEggDrop(k-1,i-1),self.superEggDrop(k,n-i)))
#         return min(number_of_drops)
#
# print(Solution().superEggDrop(1,2))
# print(Solution().superEggDrop(2,6))
# print(Solution().superEggDrop(3,14))

# #DP
# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         def p(matrix):
#             for row in matrix:
#                 # print(row)
#                 for c in row:
#                     print(("%d"%(int(c))).center(5),end='')
#                 print()
#
#         dropTable = [[-1 for x in range(N+1)] for y in range(K+1)]
#         for k in range(len(dropTable)):
#             mid = 1
#             for n in range(len(dropTable[0])):
#                 if n==0 or k==0:
#                     dropTable[k][n] = 0
#                 elif n==1 and dropTable[k][n]==-1:
#                     dropTable[k][n]=n
#                 elif k==1:
#                     dropTable[k][n]=n
#                 else:
#                     first,second =[],[]
#                     temp=[]
#                     for m in range(1,n+1):
#                         first.append(dropTable[k-1][m-1])
#                         second.append(dropTable[k][n-m]+1)
#                         temp.append(max(dropTable[k-1][m-1],dropTable[k][n-m])+1)
#                     # print('first',first)
#                     # print('second',second)
#                     # print('max',temp)
#                     dropTable[k][n]= min(temp)
#
#                     while mid<=n and dropTable[k-1][mid-1]<dropTable[k][n-mid]:
#                         mid+=1
#                     print('mid',mid)
#                     dropTable[k][n] = dropTable[k - 1][mid - 1] + 1
#
#
#
#
#                     # low,high = 1,n
#                     # while low < high:
#                     #     mid = (low+high)//2
#                     #     left,right = dropTable[k-1][mid-1],dropTable[k][n-mid]
#                     #     if left<right:
#                     #         low=mid+1
#                     #     else:
#                     #         high=mid
#                     # print(low,'mid')
#                     # print(dropTable[k-1][low-1],k-1,low-1,'***')
#                     # print(dropTable[k][n-low],k,n-low)
#                     # dropTable[k][n] = max(dropTable[k-1][low-1],dropTable[k][n-low])+1
#
#
#
#                     # dropTable[k][n] = min([1+max(dropTable[k-1][i-1],dropTable[k][n-i]) for i in range(1,n+1)])
#
#         p(dropTable)
#         return dropTable[-1][-1]
#
# print(Solution().superEggDrop(5,100))



class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        dp=[i for i in range(n+1)]

        for i in range(k-1):
            m = 1  # drop at level m
            ndp=[float('inf') for _ in range(n+1)]
            for j in range(n+1):
                if j==0 or j==1:
                    ndp[j]=j
                else:
                    while dp[m-1]<ndp[j-m]:
                        m+=1
                    ndp[j] = dp[m-1]+1
            dp=ndp

        return dp[-1]

 # min([1+max(dropTable[k-1][i-1],dropTable[k][n-i])

print(Solution().superEggDrop(2,7)) #4