#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 17. Letter Combinations of a Phone Number.py
@time: 2020/2/2 21:18
'''
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={2:'abc',
           3:'def',
           4:'ghi',
           5:'jkl',
           6:'mno',
           7:'pqrs',
           8:'tuv',
           9:'wxyz'
           }

        def merge(body,digits):

            if len(digits)==0:
                ans.append(body)
                return
            else:
                for c in d[int(digits[0])]:
                    merge(body+c,digits[1:])

        # arr=[]
        ans=[]
        # for digit in digits:
        #     arr.append(list(d[int(digit)]))
        # print(arr)
        merge('',digits)
        return ans if len(ans)!=1 else []

print(Solution().letterCombinations(''))

#
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         d={2:'abc',
#            3:'def',
#            4:'ghi',
#            5:'jkl',
#            6:'mno',
#            7:'pqrs',
#            8:'tuv',
#            9:'wxyz'
#            }
#
#         cmb=[''] if len(digits)!=0 else []
#
#         for digit in digits:
#             cmb=[p+q for p in cmb for q in d[int(digit)]]
#
#         return cmb
# print(Solution().letterCombinations('23'))

