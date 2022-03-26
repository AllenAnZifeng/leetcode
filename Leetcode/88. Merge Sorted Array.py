#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 88. Merge Sorted Array.py
@time: 2020/10/30 10:57
'''

from typing import List


# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         ptr1 = m-1
#         ptr2 = n-1
#         ptr = len(nums1)-1
#         while ptr2>=0:
#             if ptr1>=0 and nums1[ptr1]>nums2[ptr2]:
#                 nums1[ptr] = nums1[ptr1]
#                 ptr1-=1
#             else:
#                 nums1[ptr] = nums2[ptr2]
#                 ptr2-=1
#             ptr-=1


