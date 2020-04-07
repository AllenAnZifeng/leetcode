#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: Indicium.py
@time: 2020/4/4 14:28
'''



# number_of_case = int(input())
# inputList=[]
# for i in range(number_of_case):
#     inputList.append(input())

def check(dimension,trace):
    numberSet = [i+1 for i in range(dimension)]
    if trace/dimension in numberSet:
        return True #possible
    if trace > (dimension-1)*numberSet[0]+numberSet[-1] and trace < (dimension-1)*numberSet[-1]+numberSet[0]:
        return True
    return False

def transpose(m):
    return list(zip(*m))


def p(matrix): # print
    for row in matrix:
        print(row)

def generate(dimension,trace):
    numberSet = [i + 1 for i in range(dimension)]
    diagonal =[]
    number_of_biggest_value = trace//dimension
    remainder = trace%dimension
    for i in range(number_of_biggest_value):
        diagonal.append(numberSet[-1])
    if remainder!=0:
        diagonal.append(remainder)
    number_of_empty_spots = dimension-len(diagonal)
    diagonal[0] = diagonal[0] - number_of_empty_spots
    for i in range(number_of_empty_spots):
        diagonal.append(numberSet[0])
    matrix = [[0]*dimension for i in range(dimension)]
    for i in range(dimension):
        matrix[i][i] = diagonal[i]

    return matrix



def find_fill(matrix,number)->[int,int]:
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 0 and number not in matrix[r] and number not in transpose(matrix)[c]:
                return [r,c]
    return False

def complete(matrix):
    for row in matrix:
        if 0 in row:
            return False
    return True

def fill(matrix):
    if complete(matrix):
        # print('here')
        return True
    for number in range(1,len(matrix)+1):
        location = find_fill(matrix,number)
        if location:
            r,c=location[0],location[1]
            # print("filling %d --> [%d,%d]"%(number,r,c))
            matrix[r][c] = number
            if fill(matrix):
                return True
            matrix[r][c]=0
    return False



# '3 6', '2 3',
inputList = ['3 6', '2 3','4 16','5 18']
for i in range(len(inputList)):
    n,k = [int(s) for s in inputList[i].split()]
    if check(n,k):
        print("Case #%d: POSSIBLE"%(i+1))
        m=generate(n,k)
        p(m)
        fill(m)
        p(m)
    else:
        print("Case #%d: IMPOSSIBLE" % (i + 1))


