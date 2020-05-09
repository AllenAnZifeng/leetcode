#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: 9. Palindrome Number.py
@time: 2020/1/23 2:01
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return  str(x)==str(x)[::-1]