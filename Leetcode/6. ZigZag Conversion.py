#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 6. ZigZag Conversion.py
@time: 2020/1/22 20:45
'''
from functools import reduce


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         res= ['']*numRows
#         index, move = 0,1
#         if numRows==1:
#             return s
#         for s[i in s:
#             res[index]+=s[i
#             if index ==0:
#                 move= 1
#             elif index==numRows-1:
#                 move=-1
#             index+=move
#         ans=reduce(lambda x,y:x+y,res)
#         return ans

#
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         ans=['']*numRows
#         r,step=0,1 #row, step
#         if numRows==1 or len(s) <= numRows:
#             return s
#         for s[i in s:
#             ans[r]+=s[i
#             if r==0:
#                 step=1
#             elif r== numRows -1:
#                 step=-1
#             r+=step
#         print(ans)
#         return ''.join(ans)

# print zig zag

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=['']*numRows
        r,step=0,1 #row, step
        if numRows==1 or len(s) <= numRows:
            return s
        for i in range(len(s)):
            if step == -1:
                if r>=numRows -2: # last 2 rows
                    ans[r] += s[i] + ' '
                    ans[r] += ' '*(r-1)
                elif r<=1: #first 2 rows
                    ans[r] += ' ' * (numRows-2-r)
                    ans[r] += s[i] + ' '
                else:
                    ans[r] += ' ' * (numRows - 2 - r)
                    ans[r] += s[i] + ' '
                    ans[r] += ' ' * (r - 1)
            elif step == 1:
                ans[r]+=s[i] + ' '
            if r==0:
                step=1
                ans[r] += ' '
            elif r== numRows -1:
                step=-1
                ans[r] +=' ' * (r - 1) + ' '

            r+=step
        for row in ans:
            print(row)
        return ''.join(ans)


a=Solution()
a.convert('123456789abcdefghi',5)

#
# def convert(s: str, numRows: int):
#     rows = [[] for _ in range(numRows)]
#     s = list(s)
#     row = 0
#
#     rows[row].append(s.pop(0))
#
#     row = 1
#
#     downward = True
#     while len(s) > 0:
#         if not downward and row < numRows - 2:
#             spaces = [' ' for _ in range(numRows - 2 - row)]
#             rows[row].extend(spaces)
#         rows[row].append(s.pop(0))
#         if (not downward and row > 1) or (row == numRows - 1):
#             spaces = [' ' for _ in range(row - 1)]
#             rows[row].extend(spaces)
#         if downward:
#             if row == numRows - 1:
#                 downward = False
#                 row -= 1
#             else:
#                 row += 1
#         else:
#             if row == 0:
#                 downward = True
#                 row += 1
#             else:
#                 row -= 1
#     result = []
#     for row in rows:
#         print(*row)
#         result.extend(row)
#     return ''.join([c for c in result if c != ' '])
#
#
#
# if __name__ == '__main__':
#     print(convert('PAYPALISHIRING', 6))