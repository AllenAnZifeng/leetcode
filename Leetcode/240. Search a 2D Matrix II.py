#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 240. Search a 2D Matrix II.py
@time: 2020/11/19 14:50
'''

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix)==0 or len(matrix[0])==0:
#             return False
#         for r in range(len(matrix)):
#             if target >= matrix[r][0] and target<= matrix[r][-1] and target in matrix[r]:
#                 return True
#         return False


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r,c=0,len(matrix[0])-1

        while r<len(matrix) and c>=0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c-=1
            elif target >matrix[r][c]:
                r+=1
        return False


