#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 20. Valid Parentheses.py
@time: 2020/2/5 12:15
'''

#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack=[]
#         for bracket in s:
#             print(stack)
#             if bracket in ['(','[','{']:
#                 stack.append(bracket)
#             else:
#                 if bracket == ')':
#                     if len(stack)>0 and stack[-1]=='(':  stack.pop(-1)
#                     else: return False
#
#                 if bracket == ']':
#                     if len(stack)>0 and stack[-1]=='[':  stack.pop(-1)
#                     else: return False
#
#                 if bracket == '}':
#                     if len(stack)>0 and stack[-1]=='{':  stack.pop(-1)
#                     else: return False
#         if len(stack)==0:
#             return True
#

class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}
        stack=[]
        for bracket in s:
            if bracket in d.keys():
                stack.append(bracket)
            else:
                if len(stack)==0 or bracket!=d[stack.pop(-1)]:
                    return False
        return True if len(stack)==0 else False

sol=Solution().isValid('()')
print(sol)