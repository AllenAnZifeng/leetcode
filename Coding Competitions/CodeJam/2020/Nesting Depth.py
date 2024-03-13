#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Nesting Depth.py
@time: 2020/4/4 1:47
'''


inputList = []
number_of_lines = int(input())
for i in range(number_of_lines):
    temp = input()
    inputList.append(temp)

def split_zero(s):
    ptr1,ptr2 =0,0
    split_s=[]

    while ptr2<len(s):
        if s[ptr2]=='0':
            while ptr2<len(s) and s[ptr2] =='0':
                ptr2+=1
            split_s.append(s[ptr1:ptr2])
        else:
            while ptr2<len(s) and s[ptr2] != '0':
                ptr2 += 1
            split_s.append(s[ptr1:ptr2])
        ptr1=ptr2
    # print(split_s)
    return split_s


def add_brackets(s): # input str
    if s=='0'*len(s):
        # print('return',s)
        return 'X'*len(s)
    l= split_zero(s)
    output = ''
    for string in l:
        if '0' in string:
            output+='X'*len(string)
        else:
            string=''.join([str(int(c)-1) for c in list(string)])
            # print('string',string)
            output+='('+ add_brackets(string) +')'
    return output

ans = []
for s in inputList:
    bracket_string = add_brackets(s)
    count =0
    for i in range(len(bracket_string)):
        if bracket_string[i]=='X':
            bracket_string = bracket_string[:i]+s[count]+bracket_string[i+1:]
            count+=1
    ans.append(bracket_string)

for i in range(len(ans)):
    print('Case #%d: %s'%(i+1,ans[i]))
