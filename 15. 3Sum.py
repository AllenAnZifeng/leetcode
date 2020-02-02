#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 15. 3Sum.py
@time: 2020/1/26 23:19
'''
from typing import List

#
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans=[]
#         nums.sort()
#         for i in range(len(nums)):
#             if i !=0 and nums[i]==nums[i-1]:
#                 continue
#             d={}
#             target= - nums[i]
#             for j in range(i+1,len(nums)):
#                 if target-nums[j] in d:
#                     temp = [nums[i],target-nums[j],nums[j]]
#                     temp.sort()
#                     if temp not in ans:
#                         ans.append(temp)
#                     d[nums[j]] = j
#                 else:
#                     d[nums[j]]=j
#         return ans
#
# sol=Solution()
# print(sol.threeSum([-1,0,1,2,-1,-4]))
# [[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        # print(nums)
        for i in range(0,len(nums)-2): #no need to try the last two, no room
            if nums[i]>0:
                break
            if i >0 and nums[i]==nums[i-1]: continue
            left,right = i+1,len(nums)-1
            while True:
                target = -nums[i]

                if left>=right:
                    break
                if nums[left]+nums[right]==target:
                    ans.append([nums[i],nums[left],nums[right]])

                    left+=1
                    while left <len(nums) and nums[left]==nums[left-1]:
                        left+=1

                    right-=1
                    while right>= 0 and nums[right]==nums[right+1]:
                        right-=1

                elif nums[left]+nums[right]>target:
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
        # return [list(t) for t in set(ans)]
        return ans
sol=Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
# print(sol.threeSum([-2,0,1,1,1,1,1,2]))
# print(sol.threeSum([0,0,0,0,0]))


# from itertools import combinations
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         return [list(s) for s in set([t for t in combinations(nums,3) if sum(t)==0])]


# from itertools import combinations
#
# arr= [-1,0,1,2,-1,-4]
# arr.sort()
# print(set((list(combinations(arr,4)))))



# arr=['a','b','c','d','e']
#
# def permutation(arr):
#     if len(arr)<=1:
#         return arr[0]
#     ans=[]
#     for i in range(len(arr)):
#          ans.extend([arr[i] +c for c in permutation(arr[:i]+arr[i+1:])])
#     ans.sort()
#     return ans
# # print(permutation(arr))
#
# def combination(arr,num):
#     if num<=1:
#         return arr
#     ans=[]
#     for i in range(len(arr)):
#         ans.extend([ arr[i]+c for c in combination(arr[i+1:],num-1)])
#     return ans
# print(combination(arr,2))
#



