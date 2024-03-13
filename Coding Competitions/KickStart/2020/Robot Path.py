#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Robot Path.py
@time: 2020/4/18 20:57
'''


#
# def findClosingBracket(index, s):
#     #take forward bracket index, return backward bracket index
#     count=1
#     while count!=0:
#         index+=1
#         if s[index]== '(':
#             count+=1
#         elif s[index]== ')':
#             count-=1
#     return index
#
#
# def parse(s):
#     i=0
#     result=[]
#     if '(' not in s:
#         # print('return',s)
#         return s
#     while i<len(s):
#         if s[i] in '23456789':
#             closingBracketIndex = findClosingBracket(i+1,s)
#             # print(s[i])
#             # print(s[i+2:closingBracketIndex])
#             result.extend(int(s[i])*parse(s[i+2:closingBracketIndex]))
#             i=closingBracketIndex+1
#         else:
#             result.extend(s[i])
#             i+=1
#     # return ''.join(result)
#     return result
#
# def score(s):
#     row,col=1,1
#     grid=10e8
#     result = parse(s)
#     for i in result:
#         if i=='N':
#             col-=1
#         elif i=='S':
#             col+=1
#         elif i=='W':
#             row-=1
#         elif i=='E':
#             row+=1
#
#     row,col = row%grid,col%grid
#     if int(row) ==0:
#         row=grid
#     if int(col)==0:
#         col=grid
#     return row,col


def findClosingBracket(index, s):
    #take forward bracket index, return backward bracket index
    count=1
    while count!=0:
        index+=1
        if s[index]== '(':
            count+=1
        elif s[index]== ')':
            count-=1
    return index

def evaluate(s):
    row,col=0,0
    for i in s:
        if i == 'N':
            col -= 1
        elif i == 'S':
            col += 1
        elif i == 'W':
            row -= 1
        elif i == 'E':
            row += 1
    return row,col

def mutiply(num,l):
    return [num*x for x in l]

def parse(s):
    i=0
    result=[0,0]
    if '(' not in s:
        return evaluate(s)
    while i<len(s):
        if s[i] in '23456789':
            closingBracketIndex = findClosingBracket(i+1,s)
            # print(s[i])
            # print(s[i+2:closingBracketIndex])
            r,c=(mutiply(int(s[i]),parse(s[i+2:closingBracketIndex])))
            result[0]+=r
            result[1]+=c
            i=closingBracketIndex+1
        else:
            r,c=evaluate(s[i])
            result[0] += r
            result[1] += c
            i+=1
    # return ''.join(result)
    return result

def score(s):
    row,col=1,1
    grid=10e8
    r,c = parse(s)
    row+=r
    col+=c

    row,col = row%grid,col%grid
    if int(row) ==0:
        row=grid
    if int(col)==0:
        col=grid
    return row,col



if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        s=list(input())
        r,c=score(s)
        print('Case #%d: %d %d'%(i+1,r,c))

#
# def parse(program):
#     bracket_count = 0
#     repeat = 1
#     repeats = []
#     row, col = 0, 0
#     for i in range(len(program)):
#         c = program[i]
#         if c in "23456789":
#             repeats.append(int(c))
#             repeat *= int(c)
#             bracket_count += 1
#         if c == ")":
#             bracket_count -= 1
#             repeat //= repeats.pop()
#         else:
#             if c == "N":
#                 row -= repeat
#             elif c == "S":
#                 row += repeat
#             elif c == "W":
#                 col -= repeat
#             elif c == "E":
#                 col += repeat
#     return row, col
#
#
# for case_num in range(int(input())):
#     limit = 10e8
#     row, col = parse(input())
#     print("Case #%d: %d %d" % (case_num + 1, col % limit + 1, row % limit + 1))