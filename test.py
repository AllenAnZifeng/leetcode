#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: test.py
@time: 2020/1/4 23:02
'''

# print(['a']+['b'])

class Fruit(object):
    def __init__(self,value):
        self.value = value

    def increase(self,value):
        self.value+=value

    def p(self):
        return self.value

    @staticmethod
    def power2(num):
        return num**2


print(Fruit.power2(2))


