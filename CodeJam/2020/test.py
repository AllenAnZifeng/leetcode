#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: test.py
@time: 2020/4/3 22:12
'''


from __future__ import annotations
class Fruit:
    def __init__(self,value,name):
        self.value = value

        self.name=name

    def __lt__(self, other:Fruit):
        return self.value<other.value

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()


apple= Fruit(10,'apple')
banana = Fruit(333,'banana')
print(sorted([apple,banana]))