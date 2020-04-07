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
from pprint import pprint


def check(dimension, trace):
    numberSet = [i + 1 for i in range(dimension)]
    if trace / dimension in numberSet:
        return True  # possible
    if trace > (dimension - 1) * numberSet[0] + numberSet[-1] and trace < (dimension - 1) * \
            numberSet[-1] + numberSet[0]:
        return True
    return False


def transpose(m):
    return list(zip(*m))


def generate(dimension, trace):
    numberSet = [i + 1 for i in range(dimension)]
    diagonal = []
    number_of_biggest_value = trace // dimension
    remainder = trace % dimension
    for i in range(number_of_biggest_value):
        diagonal.append(numberSet[-1])
    if remainder != 0:
        diagonal.append(remainder)
    number_of_empty_spots = dimension - len(diagonal)
    diagonal[0] = diagonal[0] - number_of_empty_spots
    for i in range(number_of_empty_spots):
        diagonal.append(numberSet[0])
    matrix = [[0] * dimension for i in range(dimension)]
    for i in range(dimension):
        matrix[i][i] = diagonal[i]

    return matrix

def filled(matrix):
    filled = True
    for row in matrix:
        if 0 in row:
            filled = False
            break
    return filled

def can_fill(matrix, number, row, col):
    return not ((number in matrix[row]) or (number in transpose(matrix)[col]))

def find(matrix,number):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == number:
                return row,col

def fill(matrix):
    p(matrix)
    matrix = [list(row) for row in matrix]
    f_row, f_col = find(matrix,0)

    for number in range(1, len(matrix)+1):
        if can_fill(matrix,number,f_row,f_col):
            print("fill %d -> %d,%d" % (number, f_row, f_col))
            matrix[f_row][f_col] = number
            if filled(matrix):
                return matrix
            result = fill(matrix)
            if result != None:
                return result
    return None

def p(matrix):
    if matrix is not None:
        for row in matrix:
            print(row)
        print()
    else:
        print(None)

inputList = ['3 6', '2 3', '4 10']
for i in range(len(inputList)):
    n, k = [int(s) for s in inputList[i].split()]
    if check(n, k):
        print("Case #%d: POSSIBLE" % (i + 1))
        matrix = generate(n, k)
        matrix = fill(matrix)
        p(matrix)
    else:
        print("Case #%d: IMPOSSIBLE" % (i + 1))
