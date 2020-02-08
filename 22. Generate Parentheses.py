#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 22. Generate Parentheses.py
@time: 2020/2/7 20:14
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ['()']
        else:
            res = []
            for combo in self.generateParenthesis(n-1):
                combo+='()'
                res.append(combo)
                for i in range(1,len(combo)-2): # len(combo)-2 --> second last '('
                    if combo[i]== ')':
                        temp = list(combo)
                        temp[i],temp[-2]=temp[-2],temp[i]
                        res.append(''.join(temp))
            return list(set(res))

print(Solution().generateParenthesis(3))


