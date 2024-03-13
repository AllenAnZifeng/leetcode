#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Pattern Matching.py
@time: 2020/4/10 21:42
'''



s='''A*C*E
*B*D*'''

s1='''H*O
HELLO*
*HELLO
HE*'''

s2='''*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S'''

# l=[list(word) for word in s2.split('\n')]
# #
# print(l)





def generate(l):
    l = [list(word[0]) for word in l]
    # print(l,'00000')
    forward=[]
    backward=[]
    forward_flag,backward_flag= True,True

    while forward_flag:
        temp = [word.pop(0) for word in l if word[0] != '*']
        if temp == []:
            forward_flag = False
        else:
            if temp[0] * len(temp) == ''.join(temp):
                forward.append(temp[0])
            else:
                return '*'
    # print(l)
    while backward_flag:
        temp = [word.pop(-1) for word in l if word[-1] != '*']
        if temp == []:
            backward_flag = False
        else:
            if temp[0] * len(temp) == ''.join(temp):
                backward.append(temp[0])
            else:
                return '*'

    # print(l)
    for word in l:
        word=''.join(word)
        forward.append(''.join(word.split('*')))
    #
    # print(forward)
    # print(backward)
    backward.reverse()
    ans = ''.join(forward)+''.join(backward)
    # print(ans)
    return ans

# generate(l)



if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        count = int(input())
        L = []
        for j in range(count):
            L .append([s for s in input().split()])
        # print('L',L)
        print('Case #%d: %s' % (i + 1, generate(L)))
