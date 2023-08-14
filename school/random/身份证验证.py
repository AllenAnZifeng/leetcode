#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: card_number.py
@time: 2019/12/18 15:30
'''

from functools import reduce

# NUMBER=list('350121191206231210')
NUMBER=list('310108199811040517')
NUMBER=list(map(int,NUMBER))
# print(NUMBER)

weight=[2**(18-i)%11 for i in range(1,18)]
Sum= reduce(lambda x,y:x+y ,[NUMBER[i]*weight[i] for i in range(0,17)])
vdigit= (12- (Sum % 11)) % 11
print(vdigit)

